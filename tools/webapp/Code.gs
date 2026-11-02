/**
 * Báo cáo Insight Kangnam — Web App chạy trên Apps Script.
 *
 * Vì sao có file này: bản artifact chạy trong sandbox của claude.ai, bị CSP
 * chặn mọi lời gọi mạng và không được cấp capability `mcp`, nên trang ⛔ không
 * tự ghi vào Sheet được — phải lách qua «mở cửa sổ mới». Ở đây Google phục vụ
 * chính trang này, nên nó CÙNG GỐC với Sheet: gọi `google.script.run` là xong.
 *
 *   Đầu vào  : JSON kỳ do Claude phân tích, thả vào một thư mục Drive
 *   Đầu ra   : dashboard, và mọi thao tác hook ghi thẳng vào Google Sheet
 *
 * ⛔ LUẬT GHI giữ nguyên như bản artifact:
 *   · Chỉ ghi hai dải F:L và R:V.
 *   · Cột Q (Duyệt) là ô của BÁC SĨ và PHÁP CHẾ — ⛔ không bao giờ chạm.
 *   · Cột M–P truy ngược về hội thoại gốc, cũng khoá, trừ lúc TẠO dòng mới.
 */

// ─────────────────────────────── Cấu hình ───────────────────────────────
// Đặt ở Project Settings → Script properties để đổi mà ⛔ không sửa code.

var SHEET_ID  = '1MJbv_M5Sh3BPntLnj9mqS8c4QNXYmwyRC_1Mj_Y4j2Q';
var TEN_SHEET = 'Trang tính1';   // Google đặt tên theo ngôn ngữ tài khoản
var THU_MUC   = '1iBU86XL6R5BUxcDWpPTvPrvuVjUOi9jp';   // thư mục Drive chứa JSON kỳ
var DONG_DAU  = 2;

var COT = {
  ma: 1, cd: 2, chan_dung: 3, giai_doan: 4, dich_vu: 5,
  insight: 6, hook: 7, cta: 8, fm_text: 9, local_hoa: 10, ly_do_local: 11,
  muc_tieu: 12,
  win: 13, phan_doi: 14, truy_nguoc: 15, co_phap_che: 16, duyet: 17,
  chon: 18, ghi_chu: 19, cap_nhat: 20, nguoi_gui: 21, trang_thai: 22, nguon: 23
};
var SO_COT = 23;

/** Hai dải được phép ghi đè. ⛔ Không thêm cột 13..17 vào đây. */
var GHI_1 = ['insight', 'hook', 'cta', 'fm_text', 'local_hoa', 'ly_do_local', 'muc_tieu'];
var GHI_2 = ['chon', 'ghi_chu', 'cap_nhat', 'nguoi_gui', 'trang_thai'];

var NGUON_MOI = 'Tạo trên artifact';
var MUI_GIO   = 'Asia/Ho_Chi_Minh';

function cauHinh(k, md) {
  return PropertiesService.getScriptProperties().getProperty(k) || md;
}

// ─────────────────────────── Trang ───────────────────────────

/**
 * Trang chủ. ⛔ Không dùng createTemplateFromFile: trang có nhiều dấu `<?`
 * trong chuỗi JS sẽ bị bộ template hiểu nhầm là scriptlet.
 */
function doGet(e) {
  var p = (e && e.parameter) || {};
  if (p.api === 'ping') {                       // để kiểm tra deploy bằng curl
    return ContentService.createTextOutput(JSON.stringify(apiPing()))
      .setMimeType(ContentService.MimeType.JSON);
  }
  try {
    return HtmlService.createHtmlOutputFromFile('trang')
      .setTitle('Insight khách · line Da · Kangnam')
      .addMetaTag('viewport', 'width=device-width, initial-scale=1')
      .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
  } catch (err) {
    // Thiếu file HTML là lỗi CÀI ĐẶT, không phải lỗi chạy — nói thẳng phải làm
    // gì, thay vì để Google ném ra một dòng exception trần.
    return trangThieuFile(String(err.message || err));
  }
}

function trangThieuFile(loi) {
  return HtmlService.createHtmlOutput(
    '<div style="font:15px/1.6 -apple-system,Segoe UI,Roboto,sans-serif;' +
    'max-width:620px;margin:40px auto;padding:0 18px;color:#1f1e1b">' +
    '<h1 style="font-size:19px">⚠ Project còn thiếu file giao diện</h1>' +
    '<p>Server chạy được, nhưng chưa có file HTML tên <b>trang</b>.</p>' +
    '<ol><li>Trong Apps Script bấm <b>+</b> cạnh «Tệp» → <b>HTML</b></li>' +
    '<li>Đặt tên đúng chữ <b>trang</b> (⛔ không gõ đuôi <code>.html</code>)</li>' +
    '<li>Dán toàn bộ nội dung <code>tools/webapp/trang.html</code> vào</li>' +
    '<li><b>Deploy → Manage deployments → Edit → Version: New</b></li></ol>' +
    '<p style="color:#6a675f;font-size:13px;border-top:1px solid #e3e0d8;' +
    'padding-top:12px">Google báo: ' + loi + '</p></div>')
    .setTitle('Thiếu file trang');
}

// ─────────────────────────── Bảng tính ───────────────────────────

function bang() {
  var id = cauHinh('SHEET_ID', SHEET_ID);
  return id ? SpreadsheetApp.openById(id) : SpreadsheetApp.getActive();
}

function sheet() {
  var ss = bang(), sh = ss.getSheetByName(cauHinh('TEN_SHEET', TEN_SHEET));
  if (!sh) sh = ss.getSheets()[0];     // sai tên trang tính — ⛔ đừng chết ở đây
  if (!sh) throw new Error('Bảng «' + ss.getName() + '» không có trang tính nào');
  return sh;
}

function docTatCa() {
  var sh = sheet(), n = sh.getLastRow();
  if (n < DONG_DAU) return [];
  return sh.getRange(DONG_DAU, 1, n - DONG_DAU + 1, SO_COT).getValues();
}

function timDong(ma) {
  var v = docTatCa();
  for (var i = 0; i < v.length; i++) {
    if (String(v[i][COT.ma - 1]).trim() === String(ma).trim()) return DONG_DAU + i;
  }
  return 0;
}

function bayGio() {
  return Utilities.formatDate(new Date(), MUI_GIO, 'dd/MM/yyyy HH:mm');
}

/** Sheets tự nhận chuỗi ngày thành kiểu Date — quy về đúng một dạng khi đọc. */
function chuoi(x) {
  if (x === null || x === undefined) return '';
  if (Object.prototype.toString.call(x) === '[object Date]')
    return Utilities.formatDate(x, MUI_GIO, 'dd/MM/yyyy HH:mm');
  return String(x);
}

function maMoi() {
  var v = docTatCa(), n = 0;
  for (var i = 0; i < v.length; i++) {
    var m = String(v[i][COT.ma - 1]);
    if (m.indexOf('KN-ART-') === 0) {
      var k = parseInt(m.substring(7), 10);
      if (!isNaN(k) && k > n) n = k;
    }
  }
  return 'KN-ART-' + ('00' + (n + 1)).slice(-3);
}

function thanhObj(hang) {
  var o = {};
  for (var k in COT) o[k] = chuoi(hang[COT[k] - 1]);
  return o;
}

/** Ghi đè các trường sửa được của MỘT hook. Trường ngoài GHI_1/GHI_2 bị bỏ. */
function suaHook(ma, truong) {
  var dong = timDong(ma);
  if (!dong) throw new Error('Không thấy mã ' + ma + ' trong Sheet');
  var sh = sheet();
  if (!truong.cap_nhat) truong.cap_nhat = bayGio();

  var r1 = sh.getRange(dong, COT.insight, 1, GHI_1.length), a1 = r1.getValues()[0];
  for (var i = 0; i < GHI_1.length; i++)
    if (truong[GHI_1[i]] !== undefined) a1[i] = chuoi(truong[GHI_1[i]]);
  r1.setValues([a1]);

  var r2 = sh.getRange(dong, COT.chon, 1, GHI_2.length);
  r2.setNumberFormat('@');
  var a2 = r2.getValues()[0];
  for (var j = 0; j < GHI_2.length; j++)
    if (truong[GHI_2[j]] !== undefined) a2[j] = chuoi(truong[GHI_2[j]]);
  r2.setValues([a2]);

  return { ma: ma, dong: dong };
}

function themHook(d) {
  if (!chuoi(d.hook).trim()) throw new Error('Thiếu nội dung hook');
  var sh = sheet(), ma = maMoi(), h = [];
  for (var i = 0; i < SO_COT; i++) h.push('');
  h[COT.ma - 1]          = ma;
  h[COT.cd - 1]          = chuoi(d.cd);
  h[COT.chan_dung - 1]   = chuoi(d.chan_dung);
  h[COT.giai_doan - 1]   = chuoi(d.giai_doan);
  h[COT.dich_vu - 1]     = chuoi(d.dich_vu) || '(chưa nêu)';
  h[COT.insight - 1]     = chuoi(d.insight);
  h[COT.hook - 1]        = chuoi(d.hook);
  h[COT.cta - 1]         = chuoi(d.cta);
  h[COT.fm_text - 1]     = chuoi(d.fm_text);
  h[COT.local_hoa - 1]   = chuoi(d.local_hoa) || 'Không';
  h[COT.ly_do_local - 1] = chuoi(d.ly_do_local);
  h[COT.muc_tieu - 1]    = chuoi(d.muc_tieu);
  h[COT.win - 1]         = chuoi(d.win);
  h[COT.truy_nguoc - 1]  = chuoi(d.truy_nguoc) || '⛔ chưa gắn HT';
  h[COT.co_phap_che - 1] = '⚠ chưa soát';
  h[COT.duyet - 1]       = 'chờ BS + pháp chế';
  h[COT.chon - 1]        = chuoi(d.chon);
  h[COT.ghi_chu - 1]     = chuoi(d.ghi_chu);
  h[COT.cap_nhat - 1]    = bayGio();
  h[COT.nguoi_gui - 1]   = chuoi(d.nguoi_gui) || toiLaAi();
  h[COT.trang_thai - 1]  = chuoi(d.trang_thai) || 'Nháp';
  h[COT.nguon - 1]       = NGUON_MOI;
  sh.appendRow(h);
  return { ma: ma, dong: sh.getLastRow() };
}

function guiLo(mas, nguoi, ghiChu) {
  if (!mas || !mas.length) throw new Error('Lô rỗng');
  nguoi = chuoi(nguoi).trim() || toiLaAi();
  if (!nguoi) throw new Error('Thiếu tên người gửi');
  var luc = bayGio(), xong = [], hong = [];
  for (var i = 0; i < mas.length; i++) {
    try {
      var t = { chon: 'Chọn', cap_nhat: luc, nguoi_gui: nguoi, trang_thai: 'Đã gửi' };
      if (chuoi(ghiChu).trim()) t.ghi_chu = ghiChu;
      suaHook(mas[i], t);
      xong.push(mas[i]);
    } catch (e) {
      hong.push({ ma: mas[i], loi: String(e.message || e) });
    }
  }
  return { luc: luc, nguoi: nguoi, xong: xong, hong: hong };
}

/** Deploy «Execute as: User accessing» thì đây là người đang xem thật. */
function toiLaAi() {
  try { return Session.getActiveUser().getEmail() || ''; } catch (e) { return ''; }
}

// ─────────────────── Dữ liệu kỳ — đọc từ Drive ───────────────────

/**
 * Mỗi kỳ là một file `<id>.json` trong thư mục Drive khai ở `THU_MUC`.
 * Claude phân tích hội thoại xong thả file vào đó là trang thấy ngay —
 * ⛔ không phải deploy lại, không phải dán JSON vào code.
 */
function thuMuc() {
  var id = cauHinh('THU_MUC', THU_MUC);
  if (!id) throw new Error(
    'Chưa khai thư mục dữ liệu. Project Settings → Script properties → ' +
    'thêm THU_MUC = ID thư mục Drive chứa các file JSON kỳ.');
  return DriveApp.getFolderById(id);
}

function quetKy(tm, ds, sau) {
  // Thư mục có thể chứa cả bảng tính và tài liệu khác — chỉ nhận .json.
  var it = tm.getFiles();
  while (it.hasNext()) {
    var f = it.next(), ten = f.getName();
    if (ten.slice(-5).toLowerCase() !== '.json') continue;
    ds.push({ id: ten.slice(0, -5), nhan: ten.slice(0, -5),
              file_id: f.getId(), sua: f.getLastUpdated().getTime() });
  }
  // Người ta hay dựng thêm một thư mục con «data» rồi thả file vào đó. Quét
  // xuống 2 tầng thay vì bắt họ đoán vì sao trang ⛔ không thấy file nào.
  if (sau >= 2) return ds;
  var tc = tm.getFolders();
  while (tc.hasNext()) quetKy(tc.next(), ds, sau + 1);
  return ds;
}

function apiKy() {
  var ds = quetKy(thuMuc(), [], 0), thay = {}, ra = [];
  ds.sort(function (a, b) { return b.sua - a.sua; });   // kỳ mới nhất lên đầu
  for (var i = 0; i < ds.length; i++) {                 // cùng tên ở hai thư mục
    if (thay[ds[i].id]) continue;                       // → lấy bản mới hơn
    thay[ds[i].id] = 1; ra.push(ds[i]);
  }
  return ra;
}

function apiDuLieu(file_id) {
  var txt = DriveApp.getFileById(file_id).getBlob().getDataAsString('UTF-8');
  var D = JSON.parse(txt);
  // Nhãn kỳ lấy từ chính file, ⛔ không suy từ tên file.
  return D;
}

// ─────────────────────────── API cho trang ───────────────────────────
// Mọi hàm trả về {ok:…} hoặc ném lỗi — google.script.run có withFailureHandler.

function apiPing() {
  var sh = sheet(), ky = [], loi = '';
  // Đếm luôn số kỳ đọc được: «có khai thư mục» ⛔ không chứng minh là đọc được.
  try { ky = apiKy(); } catch (e) { loi = String(e.message || e); }
  return { ok: true, bang: sh.getParent().getName(), sheet: sh.getName(),
           dong: sh.getLastRow(), toi: toiLaAi(),
           thu_muc: !!cauHinh('THU_MUC', THU_MUC),
           so_ky: ky.length, ky: ky.map(function (x) { return x.id; }),
           loi_thu_muc: loi };
}

function apiDocHook() {
  var v = docTatCa(), ds = [];
  for (var i = 0; i < v.length; i++)
    if (chuoi(v[i][COT.ma - 1]).trim()) ds.push(thanhObj(v[i]));
  return { ok: true, so: ds.length, hook: ds };
}

function apiSua(ma, truong) { return { ok: true, ket_qua: suaHook(ma, truong || {}) }; }
function apiTao(d)          { return { ok: true, ket_qua: themHook(d || {}) }; }
function apiGui(mas, nguoi, ghiChu) {
  return { ok: true, ket_qua: guiLo(mas, nguoi, ghiChu) };
}

// ───────────────────── Menu trong Sheet cho team PM ──────────────────────

function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('Hook Kangnam')
    .addItem('Kiểm tra dữ liệu', 'kiemTra')
    .addItem('Xuất file order (hook đã chọn)', 'xuatOrder')
    .addSeparator()
    .addItem('Khoá cột Duyệt cho pháp chế', 'khoaCotDuyet')
    .addToUi();
}

/** Soát lỗi làm hỏng một lô sản xuất. Chỉ BÁO, ⛔ không tự sửa. */
function kiemTra() {
  var v = docTatCa(), loi = [], thay = {};
  for (var i = 0; i < v.length; i++) {
    var h = v[i], dong = DONG_DAU + i, ma = chuoi(h[COT.ma - 1]).trim();
    if (!ma) continue;
    if (thay[ma]) loi.push('Dòng ' + dong + ': mã ' + ma + ' trùng dòng ' + thay[ma]);
    thay[ma] = dong;
    if (!chuoi(h[COT.hook - 1]).trim()) loi.push('Dòng ' + dong + ' (' + ma + '): trống hook');
    if (!chuoi(h[COT.cta - 1]).trim())  loi.push('Dòng ' + dong + ' (' + ma + '): trống CTA');
    var truy = chuoi(h[COT.truy_nguoc - 1]).trim();
    if (!truy || truy.indexOf('⛔') === 0)
      loi.push('Dòng ' + dong + ' (' + ma + '): chưa gắn mã HT làm bằng');
    var lo = chuoi(h[COT.local_hoa - 1]).trim();
    if (lo && lo !== 'Có' && lo !== 'Không')
      loi.push('Dòng ' + dong + ' (' + ma + '): Local hóa phải «Có»/«Không», đang «' + lo + '»');
    if (chuoi(h[COT.trang_thai - 1]).trim() === 'Đã gửi' && !chuoi(h[COT.nguoi_gui - 1]).trim())
      loi.push('Dòng ' + dong + ' (' + ma + '): Đã gửi nhưng trống Người gửi');
    if (chuoi(h[COT.co_phap_che - 1]).indexOf('🔴') === 0 &&
        chuoi(h[COT.chon - 1]).trim() === 'Chọn')
      loi.push('Dòng ' + dong + ' (' + ma + '): cờ 🔴 mà vẫn chọn sản xuất');
  }
  var ui = SpreadsheetApp.getUi();
  if (!loi.length) ui.alert('Kiểm tra dữ liệu', '✓ Không thấy lỗi trong ' + v.length + ' dòng.', ui.ButtonSet.OK);
  else ui.alert('Kiểm tra dữ liệu — ' + loi.length + ' điểm cần xem',
                loi.slice(0, 40).join('\n') + (loi.length > 40 ? '\n…còn ' + (loi.length - 40) : ''),
                ui.ButtonSet.OK);
}

function xuatOrder() {
  var v = docTatCa(), ra = [[
    'Mã hook', 'Chân dung', 'Giai đoạn', 'Dịch vụ', 'Insight lõi', 'Hook', 'CTA cuối',
    'Format đề xuất', 'Local hóa', 'Lý do local', 'Mục tiêu truyền thông',
    'Duyệt', 'Người gửi', 'Cập nhật lúc']];
  for (var i = 0; i < v.length; i++) {
    var h = v[i];
    if (chuoi(h[COT.chon - 1]).trim() !== 'Chọn') continue;
    ra.push([h[COT.ma - 1], h[COT.chan_dung - 1], h[COT.giai_doan - 1], h[COT.dich_vu - 1],
      h[COT.insight - 1], h[COT.hook - 1], h[COT.cta - 1], h[COT.fm_text - 1],
      h[COT.local_hoa - 1], h[COT.ly_do_local - 1], h[COT.muc_tieu - 1],
      h[COT.duyet - 1], h[COT.nguoi_gui - 1], h[COT.cap_nhat - 1]]);
  }
  var ss = bang(), sh = ss.getSheetByName('Order');
  if (!sh) sh = ss.insertSheet('Order');
  sh.clear();
  sh.getRange(1, 1, ra.length, ra[0].length).setValues(ra);
  sh.getRange(1, 1, 1, ra[0].length).setFontWeight('bold');
  sh.setFrozenRows(1);
  SpreadsheetApp.getUi().alert('Xuất file order',
    (ra.length - 1) + ' hook đã chọn, ghi sang sheet «Order».\n' +
    'Hook còn «chờ BS + pháp chế» ở ô Duyệt ⛔ chưa được đưa đi sản xuất.',
    SpreadsheetApp.getUi().ButtonSet.OK);
}

function khoaCotDuyet() {
  var sh = sheet(), n = Math.max(sh.getLastRow(), 200);
  var ds = sh.getProtections(SpreadsheetApp.ProtectionType.RANGE);
  for (var i = 0; i < ds.length; i++)
    if (ds[i].getDescription() === 'Cột Duyệt — BS & pháp chế') ds[i].remove();
  var p = sh.getRange(DONG_DAU, COT.duyet, n, 1).protect()
            .setDescription('Cột Duyệt — BS & pháp chế');
  p.removeEditors(p.getEditors().map(function (u) { return u.getEmail(); }));
  if (p.canDomainEdit()) p.setDomainEdit(false);
  SpreadsheetApp.getUi().alert('Khoá cột Duyệt',
    'Đã bảo vệ Q' + DONG_DAU + ':Q' + (DONG_DAU + n - 1) + '.\n' +
    'Vào Dữ liệu → Trang tính và dải ô được bảo vệ để thêm BS và pháp chế.',
    SpreadsheetApp.getUi().ButtonSet.OK);
}
