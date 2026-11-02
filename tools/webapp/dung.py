# -*- coding: utf-8 -*-
"""Dựng tools/webapp/trang.html từ dashboard/index.html.

MỘT nguồn cho phần vẽ. Bản web app chỉ khác ở TẦNG TRUYỀN DỮ LIỆU:

    artifact : fetch → Apps Script  ·  capability mcp  ·  mở cửa sổ mới
    web app  : google.script.run    (cùng gốc, ⛔ không CSP, ⛔ không quyền gì)

Nhờ vậy sửa cách hiển thị ở một chỗ, chạy lại file này là bản web app có luôn.

    python tools/webapp/dung.py
"""
import io
import os
import re
import sys

GOC = os.path.join(os.path.dirname(__file__), "..", "..")
NGUON = os.path.join(GOC, "dashboard", "index.html")
RA = os.path.join(os.path.dirname(__file__), "trang.html")

s = io.open(NGUON, encoding="utf-8").read()
n0 = len(s)
dem = [0]


def thay(cu, moi, ten):
    global s
    if s.count(cu) != 1:
        sys.exit("⛔ mốc «%s» khớp %d lần — dashboard/index.html đã đổi, "
                 "sửa lại dung.py cho khớp." % (ten, s.count(cu)))
    s = s.replace(cu, moi, 1)
    dem[0] += 1
    print("  ✓", ten)


# ── ① tầng gọi: fetch → google.script.run ───────────────────────────────
thay("""function gasGet(action){
  var u=GAS_URL+'?action='+encodeURIComponent(action)+
    (GAS_TOKEN?'&token='+encodeURIComponent(GAS_TOKEN):'');
  return fetch(u,{method:'GET',redirect:'follow'}).then(function(r){return r.json()})}

/* ⚠ text/plain để trình duyệt ⛔ không bắn preflight OPTIONS — Apps Script
   không trả lời OPTIONS. charset=utf-8 là bắt buộc, thiếu nó tiếng Việt hỏng. */
function gasPost(d){
  d.token=GAS_TOKEN;
  return fetch(GAS_URL,{method:'POST',redirect:'follow',
    headers:{'Content-Type':'text/plain;charset=utf-8'},
    body:JSON.stringify(d)}).then(function(r){return r.json()})}""",
"""/* google.script.run là cầu nối sẵn có giữa trang và server Apps Script —
   CÙNG GỐC, nên ⛔ không CSP chặn, ⛔ không cần connector, ⛔ không cần token.
   Bọc thành Promise để phần còn lại của trang dùng y như lúc gọi fetch. */
function gsr(ten,args){
  return new Promise(function(ok,hong){
    if(!(window.google&&google.script&&google.script.run))
      return hong(new Error('Trang không chạy trên Apps Script'));
    var r=google.script.run.withSuccessHandler(ok).withFailureHandler(function(e){
      hong(new Error((e&&e.message)||'Server báo lỗi'))});
    /* ⛔ apply(null,…) là hỏng: runner của google.script.run cần chính nó
       làm `this`, mất `this` thì lời gọi không bao giờ tới server. */
    r[ten].apply(r,args||[])})}""",
     "gsr")

# ── ② ping / đọc / ghi / tạo / gửi ──────────────────────────────────────
thay("""function noiGas(){
  napGasToken();
  return gasGet('ping').then(function(r){
    gasKetQua(r);
    GAS_TT='ok'; GAS_CAN_TOKEN=!!r.can_token; GAS_LOI='';
    return docGas()})
   .catch(function(e){GAS_TT='loi';GAS_LOI=gasLoi(e);return false})}""",
"""function noiGas(){
  return gsr('apiPing').then(function(r){
    gasKetQua(r);
    GAS_TT='ok'; GAS_LOI=''; GAS_TOI=sv(r.toi);
    return docGas()})
   .catch(function(e){GAS_TT='loi';GAS_LOI=gasLoi(e);return false})}""", "noiGas")

thay("""  return gasGet('list').then(function(r){""",
     """  return gsr('apiDocHook').then(function(r){""", "docGas")

thay("""  return gasPost({action:'update',ma:ma,truong:t})
    .then(gasKetQua).then(function(r){return (r.ket_qua||{}).dong||0})}""",
     """  return gsr('apiSua',[ma,t])
    .then(gasKetQua).then(function(r){return (r.ket_qua||{}).dong||0})}""", "ghiGas")

thay("""  return gasPost({action:'create',hook:{""",
     """  return gsr('apiTao',[{""", "taoGas-dau")

thay("""      nguoi_gui:sv(v.nguoi_gui),trang_thai:sv(v.trang_thai)}})
    .then(gasKetQua).then(function(r){return (r.ket_qua||{}).ma||''})}""",
     """      nguoi_gui:sv(v.nguoi_gui),trang_thai:sv(v.trang_thai)}])
    .then(gasKetQua).then(function(r){return (r.ket_qua||{}).ma||''})}""", "taoGas-duoi")

thay("""  return gasPost({action:'submit',mas:mas,nguoi:nguoi,ghi_chu:ghiChu})
    .then(gasKetQua).then(function(r){""",
     """  return gsr('apiGui',[mas,nguoi,ghiChu])
    .then(gasKetQua).then(function(r){""", "guiGas")

# ── ③ dữ liệu kỳ: file tĩnh → Drive ─────────────────────────────────────
thay("""function napKy(ds,id){
  var p=find(ds,'id',id)||ds[0];
  try{localStorage.setItem('kn_ky',p.id)}catch(e){}
  fetch(p.file).then(function(r){if(!r.ok)throw new Error(r.status);return r.json()})
    .then(function(D){render(D,ds,p.id)})
    .catch(function(){loi('Không tải được dữ liệu kỳ '+esc(p.nhan)+' ('+esc(p.file)+
      '). File kỳ không nằm trong git — sinh lại bằng: python tools/id.py bao-cao --ky "'+
      esc(p.nhan)+'"')});
}""",
"""/* Kỳ nằm trong một thư mục Drive — Claude phân tích hội thoại xong thả file
   JSON vào đó là trang thấy ngay, ⛔ không phải deploy lại. */
function napKy(ds,id){
  var p=find(ds,'id',id)||ds[0];
  try{localStorage.setItem('kn_ky',p.id)}catch(e){}
  gsr('apiDuLieu',[p.file_id])
    .then(function(D){render(D,ds,p.id)})
    .catch(function(e){loi('Không đọc được kỳ '+esc(p.nhan)+' — '+esc(e.message))});
}""", "napKy")

thay("""var inline=document.getElementById('kn-data').textContent.trim();
if(inline){try{render(JSON.parse(inline),null,null)}catch(e){loi('Khối dữ liệu trong file bị lỗi: '+e.message)}}
else fetch('data/index.json').then(function(r){if(!r.ok)throw new Error(r.status);return r.json()})
  .then(function(idx){
    if(idx.bo_cuc&&BO_CUC[idx.bo_cuc])BC=idx.bo_cuc;
    try{document.title=bc().ten}catch(e){}
    var ds=idx.ky||[];
    if(!ds.length){loi('Chưa có kỳ báo cáo nào. Chạy: python tools/id.py bao-cao --ky "19-25/10"');return}
    var want=null; try{want=localStorage.getItem('kn_ky')}catch(e){}
    napKy(ds,find(ds,'id',want)?want:ds[0].id)})
  .catch(function(){loi('Không tải được danh sách kỳ báo cáo. Chạy: python tools/id.py bao-cao --ky …')});""",
"""/* Bố cục cố định ở bản web app: đây là báo cáo insight cho khối nội dung.
   Đổi bằng ?bo_cuc=truc-page trên URL khi cần xem bản khác. */
(function(){
  var m=/[?&]bo_cuc=([^&]+)/.exec(location.search||'');
  BC=(m&&BO_CUC[decodeURIComponent(m[1])])?decodeURIComponent(m[1]):'insight';
  try{document.title=bc().ten}catch(e){}
})();

gsr('apiKy').then(function(ds){
  if(!ds||!ds.length){
    loi('Thư mục Drive chưa có file JSON kỳ nào. Thả file «<tên kỳ>.json» vào '+
        'thư mục khai ở Script properties → THU_MUC.');return}
  var want=null; try{want=localStorage.getItem('kn_ky')}catch(e){}
  napKy(ds,find(ds,'id',want)?want:ds[0].id)})
 .catch(function(e){loi('Không lấy được danh sách kỳ — '+esc(e.message))});""", "khoi-dong")

# ── ④ bỏ hẳn những thứ chỉ bản artifact mới cần ─────────────────────────
thay("""/* claude.use() chỉ trả lời SAU lần chạy đồng bộ đầu tiên, và trả null khi
   trang mở ngoài claude.ai hoặc người xem chưa nối connector. Vẽ trang trước,
   bật tính năng sau — ⛔ không chặn lần vẽ đầu để chờ quyền. */
(function(){
  if(!(window.claude&&window.claude.use)){MCP_TT='khong';return}
  window.claude.use('mcp').then(function(m){
    MCP=m; MCP_TT=m?'san_sang':'khong';
    if(VE_LAI)VE_LAI();
    if(m)docSheet();
  }).catch(function(){MCP_TT='khong';if(VE_LAI)VE_LAI()});
})();""",
"""/* ⛔ Không có capability mcp ở đây, và cũng không cần: server nằm ngay sau
   google.script.run. Nhánh connector giữ nguyên trong mã nhưng không bao giờ
   chạy — khoCo() thấy GAS_TT==='ok' là xong. */""", "bo-mcp")

thay("var GAS_TOKEN='';", "var GAS_TOKEN='';\nvar GAS_TOI='';   /* email người đang xem, server trả về */", "toi")

# ── ⑤ nhãn cho đúng bản ─────────────────────────────────────────────────
thay("""    ?('✓ Nối được Sheet qua '+khoTen()+' — sửa và gửi ghi thẳng vào Sheet.')""",
     """    ?('✓ Nối thẳng Google Sheet'+(GAS_TOI?' · '+GAS_TOI:'')+
       ' — sửa và gửi ghi vào Sheet ngay.')""", "nhan")

thay("""  return k==='gas'?'Apps Script':(k==='mcp'?'connector Google Sheets':'')}""",
     """  return k==='gas'?'Apps Script':(k==='mcp'?'connector Google Sheets':'')}
/* Người gửi điền sẵn bằng email đang đăng nhập — ⛔ không bắt gõ tay nữa. */
function nguoiMacDinh(){return GAS_TOI||''}""", "nguoiMacDinh")

thay("""  var ten=''; try{ten=localStorage.getItem('kn_nguoi')||''}catch(e){}""",
     """  var ten=nguoiMacDinh();
  if(!ten){try{ten=localStorage.getItem('kn_nguoi')||''}catch(e){}}""", "dien-ten")

# ── ⑥ bỏ phần đầu/cuối của trang độc lập, giữ thân cho HtmlService ──────
s = re.sub(r"^<!doctype html>.*?<body>\n", "", s, count=1, flags=re.S)
s = re.sub(r"\n</body></html>\s*$", "\n", s, count=1, flags=re.S)

dau = ("<!-- SINH TỰ ĐỘNG bởi tools/webapp/dung.py từ dashboard/index.html.\n"
       "     ⛔ Đừng sửa thẳng file này — sửa dashboard/index.html rồi chạy lại. -->\n")

io.open(RA + ".tmp", "w", encoding="utf-8").write(dau + s)
os.replace(RA + ".tmp", RA)
print("\n%d mốc đã thay · %s · %d → %d byte" % (dem[0], os.path.basename(RA), n0, len(s)))
