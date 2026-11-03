#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
id.py · Agent-InsightDashboard-Kangnam

Làm phần ĐẾM ĐƯỢC của quy trình B1–B6:
  doc       : đọc file hội thoại Caresoft → nấc 5A · mã O · mức nóng · rào cản ·
              vì sao rơi · chấm điểm nhân viên N1–N6 · cờ đỏ
              + rút NGUYÊN LIỆU PHÁC HỌA CHÂN DUNG (cụm chữ khách tự nói, câu đầu)
              + gán chân dung NẾU out/chan-dung.json đã qua CỔNG 0
  chan-dung : quản lý bản phác họa chân dung của kỳ — tạo mẫu · kiểm · duyệt
  ads       : đọc file chỉ số quảng cáo Facebook → chi → CPM→CTR→CPI→CPL→CPB
  bao-cao   : gộp kết quả thành file JSON cho dashboard

⛔ Script KHÔNG có sẵn bộ chân dung nào. Chân dung được **phác họa từ chính hội
   thoại của kỳ** ⚠ DI SẢN: agent đọc nguyên liệu → viết out/chan-dung.json →
   người dùng duyệt ở CỔNG 0 → script mới gán được chân dung cho từng hội thoại.

⛔ Script KHÔNG làm phần đọc hiểu: phác họa chân dung, insight, câu hỏi ngầm,
   hướng nội dung, câu mẫu trong sổ tay. Đó là việc của agent (SYSTEM-PROMPT §8).

Cách dùng:
    python tools/id.py doc du-lieu/hoi-thoai.md --ky 19-25/10
    python tools/id.py chan-dung --ky 19-25/10 --mau
    python tools/id.py chan-dung --ky 19-25/10 --kiem
    python tools/id.py chan-dung --ky 19-25/10 --duyet "Tên người duyệt"
    python tools/id.py doc du-lieu/hoi-thoai.md --ky 19-25/10      # chạy lại, có CD
    python tools/id.py ads du-lieu/ads.csv --ky 19-25/10
    python tools/id.py bao-cao --ky 19-25/10
"""

import argparse
import csv
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TU_DIEN = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tu_dien.json")
RA = os.path.join(GOC, "out")
PHAC_HOA = os.path.join(RA, "chan-dung.json")           # bản phác họa chân dung của kỳ
NGUYEN_LIEU = os.path.join(RA, "nguyen-lieu-chan-dung.json")

CD_DU = "KHONG_XAC_DINH_DV"            # ★ mã DỰ TRỮ của thư viện KF-62
TEN_CD_DU = "Chưa xếp được dịch vụ — khách chưa nói đủ để biết hỏi về gì"
# ⛔ Khác hẳn <DV>-CHUA_XAC_DINH: ở đó đã biết dịch vụ, chỉ thiếu chân dung.
#    Ở đây đến DỊCH VỤ cũng chưa biết — thường là hội thoại dưới 20 ký tự chữ khách.
CD_TOI_THIEU_DE_DE = 15                # ⚠ DI SẢN — chỉ lệnh `chan-dung` cũ còn dùng

GIO_MO, GIO_DONG = 8.5, 22.0          # khung giờ trực page, id-F N1.1
SLA_PHUT = 2                           # ngưỡng trả lời tin đầu
MAU_TOI_THIEU_NV = 10                  # id-F §6


# ─────────────────────────────── tiện ích ───────────────────────────────

def khong_dau(s):
    s = unicodedata.normalize("NFD", s or "")
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower()


_CACHE_RE = {}


def _re_tu(tu):
    """Khớp theo RANH GIỚI TỪ — nếu không, 'mí' sẽ khớp nhầm trong 'mình'."""
    k = khong_dau(tu)
    if k not in _CACHE_RE:
        _CACHE_RE[k] = re.compile(r'(?<![0-9a-zđ])' + re.escape(k) + r'(?![0-9a-zđ])')
    return _CACHE_RE[k]


def co_tu(text, danh_sach):
    t = khong_dau(text)
    return any(_re_tu(tu).search(t) for tu in danh_sach)


def tu_khop(text, danh_sach):
    t = khong_dau(text)
    return [tu for tu in danh_sach if _re_tu(tu).search(t)]


def nap_tu_dien():
    with open(TU_DIEN, encoding="utf-8") as f:
        return json.load(f)


def pct(a, b):
    return round(a / b * 100, 1) if b else None


RE_SDT_TEXT = re.compile(r'(?:\+84|\b0)\d[\d .\-]{7,13}')
RE_MAIL = re.compile(r'[\w.+-]+@[\w-]+\.\w+')
RE_LINK = re.compile(r'https?://\S+|\b(?:fb|facebook|zalo|m)\.(?:com|me)/\S+', re.I)


def an_danh(s):
    """★ Luật ⑩. Mọi câu của khách phải qua hàm này trước khi ghi ra file."""
    s = RE_LINK.sub("«link»", s or "")
    s = RE_MAIL.sub("«email»", s)
    s = RE_SDT_TEXT.sub("«sđt»", s)
    return re.sub(r'\s+', ' ', s).strip()


# ─────────────────────────── đọc file hội thoại ──────────────────────────

RE_TIEU_DE_A = re.compile(r'^###\s+(?:<a id="ht-(\d+)"></a>)?(\d+)\.\s*(.+?)\s*$', re.M)
RE_TIEU_DE_B = re.compile(r'^##\s+(\d+)\.\s*(.+?)\s*$', re.M)
RE_META_A = re.compile(
    r'_Cập nhật:\s*([\d\-: ]+)\s*·\s*NV:\s*(.*?)\s*·\s*SĐT:\s*(\S+)\s*·\s*ID:\s*(\S+?)_')
RE_META_B = re.compile(
    r'\*\*Page:\*\*\s*(.*?)\s*·\s*\*\*Nhân viên:\*\*\s*(.*?)\s*·\s*\*\*Cập nhật:\*\*\s*([\d\-: ]+)')
RE_TIN = re.compile(r'^-\s+`(\d{2}-\d{2}\s+\d{2}:\d{2})`\s+\*\*(.+?):?\*\*:?\s*(.*)$')

# Dòng do HỆ THỐNG sinh, không phải lời khách. ⛔ Không đếm là một lượt của khách,
# không đưa vào văn bản phân loại — nếu đếm thì "bỏ sau 1 lượt" luôn ra 0%.
RE_NHIEU = re.compile(
    r'(\[tệp đính kèm|\[hình ảnh|cuộc gọi thoại|cuộc gọi video|đã gọi cho bạn|'
    r'bạn có thể gọi cho|bạn có một tin nhắn|^\{"filename"|^https?://|'
    r'đã gửi một|người dùng đã|^\s*$)', re.I)


def la_nhieu(text):
    return bool(RE_NHIEU.search((text or "").strip()))


def co_anh(text):
    return bool(re.search(r'(\[tệp đính kèm|\[hình ảnh|"type"\s*:\s*"image")', text or "", re.I))


def doc_hoi_thoai(duong_dan):
    """Trả về danh sách hội thoại. Hỗ trợ hai khuôn xuất Caresoft."""
    with open(duong_dan, encoding="utf-8") as f:
        raw = f.read()

    moc = [(m.start(), m.group(2) or m.group(1), m.group(3)) for m in RE_TIEU_DE_A.finditer(raw)]
    if not moc:
        moc = [(m.start(), m.group(1), m.group(2)) for m in RE_TIEU_DE_B.finditer(raw)]
    if not moc:
        sys.exit("⛔ Không nhận ra khuôn file hội thoại. Xem knowledge/id-B §2.")

    ket = []
    for i, (vt, so, ten) in enumerate(moc):
        het = moc[i + 1][0] if i + 1 < len(moc) else len(raw)
        khoi = raw[vt:het]

        nv_ho_so, co_sdt = "", False
        m = RE_META_A.search(khoi)
        if m:
            nv_ho_so = m.group(2).strip()
            co_sdt = khong_dau(m.group(3)).startswith("co")
        else:
            m = RE_META_B.search(khoi)
            if m:
                nv_ho_so = m.group(2).strip()

        tin = []
        for dong in khoi.splitlines():
            mt = RE_TIN.match(dong.strip())
            if not mt:
                continue
            tem, ai, noi_dung = mt.group(1), mt.group(2).strip(), mt.group(3).strip()
            la_nv = khong_dau(ai).startswith("nv")
            nv_ten = ai[2:].strip() if la_nv else ""
            if not la_nv and khong_dau(ai) not in ("kh",) and nv_ho_so and ai == nv_ho_so:
                la_nv, nv_ten = True, ai
            tin.append({"tem": tem, "nv": la_nv, "ten": nv_ten, "text": noi_dung,
                        "nhieu": la_nhieu(noi_dung), "anh": co_anh(noi_dung)})

        thuc = [t for t in tin if not t["nhieu"]]
        if len(thuc) < 2:
            continue

        nv = nv_ho_so or next((t["ten"] for t in tin if t["nv"] and t["ten"]), "")
        if co_sdt is False:
            co_sdt = bool(re.search(r'\b0\d{8,10}\b', khoi))

        # ⚠ Bản xuất Caresoft gắn sẵn một dòng [Tệp đính kèm] vào MỌI hội thoại đến
        #   từ quảng cáo (ảnh preview của ad), nên "có dòng ảnh" KHÔNG đồng nghĩa
        #   "khách gửi ảnh tình trạng".
        anh_kh = [i for i, t in enumerate(tin) if t["anh"] and not t["nv"]]
        vt_moi_anh = next((i for i, t in enumerate(tin)
                           if t["nv"] and re.search(r'(gửi|xin|chụp).{0,12}(ảnh|hình)',
                                                    t["text"], re.I)), None)
        #   Dòng ảnh mặc định nằm ngay đầu hội thoại nên ⛔ không dùng số lượng ảnh
        #   làm căn cứ — chỉ nhận khi ảnh đến SAU lời mời gửi ảnh của nhân viên.
        gui_anh = vt_moi_anh is not None and any(i > vt_moi_anh for i in anh_kh)

        ket.append({
            "ma": "HT-%03d" % int(so),
            "nv": nv or "(không rõ)",
            "co_sdt": co_sdt,
            "tin": thuc,                       # ⛔ đã bỏ dòng hệ thống
            # Đồng hồ SLA chạy từ tin ĐẦU TIÊN của hội thoại, kể cả dòng hệ thống:
            # đó là lúc khách bấm quảng cáo, không phải lúc khách gõ câu đầu.
            "moc_bat_dau": tin[0]["tem"] if tin else None,
            "kh_gui_anh": gui_anh,
            "kh_text": " ".join(t["text"] for t in thuc if not t["nv"]),
            "nv_text": " ".join(t["text"] for t in thuc if t["nv"]),
        })
    return ket


def phut(tem_a, tem_b):
    """Khoảng cách phút giữa hai tem `MM-DD HH:MM`."""
    try:
        a = datetime.strptime("2026-" + tem_a, "%Y-%m-%d %H:%M")
        b = datetime.strptime("2026-" + tem_b, "%Y-%m-%d %H:%M")
        return (b - a).total_seconds() / 60
    except ValueError:
        return None


def gio_cua(tem):
    try:
        t = datetime.strptime("2026-" + tem, "%Y-%m-%d %H:%M")
        return t.hour + t.minute / 60
    except ValueError:
        return None


# ───────────────────────────── phân loại ─────────────────────────────────

RE_MA_CD = re.compile(r'^CD[1-9][0-9]*$')


def kiem_phac_hoa(pho):
    """Soát bản phác họa chân dung. Trả về danh sách lỗi — rỗng là sạch."""
    if not isinstance(pho, dict):
        return ["file không phải một đối tượng JSON"]
    loi = []
    tep = pho.get("tep")
    if not isinstance(tep, list) or not tep:
        return ["thiếu danh sách `tep` — phải có ít nhất một chân dung"]
    da_thay = set()
    for i, c in enumerate(tep, 1):
        c = c or {}
        vt = "dòng %d" % i
        ma = (c.get("ma") or "").strip()
        if not RE_MA_CD.match(ma):
            loi.append("%s: mã «%s» sai khuôn — phải là CD1, CD2, … (CD0 là mã dự trữ)" % (vt, ma))
        elif ma in da_thay:
            loi.append("%s: mã «%s» bị trùng" % (vt, ma))
        da_thay.add(ma)
        if not (c.get("ten") or "").strip():
            loi.append("%s «%s»: thiếu `ten`" % (vt, ma))
        dh = [x for x in (c.get("dau_hieu") or []) if (x or "").strip()]
        if not dh:
            loi.append("%s «%s»: thiếu `dau_hieu` — không có dấu hiệu thì script không gán được" % (vt, ma))
        hs = c.get("he_so_gia_tri")
        if hs is not None and hs not in (1, 2, 3):
            loi.append("%s «%s»: `he_so_gia_tri` phải là 1, 2 hoặc 3 (id-G §3)" % (vt, ma))
        if not (c.get("trich") or []):
            loi.append("%s «%s»: thiếu `trich` — chân dung phải truy ngược về HT-nnn (luật ①)" % (vt, ma))
    if pho.get("trang_thai") == "da_duyet" and not (pho.get("duyet_boi") or "").strip():
        loi.append("`trang_thai` là da_duyet nhưng `duyet_boi` trống "
                   "— ⛔ agent không tự duyệt thay người dùng")
    return loi


def nap_phac_hoa(ky):
    """★ BỎ TỪ 02/11/2026 — chân dung nay lấy từ THƯ VIỆN KF-62, ⛔ không phác họa theo kỳ.

    Hàm giữ lại để các lệnh cũ còn chạy, và để đọc được bản phác họa cũ nếu ai
    đó còn giữ file. Nó ⛔ KHÔNG còn quyết định chân dung của hội thoại nữa:
    `gan_chan_dung_kf62()` mới là nơi quyết định.
    """
    if not os.path.exists(PHAC_HOA):
        return None, "chưa xếp được mã nào của thư viện KF-62 cho kỳ này"
    try:
        with open(PHAC_HOA, encoding="utf-8") as f:
            pho = json.load(f)
    except ValueError as e:
        return None, "out/chan-dung.json không đọc được: %s" % e
    loi = kiem_phac_hoa(pho)
    if loi:
        return None, ("out/chan-dung.json còn %d lỗi — chạy `id.py chan-dung --kiem`" % len(loi))
    if (pho.get("ky") or "") != ky:
        return None, ("out/chan-dung.json là của kỳ «%s», không phải «%s»"
                      % (pho.get("ky") or "trống", ky))
    if pho.get("trang_thai") != "da_duyet":
        return None, "chân dung chưa qua CỔNG 0 — chờ `id.py chan-dung --duyet «tên người»`"
    return pho, None


# ══════════ THƯ VIỆN CHÂN DUNG KF-62 v2.2 — ⛔ KHÔNG phác họa theo kỳ ══════════
# Từ 02/11/2026 chân dung KHÔNG còn được phác họa lại mỗi kỳ. Hệ dùng một thư
# viện CỐ ĐỊNH toàn hệ sinh thái: 18 dịch vụ · 85 chân dung · 12 thẻ ngữ cảnh.
#
#   Trước: CD1…CDn do agent phác họa từ hội thoại của kỳ, người duyệt ở CỔNG 0.
#          ⛔ Mã đổi nghĩa mỗi kỳ → không so được giữa các kỳ.
#   Nay  : mã đọc được và cố định, vd `SACTO-NAM_TAI_PHAT`. So được giữa các kỳ,
#          dùng chung với Sale, pháp chế và các agent khác.
#
# Một hội thoại = ĐÚNG MỘT chân dung × TỐI ĐA BA thẻ × một nhãn nóng (id-D §2).
# ⛔ Thẻ ngữ cảnh KHÔNG phải chân dung: «ở tỉnh», «so giá», «nam giới» là THẺ.
# ⛔ «Chỉ hỏi giá, chưa nói tình trạng» là TRẠNG THÁI LEAD, không gán chân dung.

THU_VIEN = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chan_dung_kf62.json")
_TV = None


def nap_thu_vien():
    """Đọc thư viện KF-62. ⛔ Thiếu file thì dừng — không có bộ mặc định nào khác."""
    global _TV
    if _TV is None:
        if not os.path.exists(THU_VIEN):
            sys.exit("⛔ Không có tools/chan_dung_kf62.json — thư viện chân dung là "
                     "bắt buộc từ bản KF-62 v2.2.")
        with open(THU_VIEN, encoding="utf-8") as f:
            _TV = json.load(f)
    return _TV


def gan_dich_vu_kf62(ht, tv):
    """Hội thoại thuộc dịch vụ nào. Tin CỤM của bản xuất trước, rồi mới đọc chữ khách."""
    cum = str(ht.get("cum_knb") or ht.get("dich_vu_knb") or "")
    for ma, d in tv["dich_vu"].items():
        if cum and cum in (d.get("cum_knb") or []):
            return ma, "cụm bản xuất"
    # Cụm gộp nhiều thứ → đọc chữ khách theo đúng thứ tự ưu tiên đã khai.
    nn = (tv.get("cum_knb_nhap_nhang") or {}).get(cum)
    kh = ht["kh_text"]
    if nn:
        for ma in nn.get("uu_tien") or []:
            if co_tu(kh, tv["dich_vu"][ma]["router"]):
                return ma, "chữ khách (cụm gộp)"
    # Không khai cụm → chạy router trên chữ khách, lấy dịch vụ trúng nhiều từ nhất.
    diem = [(len(tu_khop(kh, d["router"])), ma) for ma, d in tv["dich_vu"].items()]
    diem.sort(reverse=True)
    if diem and diem[0][0] > 0:
        return diem[0][1], "chữ khách"
    return None, "⛔ không xếp được dịch vụ"


def gan_chan_dung_kf62(ht, tv, dich_vu):
    """Chạy THỨ TỰ KIỂM TRA của dịch vụ: câu «Có» ĐẦU TIÊN quyết định chân dung.

    ⛔ Không chấm điểm, không lấy cái khớp nhiều từ nhất — KF-62 quy định thứ tự,
    và thứ tự đó có lý do: tiền sử can thiệp và vấn đề y khoa phải hỏi TRƯỚC mục
    tiêu thẩm mỹ, nếu không thì ca sửa hỏng bị xếp nhầm thành ca làm lần đầu.
    """
    if not dich_vu:
        # ⛔ KHÔNG trả None: 102 HT của kỳ 24-29/10 đã lọt ra CSV và hàng chờ Sale
        # với ô chân dung RỖNG, trong khi bảng chân dung đếm chúng là mã dự trữ.
        # Hai con số cho một hội thoại. Mã dự trữ phải gán NGAY ở đây (id-M §1).
        return CD_DU, ""
    kh = ht["kh_text"]
    for c in sorted(tv["dich_vu"][dich_vu]["chan_dung"], key=lambda x: x["thu_tu"]):
        if not c["tu"]:
            continue
        hit = tu_khop(kh, c["tu"])
        if hit:
            return c["ma"], hit[0]
    return dich_vu + "-CHUA_XAC_DINH", ""


def gan_the(ht, tv):
    """Tối đa BA thẻ ngữ cảnh, theo đúng thứ tự AR01→AR12 (KF-62 §2)."""
    kh = ht["kh_text"]
    ra = []
    for ma, t in tv["the_ngu_canh"].items():
        if co_tu(kh, t["tu"]):
            ra.append(ma)
        if len(ra) >= 3:
            break
    return ra


def trang_thai_lead(ht, td, ma_o, rao_can):
    """Trạng thái NGOÀI chân dung — KF-62 §1 và bước 0 của KF-60."""
    if "hỏi giá ngay" in rao_can and "chưa nói tình trạng" in rao_can:
        return "CHI_HOI_GIA"
    return ""


def gan_chan_dung(ht, pho):
    """Gán theo DẤU HIỆU của bản phác họa đã duyệt, xét từ trên xuống.

    Dòng đầu khớp thì lấy dòng đó → xếp chân dung HẸP trước, RỘNG sau.
    ⚠ DI SẢN: nay chân dung do `gan_chan_dung_kf62()` quyết (`id-M`).
    Không khớp dòng nào → CD0, mã dự trữ, ⛔ không phải "rác".
    """
    if not pho:
        return None
    kh = ht["kh_text"]
    for c in pho["tep"]:
        if not co_tu(kh, c["dau_hieu"]):
            continue
        if c.get("khong_phai") and co_tu(kh, c["khong_phai"]):
            continue
        return c["ma"]
    return CD_DU


def gan_nac(ht, td):
    """Gán nấc 5A: đọc câu hỏi ĐẦU TIÊN của khách, ⛔ không đọc cả hội thoại (id-D §3)."""
    dau = next((t["text"] for t in ht["tin"] if not t["nv"] and len(t["text"]) > 3), "")
    if co_tu(dau, td["ma_o"]["O-09"] + ["còn suất", "ưu đãi", "đặt lịch"]):
        return "A4"
    if co_tu(dau, td["ma_o"]["O-01"] + td["ma_o"]["O-04"] + td["ma_o"]["O-05"] + td["ma_o"]["O-07"]):
        return "A3"
    if co_tu(dau, ["công nghệ", "phương pháp", "cấu trúc", "sụn", "loại nào", "dáng nào", "khác gì"]):
        return "A2"
    if co_tu(dau, ["kiêng", "tái khám", "sau mổ", "hậu phẫu"]):
        return "A5"
    return "A1"


def gan_ma_o(ht, td):
    kh = ht["kh_text"]
    ma = [m for m, tu in td["ma_o"].items() if co_tu(kh, tu)]
    # Khách gửi ảnh tình trạng mà không tả bằng chữ vẫn là O-08 "không biết mình cần gì".
    if ht.get("kh_gui_anh") and "O-08" not in ma:
        ma.append("O-08")
    if ma:
        return sorted(ma)
    # ⚠ Phân biệt hai thứ hay bị gộp:
    #   "(chưa nêu)" = khách chưa nói gì đủ để có phản đối  → KHÔNG tính vào O-00
    #   "O-00"       = khách CÓ nêu điều gì đó mà danh sách 12 mã không chứa
    #                  → vượt 10% mẫu là tín hiệu phải bổ sung từ điển (id-D §1)
    return ["(chưa nêu)"] if len(re.sub(r'\W+', '', kh)) < 20 else ["O-00"]


def gan_nhiet(ht, td):
    th = []
    kh = ht["kh_text"]
    if co_tu(kh, sum(td["dich_vu_chinh"].values(), [])) or ht.get("kh_gui_anh"):
        th.append("1_dich_vu")
    if co_tu(kh, td["tin_hieu_nong"]["2_thoi_gian"]):
        th.append("2_thoi_gian")
    if ht["co_sdt"]:
        th.append("3_sdt")
    if co_tu(kh, td["tin_hieu_nong"]["4_dieu_kien"]):
        th.append("4_dieu_kien")
    if co_tu(kh, td["tin_hieu_nong"]["5_khung_gio"]):
        th.append("5_khung_gio")
    n = len(th)
    muc = "HOT" if n >= 4 else ("WARM" if n >= 2 else "COLD")
    return muc, th


def gan_dich_vu(ht, td):
    kh = ht["kh_text"]
    for dv, tu in td["dich_vu_chinh"].items():
        if co_tu(kh, tu):
            return dv
    return "(chưa nêu)"


def he_so_gia_tri(ht, td):
    kh = ht["kh_text"]
    for bac in ("3", "2", "1"):
        if co_tu(kh, td["gia_tri_don"][bac]):
            return int(bac)
    return 1


def gan_vi_sao_roi(ht, td, diem):
    """Mỗi hội thoại ĐÚNG MỘT giá trị (id-D §4)."""
    if ht["co_sdt"] or ht.get("chot_lich"):
        return "không rơi"
    tin = ht["tin"]
    kh_luot = sum(1 for t in tin if not t["nv"])
    nv_luot = sum(1 for t in tin if t["nv"])
    if nv_luot == 0:
        return "hệ thống"
    cuoi = tin[-1]
    if cuoi["nv"] and kh_luot >= 2:
        return "khách tự dừng"
    if kh_luot == 1 and nv_luot >= 1:
        return "trực page"
    if diem is not None and diem < 55:
        return "trực page"
    if co_tu(ht["kh_text"], td["ma_o"]["O-01"]) and not co_tu(ht["nv_text"], ["triệu", "tr ", "giá từ", "khoảng"]):
        return "hệ thống"
    return "khách tự dừng"


# Rào cản suy ra từ mã O. Hai nhãn "đã làm nơi khác" và "chờ ưu đãi" nhận bằng
# từ khoá ở tu_dien.json → `rao_can`; "chưa nói tình trạng" và "hỏi giá ngay"
# tính riêng bên dưới.
# ⛔ Không nhãn nào được suy ra từ CHÂN DUNG. Chân dung của kỳ do người dùng duyệt
#   ở CỔNG 0 — lấy nó làm căn cứ chấm rào cản là chấm lại hội thoại (luật ③).
RAO_CAN = {
    "sợ đau/nghỉ việc": "O-04",
    "ở xa": "O-09",
    "người nhà cản": "O-11",
    "so giá đối thủ": "O-10",
    "chưa tin cơ sở": "O-06",
}


def gan_rao_can(ht, td, ma_o):
    rc = []
    kh = ht["kh_text"]
    # Khách không nêu được dịch vụ nào và cũng không gửi ảnh tình trạng
    # → chưa nói tình trạng. ⚠ Đây là tình trạng của HỘI THOẠI, không phải
    #   của chân dung: quảng cáo kéo được người vào mà không làm họ kể.
    if not co_tu(kh, sum(td["dich_vu_chinh"].values(), [])) and not ht.get("kh_gui_anh"):
        rc.append("chưa nói tình trạng")
    dau = next((t["text"] for t in ht["tin"] if not t["nv"] and len(t["text"]) > 3), "")
    if co_tu(dau, td["ma_o"]["O-01"]):
        rc.append("hỏi giá ngay")
    for ten, tu in td.get("rao_can", {}).items():
        if ten.startswith("_") or not isinstance(tu, list):
            continue
        if co_tu(kh, tu):
            rc.append(ten)
    for ten, ma in RAO_CAN.items():
        if isinstance(ma, str) and ma in ma_o:
            rc.append(ten)
    return sorted(set(rc))


# ══════════════ bộ chấm lead KF-60 v1.1 — XẾP HÀNG CHỜ GỌI ══════════════
# ⛔ Bộ này KHÔNG thay nhãn 5 tín hiệu của `id-D` §2. Nhãn báo ra ngoài vẫn là
#    `nhiet`. Điểm dưới đây là THỨ TỰ GỌI bên trong một nhãn, cộng 6 luật ghi đè.
#    Hai nơi cùng gọi một hội thoại là HOT theo hai cách khác nhau thì không ai
#    còn tin con số nào — vì thế mỗi bản ghi mang CẢ HAI nhãn và một cờ `lech`.
#
#    Tiêu chí, bằng chứng hiệu chỉnh và ba ngưỡng tạm:
#    knowledge/id-L-lead-scoring-kf60.md

KF60 = "KF-60/1.1"
TRAN_AM = -30                         # trần nhóm tín hiệu âm (§5)

# ★ ĐO RỒI MỚI CHỐT. Chấm 493 hội thoại kỳ 24–29/10 bằng đúng thang điểm KF-60:
#   điểm gốc trung vị 12 · p75 20 · p90 35 · CAO NHẤT 65. Chỉ 5 hội thoại vượt 50.
#   ⛔ Vì vậy KF-60 ⛔ KHÔNG phát nhãn HOT/WARM/COLD: không có cặp ngưỡng nào
#   làm nhãn đó khớp nhãn 5 tín hiệu của id-D (lệch thấp nhất đo được là 12.8%,
#   và cấu hình đó chỉ cho 5 lead vào hàng chờ — vô dụng). Hai bộ đo hai thứ
#   khác nhau CÓ CHỦ Ý: id-D đếm 5 tín hiệu nhị phân, KF-60 cân 19 tiêu chí.
#   Bắt chúng khớp nhau là sai đề.
#
#   Đầu ra của bộ này là VIỆC, không phải nhãn: bốn NHÓM GỌI dưới đây.
NGUONG_NUOI = 17                      # p75 của phân bố nhiệt đo được
NHOM_GOI = {
    "GOI_NGAY": "Sale gọi ≤15′ — có SĐT và khớp luật ghi đè",
    "XIN_SO": "Trực page xin số ≤15′ — nóng mà chưa có SĐT",
    "NUOI": "Chuỗi chăm sóc 24–72h theo mã O",
    "KHONG": "Remarketing tự động",
}
B3_CHU_DE = ("b3_bac_si", "b3_quy_trinh", "b3_gay_me", "b3_hoi_phuc",
             "b3_bao_hanh", "b3_chat_lieu")

TEN_LUONG = {
    "LEAD": "Lead — chấm nhiệt độ",
    "N1a": "Chưa tương tác thật",
    "N1b": "Đã trả lời rồi khách im",
    "N2": "Không phải lead",
    "N3": "Khách cũ – CSKH",
    "N4": "Cảnh báo đỏ",
    "N5": "Chưa đủ điều kiện",
}
TEN_GHI_DE = {
    "HOT_SDT_MOC": "① có SĐT + mốc thời gian/lịch cụ thể",
    "HOT_COC": "② hỏi cách chuyển cọc",
    "HOT_SDT_DV": "③ có SĐT + dịch vụ cụ thể hoặc ≥2 chủ đề quyết định",
    "HOT_CHUA_SO": "④⑤ nóng mà chưa có SĐT",
    "TRAN_WARM": "⑥ có SĐT nhưng nhóm B = 0",
}
HE_SO_TG = ((24, 1.0), (72, 0.85), (168, 0.7))      # ≤24h · 1–3 ngày · 4–7 ngày


def _lk(td, ten):
    return td.get("lead_kf60", {}).get(ten) or []


def _phan_luong(ht, td):
    """Bước 0 (§3). ⚠ `N1b` vẫn được chấm như LEAD — đó là sửa chính của v1.1."""
    kh = ht["kh_text"]
    if co_tu(kh, _lk(td, "n4_canh_bao_do")):
        return "N4"
    if co_tu(kh, _lk(td, "n2_khong_phai_lead")):
        return "N2"
    if co_tu(kh, _lk(td, "n5_chua_du_dieu_kien")):
        return "N5"
    if ht.get("khach") == "cu" and co_tu(kh, _lk(td, "n3_khach_cu")):
        return "N3"
    luot_kh = sum(1 for t in ht["tin"] if not t["nv"])
    co_nv = any(t["nv"] for t in ht["tin"])
    if luot_kh <= 1 and not co_nv:
        return "N1a"
    # Khách được trả lời rồi mới im: ⛔ KHÔNG phải N1a. Là lead thật, và là
    # bằng chứng lỗi câu trả lời — 43.9% hội thoại của kỳ 24–29/10 rơi kiểu này.
    if luot_kh <= 2 and co_nv and not ht["co_sdt"]:
        return "N1b"
    return "LEAD"


def _trung_vi(ds):
    if not ds:
        return None
    s = sorted(ds)
    m = len(s) // 2
    return s[m] if len(s) % 2 else (s[m - 1] + s[m]) / 2.0


def cham_lead(ht, td, ma_o, rao_can, roi, cham, nhiet_id_d, he_so, moc_chot=None):
    """Chấm một hội thoại theo KF-60 v1.1. Trả về dict đủ để truy ngược từng ô."""
    kh = ht["kh_text"]
    tin = ht["tin"]
    tin_kh = [t for t in tin if not t["nv"]]
    luot_kh = len(tin_kh)
    co_sdt = bool(ht["co_sdt"])
    chot = bool(ht.get("chot_lich"))
    route = _phan_luong(ht, td)

    o = {}          # từng ô tiêu chí → điểm, để người đọc cãi được

    # ── A · nhu cầu & mức phù hợp (tối đa 25) ───────────────────────────
    if co_tu(kh, sum(td["dich_vu_chinh"].values(), [])):
        o["A1"] = 8                                  # khách TỰ gọi tên dịch vụ
    elif ht.get("kh_gui_anh") or ht.get("gan_theo_qc"):
        o["A1"] = 4                                  # chỉ biết qua ảnh / thẻ QC
    else:
        o["A1"] = 0
    o["A2"] = 8 if ht.get("kh_gui_anh") else (4 if "chưa nói tình trạng" not in rao_can else 0)
    o["A3"] = 5 if co_tu(kh, _lk(td, "a3_se_den")) else (3 if ht.get("viet_kieu") else 0)
    o["A4"] = 4 if (co_tu(kh, _lk(td, "a4_cho_minh"))
                    or co_tu(kh, _lk(td, "a4_nguoi_than"))) else 0

    # ── B · ý định mua (tối đa 35) ──────────────────────────────────────
    if co_tu(kh, _lk(td, "b1_hai_tuan")):
        o["B1"] = 12
    elif co_tu(kh, _lk(td, "b1_mot_thang")):
        o["B1"] = 9
    elif co_tu(kh, _lk(td, "b1_ba_thang")):
        o["B1"] = 5
    else:
        o["B1"] = 0
    if co_tu(kh, _lk(td, "b2_cam_ket_tien")):
        o["B2"] = 8
    elif "O-01" in ma_o:
        # «hỏi giá ngay» = giá nằm ở CÂU ĐẦU, chưa kể gì về mình → giá trống không.
        o["B2"] = 2 if "hỏi giá ngay" in rao_can else 5
    else:
        o["B2"] = 0
    cd = sum(1 for g in B3_CHU_DE if co_tu(kh, _lk(td, g)))
    o["B3"] = 8 if cd >= 2 else (4 if cd == 1 else 0)
    o["B4"] = 7 if "O-10" in ma_o else 0

    # ── C · cam kết hành động (tối đa 25) ───────────────────────────────
    o["C1"] = 12 if co_sdt else 0
    o["C2"] = 8 if chot else (4 if co_tu(kh, _lk(td, "c2_hoi_lich")) else 0)
    co_coc = co_tu(kh, _lk(td, "c3_coc"))
    # ⚠ v1.1 hạ hỏi-địa-chỉ 5 → 2: nhóm khách tỉnh hỏi địa chỉ rất nhiều mà
    #   chỉ 9.4% cho SĐT. Hỏi ĐƯỜNG ĐI không phải cam kết; hỏi CHUYỂN CỌC thì có.
    o["C3"] = 5 if co_coc else (2 if co_tu(kh, _lk(td, "c3_duong_di")) else 0)

    # ── D · mức tương tác (tối đa 15) ───────────────────────────────────
    o["D1"] = 6 if luot_kh > 10 else (5 if luot_kh >= 6 else (3 if luot_kh >= 3 else 0))
    vt_gia = next((i for i, t in enumerate(tin)
                   if t["nv"] and co_tu(t["text"], _lk(td, "nv_da_neu_gia"))), None)
    nv_neu_gia = vt_gia is not None
    o["D2"] = 5 if (nv_neu_gia and any(i > vt_gia for i, t in enumerate(tin) if not t["nv"])) else 0
    tre = []
    for i, t in enumerate(tin[:-1]):
        if t["nv"] and not tin[i + 1]["nv"]:
            d = phut(t["tem"], tin[i + 1]["tem"])
            if d is not None and d >= 0:
                tre.append(d)
    tv = _trung_vi(tre)
    o["D3"] = 0 if tv is None else (4 if tv < 10 else (2 if tv < 60 else 0))

    # ── E · tín hiệu âm (trần −30) ──────────────────────────────────────
    # ⛔ LUẬT v1.1: chỉ trừ E1/E3 khi hội thoại rơi vì «khách tự dừng».
    #    Khách im sau một câu trả lời không đóng được nỗi sợ ⛔ không phải khách
    #    nguội — đó là lead còn nóng bị trả lời sai, và là việc của id-F.
    kh_tu_dung = (roi == "khách tự dừng")
    gio_im = None
    moc_cuoi_kh = tin_kh[-1]["tem"] if tin_kh else None
    if moc_chot and moc_cuoi_kh:
        p = phut(moc_cuoi_kh, moc_chot)
        gio_im = round(p / 60.0, 1) if p is not None and p >= 0 else None
    o["E1"] = -10 if (kh_tu_dung and nv_neu_gia and gio_im is not None and gio_im >= 48) else 0
    o["E2"] = -5 if (kh_tu_dung and co_tu(kh, _lk(td, "e2_phan_doi_gia"))) else 0
    so_xin = sum(1 for t in tin if t["nv"] and co_tu(t["text"], td["nv_xin_so"]))
    o["E3"] = -5 if (kh_tu_dung and so_xin >= 2 and not co_sdt
                     and cham.get("N5.1") == "✓") else 0
    o["E4"] = -5 if co_tu(kh, _lk(td, "e4_hoi_cho_biet")) else 0
    o["E5"] = -5 if ("O-09" in ma_o and not co_tu(kh, _lk(td, "a3_se_den"))) else 0

    nhom = {g: sum(v for k, v in o.items() if k[0] == g) for g in "ABCDE"}
    nhom["E"] = max(nhom["E"], TRAN_AM)
    goc = max(0, nhom["A"] + nhom["B"] + nhom["C"] + nhom["D"] + nhom["E"])

    # ── Bước 4 · hệ số thời gian ────────────────────────────────────────
    hs = 1.0
    if not chot and gio_im is not None:
        hs = next((h for moc, h in HE_SO_TG if gio_im <= moc), 0.5)
    nhiet_ht = round(goc * hs, 1)

    # ── Bước 3 · luật ghi đè → NHÓM GỌI ────────────────────────────────
    ghi_de = []
    if route in ("N2", "N3", "N4", "N5", "N1a"):
        return {"route": route, "ten_luong": TEN_LUONG[route], "cham_nhiet": False,
                "o": o, "nhom": nhom, "goc": goc, "he_so_tg": hs, "gio_im": gio_im,
                "diem": None, "nhom_goi": None, "ghi_de": [], "uu_tien": None,
                "chua_so": False}
    if co_sdt and (o["B1"] >= 9 or chot):
        ghi_de.append("HOT_SDT_MOC")
    if co_coc:
        ghi_de.append("HOT_COC")
    if co_sdt and (o["A1"] == 8 or o["B3"] == 8):
        ghi_de.append("HOT_SDT_DV")
    # ⑥ để số vì form/ưu đãi mà chưa có ý định thật → ⛔ không vào hàng gọi ngay
    tran = co_sdt and nhom["B"] == 0 and bool(ghi_de)
    if tran:
        ghi_de.append("TRAN_WARM")

    # ── Bốn nhóm gọi ────────────────────────────────────────────────────
    # ★ Nhóm XIN_SO tái tạo đúng ô đỏ của id-D §2 — nóng mà chưa vào tay
    #   telesale. Người phải làm là TRỰC PAGE, ⛔ không phải Sale.
    nong_id_d = nhiet_id_d in ("HOT", "WARM")
    if co_sdt and ghi_de and not tran:
        nhom_goi = "GOI_NGAY"
    elif not co_sdt and (nong_id_d or nhiet_ht >= NGUONG_NUOI):
        nhom_goi = "XIN_SO"
    elif co_sdt or nong_id_d or nhiet_ht >= NGUONG_NUOI:
        nhom_goi = "NUOI"
    else:
        nhom_goi = "KHONG"
    chua_so = nhom_goi == "XIN_SO"
    if chua_so:
        ghi_de.append("HOT_CHUA_SO")

    return {"route": route, "ten_luong": TEN_LUONG[route], "cham_nhiet": True,
            "o": o, "nhom": nhom, "goc": goc, "he_so_tg": hs, "gio_im": gio_im,
            "diem": nhiet_ht, "nhom_goi": nhom_goi, "ghi_de": ghi_de,
            "uu_tien": round(nhiet_ht * (he_so or 1), 1), "chua_so": chua_so}


def viec_cua(ma_cd, nhom_goi):
    """Việc phải làm = CHÂN DUNG (KF-62) × NHÓM GỌI (KF-60).

    ★ Đây là chỗ hai bộ gặp nhau. Nhóm gọi nói GỌI AI TRƯỚC và AI gọi; chân dung
    nói NÓI GÌ với người đó. Thiếu một trong hai thì hàng chờ ⛔ không dùng được:
    biết gọi mà không biết nói, hoặc biết nói mà không biết gọi ai trước.
    """
    tv = nap_thu_vien()
    lk = tv.get("lien_ket_kf60") or {}
    mac_dinh = (lk.get("mac_dinh") or {}).get(nhom_goi, "")
    if not ma_cd:
        return mac_dinh, True
    for dv in tv["dich_vu"].values():
        for c in dv["chan_dung"]:
            if c["ma"] == ma_cd and c.get("hanh_dong"):
                return c["hanh_dong"].get(nhom_goi) or mac_dinh, False
    return mac_dinh, True


def gom_lead(ban_ghi):
    """Gom khối `lead` cho file báo cáo (id-J §2b).

    ⛔ Không chữ của khách trong khối này: hàng chờ chỉ mang mã HT, dịch vụ,
    mã O và việc phải làm. Nội dung hội thoại ở lại out/ban-ghi.json.
    """
    cham = [r for r in ban_ghi if (r.get("lead") or {}).get("cham_nhiet")]
    n = len(cham)

    def dem_nhom(x):
        return sum(1 for r in cham if r["lead"]["nhom_goi"] == x)

    # ── Hai bất biến THẬT, thay cho luật «lệch nhãn 5%» đã bỏ ───────────
    #    Luật cũ bắt hai bộ đo khác nhau phải khớp nhãn — sai đề. Hai luật
    #    dưới đây kiểm được và phải luôn đúng; khác 0 là lỗi code, ⛔ không
    #    phải chuyện hiệu chỉnh ngưỡng.
    v1 = [r["ma"] for r in cham
          if r["lead"]["nhom_goi"] == "GOI_NGAY" and not r["co_sdt"]]
    v2 = [r["ma"] for r in cham
          if r["nhiet"] == "HOT" and r["lead"]["nhom_goi"] == "KHONG"]

    hang = sorted([r for r in cham if r["lead"]["nhom_goi"] in ("GOI_NGAY", "XIN_SO")],
                  key=lambda r: (r["lead"]["nhom_goi"] != "GOI_NGAY",
                                 -(r["lead"]["uu_tien"] or 0)))
    return {
        "bo_cham": KF60,
        "nguong_nuoi": NGUONG_NUOI,
        "so_cham": n,
        "phan_luong": [{"ma": m, "ten": TEN_LUONG[m],
                        "so": sum(1 for r in ban_ghi
                                  if (r.get("lead") or {}).get("route") == m)}
                       for m in ("LEAD", "N1b", "N1a", "N3", "N5", "N2", "N4")],
        "nhom_goi": [{"ma": m, "ten": NHOM_GOI[m], "so": dem_nhom(m),
                      "pct": pct(dem_nhom(m), n)}
                     for m in ("GOI_NGAY", "XIN_SO", "NUOI", "KHONG")],
        "chua_so": dem_nhom("XIN_SO"),
        "ghi_de": [{"ma": m, "ten": TEN_GHI_DE[m],
                    "so": sum(1 for r in cham if m in r["lead"]["ghi_de"])}
                   for m in ("HOT_SDT_MOC", "HOT_COC", "HOT_SDT_DV",
                             "TRAN_WARM", "HOT_CHUA_SO")],
        "nhom_diem": [{"nhan": g, "trung_binh": round(
            sum(r["lead"]["nhom"][g] for r in cham) / n, 1) if n else None,
            "toi_da": {"A": 25, "B": 35, "C": 25, "D": 15, "E": -30}[g],
            "cao_nhat": max([r["lead"]["nhom"][g] for r in cham], default=None)}
            for g in "ABCDE"],
        "diem": {"trung_vi": _trung_vi([r["lead"]["diem"] for r in cham]),
                 "cao_nhat": max([r["lead"]["diem"] for r in cham], default=None),
                 "goc_cao_nhat": max([r["lead"]["goc"] for r in cham], default=None)},
        # Nhóm gọi × nhãn id-D: bảng này cho người đọc thấy HAI bộ nói gì về
        # cùng một tệp, ⛔ không phải để bắt chúng khớp nhau.
        "doi_chieu": [{"id_d": m,
                       "nhom": {k: sum(1 for r in cham if r["nhiet"] == m
                                       and r["lead"]["nhom_goi"] == k)
                                for k in ("GOI_NGAY", "XIN_SO", "NUOI", "KHONG")}}
                      for m in ("HOT", "WARM", "COLD")],
        "bat_bien": {"goi_ngay_thieu_sdt": len(v1), "id_d_hot_roi_khong": len(v2),
                     "dat": not (v1 or v2),
                     "ht_v1": v1[:20], "ht_v2": v2[:20]},
        "hang_cho": [{"ht": r["ma"], "cd": r.get("cd") or CD_DU, "dich_vu": r.get("dich_vu"),
                      "he_so": r.get("he_so"), "nhom_goi": r["lead"]["nhom_goi"],
                      "id_d": r["nhiet"], "diem": r["lead"]["diem"],
                      "uu_tien": r["lead"]["uu_tien"], "co_sdt": bool(r["co_sdt"]),
                      "ma_o": [m for m in r["ma_o"] if m != "(chưa nêu)"],
                      "ghi_de": r["lead"]["ghi_de"], "gio_im": r["lead"]["gio_im"],
                      "viec": ("Sale gọi ≤15′" if r["lead"]["nhom_goi"] == "GOI_NGAY"
                               else "Trực page xin số ≤15′"),
                      "the": r.get("the") or [],
                      "viec_chi_tiet": viec_cua(r.get("cd"), r["lead"]["nhom_goi"])[0],
                      "viec_mac_dinh": viec_cua(r.get("cd"), r["lead"]["nhom_goi"])[1]}
                     for r in hang],
        "viec_mac_dinh": sum(1 for r in hang
                             if viec_cua(r.get("cd"), r["lead"]["nhom_goi"])[1]),
        "ghi_chu": [
            "Nhãn HOT/WARM/COLD của kỳ là nhãn 5 tín hiệu (id-D §2). KF-60 ⛔ KHÔNG "
            "phát nhãn thứ hai — nó chia tệp thành bốn NHÓM GỌI và xếp thứ tự trong nhóm.",
            "Ngưỡng nuôi ≥%d là p75 của phân bố nhiệt đo trên kỳ này — ⚠ chưa có "
            "dòng CRM để đối chiếu booking thật." % NGUONG_NUOI,
            "Hệ số thời gian tính từ tin cuối của khách tới mốc chốt dữ liệu của kỳ, "
            "⛔ không tính tới «bây giờ».",
            "Chấm tự động bằng tools/id.py, CHƯA qua người soát.",
        ],
    }


# ───────────── nguyên liệu PHÁC HỌA chân dung — bước B3 ──────────────────
# ⛔ Phần này KHÔNG xếp chân dung. Nó chỉ bày ra chữ của khách để agent đọc và
#   phác họa, rồi người dùng duyệt ở CỔNG 0. ⚠ DI SẢN — xem `id-M` §1.

RE_TACH_TU = re.compile(r"[^0-9A-Za-zÀ-ỹ]+")


def _tach_tu(text):
    t = unicodedata.normalize("NFC", (text or "")).lower()
    return [x for x in RE_TACH_TU.split(t) if len(x) > 1]


def cum_chu_khach(cap_ht_text, tu_dung, toi_thieu, lay=60):
    """Cụm 2–3 chữ khách tự nói, đếm theo SỐ HỘI THOẠI chứa cụm.

    ⚠ Đếm theo hội thoại, ⛔ không theo số lần xuất hiện: một người nhắc
    «đầu mũi bóng đỏ» chín lần không làm cụm đó thành tiếng của chín người.
    """
    dem, vi_du = Counter(), defaultdict(list)
    for ma, text in cap_ht_text:
        tu = _tach_tu(text)
        cum = set()
        for k in (2, 3):
            for i in range(len(tu) - k + 1):
                p = tu[i:i + k]
                if p[0] in tu_dung or p[-1] in tu_dung:
                    continue          # bỏ cụm mở/đóng bằng từ dừng
                if all(x in tu_dung for x in p):
                    continue
                cum.add(" ".join(p))
        for c in cum:
            dem[c] += 1
            if len(vi_du[c]) < 6:
                vi_du[c].append(ma)
    ra = [{"cum": c, "so_ht": v, "ht": vi_du[c]} for c, v in dem.most_common() if v >= toi_thieu]
    return ra[:lay]


def nguyen_lieu_chan_dung(ban_ghi, hts, td, ky, nguon):
    n = len(ban_ghi)
    theo_ma = {h["ma"]: h for h in hts}
    tu_dung = set(td.get("_tu_dung") or [])
    toi_thieu = max(3, int(round(n * 0.02)))
    cum = cum_chu_khach([(r["ma"], theo_ma[r["ma"]]["kh_text"]) for r in ban_ghi],
                        tu_dung, toi_thieu)
    cau_dau = []
    for r in ban_ghi:
        tin = theo_ma[r["ma"]]["tin"]
        dau = next((t["text"] for t in tin if not t["nv"] and len(t["text"]) > 3), "")
        cau_dau.append({"ht": r["ma"], "nac": r["nac"], "dich_vu": r["dich_vu"],
                        "nhiet": r["nhiet"], "ma_o": r["ma_o"], "co_sdt": r["co_sdt"],
                        "rao_can": r["rao_can"], "cau_dau": an_danh(dau)[:200]})
    return {
        "schema": "nguyen-lieu-chan-dung/1",
        "ky": ky, "nguon": nguon, "so_ht": n,
        "tao": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "muc_dich": "⚠ DI SẢN của lối phác họa theo kỳ (xem id-M §1). "
                    "⛔ Đây CHƯA phải chân dung.",
        "nguong_cum": toi_thieu,
        "cum_chu": cum,
        "dich_vu": dict(Counter(r["dich_vu"] for r in ban_ghi).most_common()),
        "nac": dict(Counter(r["nac"] for r in ban_ghi)),
        "rao_can": [{"nhan": a, "so": b} for a, b in
                    Counter(rc for r in ban_ghi for rc in r["rao_can"]).most_common()],
        "cau_dau": cau_dau,
        "ghi_chu": [
            "Cụm chữ đếm theo SỐ HỘI THOẠI chứa cụm, ngưỡng ≥ %d HT." % toi_thieu,
            "Câu đầu đã ẩn danh — số điện thoại, email, link thay bằng «…» (luật ⑩).",
            "⛔ Cụm chữ đông nhất KHÔNG tự thành một chân dung. Chân dung cần một "
            "NỖI SỢ riêng và truy ngược được về HT-nnn — xem id-M §1.",
        ],
    }


# ──────────────────────── chấm điểm nhân viên N1–N6 ──────────────────────

TIEU_CHI = [
    ("N1", "Phản hồi & SLA", [
        ("N1.1", "Trả lời tin đầu ≤2 phút", 8),
        ("N1.2", "Không để khách bỏ sau 1 lượt", 6),
        ("N1.3", "Không bỏ sót câu hỏi của khách", 3),
        ("N1.4", "Theo đuổi lại khi khách im", 3)]),
    ("N2", "Khai thác tình trạng", [
        ("N2.1", "Hỏi tình trạng trước khi báo giá / xin số", 8),
        ("N2.2", "Có ≥2 câu hỏi mở", 4),
        ("N2.3", "Mời gửi ảnh / tả vùng cụ thể", 4),
        ("N2.4", "Nhắc lại đúng điều khách vừa nói", 4)]),
    ("N3", "Trả lời đúng & minh bạch", [
        ("N3.1", "Nêu khung giá khi khách hỏi giá", 6),
        ("N3.2", "Thông tin khớp bảng hiện hành", 5),
        ("N3.3", "Không cam kết kết quả", 5),
        ("N3.4", "Không nói quá về bác sĩ / chứng chỉ", 4)]),
    ("N4", "Xử lý rào cản", [
        ("N4.1", "Nhận diện đúng mã O khách nêu", 5),
        ("N4.2", "Xử đúng tầng", 5),
        ("N4.3", "Giữ cửa mở", 5)]),
    ("N5", "Xin số & chốt", [
        ("N5.1", "Xin số có lý do cụ thể", 6),
        ("N5.2", "Xin lại lần 2 khác cách", 4),
        ("N5.3", "Hỏi khung giờ nghe máy", 4),
        ("N5.4", "Mời lịch cụ thể ngày + giờ", 6)]),
    ("N6", "Ngôn từ & thái độ", [
        ("N6.1", "Không dán khối dài lệch câu hỏi", 2),
        ("N6.2", "Xưng hô, chính tả đọc được", 2),
        ("N6.3", "Không gắt, không ép khách", 1)]),
]
DIEM = {ma: d for _, _, ds in TIEU_CHI for ma, _, d in ds}



# ══════════ bộ chọn tệp & tầng nội dung KF-64 v1.0 — XẾP HẠNG CHÂN DUNG ══════════
# ★ Bộ này THAY công thức của `id-M` §7. ⛔ Không chạy song song hai bảng xếp
#   hạng chân dung: đó đúng là lỗi đã phải bỏ sổ `id-C` §4.
#
# ⚠ KF-64 v1.0 là bản khối Sale gửi sang, và nó ⛔ KHÔNG trả lời đủ bốn chỗ
#   dưới đây. Người dùng chốt 02/11/2026 «không chờ duyệt nữa», nên repo tự
#   chốt bốn cái — ghi ra đây để còn cãi lại được, ⛔ không chôn trong code:
#
#   ① MẪU SỐ «trung bình dịch vụ» = TIỀN TỐ MÃ KF-62 (18 dịch vụ), ⛔ không
#     phải cột `dich_vu` của `id-G` §3. Lý do: chân dung được ĐỊNH NGHĨA bên
#     trong dịch vụ KF-62 (`id-M` §2); lấy mẫu số kia thì một chân dung bị so
#     với những chân dung không cùng dịch vụ với nó. Cột `dich_vu` vẫn giữ —
#     nó là chỗ lấy hệ số 1/2/3, ⛔ không phải trục chân dung.
#
#   ② `%Hot` của CẢ DỊCH VỤ bằng 0 thì BỎ chỉ số đó, tính Chất lượng bằng
#     nhiệt độ một mình. ⛔ Không tính `%Hot` thành 0: khi mẫu số bằng 0 thì
#     tỷ lệ là KHÔNG XÁC ĐỊNH, ⛔ không phải bằng không. Tính thành 0 là chia
#     đôi Chất lượng của mọi chân dung trong dịch vụ đó — kỳ 24-29/10 có 3 HOT
#     trên 494 nên 6/10 dịch vụ rơi vào đúng cảnh này.
#
#   ③ `điểm hiệu quả` ⛔ KHÔNG có bản dự phòng trong KF-64, mà Chuyển đổi
#     chiếm 62,5% của nó. Dùng đúng cách KF-64 đã làm cho «chỉ số tạm»: chuẩn
#     hoá lại trên những trục ĐO ĐƯỢC → chưa có CRM thì hiệu quả = Chất lượng.
#     ⚠ Ô ③ lúc này đọc là «đông nhưng NGUỘI», ⛔ chưa phải «đông nhưng YẾU» —
#     mọi dòng gắn `tam=True`.
#
#   ④ TÊN TẦNG: giữ `5A` của `id-D` §3, trục phễu của KF-64 đặt `T1…T4`.
#     Lý do: cùng 494 hội thoại, `A2` theo `id-D` = 1 HT, theo KF-64 = 324 HT.
#     ⛔ Một nhãn hai nghĩa thì không bảng nào đọc được. Bảng quy đổi ở KF64_TANG.

KF64 = "KF-64/1.0"
KF64_TS = (0.2, 0.3, 0.5)        # quy mô · chất lượng · chuyển đổi (§3.1)
KF64_TS_TAM = (0.4, 0.6)         # chưa có booking CRM → quy mô · chất lượng
KF64_TRAN = 2.0                  # mỗi trục chặn ở 2,0 — mẫu nhỏ ⛔ không kéo lệch
KF64_MIN_HT = 30                 # dưới ngần này: «chưa đủ dữ liệu», ⛔ không xếp hạng
KF64_MIN_BOOKING = 5
KF64_NGHEN = 0.8                 # bước yếu nhất phải < mốc này mới gọi là nghẽn
KF64_MOC = (110, 90)             # ≥110 CAO · 90–109 TRUNG BÌNH · <90 THẤP
KF64_SAT_MOC = 5.0               # |hiệu quả − 100| nhỏ hơn ngần này: ô ⛔ không chốt được

# Trục phễu của KF-64 — ⛔ KHÔNG dùng tên A1…A4 (xem quyết định ④).
KF64_TANG = {
    "T1": ("T1 · TOF", "Mở tệp — nội dung nhận biết vấn đề", "A1 của id-D"),
    "T2": ("T2 · TOF→MOF", "Nội dung tự phân loại «bạn thuộc kiểu nào»",
           "⚠ đo ở CẤP DỊCH VỤ, ⛔ không ở cấp chân dung"),
    "T3": ("T3 · MOF", "Gỡ rào cản chính · bác sĩ · ca thật · so sánh phương án",
           "A2+A3 của id-D"),
    "T4": ("T4 · BOF", "Giá · ưu đãi có hạn · lịch trống · tốc độ gọi",
           "A4 của id-D"),
}
# Cơ cấu ngân sách khởi điểm theo ô ma trận (§3.2). Ràng buộc KF-50 giữ nguyên:
# BOF ≥ 10% và remarketing ≤ 40% tổng chi của dịch vụ.
KF64_O = {
    "①": ("① Trụ cột", "Lớn + Tốt", "Scale có kiểm soát +15–20%/3 ngày (KF-49)", (30, 40, 30)),
    "②": ("② Ngách hiệu quả", "Nhỏ + Tốt", "Mở rộng tệp — tăng TOF kéo thêm ĐÚNG người", (45, 35, 20)),
    "③": ("③ Đông nhưng yếu", "Lớn + Chưa tốt", "⛔ KHÔNG tăng ngân sách kéo khách — sửa MOF, kịch bản, tốc độ Sale", (15, 55, 30)),
    "④": ("④ Duy trì tối thiểu", "Nhỏ + Chưa tốt", "Giữ remarketing + nội dung nền, xem lại sau 30 ngày", (20, 40, 40)),
}


def _kf64_dv(r):
    """Dịch vụ KF-62 của một bản ghi — quyết định ① ở trên.

    Lấy từ `dich_vu_kf62` nếu khuôn đầu vào có khai (đường KNB); không có thì
    suy từ TIỀN TỐ của mã chân dung. ⛔ Không dùng cột `dich_vu`.
    """
    dv = r.get("dich_vu_kf62")
    if dv:
        return dv
    cd = r.get("cd") or CD_DU
    if cd == CD_DU or "-" not in cd:
        return None
    return cd.split("-")[0]


def _kf64_ti(so, mau):
    """Chỉ số tương đối, chặn ở KF64_TRAN. Mẫu số 0 → None (⛔ KHÔNG phải 0)."""
    if not mau:
        return None
    return min(KF64_TRAN, 1.0 * so / mau)


def _kf64_muc(x):
    if x is None:
        return None
    return "CAO" if x >= KF64_MOC[0] else ("TRUNG BÌNH" if x >= KF64_MOC[1] else "THẤP")


def gom_kf64(ban_ghi):
    """Khối `kf64` — chọn tệp tập trung và tầng nội dung ưu tiên.

    ⛔ Đây là khối MÁY SINH, ⛔ không phải lớp phủ chữ người: mọi con số đều
    suy ra được từ bản ghi, nên để người gõ tay là mở đường cho số không cãi
    được. Phần đọc hiểu đi vào `pheu.van_de` và `ket_luan` như cũ.
    """
    tv = nap_thu_vien()
    ten_dv = {k: v.get("ten", k) for k, v in tv["dich_vu"].items()}
    # ⛔ Chỉ đếm chân dung THẬT: mỗi dịch vụ còn một dòng <DV>-CHUA_XAC_DINH
    #    không có từ nhận dạng — 103 dòng JSON = 85 chân dung + 18 dòng dự trữ.
    so_cd_tv = {k: sum(1 for c in (v.get("chan_dung") or []) if c.get("tu"))
                for k, v in tv["dich_vu"].items()}

    def chua_ro(r):
        cd = r.get("cd") or CD_DU
        return cd == CD_DU or cd.endswith("CHUA_XAC_DINH")

    def nhiet_tb(rs):
        v = [(r.get("lead") or {}).get("diem") for r in rs]
        v = [x for x in v if x is not None]
        return (sum(v) / len(v)) if v else None

    # ── cấp dịch vụ ──────────────────────────────────────────────────────
    theo_dv = {}
    for r in ban_ghi:
        theo_dv.setdefault(_kf64_dv(r), []).append(r)

    dich_vu, chan_dung = [], []
    for dv, rs in sorted(theo_dv.items(), key=lambda kv: -len(kv[1])):
        cr = sum(1 for r in rs if chua_ro(r))
        pct = 100.0 * cr / len(rs)
        dich_vu.append({
            "ma": dv or CD_DU,
            "ten": ten_dv.get(dv, CD_DU if dv is None else dv),
            "ht": len(rs), "chua_ro": cr, "pct_chua_ro": round(pct, 1),
            "ma_thu_vien": so_cd_tv.get(dv, 0),
            # ★ Luật T2 cấp dịch vụ (§4.2) — chạy được ngay, ⛔ không cần CRM.
            "uu_tien_t2": bool(dv and pct >= 30),
            "la_du_tru": dv is None,
        })
        if dv is None:
            continue

        thuc = [r for r in rs if not chua_ro(r)]
        ma_cd = sorted({r["cd"] for r in thuc})
        if not ma_cd:
            continue
        N = len(thuc)
        H = sum(1 for r in thuc if r["nhiet"] == "HOT")
        W = sum(1 for r in thuc if r["nhiet"] == "WARM")
        tb_hot = 100.0 * H / N
        tb_nhiet = nhiet_tb(thuc)
        tb_s3 = 1.0 * (H + W) / N
        tb_s4 = (1.0 * H / (H + W)) if (H + W) else None
        chia_deu = 1.0 / len(ma_cd)

        for m in ma_cd:
            g = [r for r in thuc if r["cd"] == m]
            n = len(g)
            hot = sum(1 for r in g if r["nhiet"] == "HOT")
            warm = sum(1 for r in g if r["nhiet"] == "WARM")
            dm = nhiet_tb(g)

            quy_mo = min(KF64_TRAN, (1.0 * n / N) / chia_deu)
            ti_nhiet = _kf64_ti(dm or 0, tb_nhiet)
            # Quyết định ②: dịch vụ không có HOT nào → BỎ chỉ số %Hot.
            ti_hot = _kf64_ti(100.0 * hot / n, tb_hot)
            co = [x for x in (ti_hot, ti_nhiet) if x is not None]
            chat_luong = min(KF64_TRAN, sum(co) / len(co)) if co else None

            du_mau = n >= KF64_MIN_HT
            if chat_luong is None:
                chi_so = None
            else:
                a, b = KF64_TS_TAM
                chi_so = round(100.0 * (a * quy_mo + b * chat_luong), 1)
            # Quyết định ③: chưa có CRM → hiệu quả = Chất lượng, gắn `tam`.
            hieu_qua = None if chat_luong is None else round(100.0 * chat_luong, 1)

            # ⛔ Dưới ngưỡng mẫu thì KHÔNG gán ô ma trận và KHÔNG gán mức.
            #    Ô ma trận là một PHÁT BIỂU XẾP HẠNG («trụ cột», «đông nhưng
            #    yếu») — gán nó cho một mã 1 hội thoại là nói sai bằng con số.
            #    KF-64 §7 đã dặn: mẫu nhỏ thì chỉ đánh giá ở CẤP DỊCH VỤ.
            o = None
            if hieu_qua is not None and du_mau:
                lon = quy_mo >= 1.0
                tot = hieu_qua >= 100
                o = "①" if (lon and tot) else ("③" if lon else ("②" if tot else "④"))

            # ── năm bước chuyển tầng: S1 S3 S4 đo được, S5 S6 cần CRM ──
            s3 = _kf64_ti(1.0 * (hot + warm) / n, tb_s3)
            s4 = (_kf64_ti(1.0 * hot / (hot + warm), tb_s4)
                  if (hot + warm) and tb_s4 else None)
            buoc = [("S1", quy_mo, "T1"), ("S3", s3, "T3"), ("S4", s4, "T3")]
            co_b = [(v, ma, tg) for ma, v, tg in buoc if v is not None]
            tang, yeu_nhat, ma_yeu = None, None, None
            if co_b:
                v, ma_yeu, tg = min(co_b)
                yeu_nhat = round(v, 2)
                # ⛔ Dưới ngưỡng mẫu thì không đề xuất tầng nội dung: một mã
                #    1 hội thoại ⛔ chưa đáng làm nội dung riêng, và bước yếu
                #    của nó là nhiễu chứ không phải điểm nghẽn.
                if v < KF64_NGHEN and du_mau:
                    tang = tg
            chan_dung.append({
                "cd": m, "ten": (lambda: next(
                    (c["ten"] for c in tv["dich_vu"][dv]["chan_dung"] if c["ma"] == m), m))(),
                "dich_vu": dv, "ten_dich_vu": ten_dv.get(dv, dv),
                "ht": n, "hot": hot, "warm": warm, "co_sdt": sum(1 for r in g if r["co_sdt"]),
                "roi_truc": sum(1 for r in g if r["roi"] == "trực page"),
                "he_so": max([r["he_so"] for r in g], default=1),
                "quy_mo": round(quy_mo, 2), "nhiet_tb": None if dm is None else round(dm, 1),
                "pct_hot": round(100.0 * hot / n, 1),
                "chat_luong": None if chat_luong is None else round(chat_luong, 2),
                "bo_pct_hot": ti_hot is None,
                "chuyen_doi": None, "booking": None,
                "chi_so": chi_so, "muc": _kf64_muc(chi_so) if du_mau else None,
                "hieu_qua": hieu_qua, "o": o,
                # ★ Ô ma trận chốt bằng một mốc CỨNG ở 100. Sát mốc thì
                #   ⛔ không chốt được: hai bên mốc là hai chiến lược trái
                #   nhau (scale +15–20% vs duy trì tối thiểu).
                "o_sat_moc": bool(o and abs(hieu_qua - 100) < KF64_SAT_MOC),
                "s1": round(quy_mo, 2), "s3": None if s3 is None else round(s3, 2),
                "s4": None if s4 is None else round(s4, 2),
                "s5": None, "s6": None,
                "buoc_yeu": ma_yeu, "buoc_yeu_tri": yeu_nhat,
                "tang": tang, "co_van_hanh": False,
                "co_cau": list(KF64_O[o][3]) if o else None,
                "du_mau": du_mau, "tam": True,
            })

    # ⛔ Mã ĐỦ MẪU lên trước, rồi mới tới mã «chưa đủ dữ liệu». Trộn lẫn thì
    #    một mã 3 hội thoại ngồi trên một mã 41 hội thoại, và bảng trông y như
    #    một bảng xếp hạng dù ba phần tư dòng ⛔ không được xếp hạng.
    chan_dung.sort(key=lambda x: (not x["du_mau"], x["chi_so"] is None,
                                  -(x["chi_so"] or 0)))
    for i, x in enumerate([c for c in chan_dung if c["du_mau"]], 1):
        x["hang"] = i

    du = [c for c in chan_dung if c["du_mau"]]
    return {
        "bo": KF64, "trang_thai": "dang_chay",
        "duyet": "02/11/2026 · người dùng chốt bỏ bước chờ anh UY duyệt",
        "thay_the": "id-M §7",
        "trong_so": {"quy_mo": KF64_TS[0], "chat_luong": KF64_TS[1],
                     "chuyen_doi": KF64_TS[2]},
        "trong_so_dang_dung": {"quy_mo": KF64_TS_TAM[0], "chat_luong": KF64_TS_TAM[1]},
        "co_crm": False,
        "min_ht": KF64_MIN_HT, "min_booking": KF64_MIN_BOOKING,
        "nghen": KF64_NGHEN,
        "tang": {k: {"nhan": v[0], "viec": v[1], "quy_doi": v[2]}
                 for k, v in KF64_TANG.items()},
        "o": {k: {"nhan": v[0], "dieu_kien": v[1], "chien_luoc": v[2],
                  "co_cau": list(v[3])} for k, v in KF64_O.items()},
        "dich_vu": dich_vu,
        "chan_dung": chan_dung,
        "so_du_mau": len(du), "so_co_khach": len(chan_dung),
        "so_thu_vien": sum(so_cd_tv.values()),
        "quyet_dinh": [
            "① Mẫu số «trung bình dịch vụ» = tiền tố mã KF-62 (18 dịch vụ), ⛔ không "
            "phải cột dich_vu của id-G §3 — chân dung được định nghĩa bên trong dịch "
            "vụ KF-62. Đổi mẫu số là đổi mọi chỉ số: FILLER-BOTOX_LAN_DAU có Quy mô "
            "1,87 theo cột dich_vu nhưng 0,85 theo tiền tố KF-62.",
            "② %Hot của cả dịch vụ bằng 0 thì BỎ chỉ số đó, ⛔ không tính thành 0 — "
            "mẫu số 0 là KHÔNG XÁC ĐỊNH. Kỳ này 3 HOT trên 494 nên nhiều dịch vụ "
            "rơi vào cảnh đó; tính thành 0 là chia đôi Chất lượng của mọi chân dung.",
            "③ KF-64 ⛔ không cho bản dự phòng cho «điểm hiệu quả» mà Chuyển đổi "
            "chiếm 62,5%. Đang chuẩn hoá lại trên trục đo được → hiệu quả = Chất "
            "lượng. ⚠ Ô ③ vì vậy đọc là «đông nhưng NGUỘI», ⛔ chưa phải «đông "
            "nhưng YẾU». Mọi dòng gắn tam=true.",
            "④ Trục phễu KF-64 đặt tên T1…T4, ⛔ không dùng A1…A4: cùng 494 hội "
            "thoại, A2 theo id-D §3 = 1 HT, theo KF-64 = 324 HT. Nấc 5A của id-D "
            "⛔ không đổi — bảng quy đổi ở khối `tang`.",
        ],
        "ghi_chu": [
            "Chỉ số đang là BẢN TẠM 0,4 Quy mô + 0,6 Chất lượng — trục Chuyển đổi "
            "(50%% của bản đủ) trống vì chưa có dòng booking CRM nào. ⛔ Không dùng "
            "để chia ngân sách lớn.",
            "%d/%d mã có khách trong kỳ đạt ngưỡng %d hội thoại nên được xếp hạng; "
            "%d mã còn lại ghi «chưa đủ dữ liệu». Ngưỡng chính thức còn cần ≥%d "
            "booking nên hiện 0 mã nào đạt."
            % (len(du), len(chan_dung), KF64_MIN_HT,
               len(chan_dung) - len(du), KF64_MIN_BOOKING),
            "Mỗi chân dung so với TRUNG BÌNH DỊCH VỤ KF-62 của nó, ⛔ không tính các "
            "dòng CHUA_XAC_DINH và KHONG_XAC_DINH_DV vào trung bình đó.",
            "Bước S5 (Hot→booking) và S6 (booking→đến khám) ⛔ chưa đo được — thiếu "
            "CRM. Nên cờ «Vận hành/Sale» của KF-64 §4.2 luật ③ chưa bao giờ bật, và "
            "mọi tầng ưu tiên hiện ra đều là T1 hoặc T3.",
            "Bảng 5 bước của KF-64 v1.0 đánh số S1 · S3 · S4 · S5 · S6 — ⛔ thiếu S2. "
            "Đọc §4.2 thì S2 gần như chắc là «nói rõ nhu cầu», nhưng nó được mô tả ở "
            "cấp dịch vụ nên ⛔ không có dòng ở cấp chân dung.",
        ],
    }


def cham_hoi_thoai(ht, td, ma_o):
    """Trả về (bảng ✓/✗/—, điểm 0-100 hoặc None, danh sách cờ đỏ)."""
    k = {}
    tin, kh_text, nv_text = ht["tin"], ht["kh_text"], ht["nv_text"]
    tin_kh = [t for t in tin if not t["nv"]]
    tin_nv = [t for t in tin if t["nv"]]

    # ── N1
    moc = ht.get("moc_bat_dau") or (tin_kh[0]["tem"] if tin_kh else None)
    if moc and tin_nv:
        g = gio_cua(moc)
        tra_loi = next((t for t in tin_nv if phut(moc, t["tem"]) is not None
                        and phut(moc, t["tem"]) >= 0), None)
        if g is None or not (GIO_MO <= g <= GIO_DONG):
            k["N1.1"] = "—"                      # ngoài khung ca → không áp dụng
        elif tra_loi is None:
            k["N1.1"] = "✗"
        else:
            k["N1.1"] = "✓" if phut(moc, tra_loi["tem"]) <= SLA_PHUT else "✗"
    else:
        k["N1.1"] = "—"

    k["N1.2"] = "✓" if len(tin_kh) >= 2 else ("✗" if tin_nv else "—")

    hoi = [t for t in tin_kh if "?" in t["text"] or co_tu(t["text"], ["bao nhiêu", "thế nào", "có không", "được không"])]
    if not hoi:
        k["N1.3"] = "—"
    else:
        tra = sum(1 for h in hoi if any(t["nv"] and phut(h["tem"], t["tem"]) is not None
                                        and phut(h["tem"], t["tem"]) >= 0 for t in tin))
        k["N1.3"] = "✓" if tra >= len(hoi) else "✗"

    duoi = False
    for i, t in enumerate(tin[:-1]):
        if not t["nv"] and tin[i + 1]["nv"]:
            d = phut(t["tem"], tin[i + 1]["tem"])
            if d is not None and d > 30:
                duoi = True
    k["N1.4"] = "✓" if duoi else ("—" if tin[-1]["nv"] else "✗")

    # ── N2
    vt_xin = next((i for i, t in enumerate(tin) if t["nv"] and co_tu(t["text"], td["nv_xin_so"])), None)
    vt_gia = next((i for i, t in enumerate(tin) if t["nv"] and co_tu(t["text"], ["triệu", "giá từ", "chi phí khoảng"])), None)
    vt_moc = min([x for x in (vt_xin, vt_gia) if x is not None], default=None)
    vt_hoi = next((i for i, t in enumerate(tin) if t["nv"] and co_tu(t["text"], td["nv_hoi_tinh_trang"])), None)
    if vt_moc is None:
        k["N2.1"] = "✓" if vt_hoi is not None else "—"
    else:
        k["N2.1"] = "✓" if (vt_hoi is not None and vt_hoi < vt_moc) else "✗"

    so_hoi = sum(1 for t in tin_nv if "?" in t["text"])
    k["N2.2"] = "✓" if so_hoi >= 2 else "✗"
    k["N2.3"] = "✓" if co_tu(nv_text, td["nv_moi_anh"]) else "✗"

    nhac_lai = False
    for i, t in enumerate(tin[:-1]):
        if not t["nv"] and tin[i + 1]["nv"]:
            tu_kh = [w for w in khong_dau(t["text"]).split() if len(w) >= 4]
            if sum(1 for w in tu_kh if w in khong_dau(tin[i + 1]["text"])) >= 2:
                nhac_lai = True
    k["N2.4"] = "✓" if nhac_lai else "✗"

    # ── N3
    if "O-01" in ma_o:
        k["N3.1"] = "✓" if co_tu(nv_text, ["triệu", "giá từ", "khoảng", "trọn gói", "bảng giá"]) else "✗"
    else:
        k["N3.1"] = "—"
    k["N3.2"] = "—"      # ⚠ cần người đối chiếu bảng giá hiện hành — id-F §3
    co_do = []
    for ma, tu in td["co_do"].items():
        if co_tu(nv_text, tu):
            co_do.append({"ma": ma, "trich": (tu_khop(nv_text, tu) or [""])[0]})
    k["N3.3"] = "✗" if any(c["ma"] == "CĐ-1" for c in co_do) else "✓"
    k["N3.4"] = "✗" if any(c["ma"] == "CĐ-4" for c in co_do) else "✓"

    # ── N4
    if not [m for m in ma_o if m != "O-00"]:
        k["N4.1"] = k["N4.2"] = k["N4.3"] = "—"
    else:
        k["N4.1"] = "✓" if len(nv_text) > 120 else "✗"
        k["N4.2"] = "✓" if not ("O-01" in ma_o and co_tu(nv_text, ["chất lượng", "uy tín hàng đầu"])
                                and not co_tu(nv_text, ["triệu", "trả góp", "ưu đãi"])) else "✗"
        k["N4.3"] = "✓" if co_tu(nv_text, ["khi nào cần", "em luôn ở đây", "chị cứ nhắn", "bất cứ lúc nào", "em hỗ trợ"]) else "✗"

    # ── N5
    xin = [t for t in tin_nv if co_tu(t["text"], td["nv_xin_so"])]
    if not xin:
        k["N5.1"] = k["N5.2"] = "✗"
    else:
        k["N5.1"] = "✓" if co_tu(xin[0]["text"], td["nv_ly_do_xin_so"]) else "✗"
        k["N5.2"] = "✓" if len(xin) >= 2 and khong_dau(xin[0]["text"]) != khong_dau(xin[1]["text"]) else "✗"
    k["N5.3"] = "✓" if co_tu(nv_text, td["nv_khung_gio"]) else "✗"
    k["N5.4"] = "✓" if (co_tu(nv_text, td["nv_moi_lich"]) and re.search(r'\d{1,2}\s*[hg:]', nv_text)) else "✗"

    # ── N6
    dai = [t for t in tin_nv if len(t["text"]) > 400]
    k["N6.1"] = "✗" if len(dai) >= 2 else "✓"
    k["N6.2"] = "✓"
    k["N6.3"] = "✗" if any(c["ma"] == "CĐ-6" for c in co_do) else "✓"

    tu_so = sum(DIEM[m] for m, v in k.items() if v == "✓")
    mau_so = sum(DIEM[m] for m, v in k.items() if v in ("✓", "✗"))
    diem = round(tu_so / mau_so * 100, 1) if mau_so else None
    if co_do and diem is not None:
        diem = min(diem, 49.0)           # id-F §4: có cờ đỏ → trần 49
    return k, diem, co_do


def xep_loai(diem, so_ht, co_do):
    if so_ht < MAU_TOI_THIEU_NV or diem is None:
        return "chưa đủ mẫu"
    if co_do:
        return "B" if diem >= 70 else ("C" if diem >= 55 else "D")
    return "A" if diem >= 85 else ("B" if diem >= 70 else ("C" if diem >= 55 else "D"))


# ───────────────────────────── lệnh `doc` ────────────────────────────────

def lenh_doc(args):
    td = nap_tu_dien()
    hts = doc_hoi_thoai(args.file)
    if not hts:
        sys.exit("⛔ Không đọc được hội thoại nào.")

    pho, vi_sao = nap_phac_hoa(args.ky)

    # Mốc chốt dữ liệu của kỳ = tem muộn nhất trong file. Hệ số thời gian của
    # KF-60 đo từ tin cuối của khách tới mốc này — ⛔ không dùng "bây giờ",
    # vì chạy lại báo cáo cũ sau một tháng thì mọi lead đều nguội giả.
    moc_chot = max([t["tem"] for ht in hts for t in ht["tin"] if t.get("tem")],
                   default=None)

    ban_ghi = []
    for ht in hts:
        cd = gan_chan_dung(ht, pho)          # None khi chưa qua CỔNG 0
        nac = gan_nac(ht, td)
        ma_o = gan_ma_o(ht, td)
        nhiet, tin_hieu = gan_nhiet(ht, td)
        k, diem, co_do = cham_hoi_thoai(ht, td, ma_o)
        ht["chot_lich"] = bool(co_tu(ht["nv_text"], td["nv_moi_lich"]) and co_tu(ht["kh_text"], ["vâng", "ok", "được", "em qua"]))
        roi = gan_vi_sao_roi(ht, td, diem)
        rc = gan_rao_can(ht, td, ma_o)
        hs = he_so_gia_tri(ht, td)
        for c in co_do:
            c["nguoi"] = ht["nv"]
        ban_ghi.append({
            "ma": ht["ma"], "nv": ht["nv"], "cd": cd, "nac": nac, "ma_o": ma_o,
            "nhiet": nhiet, "tin_hieu": tin_hieu, "co_sdt": ht["co_sdt"],
            "chot_lich": ht["chot_lich"], "roi": roi, "rao_can": rc,
            "dich_vu": gan_dich_vu(ht, td), "he_so": hs,
            "diem": diem, "cham": k, "co_do": co_do,
            "so_luot_kh": sum(1 for t in ht["tin"] if not t["nv"]),
            "lead": cham_lead(ht, td, ma_o, rc, roi, k, nhiet, hs, moc_chot),
        })

    n = len(ban_ghi)
    os.makedirs(RA, exist_ok=True)
    ghi_csv(ban_ghi)
    ket = gom_doc(ban_ghi, args.ky, os.path.basename(args.file), pho, vi_sao)

    with open(os.path.join(RA, "doc-hoi-thoai.json"), "w", encoding="utf-8") as f:
        json.dump(ket, f, ensure_ascii=False, indent=1)

    # Nguyên liệu phác họa ghi lại MỖI LẦN chạy: kỳ sau chân dung có thể khác,
    # và bản phác họa cũ phải đối chiếu được với chữ của khách kỳ này.
    nl = nguyen_lieu_chan_dung(ban_ghi, hts, td, args.ky, os.path.basename(args.file))
    with open(NGUYEN_LIEU, "w", encoding="utf-8") as f:
        json.dump(nl, f, ensure_ascii=False, indent=1)

    _in_tom_tat(ket, ban_ghi, nl)



def _ma_co_do(r):
    """Cờ đỏ trong bản ghi có thể là dict (có trích dẫn) hoặc chuỗi mã."""
    return [c["ma"] if isinstance(c, dict) else c for c in (r.get("co_do") or [])]


def ghi_csv(ban_ghi):
    """Bảng chấm từng hội thoại — một dòng một HT, truy ngược được."""
    with open(os.path.join(RA, "cham-hoi-thoai.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        cot = [m for _, _, ds in TIEU_CHI for m, _, _ in ds]
        o_cot = ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4",
                 "C1", "C2", "C3", "D1", "D2", "D3", "E1", "E2", "E3", "E4", "E5"]
        w.writerow(["ma", "nv", "cd", "nac", "ma_o", "nhiet", "co_sdt", "chot_lich",
                    "vi_sao_roi", "rao_can", "dich_vu", "dich_vu_kf62",
                    "he_so", "diem", "co_do",
                    # ── KF-60: VIỆC phải làm, đứng CẠNH nhãn id-D ở cột `nhiet`.
                    #    ⛔ Không có cột nhãn HOT/WARM/COLD thứ hai.
                    "luong", "lead_goc", "lead_hs_tg", "lead_diem", "lead_nhom_goi",
                    "lead_ghi_de", "lead_uu_tien", "gio_im"]
                   + cot + o_cot)
        for r in ban_ghi:
            L = r.get("lead") or {}
            w.writerow([r["ma"], r["nv"], r["cd"] or CD_DU, r["nac"],
                        " ".join(r["ma_o"]), r["nhiet"],
                        "Có" if r["co_sdt"] else "", "Có" if r["chot_lich"] else "",
                        r["roi"], " · ".join(r["rao_can"]), r["dich_vu"],
                        r.get("dich_vu_kf62") or "", r["he_so"],
                        r["diem"] if r["diem"] is not None else "",
                        " ".join(_ma_co_do(r)),
                        L.get("route", ""), L.get("goc", ""), L.get("he_so_tg", ""),
                        L.get("diem", ""), L.get("nhom_goi", "") or "",
                        " ".join(L.get("ghi_de") or []), L.get("uu_tien", ""),
                        L.get("gio_im", "")]
                       + [r["cham"].get(c, "") for c in cot]
                       + [(L.get("o") or {}).get(c, "") for c in o_cot])


def gom_doc(ban_ghi, ky, nguon, pho, vi_sao):
    """Gom bản ghi thành out/doc-hoi-thoai.json.

    ★ Dùng chung cho MỌI khuôn đầu vào (Caresoft qua `lenh_doc`, KNB qua
    tools/knb.py). ⛔ Đừng chép logic này sang chỗ thứ hai — hai bản sẽ
    lệch nhau sau hai kỳ.
    """
    n = len(ban_ghi)
    co_do_all = [{"ma": c["ma"], "nguoi": c.get("nguoi") or r.get("nv") or "(không rõ)",
                  "ht": r["ma"], "trich": c.get("trich", "")}
                 for r in ban_ghi for c in (r.get("co_do") or [])
                 if isinstance(c, dict)]
    # tổng hợp nhân viên
    # ⛔ Hai rổ dưới đây ⛔ KHÔNG được xếp loại: hội thoại nhiều người trực thì
    #    điểm không thuộc về ai, hội thoại không rõ người thì không có bằng
    #    chứng. Chúng vẫn nằm trong chỉ số CẢ ĐỘI (`nhom`) — chỗ đó không có tên.
    KHONG_XEP = ("(nhiều người)", "(không rõ)")
    theo_nv = defaultdict(list)
    for r in ban_ghi:
        if r["nv"] in KHONG_XEP:
            continue
        theo_nv[r["nv"]].append(r)
    ca_nhan = []
    for nv, rs in sorted(theo_nv.items(), key=lambda x: -len(x[1])):
        ds = [r["diem"] for r in rs if r["diem"] is not None]
        d = round(sum(ds) / len(ds), 1) if ds else None
        cds = sorted({m for r in rs for m in _ma_co_do(r)})
        yeu = min(TIEU_CHI, key=lambda g: _pct_nhom(rs, g[0]) if _pct_nhom(rs, g[0]) is not None else 999)
        manh = max(TIEU_CHI, key=lambda g: _pct_nhom(rs, g[0]) if _pct_nhom(rs, g[0]) is not None else -1)
        ca_nhan.append({"ten": nv, "ht": len(rs), "diem": d,
                        "loai": xep_loai(d, len(rs), cds),
                        "yeu_nhat": yeu[0], "manh_nhat": manh[0], "co_do": cds})

    # chỉ số nhóm toàn khối
    nhom = []
    for ma, ten, ds in TIEU_CHI:
        tc = []
        for m, t, d in ds:
            dat = sum(1 for r in ban_ghi if r["cham"].get(m) == "✓")
            chua = sum(1 for r in ban_ghi if r["cham"].get(m) == "✗")
            kad = sum(1 for r in ban_ghi if r["cham"].get(m) == "—")
            tc.append({"ma": m, "ten": t, "diem": d, "dat": dat, "chua": chua,
                       "khong_ap_dung": kad, "pct_dat": pct(dat, dat + chua)})
        nhom.append({"ma": ma, "ten": ten, "diem_toi_da": sum(d for _, _, d in ds),
                     "pct_dat": _pct_nhom(ban_ghi, ma), "tieu_chi": tc})

    ket = {
        "ky": ky, "so_ht": n, "nguon": nguon,
        "tao": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "nhiet": dict(Counter(r["nhiet"] for r in ban_ghi)),
        "nhiet_x_sdt": [{"muc": m,
                         "chua": sum(1 for r in ban_ghi if r["nhiet"] == m and not r["co_sdt"]),
                         "co": sum(1 for r in ban_ghi if r["nhiet"] == m and r["co_sdt"])}
                        for m in ("HOT", "WARM", "COLD")],
        "tin_hieu": [{"nhan": t, "so": sum(1 for r in ban_ghi if t in r["tin_hieu"])}
                     for t in ("1_dich_vu", "2_thoi_gian", "3_sdt", "4_dieu_kien", "5_khung_gio")],
        "nguyen_nhan_roi": dict(Counter(r["roi"] for r in ban_ghi)),
        "rao_can": [{"nhan": k2, "so": v} for k2, v in
                    Counter(rc for r in ban_ghi for rc in r["rao_can"]).most_common()],
        "ma_o": [{"ma": m, "so": sum(1 for r in ban_ghi if m in r["ma_o"]),
                  "pct": pct(sum(1 for r in ban_ghi if m in r["ma_o"]), n)}
                 for m in ["O-%02d" % i for i in range(1, 13)] + ["O-00", "(chưa nêu)"]],
        "phac_hoa": {
            "trang_thai": "da_duyet" if pho else "chua_phac_hoa",
            "vi_sao": vi_sao,
            "file": "out/chan-dung.json",
            "nguyen_lieu": "out/nguyen-lieu-chan-dung.json",
            "so_chan_dung": len(pho["tep"]) if pho else 0,
            "duyet_boi": (pho or {}).get("duyet_boi"),
            "duyet_luc": (pho or {}).get("duyet_luc"),
        },
        "chan_dung": _bang_chan_dung(ban_ghi, pho),
        "nac": dict(Counter(r["nac"] for r in ban_ghi)),
        "chot_lich": sum(1 for r in ban_ghi if r["chot_lich"]),
        # ⚠ Luôn ghi đủ 5 khoá: ở đây `0` nghĩa là ĐÃ ĐO và bằng không, khác
        #   hẳn "chưa đo". Thiếu khoá thì trang không phân biệt được hai thứ đó.
        "nhan_vien": {"du_mau": any(c["loai"] != "chưa đủ mẫu" for c in ca_nhan),
                      "ht_khong_xep": {k: sum(1 for r in ban_ghi if r["nv"] == k)
                                       for k in KHONG_XEP},
                      "phan_bo": dict({k: 0 for k in ("A", "B", "C", "D", "chưa đủ mẫu")},
                                      **Counter(c["loai"] for c in ca_nhan)),
                      "nhom": nhom, "ca_nhan": ca_nhan, "co_do": co_do_all,
                      "ghi_chu": "Điểm dùng để phân việc kèm cặp. "
                                 "Không phải căn cứ kỷ luật hay xếp hạng công khai."},
        "the_tong": _the_tong(ban_ghi),
        # ★ Khối lead: xếp HÀNG CHỜ GỌI. Nhãn id-D ở trên ⛔ không bị thay.
        "lead": gom_lead(ban_ghi),
        # ★ Khối kf64: XẾP HẠNG CHÂN DUNG + tầng nội dung. Thay `id-M` §7 —
        #   ⛔ không để hai bảng xếp hạng cùng sống (bài học `id-C` §4).
        "kf64": gom_kf64(ban_ghi),
    }
    return ket


def _pct_nhom(rs, ma_nhom):
    ds = [m for g, _, lst in TIEU_CHI if g == ma_nhom for m, _, _ in lst]
    dat = sum(1 for r in rs for m in ds if r["cham"].get(m) == "✓")
    chua = sum(1 for r in rs for m in ds if r["cham"].get(m) == "✗")
    return pct(dat, dat + chua)


def _bang_chan_dung(ban_ghi, pho):
    """Bảng chân dung dựng từ THƯ VIỆN KF-62 — chỉ liệt kê chân dung CÓ hội thoại.

    ⛔ Không liệt kê cả 85 chân dung: một kỳ chỉ chạm tới vài line, 80 dòng rỗng
    làm bảng vô dụng. Chân dung 0 HT vẫn ⛔ không mất — nó nằm trong thư viện và
    đọc được ở `tools/chan_dung_kf62.json`.
    """
    tv = nap_thu_vien()
    ten = {}
    for dv in tv["dich_vu"].values():
        for c in dv["chan_dung"]:
            ten[c["ma"]] = c["ten"]
    co = []
    for r in ban_ghi:
        m = r.get("cd") or CD_DU
        if m not in co:
            co.append(m)
    ten[CD_DU] = TEN_CD_DU
    # Nhóm CHUA_XAC_DINH của mỗi dịch vụ luôn xuống cuối, như CD0 trước đây.
    co.sort(key=lambda m: (m == CD_DU, m.endswith("CHUA_XAC_DINH"), m))
    return [_dong_cd(ban_ghi, m, ten.get(m, m), None) for m in co]


def _dong_cd(ban_ghi, cd, ten, dn):
    rs = [r for r in ban_ghi if (r.get("cd") or CD_DU) == cd]
    hs = (dn or {}).get("he_so_gia_tri")
    return {"cd": cd, "ten": ten, "ht": len(rs), "quan_sat": len(rs) < 5,
            "hot": sum(1 for r in rs if r["nhiet"] == "HOT"),
            "warm": sum(1 for r in rs if r["nhiet"] == "WARM"),
            "cold": sum(1 for r in rs if r["nhiet"] == "COLD"),
            "co_sdt": sum(1 for r in rs if r["co_sdt"]),
            "chot_lich": sum(1 for r in rs if r["chot_lich"]),
            "bo_1_luot": sum(1 for r in rs if r["so_luot_kh"] <= 1),
            "roi_truc": sum(1 for r in rs if r["roi"] == "trực page"),
            "he_so": hs or max([r["he_so"] for r in rs], default=1)}


def _the_tong(ban_ghi):
    n = len(ban_ghi)
    bo1 = sum(1 for r in ban_ghi if r["so_luot_kh"] <= 1)
    sdt = sum(1 for r in ban_ghi if r["co_sdt"])
    sla = [r for r in ban_ghi if r["cham"].get("N1.1") in ("✓", "✗")]
    nong_chua = sum(1 for r in ban_ghi if r["nhiet"] in ("HOT", "WARM") and not r["co_sdt"])
    roi_truc = sum(1 for r in ban_ghi if r["roi"] == "trực page")
    goi_ngay = sum(1 for r in ban_ghi
                   if (r.get("lead") or {}).get("nhom_goi") == "GOI_NGAY")
    return [
        {"id": "ht", "nhan": "Hội thoại phân tích", "gia_tri": n, "kieu": "n"},
        {"id": "bo_1", "nhan": "Bỏ sau 1 lượt", "gia_tri": pct(bo1, n), "kieu": "pct",
         "tot": "thap", "phu": "%d/%d HT" % (bo1, n)},
        {"id": "co_sdt", "nhan": "Có SĐT", "gia_tri": pct(sdt, n), "kieu": "pct",
         "tot": "cao", "phu": "%d/%d HT" % (sdt, n)},
        {"id": "sla", "nhan": "Trả lời tin đầu ≤2′", "gia_tri":
            pct(sum(1 for r in sla if r["cham"]["N1.1"] == "✓"), len(sla)), "kieu": "pct",
         "tot": "cao", "phu": "trong khung 8h30–22h · chuẩn ≥90%"},
        {"id": "roi_truc", "nhan": "Rơi do trực page", "gia_tri": pct(roi_truc, n),
         "kieu": "pct", "tot": "thap",
         "phu": "%d/%d HT — câu trả lời của trực page làm khách dừng" % (roi_truc, n)},
        {"id": "nong_chua_sdt", "nhan": "HOT/WARM chưa có SĐT", "gia_tri": nong_chua,
         "kieu": "n", "tot": "thap", "phu": "lead nóng chưa vào tay telesale"},
        {"id": "goi_ngay", "nhan": "Hàng chờ Sale gọi ≤15′", "gia_tri": goi_ngay,
         "kieu": "n", "phu": "hàng chờ Sale theo KF-60 · %s" % KF60},
    ]


def _in_tom_tat(k, ban_ghi, nl):
    p = print
    p("")
    p("═" * 66)
    p("  ĐỌC HỘI THOẠI · kỳ %s · %d hội thoại · nguồn %s" % (k["ky"], k["so_ht"], k["nguon"]))
    p("═" * 66)
    p("")
    p("  THẺ SỐ TỔNG")
    for t in k["the_tong"]:
        v = t["gia_tri"]
        p("    %-26s %s%s" % (t["nhan"], "—" if v is None else v,
                              "%" if t["kieu"] == "pct" and v is not None else ""))
    p("")
    p("  MỨC NÓNG   " + " · ".join("%s %d" % (m, k["nhiet"].get(m, 0)) for m in ("HOT", "WARM", "COLD")))
    p("  VÌ SAO RƠI " + " · ".join("%s %d" % (a, b) for a, b in
                                   sorted(k["nguyen_nhan_roi"].items(), key=lambda x: -x[1])))
    p("")
    if k["chan_dung"]:
        p("  CHÂN DUNG — theo bản phác họa đã duyệt (%s · %s)"
          % (k["phac_hoa"]["duyet_boi"] or "—", k["phac_hoa"]["duyet_luc"] or "—"))
        p("    %-5s %-30s %4s %4s %4s %4s %6s %5s" % ("mã", "tên", "HT", "HOT", "WRM", "SĐT", "%SĐT", "lịch"))
        for c in k["chan_dung"]:
            p("    %-5s %-30s %4d %4d %4d %4d %5s%% %5d%s" % (
                c["cd"], c["ten"][:30], c["ht"], c["hot"], c["warm"], c["co_sdt"],
                pct(c["co_sdt"], c["ht"]) if c["ht"] else "—", c["chot_lich"],
                "  👁 quan sát" if c["quan_sat"] else ""))
        du = next((c for c in k["chan_dung"] if c["cd"] == CD_DU), None)
        if du and du["ht"] >= CD_TOI_THIEU_DE_DE:
            p("")
            p("    ⚠ %d HT rơi %s. Nếu nhóm này có một NỖI SỢ riêng thì phác họa thêm"
              % (du["ht"], CD_DU))
            p("      một chân dung và xin duyệt lại CỔNG 0 — ⚠ DI SẢN, xem id-M.")
    else:
        p("  CHÂN DUNG — ⏳ CHƯA PHÁC HỌA")
        p("    %s" % (k["phac_hoa"]["vi_sao"] or ""))
        p("    Nguyên liệu đã ghi: out/nguyen-lieu-chan-dung.json")
        p("      · %d cụm chữ khách tự nói (ngưỡng ≥ %d HT)"
          % (len(nl["cum_chu"]), nl["nguong_cum"]))
        p("      · %d câu hỏi đầu đã ẩn danh" % len(nl["cau_dau"]))
        if nl["cum_chu"]:
            p("    Mười cụm đông nhất:")
            for c in nl["cum_chu"][:10]:
                p("      %-34s %3d HT  (%s)" % (c["cum"][:34], c["so_ht"], " ".join(c["ht"][:3])))
        p("")
        p("    → Agent đọc nguyên liệu, phác họa chân dung của kỳ, ghi out/chan-dung.json")
        p("      (`id.py chan-dung --ky %s --mau` để lấy khuôn), rồi người dùng duyệt:" % k["ky"])
        p("      `id.py chan-dung --ky %s --duyet \"<tên>\"` → chạy lại `id.py doc`." % k["ky"])
    p("")
    p("  MÃ O — 5 mã cao nhất")
    for o in sorted(k["ma_o"], key=lambda x: -x["so"])[:5]:
        p("    %-6s %4d  (%s%%)" % (o["ma"], o["so"], o["pct"]))
    p("")
    p("  CHẤM ĐIỂM — % đạt theo nhóm")
    for g in k["nhan_vien"]["nhom"]:
        p("    %-3s %-28s %s%%" % (g["ma"], g["ten"], g["pct_dat"] if g["pct_dat"] is not None else "—"))
    p("")
    p("  PHÂN BỐ NHÂN VIÊN  " + " · ".join("%s %d" % (a, b) for a, b in
                                            sorted(k["nhan_vien"]["phan_bo"].items())))
    if k["nhan_vien"]["co_do"]:
        p("")
        p("  🔴 CỜ ĐỎ — %d" % len(k["nhan_vien"]["co_do"]))
        for c in k["nhan_vien"]["co_do"][:10]:
            p("    %-6s %-24s %s  « %s »" % (c["ma"], c["nguoi"][:24], c["ht"], c["trich"]))
    p("")
    p("  ⚠ Script chỉ làm phần ĐẾM. Phác họa chân dung, insight, câu hỏi ngầm,")
    p("    hướng nội dung, câu mẫu trong sổ tay — agent phải đọc và viết (SYSTEM-PROMPT §8).")
    p("")
    p("  Đã ghi: out/doc-hoi-thoai.json · out/cham-hoi-thoai.csv")
    p("          out/nguyen-lieu-chan-dung.json")
    p("")


# ──────────────────── lệnh `chan-dung` · CỔNG 0 ──────────────────────────

MAU_PHAC_HOA = {
    "schema": "chan-dung-ky/1",
    "ky": None,
    "nguon": "out/nguyen-lieu-chan-dung.json",
    "phac_hoa_luc": None,
    "trang_thai": "cho_duyet",
    "duyet_boi": None,
    "duyet_luc": None,
    "ke_thua_tu_ky": None,
    "_huong_dan": [
        "Chân dung của kỳ này phác họa TỪ HỘI THOẠI của kỳ này, ⛔ không chép từ "
        "một bộ chân dung có sẵn và ⛔ không suy ra từ dịch vụ.",
        "`ten` viết bằng CHỮ CỦA KHÁCH, ⛔ không bằng tính từ marketing.",
        "`noi_so` là nỗi sợ chi phối — hai nhóm cùng nỗi sợ thì là MỘT chân dung.",
        "`dau_hieu` là cụm chữ khách tự nói; script gán theo cụm này, xét TỪ TRÊN "
        "XUỐNG nên xếp chân dung HẸP trước, RỘNG sau.",
        "`khong_phai` (không bắt buộc): cụm loại trừ, dùng khi hai chân dung chồng chữ.",
        "`trich`: ít nhất một HT-nnn cho mỗi chân dung — không truy ngược được là bịa.",
        "CD0 là mã DỰ TRỮ cho hội thoại không khớp dấu hiệu nào. ⛔ Không khai ở đây, "
        "⛔ không gọi là «rác» — CD0 đông là lỗi của quảng cáo, không phải của khách.",
        "Giữ lại mã của kỳ trước cho chân dung CÙNG NỖI SỢ (ghi `ke_thua_tu_ky`) — "
        "đổi mã giữa hai kỳ là mất mọi so sánh.",
        "⛔ Agent không tự điền `duyet_boi` / `trang_thai`. Duyệt bằng lệnh "
        "`id.py chan-dung --ky <kỳ> --duyet \"<tên người>\"`.",
    ],
    "tep": [
        {
            "ma": "CD1",
            "ten": "",
            "ho_la_ai": "",
            "noi_so": "",
            "dau_hieu": [],
            "khong_phai": [],
            "he_so_gia_tri": None,
            "trich": [],
        }
    ],
    "ghi_chu": [],
}


def lenh_chan_dung(args):
    os.makedirs(RA, exist_ok=True)

    if args.mau:
        if os.path.exists(PHAC_HOA) and not args.ghi_de:
            sys.exit("⛔ out/chan-dung.json đã có. Thêm --ghi-de nếu muốn ghi lại khuôn trống.")
        mau = json.loads(json.dumps(MAU_PHAC_HOA))
        mau["ky"] = args.ky
        mau["phac_hoa_luc"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open(PHAC_HOA, "w", encoding="utf-8") as f:
            json.dump(mau, f, ensure_ascii=False, indent=1)
        print("")
        print("  Đã ghi khuôn trống out/chan-dung.json cho kỳ %s." % args.ky)
        print("  → Agent đọc out/nguyen-lieu-chan-dung.json rồi điền `tep`.")
        print("  → Kiểm: id.py chan-dung --ky %s --kiem" % args.ky)
        print("")
        return

    if not os.path.exists(PHAC_HOA):
        sys.exit("⛔ chưa có out/chan-dung.json. Chạy: id.py chan-dung --ky %s --mau" % args.ky)
    with open(PHAC_HOA, encoding="utf-8") as f:
        pho = json.load(f)

    loi = kiem_phac_hoa(pho)
    if (pho.get("ky") or "") != args.ky:
        loi.insert(0, "`ky` trong file là «%s», không phải «%s»"
                   % (pho.get("ky") or "trống", args.ky))

    print("")
    print("═" * 66)
    print("  PHÁC HỌA CHÂN DUNG · kỳ %s · %d chân dung + %s dự trữ"
          % (pho.get("ky") or "—", len(pho.get("tep") or []), CD_DU))
    print("═" * 66)
    print("")
    for c in (pho.get("tep") or []):
        c = c or {}
        print("  %-5s %-34s hệ số %s · %d dấu hiệu · %d trích"
              % (c.get("ma") or "—", (c.get("ten") or "⚠ chưa đặt tên")[:34],
                 c.get("he_so_gia_tri") or "—",
                 len(c.get("dau_hieu") or []), len(c.get("trich") or [])))
        if c.get("noi_so"):
            print("        nỗi sợ: %s" % c["noi_so"])
    print("")

    if loi:
        print("  ⛔ CÒN %d LỖI — chưa duyệt được:" % len(loi))
        for x in loi:
            print("     · %s" % x)
        print("")
        sys.exit(1)

    if args.duyet:
        pho["trang_thai"] = "da_duyet"
        pho["duyet_boi"] = args.duyet.strip()
        pho["duyet_luc"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open(PHAC_HOA, "w", encoding="utf-8") as f:
            json.dump(pho, f, ensure_ascii=False, indent=1)
        print("  ✅ CỔNG 0 ĐÃ MỞ — duyệt bởi %s lúc %s" % (pho["duyet_boi"], pho["duyet_luc"]))
        print("  → Chạy lại: id.py doc <file-hoi-thoai.md> --ky %s" % args.ky)
        print("")
        return

    print("  Bản phác họa sạch lỗi. Trạng thái: %s" % (pho.get("trang_thai") or "—"))
    if pho.get("trang_thai") != "da_duyet":
        print("  → Duyệt: id.py chan-dung --ky %s --duyet \"<tên người duyệt>\"" % args.ky)
        print("  ⛔ Agent không tự duyệt thay người dùng.")
    else:
        print("  Đã duyệt bởi %s lúc %s" % (pho.get("duyet_boi"), pho.get("duyet_luc")))
    print("")


# ───────────────────────────── lệnh `ads` ────────────────────────────────

def lenh_ads(args):
    with open(args.file, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        sys.exit("⛔ File ads rỗng.")

    def s(r, c):
        v = (r.get(c) or "").replace(",", "").replace(".", "").strip()
        try:
            return float(v)
        except ValueError:
            return 0.0

    tong = {c: sum(s(r, c) for r in rows) for c in ("chi", "hien_thi", "click", "inbox", "lead", "booking")}
    def _n(x):
        return "{:,.0f}".format(x).replace(",", ".")

    chuoi = [
        # ★ Mắt xích 0: tiêu bao nhiêu. Mọi chỉ số sau đều là thương của con số này,
        #   nên đọc chuỗi mà không thấy mẫu số là đọc tỷ lệ trong chân không.
        {"ma": "CHI", "nhan": "Chi phí tổng", "gia_tri": tong["chi"] or None,
         "phu": "%d nội dung · %s hiển thị · %s inbox · %s lead · %s booking"
                % (len({(r.get("noi_dung") or r.get("chien_dich") or "(không tên)").strip()
                        for r in rows}), _n(tong["hien_thi"]), _n(tong["inbox"]),
                   _n(tong["lead"]), _n(tong["booking"]))},
        {"ma": "CPM", "nhan": "CPM", "gia_tri": _chia(tong["chi"], tong["hien_thi"] / 1000), "tot": "thap"},
        {"ma": "CTR", "nhan": "CTR", "gia_tri": _chia(tong["click"] * 100, tong["hien_thi"]), "tot": "cao", "kieu": "pct"},
        {"ma": "CPI", "nhan": "CPI — chi / inbox", "gia_tri": _chia(tong["chi"], tong["inbox"]), "tot": "thap"},
        {"ma": "CPL", "nhan": "CPL — chi / lead", "gia_tri": _chia(tong["chi"], tong["lead"]), "tot": "thap"},
        {"ma": "CPB", "nhan": "CPB — chi / booking", "gia_tri": _chia(tong["chi"], tong["booking"]), "tot": "thap"},
        {"ma": "BK_LEAD", "nhan": "Booking / Lead", "gia_tri": _chia(tong["booking"] * 100, tong["lead"]),
         "tot": "cao", "kieu": "pct"},
    ]
    for c in chuoi:
        c.setdefault("kieu", "n")
        c["muc_tieu"] = None          # ⚠ chưa có mốc — id-E §1
        c["ky_truoc"] = None

    theo_nd = defaultdict(lambda: Counter())
    for r in rows:
        ten = (r.get("noi_dung") or r.get("chien_dich") or "(không tên)").strip()
        for c in ("chi", "inbox", "lead", "booking"):
            theo_nd[ten][c] += s(r, c)
    dong = []
    for ten, v in sorted(theo_nd.items(), key=lambda x: -x[1]["chi"]):
        dong.append({"noi_dung": ten, "chi": v["chi"], "inbox": v["inbox"],
                     "deal": v["lead"], "bk": v["booking"],
                     "cpi": _chia(v["chi"], v["inbox"]), "cpl": _chia(v["chi"], v["lead"]),
                     "cpb": _chia(v["chi"], v["booking"])})
    tv_ctr = sorted([d["cpl"] for d in dong if d["cpl"]])
    gi = tv_ctr[len(tv_ctr) // 2] if tv_ctr else None
    for d in dong:
        d["danh_gia"] = "—" if not gi or not d["cpl"] else ("tot" if d["cpl"] <= gi else "kem")

    os.makedirs(RA, exist_ok=True)
    ket = {"ky": args.ky, "nguon": os.path.basename(args.file), "don_vi": "đ",
           "tong": tong, "chuoi": chuoi, "dong": dong,
           "ghi_chu": ["Ô «Chi phí tổng» là mẫu số chung của CPI, CPL và CPB — "
                       "CPL giảm mà chi cũng giảm theo thì chưa chắc đã tốt lên (id-E §1).",
                       "⚠ Mốc mục tiêu chưa có — cần TB 30 ngày của từng dịch vụ (id-E §1).",
                       "⛔ Chưa phân rã CPL thì chưa kết luận lỗi nội dung (id-E §1)."]}
    with open(os.path.join(RA, "doc-ads.json"), "w", encoding="utf-8") as f:
        json.dump(ket, f, ensure_ascii=False, indent=1)

    print("")
    print("═" * 66)
    print("  CHỈ SỐ QUẢNG CÁO · kỳ %s · %d dòng" % (args.ky, len(rows)))
    print("═" * 66)
    for c in chuoi:
        v = c["gia_tri"]
        so = "—" if v is None else ("%.1f%%" % v if c["kieu"] == "pct" else "{:,.0f} đ".format(v))
        print("    %-24s %12s   %s" %
              (c["nhan"], so, c.get("phu") or "mục tiêu: ⚠ chưa có mốc so sánh"))
    print("")
    print("  %d nội dung · đã ghi out/doc-ads.json" % len(dong))
    print("")


def _chia(a, b):
    return round(a / b, 1) if b else None


# ─────────────────────────── lệnh `bao-cao` ──────────────────────────────


# ═══════════ lớp phủ CHỮ NGƯỜI — ⛔ chạy lại báo cáo không được xoá ═══════════
# Phần ĐẾM ĐƯỢC do script sinh lại mỗi lần chạy. Phần ĐỌC HIỂU — vấn đề cốt
# lõi, thẻ insight, ma trận, hook, sổ tay, việc, ghi chú kỳ — do agent và người
# viết. Trước v2, chạy lại `bao-cao` ghi đè sạch phần thứ hai.
#
# Nay phần chữ người nằm ở `dashboard/data/<ky>.nguoi.json` và được phủ LÊN
# bản máy sinh. Lần chạy đầu trên một kỳ đã có file, script TỰ RÚT phần chữ
# người ra lớp phủ rồi mới ghi — ⛔ không mất gì.

NGUOI_DUONG = [
    ("ky", "tu"), ("ky", "den"), ("ky", "tu_hien"), ("ky", "den_hien"),
    ("ky", "crawl"), ("ky", "nguon"),
    ("chan",), ("chi_phi",), ("ket_luan",), ("theo_doi",),
    ("canh_bao",),                      # cảnh báo do người viết, cụ thể hơn bản máy
    ("pheu", "van_de"),
    ("nhan_vien", "viec_he_thong"),     # lỗi hệ, gom theo nguyên nhân — id-F §8 ⑤
    ("facebook",),                      # ⚠ gồm cả câu "kỳ này không có số quảng cáo"
    ("chan_dung", "insight"), ("chan_dung", "co_hoi_win"),
    ("chan_dung", "cach_tinh_win"), ("chan_dung", "ma_tran_cd_5a"),
    ("ma_tran",), ("hook",), ("so_tay",), ("viec",),
    ("facebook", "van_de"), ("truoc",), ("moc_goc",), ("ghi_chu",),
]


def _lay(d, duong):
    for k in duong:
        if not isinstance(d, dict) or k not in d:
            return None
        d = d[k]
    return d


def _dat(d, duong, v):
    for k in duong[:-1]:
        d = d.setdefault(k, {})
    d[duong[-1]] = v


def _rong(v):
    return v is None or v == [] or v == {} or v == ""


def rut_lop_phu(cu):
    """Rút phần chữ người từ một file kỳ đã có."""
    lp = {"_ghi_chu": "CHỮ NGƯỜI của kỳ này — phủ lên bản máy sinh mỗi lần chạy "
                      "`id.py bao-cao`. ⛔ Con số trong này KHÔNG tự cập nhật: "
                      "sửa số thì sửa cả câu.",
          "_schema": "insight-dashboard-kangnam#nguoi/1"}
    for duong in NGUOI_DUONG:
        v = _lay(cu, duong)
        if not _rong(v):
            _dat(lp, duong, v)
    phu = {t["id"]: t["phu"] for t in (cu.get("the_tong") or [])
           if t.get("id") and t.get("phu")}
    if phu:
        lp["the_phu"] = phu
    return lp


def _phu_sau(may, lp):
    """Phủ dict `lp` lên dict `may`; dict thì đệ quy, còn lại thì lp thắng."""
    for k, v in lp.items():
        if k.startswith("_") or k == "the_phu":
            continue
        if isinstance(v, dict) and isinstance(may.get(k), dict):
            _phu_sau(may[k], v)
        else:
            may[k] = v


def phu_nguoi(D, lp):
    _phu_sau(D, lp)
    for t in D.get("the_tong") or []:
        if t.get("id") in (lp.get("the_phu") or {}):
            t["phu"] = lp["the_phu"][t["id"]]
    return D


def lenh_bao_cao(args):
    ht_f = os.path.join(RA, "doc-hoi-thoai.json")
    if not os.path.exists(ht_f):
        sys.exit("⛔ Chưa có out/doc-hoi-thoai.json. Chạy `id.py doc` trước.")
    with open(ht_f, encoding="utf-8") as f:
        H = json.load(f)
    A, ads_lech = None, None
    ads_f = os.path.join(RA, "doc-ads.json")
    if os.path.exists(ads_f):
        with open(ads_f, encoding="utf-8") as f:
            A = json.load(f)
        # ⛔ Số quảng cáo của kỳ khác ⛔ KHÔNG được lẫn vào báo cáo kỳ này.
        #    Bản cũ nhận bất cứ doc-ads.json nào có trong out/ — một kỳ cũ còn
        #    sót lại là đủ để dựng cả chuỗi CPM→CPB sai mà không ai thấy.
        if (A.get("ky") or "") != args.ky:
            ads_lech = A.get("ky") or "trống"
            A = None

    ky_id = args.ky.replace("/", "-").replace(" ", "")
    D = {
        "schema": "insight-dashboard-kangnam/3",
        "ky": {"id": ky_id, "nhan": args.ky, "tao": H["tao"], "nguon": H["nguon"]},
        "canh_bao": [],
        "the_tong": H["the_tong"],
        "ket_luan": {"marketing": [], "truc_page": [], "he_thong": [], "bu_quyet": []},
        "theo_doi": [],
        "pheu": {"so_ht_phan_tich": H["so_ht"], "nhiet": H["nhiet"],
                 "nhiet_x_sdt": H["nhiet_x_sdt"], "tin_hieu": H["tin_hieu"],
                 "nguyen_nhan_roi": H["nguyen_nhan_roi"], "rao_can": H["rao_can"],
                 "ma_o": H["ma_o"], "chot_lich": H.get("chot_lich"), "van_de": []},
        # ★ Khối lead — tab «Hàng chờ gọi». Thiếu khối này (file schema /1)
        #   thì trang hiện ô khoá, ⛔ không hiện 0 (id-J §3 luật ①).
        "lead": H.get("lead"),
        # ★ Khối kf64 — bảng xếp hạng chân dung CỦA RECORD từ 02/11/2026.
        #   `chan_dung.co_hoi_win` là bản proxy cũ của `id-M` §7, đã nghỉ.
        "kf64": H.get("kf64"),
        "chan_dung": {"phac_hoa": H.get("phac_hoa", {}), "tep": H["chan_dung"],
                      "insight": [], "nac": H["nac"]},
        "nhan_vien": H["nhan_vien"],
        "facebook": ({"nguon": A["nguon"], "don_vi": "đ", "chuoi": A["chuoi"],
                      "dong": A["dong"], "van_de": []} if A else
                     {"co_du_lieu": False, "ghi_chu": "⚠ chưa có dữ liệu quảng cáo Facebook"}),
        "google": {"co_du_lieu": False, "ghi_chu": "⚠ chưa có dữ liệu Google Ads"},
        "ma_tran": {"trang_thai": "cho_duyet", "khoi": [], "sua_van_hanh": [], "quan_sat": []},
        "hook": {"dong": [], "ghi_chu": "chưa viết — ma trận chưa được duyệt"},
        "so_tay": {"da_sinh": False, "so_ban": 0, "duong_dan": "out/so-tay/"},
        "viec": [],
        "ghi_chu": [
            "Nguồn hội thoại: %s · %d hội thoại phân tích." % (H["nguon"], H["so_ht"]),
            "Nấc 5A · mã O · mức nóng · rào cản · vì sao rơi · chấm N1–N6: đọc tự động "
            "bằng tools/id.py, CHƯA qua người soát.",
            "Chân dung KHÔNG có bộ mặc định: phác họa từ hội thoại của kỳ, gán theo dấu "
            "hiệu trong tools/chan_dung_kf62.json — thư viện cố định KF-62 (id-M).",
            "N3.2 (thông tin khớp bảng hiện hành) luôn chấm «—» vì cần người đối chiếu "
            "bảng giá hiện hành — xem id-F §3.",
            "Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay xếp hạng công khai.",
        ],
    }
    # ⛔ Ô ma trận KF-64 chốt bằng mốc cứng 100, mà kỳ này `hiệu quả` chỉ còn
    #    MỘT trục (Chất lượng) vì chưa có booking CRM. Chất lượng lại so với
    #    trung bình của chính dịch vụ mình, nên khi một dịch vụ chỉ có vài chân
    #    dung thì mọi chỉ số dồn về đúng 100 — ô rơi bên nào là chuyện may rủi.
    K = H.get("kf64") or {}
    sat = [c for c in (K.get("chan_dung") or []) if c.get("o_sat_moc")]
    if sat:
        D["canh_bao"].append({"muc": "bad", "may": 1, "text":
            "⛔ Ma trận 4 ô của KF-64 CHƯA chốt được kỳ này: %d/%d chân dung được "
            "xếp hạng có «điểm hiệu quả» lệch mốc 100 dưới %g điểm (%s). Hai bên "
            "mốc là hai chiến lược trái nhau — ô ① scale +15–20%%/3 ngày, ô ④ duy "
            "trì tối thiểu. Lý do không phải mốc sai mà là `hiệu quả` đang chỉ còn "
            "MỘT trục: Chuyển đổi (62,5%% trọng số) trống vì chưa có booking CRM, "
            "và Chất lượng thì so với trung bình chính dịch vụ mình nên vài chân "
            "dung trong một dịch vụ luôn dồn về quanh 100. ⛔ Đừng dùng ô ma trận "
            "để chia ngân sách trước khi CRM gắn mã chân dung (id-N §10 ①)."
            % (len(sat), K.get("so_du_mau", 0), KF64_SAT_MOC,
               " · ".join("%s %.1f" % (c["cd"], c["hieu_qua"]) for c in sat))})
    if K.get("chan_dung") and not any(c.get("tang") for c in K["chan_dung"]):
        D["canh_bao"].append({"muc": "warn", "may": 1, "text":
            "⚠ KF-64 ⛔ không tìm ra tầng nội dung ưu tiên nào ở cấp chân dung: "
            "không bước nào tụt dưới %g so với trung bình dịch vụ. Nhưng hai bước "
            "hay nghẽn nhất — S5 (Hot→booking) và S6 (booking→đến khám) — ⛔ chưa "
            "đo được vì thiếu CRM, nên kết quả này ⛔ KHÔNG có nghĩa là phễu không "
            "nghẽn. Việc đọc được ngay là luật T2 ở cấp dịch vụ (id-N §5)."
            % KF64_NGHEN})
    if H["nhan_vien"]["co_do"]:
        D["canh_bao"].append({"muc": "bad", "text": "Có %d cờ đỏ trong kỳ — xem tab Chấm điểm."
                                                   % len(H["nhan_vien"]["co_do"])})
    pha = H.get("phac_hoa") or {}
    if pha.get("trang_thai") != "da_duyet":
        D["canh_bao"].append({"muc": "bad",
                              "text": "Chân dung chưa qua CỔNG 0 — tab Chân dung còn trống (%s)."
                                      % (pha.get("vi_sao") or "chưa phác họa")})
    if ads_lech:
        D["canh_bao"].append({"muc": "bad", "may": 1, "text":
            "⛔ Bỏ qua out/doc-ads.json: file đó là của kỳ «%s», không phải «%s». "
            "Tab Marketing để trống — ⛔ không lấy số kỳ khác gán sang." % (ads_lech, args.ky)})
    elif not A:
        D["canh_bao"].append({"muc": "warn", "text": "Chưa có file chỉ số quảng cáo — tab Marketing trống."})
    D["canh_bao"].append({"muc": "warn", "text": "Chưa có dữ liệu Google Ads (id-B §4)."})
    # ★ CỔNG ① KF-62 §4: «Chưa xác định» ≤15%. Trượt thì thư viện CHƯA ổn định
    #   cho line này — nói ra ngay ở đầu trang, ⛔ không để bảng trông như đã chuẩn.
    tep = H.get("chan_dung") or []
    nt = H.get("so_ht") or 0
    chua = sum(r["ht"] for r in tep
               if r["cd"].endswith("CHUA_XAC_DINH") or r["cd"] == CD_DU)
    if nt and chua * 100.0 / nt > 15:
        D["canh_bao"].append({"muc": "bad", "may": 1, "text":
            "⛔ Thư viện chân dung KF-62 CHƯA qua cổng ① cho kỳ này: %d/%d hội thoại "
            "(%.1f%%) chưa xếp được chân dung, ngưỡng là 15%%. Nguyên nhân đo được: "
            "khách chưa nói tình trạng (trung vị chữ khách 44 ký tự) và 2 câu hỏi vàng "
            "chưa được áp dụng. ⛔ Đừng dùng bảng chân dung kỳ này để chia ngân sách."
            % (chua, nt, chua * 100.0 / nt)})
    L = H.get("lead") or {}
    bb = L.get("bat_bien") or {}
    if L and not bb.get("dat", True):
        # ⛔ Hai bất biến này sai là LỖI CODE, không phải chuyện ngưỡng.
        D["canh_bao"].append({"muc": "bad", "may": 1, "text":
            "Khối lead sai bất biến: %d HT vào hàng gọi mà không có SĐT · "
            "%d HT nhãn HOT rơi xuống nhóm Remarketing — ⛔ đừng phát hàng chờ."
            % (bb.get("goi_ngay_thieu_sdt", 0), bb.get("id_d_hot_roi_khong", 0))})
    if L:
        D["ghi_chu"].append(
            "Hàng chờ gọi chấm bằng bộ %s. Nhãn HOT/WARM/COLD của kỳ vẫn là nhãn "
            "5 tín hiệu (id-D §2) — KF-60 ⛔ không phát nhãn thứ hai, nó chia tệp "
            "thành bốn nhóm việc và xếp thứ tự trong nhóm." % L.get("bo_cham", "KF-60"))

    dd = os.path.join(GOC, "dashboard", "data")
    os.makedirs(dd, exist_ok=True)
    fp = os.path.join(dd, ky_id + ".json")
    lp_p = os.path.join(dd, ky_id + ".nguoi.json")

    # ① Chưa có lớp phủ mà kỳ đã có file → RÚT chữ người ra trước khi ghi đè.
    if not os.path.exists(lp_p) and os.path.exists(fp):
        with open(fp, encoding="utf-8") as f:
            cu = json.load(f)
        lp = rut_lop_phu(cu)
        with open(lp_p, "w", encoding="utf-8") as f:
            json.dump(lp, f, ensure_ascii=False, indent=1)
        print("  ✓ đã rút chữ người của kỳ ra %s.nguoi.json" % ky_id)

    # ② Phủ chữ người lên bản máy sinh.
    #    ⚠ Lớp phủ thay CẢ danh sách `canh_bao`, nên cảnh báo CHẶN do máy sinh
    #    (cổng KF-62, bất biến lead, lệch kỳ của file ads) phải được gắn lại
    #    SAU khi phủ — ⛔ không để chữ người vô tình xoá mất một cờ đỏ.
    may = [c for c in D["canh_bao"] if c.get("may")]
    if os.path.exists(lp_p):
        with open(lp_p, encoding="utf-8") as f:
            D = phu_nguoi(D, json.load(f))
    co = set(json.dumps(c, ensure_ascii=False) for c in D.get("canh_bao") or [])
    for c in may:
        if json.dumps(c, ensure_ascii=False) not in co:
            D.setdefault("canh_bao", []).insert(0, c)

    with open(fp, "w", encoding="utf-8") as f:
        json.dump(D, f, ensure_ascii=False, indent=1)

    ip = os.path.join(dd, "index.json")
    idx = {"schema": "insight-dashboard-kangnam#index", "ky": []}
    if os.path.exists(ip):
        with open(ip, encoding="utf-8") as f:
            idx = json.load(f)
    idx["cap_nhat"] = datetime.now().strftime("%Y-%m-%d")
    idx["ky"] = [k for k in idx.get("ky", []) if k["id"] != ky_id]
    idx["ky"].insert(0, {"id": ky_id, "nhan": args.ky, "file": "data/%s.json" % ky_id})
    with open(ip, "w", encoding="utf-8") as f:
        json.dump(idx, f, ensure_ascii=False, indent=1)

    print("\n  Đã ghi dashboard/data/%s.json và cập nhật index.json" % ky_id)
    print("  Mở dashboard/index.html để xem.")
    # ⚠ Trạng thái đọc từ file VỪA GHI (đã phủ chữ người), ⛔ không in cứng:
    #    lớp phủ mở được CỔNG 1 thì dòng này phải nói đúng điều đó.
    mt = D.get("ma_tran") or {}
    if mt.get("trang_thai") == "da_duyet":
        print("  ✓ CỔNG 1 đã mở — %d khối ma trận · %d hook%s\n"
              % (len(mt.get("khoi") or []), len((D.get("hook") or {}).get("dong") or []),
                 " · duyệt bởi " + mt["duyet_boi"] if mt.get("duyet_boi") else ""))
    else:
        print("  ⚠ Ma trận đang ở trạng thái CHỜ DUYỆT — tab Hook và Sổ tay còn trống.\n")


# ──────────────────────────────── main ───────────────────────────────────

def main():
    p = argparse.ArgumentParser(description="Agent-InsightDashboard-Kangnam · công cụ đếm")
    sp = p.add_subparsers(dest="lenh", required=True)

    a = sp.add_parser("doc", help="đọc file hội thoại → phân loại + chấm điểm")
    a.add_argument("file")
    a.add_argument("--ky", required=True)
    a.set_defaults(fn=lenh_doc)

    d = sp.add_parser("chan-dung", help="CỔNG 0 — khuôn · kiểm · duyệt bản phác họa chân dung")
    d.add_argument("--ky", required=True)
    d.add_argument("--mau", action="store_true", help="ghi khuôn trống out/chan-dung.json")
    d.add_argument("--ghi-de", dest="ghi_de", action="store_true", help="cho --mau ghi đè file cũ")
    d.add_argument("--kiem", action="store_true", help="soát bản phác họa (mặc định)")
    d.add_argument("--duyet", metavar="NGUOI", help="mở CỔNG 0 — ghi tên người duyệt")
    d.set_defaults(fn=lenh_chan_dung)

    b = sp.add_parser("ads", help="đọc file chỉ số quảng cáo Facebook")
    b.add_argument("file")
    b.add_argument("--ky", required=True)
    b.set_defaults(fn=lenh_ads)

    c = sp.add_parser("bao-cao", help="gộp thành JSON cho dashboard")
    c.add_argument("--ky", required=True)
    c.set_defaults(fn=lenh_bao_cao)

    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    main()
