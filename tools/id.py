#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
id.py · Agent-InsightDashboard-Kangnam

Làm phần ĐẾM ĐƯỢC của quy trình B1–B6:
  doc     : đọc file hội thoại Caresoft → phân loại CD · 5A · mã O · mức nóng ·
            rào cản · vì sao rơi · chấm điểm nhân viên N1–N6 · cờ đỏ
  ads     : đọc file chỉ số quảng cáo Facebook → chuỗi CPM→CTR→CPI→CPL→CPB
  bao-cao : gộp kết quả thành file JSON cho dashboard

⛔ Script KHÔNG làm phần đọc hiểu: insight, câu hỏi ngầm, hướng nội dung,
   câu mẫu trong sổ tay. Đó là việc của agent (xem SYSTEM-PROMPT.md §8).

Cách dùng:
    python tools/id.py doc du-lieu/hoi-thoai.md --ky 19-25/10
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

def gan_chan_dung(ht, td):
    kh = ht["kh_text"]
    for cd in ("CD3", "CD6", "CD5", "CD4", "CD2", "CD1"):
        if co_tu(kh, td["chan_dung"][cd]):
            return cd
    return "CD0"


def gan_nac(ht, td):
    """Đọc câu hỏi ĐẦU TIÊN của khách (id-C §2)."""
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
    """Mỗi hội thoại ĐÚNG MỘT giá trị (id-D §3)."""
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


RAO_CAN = {
    "chưa nói tình trạng": [],   # tính riêng
    "hỏi giá ngay": [],
    "sợ đau/nghỉ việc": "O-04",
    "ở xa": "O-09",
    "người nhà cản": "O-11",
    "đã làm nơi khác": None,
    "so giá đối thủ": "O-10",
    "chờ ưu đãi": None,
    "chưa tin cơ sở": "O-06",
}


def gan_rao_can(ht, td, cd, ma_o):
    rc = []
    if cd == "CD0":
        rc.append("chưa nói tình trạng")
    dau = next((t["text"] for t in ht["tin"] if not t["nv"] and len(t["text"]) > 3), "")
    if co_tu(dau, td["ma_o"]["O-01"]):
        rc.append("hỏi giá ngay")
    if cd == "CD3":
        rc.append("đã làm nơi khác")
    if co_tu(ht["kh_text"], ["đợi ưu đãi", "chờ sale", "khi nào giảm"]):
        rc.append("chờ ưu đãi")
    for ten, ma in RAO_CAN.items():
        if isinstance(ma, str) and ma in ma_o:
            rc.append(ten)
    return sorted(set(rc))


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

    ban_ghi, co_do_all = [], []
    for ht in hts:
        cd = gan_chan_dung(ht, td)
        nac = gan_nac(ht, td)
        ma_o = gan_ma_o(ht, td)
        nhiet, tin_hieu = gan_nhiet(ht, td)
        k, diem, co_do = cham_hoi_thoai(ht, td, ma_o)
        ht["chot_lich"] = bool(co_tu(ht["nv_text"], td["nv_moi_lich"]) and co_tu(ht["kh_text"], ["vâng", "ok", "được", "em qua"]))
        roi = gan_vi_sao_roi(ht, td, diem)
        rc = gan_rao_can(ht, td, cd, ma_o)
        for c in co_do:
            co_do_all.append({"ma": c["ma"], "nguoi": ht["nv"], "ht": ht["ma"], "trich": c["trich"]})
        ban_ghi.append({
            "ma": ht["ma"], "nv": ht["nv"], "cd": cd, "nac": nac, "ma_o": ma_o,
            "nhiet": nhiet, "tin_hieu": tin_hieu, "co_sdt": ht["co_sdt"],
            "chot_lich": ht["chot_lich"], "roi": roi, "rao_can": rc,
            "dich_vu": gan_dich_vu(ht, td), "he_so": he_so_gia_tri(ht, td),
            "diem": diem, "cham": k, "co_do": [c["ma"] for c in co_do],
            "so_luot_kh": sum(1 for t in ht["tin"] if not t["nv"]),
        })

    n = len(ban_ghi)
    os.makedirs(RA, exist_ok=True)

    # bảng chấm từng hội thoại
    with open(os.path.join(RA, "cham-hoi-thoai.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        cot = [m for _, _, ds in TIEU_CHI for m, _, _ in ds]
        w.writerow(["ma", "nv", "cd", "nac", "ma_o", "nhiet", "co_sdt", "chot_lich",
                    "vi_sao_roi", "rao_can", "dich_vu", "he_so", "diem", "co_do"] + cot)
        for r in ban_ghi:
            w.writerow([r["ma"], r["nv"], r["cd"], r["nac"], " ".join(r["ma_o"]), r["nhiet"],
                        "Có" if r["co_sdt"] else "", "Có" if r["chot_lich"] else "",
                        r["roi"], " · ".join(r["rao_can"]), r["dich_vu"], r["he_so"],
                        r["diem"] if r["diem"] is not None else "", " ".join(r["co_do"])]
                       + [r["cham"].get(c, "") for c in cot])

    # tổng hợp nhân viên
    theo_nv = defaultdict(list)
    for r in ban_ghi:
        theo_nv[r["nv"]].append(r)
    ca_nhan = []
    for nv, rs in sorted(theo_nv.items(), key=lambda x: -len(x[1])):
        ds = [r["diem"] for r in rs if r["diem"] is not None]
        d = round(sum(ds) / len(ds), 1) if ds else None
        cds = sorted({c for r in rs for c in r["co_do"]})
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
        "ky": args.ky, "so_ht": n, "nguon": os.path.basename(args.file),
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
        "chan_dung": [_dong_cd(ban_ghi, cd) for cd in
                      ("CD0", "CD1", "CD2", "CD3", "CD4", "CD5", "CD6")],
        "nac": dict(Counter(r["nac"] for r in ban_ghi)),
        "nhan_vien": {"phan_bo": dict(Counter(c["loai"] for c in ca_nhan)),
                      "nhom": nhom, "ca_nhan": ca_nhan, "co_do": co_do_all,
                      "ghi_chu": "Điểm dùng để phân việc kèm cặp. "
                                 "Không phải căn cứ kỷ luật hay xếp hạng công khai."},
        "the_tong": _the_tong(ban_ghi),
    }
    with open(os.path.join(RA, "doc-hoi-thoai.json"), "w", encoding="utf-8") as f:
        json.dump(ket, f, ensure_ascii=False, indent=1)

    _in_tom_tat(ket, ban_ghi)


def _pct_nhom(rs, ma_nhom):
    ds = [m for g, _, lst in TIEU_CHI if g == ma_nhom for m, _, _ in lst]
    dat = sum(1 for r in rs for m in ds if r["cham"].get(m) == "✓")
    chua = sum(1 for r in rs for m in ds if r["cham"].get(m) == "✗")
    return pct(dat, dat + chua)


TEN_CD = {"CD0": "Thăm dò — chưa rõ nhu cầu", "CD1": "Khuyết điểm", "CD2": "Hot Face",
          "CD3": "Sửa lại", "CD4": "Nam giới", "CD5": "Phong thủy", "CD6": "Khó, bệnh lý"}


def _dong_cd(ban_ghi, cd):
    rs = [r for r in ban_ghi if r["cd"] == cd]
    return {"cd": cd, "ten": TEN_CD[cd], "ht": len(rs),
            "hot": sum(1 for r in rs if r["nhiet"] == "HOT"),
            "warm": sum(1 for r in rs if r["nhiet"] == "WARM"),
            "cold": sum(1 for r in rs if r["nhiet"] == "COLD"),
            "co_sdt": sum(1 for r in rs if r["co_sdt"]),
            "chot_lich": sum(1 for r in rs if r["chot_lich"]),
            "bo_1_luot": sum(1 for r in rs if r["so_luot_kh"] <= 1),
            "roi_truc": sum(1 for r in rs if r["roi"] == "trực page"),
            "he_so": max([r["he_so"] for r in rs], default=1)}


def _the_tong(ban_ghi):
    n = len(ban_ghi)
    bo1 = sum(1 for r in ban_ghi if r["so_luot_kh"] <= 1)
    sdt = sum(1 for r in ban_ghi if r["co_sdt"])
    sla = [r for r in ban_ghi if r["cham"].get("N1.1") in ("✓", "✗")]
    nong_chua = sum(1 for r in ban_ghi if r["nhiet"] in ("HOT", "WARM") and not r["co_sdt"])
    return [
        {"id": "ht", "nhan": "Hội thoại phân tích", "gia_tri": n, "kieu": "n"},
        {"id": "bo_1", "nhan": "Bỏ sau 1 lượt", "gia_tri": pct(bo1, n), "kieu": "pct",
         "tot": "thap", "phu": "%d/%d HT" % (bo1, n)},
        {"id": "co_sdt", "nhan": "Có SĐT", "gia_tri": pct(sdt, n), "kieu": "pct",
         "tot": "cao", "phu": "%d/%d HT" % (sdt, n)},
        {"id": "sla", "nhan": "Trả lời tin đầu ≤2′", "gia_tri":
            pct(sum(1 for r in sla if r["cham"]["N1.1"] == "✓"), len(sla)), "kieu": "pct",
         "tot": "cao", "phu": "trong khung 8h30–22h · chuẩn ≥90%"},
        {"id": "nong_chua_sdt", "nhan": "HOT/WARM chưa có SĐT", "gia_tri": nong_chua,
         "kieu": "n", "tot": "thap", "phu": "lead nóng chưa vào tay telesale"},
    ]


def _in_tom_tat(k, ban_ghi):
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
    p("  CHÂN DUNG")
    p("    %-5s %-30s %4s %4s %4s %4s %6s %5s" % ("mã", "tên", "HT", "HOT", "WRM", "SĐT", "%SĐT", "lịch"))
    for c in k["chan_dung"]:
        p("    %-5s %-30s %4d %4d %4d %4d %5s%% %5d" % (
            c["cd"], c["ten"][:30], c["ht"], c["hot"], c["warm"], c["co_sdt"],
            pct(c["co_sdt"], c["ht"]) if c["ht"] else "—", c["chot_lich"]))
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
    p("  ⚠ Script chỉ làm phần ĐẾM. Insight, câu hỏi ngầm, hướng nội dung,")
    p("    câu mẫu trong sổ tay — agent phải đọc và viết, xem SYSTEM-PROMPT §8.")
    p("")
    p("  Đã ghi: out/doc-hoi-thoai.json · out/cham-hoi-thoai.csv")
    p("")


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
    chuoi = [
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
           "ghi_chu": ["⚠ Mốc mục tiêu chưa có — cần TB 30 ngày của từng dịch vụ (id-E §1).",
                       "⛔ Chưa phân rã CPL thì chưa kết luận lỗi nội dung (id-E §1)."]}
    with open(os.path.join(RA, "doc-ads.json"), "w", encoding="utf-8") as f:
        json.dump(ket, f, ensure_ascii=False, indent=1)

    print("")
    print("═" * 66)
    print("  CHỈ SỐ QUẢNG CÁO · kỳ %s · %d dòng" % (args.ky, len(rows)))
    print("═" * 66)
    for c in chuoi:
        v = c["gia_tri"]
        print("    %-24s %12s   mục tiêu: ⚠ chưa có mốc so sánh" %
              (c["nhan"], "—" if v is None else ("%.1f%%" % v if c["kieu"] == "pct" else "{:,.0f} đ".format(v))))
    print("")
    print("  %d nội dung · đã ghi out/doc-ads.json" % len(dong))
    print("")


def _chia(a, b):
    return round(a / b, 1) if b else None


# ─────────────────────────── lệnh `bao-cao` ──────────────────────────────

def lenh_bao_cao(args):
    ht_f = os.path.join(RA, "doc-hoi-thoai.json")
    if not os.path.exists(ht_f):
        sys.exit("⛔ Chưa có out/doc-hoi-thoai.json. Chạy `id.py doc` trước.")
    with open(ht_f, encoding="utf-8") as f:
        H = json.load(f)
    A = None
    ads_f = os.path.join(RA, "doc-ads.json")
    if os.path.exists(ads_f):
        with open(ads_f, encoding="utf-8") as f:
            A = json.load(f)

    ky_id = args.ky.replace("/", "-").replace(" ", "")
    D = {
        "schema": "insight-dashboard-kangnam/1",
        "ky": {"id": ky_id, "nhan": args.ky, "tao": H["tao"], "nguon": H["nguon"]},
        "canh_bao": [],
        "the_tong": H["the_tong"],
        "ket_luan": {"marketing": [], "truc_page": [], "he_thong": [], "bu_quyet": []},
        "theo_doi": [],
        "pheu": {"so_ht_phan_tich": H["so_ht"], "nhiet": H["nhiet"],
                 "nhiet_x_sdt": H["nhiet_x_sdt"], "tin_hieu": H["tin_hieu"],
                 "nguyen_nhan_roi": H["nguyen_nhan_roi"], "rao_can": H["rao_can"],
                 "ma_o": H["ma_o"], "van_de": []},
        "chan_dung": {"tep": H["chan_dung"], "insight": [], "nac": H["nac"]},
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
            "Phân loại CD · nấc 5A · mã O · mức nóng · rào cản · vì sao rơi · chấm N1–N6: "
            "đọc tự động bằng tools/id.py, CHƯA qua người soát.",
            "N3.2 (thông tin khớp bảng hiện hành) luôn chấm «—» vì cần người đối chiếu "
            "bảng giá hiện hành — xem id-F §3.",
            "Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay xếp hạng công khai.",
        ],
    }
    if H["nhan_vien"]["co_do"]:
        D["canh_bao"].append({"muc": "bad", "text": "Có %d cờ đỏ trong kỳ — xem tab Chấm điểm."
                                                   % len(H["nhan_vien"]["co_do"])})
    if not A:
        D["canh_bao"].append({"muc": "warn", "text": "Chưa có file chỉ số quảng cáo — tab Marketing trống."})
    D["canh_bao"].append({"muc": "warn", "text": "Chưa có dữ liệu Google Ads (id-B §4)."})

    dd = os.path.join(GOC, "dashboard", "data")
    os.makedirs(dd, exist_ok=True)
    fp = os.path.join(dd, ky_id + ".json")
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
    print("  ⚠ Ma trận đang ở trạng thái CHỜ DUYỆT — tab Hook và Sổ tay còn trống.\n")


# ──────────────────────────────── main ───────────────────────────────────

def main():
    p = argparse.ArgumentParser(description="Agent-InsightDashboard-Kangnam · công cụ đếm")
    sp = p.add_subparsers(dest="lenh", required=True)

    a = sp.add_parser("doc", help="đọc file hội thoại → phân loại + chấm điểm")
    a.add_argument("file")
    a.add_argument("--ky", required=True)
    a.set_defaults(fn=lenh_doc)

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
