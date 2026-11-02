#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
knb.py · Agent-InsightDashboard-Kangnam

Đọc **bản xuất KNB** (`schema knb-xuat-hoi-thoai/1`, extension KNB 1.3.0) và chạy
đúng bộ phân loại / chấm điểm của `tools/id.py`, rồi ghi ra cùng những file mà
`id.py bao-cao` đọc. Nhờ vậy hai khuôn đầu vào đi về **một** file báo cáo.

    Caresoft  →  id.py doc   ─┐
                              ├─→  out/doc-hoi-thoai.json  →  id.py bao-cao
    KNB 1.3.0 →  knb.py      ─┘

Khuôn KNB khác khuôn Caresoft mà `id.py doc` đọc:

    ## N. HT-xxxx · KH-xxxx · <dịch vụ>
    - Page: … | Nhóm: … | Khu vực page: —
    - Khách mới — hồ sơ tạo … | Vào Beauty vì: …
    - Cụm: … | Dịch vụ theo: … | Nhóm QC: …
    - Lượt khách: N | SĐT: … | Phản hồi đầu của NV: … | Bỏ sót: N
    [DD/MM HH:MM] **KH:** …   **NV (NV-id) ⏱ 7p20 ✗:** …   **BOT:** …  **QC:** …

⛔ Script này KHÔNG định nghĩa lại tiêu chí nào. Nó **dịch khuôn** rồi gọi lại
   `id.py`: `gan_nac` · `gan_ma_o` · `gan_nhiet` · `cham_hoi_thoai` · `cham_lead`
   · `gom_doc`. Sửa tiêu chí thì sửa ở `id.py`, ⛔ không sửa ở đây.

★ Hai chỗ bản KNB nói chính xác hơn, và script tin bản xuất:
   ① `N1.1` dùng cờ ⏱ của bản xuất — nó chỉ cộng phần chờ TRONG giờ trực.
   ② Mẫu phân tích = **khách mới**. Khách cũ đã cho SĐT từ kỳ trước nên để lẫn
      vào sẽ làm lệch «% có SĐT» của kỳ.

Cách dùng:
    python tools/knb.py data/KNB_1_toan_bo_24-10_den_29-10.txt --ky "24-29/10"
    python tools/id.py bao-cao --ky "24-29/10"
"""

import argparse
import importlib.util
import json
import os
import re
import sys
from collections import Counter

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RA_MD = os.path.join(GOC, "out")


def nap_id_py():
    """Nạp tools/id.py như một module (tên file trùng builtin `id`)."""
    p = os.path.join(GOC, "tools", "id.py")
    spec = importlib.util.spec_from_file_location("kn_id", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# ───────────────────────────── đọc khuôn KNB ─────────────────────────────

RE_TIEU_DE = re.compile(r'^##\s+(\d+)\.\s+(HT-\w+)\s+·\s+(KH-\w+)\s+·\s+(.+?)\s*$', re.M)
RE_TIN = re.compile(r'^\[(\d{2})/(\d{2})\s+(\d{2}:\d{2})(?::\d{2})?\]\s+\*\*(.+?):\*\*\s?(.*)$')
RE_NV = re.compile(r'^NV\s+\((NV-\d+)\)(.*)$')
RE_SLA = re.compile(r'⏱\s*(ngoài giờ|[^✓✗]*?)\s*([✓✗])?$')


def _tem(dd, mm, hhmm):
    """DD/MM HH:MM  →  MM-DD HH:MM  (khuôn tem của id.py)."""
    return "%s-%s %s" % (mm, dd, hhmm)


def doc_knb(duong_dan, id_py):
    raw = open(duong_dan, encoding="utf-8-sig").read()
    moc = [(m.start(), m.group(1), m.group(2), m.group(3), m.group(4))
           for m in RE_TIEU_DE.finditer(raw)]
    if not moc:
        sys.exit("⛔ Không nhận ra khuôn KNB.")

    ket = []
    for i, (vt, so, ht_id, kh_id, dv) in enumerate(moc):
        het = moc[i + 1][0] if i + 1 < len(moc) else len(raw)
        khoi = raw[vt:het]
        dong = khoi.splitlines()

        meta = {"page": "", "nhom_page": "", "khach": "", "vao_vi": "",
                "cum": "", "dv_theo": "", "nhom_qc": "", "luot_kh": None,
                "sdt": "", "bo_sot": 0, "chi_bot": "⚠ chỉ bot trả lời" in khoi,
                "qc_pttm": "⛔ QC PTTM" in dong[0], "viet_kieu": "🌏" in dong[0],
                "gan_theo_qc": "⚑" in dong[0]}
        for d in dong[1:6]:
            if not d.startswith("- "):
                continue
            if d.startswith("- Page:"):
                m = re.search(r'Page:\s*(.*?)\s*\|\s*Nhóm:\s*(.*?)\s*\|', d)
                if m:
                    meta["page"], meta["nhom_page"] = m.group(1), m.group(2)
            elif d.startswith("- Khách"):
                meta["khach"] = "moi" if d.startswith("- Khách mới") else "cu"
                m = re.search(r'Vào Beauty vì:\s*(.*?)\s*$', d)
                if m:
                    meta["vao_vi"] = m.group(1)
            elif d.startswith("- Cụm:"):
                m = re.search(r'Cụm:\s*(.*?)\s*\|\s*Dịch vụ theo:\s*(.*?)\s*\|\s*Nhóm QC:\s*(.*?)\s*$', d)
                if m:
                    meta["cum"], meta["dv_theo"], meta["nhom_qc"] = m.group(1), m.group(2), m.group(3)
            elif d.startswith("- Lượt khách:"):
                m = re.search(r'Lượt khách:\s*(\d+)', d)
                if m:
                    meta["luot_kh"] = int(m.group(1))
                meta["sdt"] = "co" if "SĐT: khách chủ động cho" in d else "chua"
                m = re.search(r'Bỏ sót:\s*(\d+)', d)
                if m:
                    meta["bo_sot"] = int(m.group(1))

        # ── tin nhắn, gộp dòng tiếp nối vào tin trước ──
        tin, sla_dau = [], None
        for d in dong:
            mt = RE_TIN.match(d)
            if not mt:
                if tin and d.strip() and not d.startswith(("- ", "## ", "---", "───")):
                    tin[-1]["text"] += " " + d.strip()
                continue
            tem = _tem(mt.group(1), mt.group(2), mt.group(3))
            ai, text = mt.group(4).strip(), mt.group(5).strip()
            mnv = RE_NV.match(ai)
            if mnv:
                nv_id, duoi = mnv.group(1), mnv.group(2)
                if sla_dau is None and "⏱" in duoi:
                    s = RE_SLA.search(duoi)
                    if s:
                        sla_dau = "ngoai_gio" if "ngoài giờ" in s.group(1) else \
                                  ("dat" if s.group(2) == "✓" else "truot")
                tin.append({"tem": tem, "nv": True, "ten": nv_id, "text": text,
                            "nhieu": id_py.la_nhieu(text), "anh": id_py.co_anh(text),
                            "loai": "nv"})
            elif ai == "KH":
                tin.append({"tem": tem, "nv": False, "ten": "", "text": text,
                            "nhieu": id_py.la_nhieu(text), "anh": id_py.co_anh(text),
                            "loai": "kh"})
            else:
                # BOT · QC · HT — ⛔ không phải lời khách, cũng không ghi cho người nào.
                #   BOT trả lời mà không có NV nào vào → hội thoại rơi do "hệ thống".
                tin.append({"tem": tem, "nv": False, "ten": "", "text": text,
                            "nhieu": True, "anh": id_py.co_anh(text),
                            "loai": "bot" if ai == "BOT" else ("qc" if ai == "QC" else "ht")})

        thuc = [t for t in tin if not t["nhieu"]]
        if len(thuc) < 2:
            meta["loai_vi"] = "dưới 2 tin thật"

        anh_kh = [j for j, t in enumerate(tin) if t["anh"] and not t["nv"]]
        vt_moi_anh = next((j for j, t in enumerate(tin)
                           if t["nv"] and re.search(r'(gửi|xin|chụp).{0,12}(ảnh|hình)', t["text"], re.I)), None)

        ket.append({
            "ma": ht_id, "kh": kh_id, "nv": "", "co_sdt": meta["sdt"] == "co",
            "tin": thuc,
            "tin_tat": tin,
            "moc_bat_dau": tin[0]["tem"] if tin else None,
            "kh_gui_anh": vt_moi_anh is not None and any(j > vt_moi_anh for j in anh_kh),
            "kh_text": " ".join(t["text"] for t in thuc if not t["nv"]),
            "nv_text": " ".join(t["text"] for t in thuc if t["nv"]),
            "dich_vu_knb": dv.split(" ⚑")[0].split(" ⛔")[0].split(" 🌏")[0].strip(),
            "sla_dau": sla_dau,
            "so": int(so),
            **meta,
        })
    return ket

# ───────────────────────────── chạy phân loại ────────────────────────────

def main():
    ap = argparse.ArgumentParser(description="đọc bản xuất KNB → out/doc-hoi-thoai.json")
    ap.add_argument("file")
    ap.add_argument("--ky", required=True)
    ap.add_argument("--ra", default=RA_MD, help="thư mục ghi (mặc định out/)")
    a = ap.parse_args()

    I = nap_id_py()
    td = I.nap_tu_dien()
    pho, vi_sao = I.nap_phac_hoa(a.ky)
    hts = doc_knb(a.file, I)
    print("Đọc được %d hội thoại." % len(hts))
    print("  khách mới %d · khách cũ %d"
          % (sum(1 for h in hts if h["khach"] == "moi"),
             sum(1 for h in hts if h["khach"] == "cu")))

    # ★ Mẫu phân tích = KHÁCH MỚI (luật của bản xuất: mọi tỷ lệ tính trên khách mới).
    mau = [h for h in hts if h["khach"] == "moi" and len(h["tin"]) >= 2]
    ma_mau = {h["ma"] for h in mau}
    loai = [h for h in hts if h["ma"] not in ma_mau]
    print("  mẫu phân tích %d · loại %d" % (len(mau), len(loai)))

    # Mốc chốt dữ liệu của kỳ = tem muộn nhất trong file. Hệ số thời gian của
    # KF-60 đo tới mốc này — ⛔ không dùng "bây giờ", vì chạy lại báo cáo cũ
    # sau một tháng thì mọi lead đều nguội giả.
    moc_chot = max([t["tem"] for h in hts for t in h["tin"] if t.get("tem")], default=None)

    ban_ghi = []
    for ht in mau:
        cd = I.gan_chan_dung(ht, pho)            # None khi chưa qua CỔNG 0
        nac = I.gan_nac(ht, td)
        ma_o = I.gan_ma_o(ht, td)
        nhiet, tin_hieu = I.gan_nhiet(ht, td)
        k, diem, co_do = I.cham_hoi_thoai(ht, td, ma_o)

        # ① N1.1 theo cờ ⏱ của bản xuất, rồi tính lại điểm nhân viên cho khớp.
        k["N1.1"] = {"dat": "✓", "truot": "✗", "ngoai_gio": "—", None: "—"}[ht["sla_dau"]]
        tu = sum(I.DIEM[m] for m, v in k.items() if v == "✓")
        ms = sum(I.DIEM[m] for m, v in k.items() if v in ("✓", "✗"))
        diem = round(tu / ms * 100, 1) if ms else None
        if co_do and diem is not None:
            diem = min(diem, 49.0)               # id-F §4: có cờ đỏ → trần 49

        ht["chot_lich"] = bool(
            (I.co_tu(ht["nv_text"], td["nv_moi_lich"])
             and I.co_tu(ht["kh_text"], ["vâng", "ok", "được", "em qua", "có"]))
            or I.co_tu(ht["nv_text"], ["đặt lịch thành công", "xác nhận chị đã đặt lịch",
                                       "mã khám"]))
        roi = I.gan_vi_sao_roi(ht, td, diem)
        rc = I.gan_rao_can(ht, td, ma_o)
        hs = I.he_so_gia_tri(ht, td)

        # Cờ đỏ phải chỉ đúng người đã nói câu đó — id-F §5 đòi tên người xử lý.
        for c in co_do:
            c["nguoi"] = next((t["ten"] for t in ht["tin"]
                               if t["nv"] and I.co_tu(t["text"], [c["trich"]])), "(không rõ)")

        # ⛔ Một hội thoại có TỪ HAI nhân viên trở lên thì ⛔ không gán được cho
        #    ai: điểm của cả hội thoại không phải việc của một người. Gán cho
        #    người nói nhiều nhất là tạo ra một con số sai GẮN VỚI TÊN NGƯỜI —
        #    đúng thứ id-F §7 rào ② cấm. Những HT đó vào rổ «(nhiều người)» và
        #    bị loại khỏi phần xếp loại cá nhân, vẫn tính vào chỉ số cả đội.
        nv_dem = Counter(t["ten"] for t in ht["tin"] if t["nv"] and t["ten"])
        nv_ten = (list(nv_dem)[0] if len(nv_dem) == 1
                  else ("(nhiều người)" if nv_dem else "(không rõ)"))
        ban_ghi.append({
            "ma": ht["ma"], "nv": nv_ten,
            "cd": cd, "nac": nac, "ma_o": ma_o, "nhiet": nhiet, "tin_hieu": tin_hieu,
            "co_sdt": ht["co_sdt"], "chot_lich": ht["chot_lich"], "roi": roi,
            "rao_can": rc, "dich_vu": ht["dich_vu_knb"], "he_so": hs,
            "diem": diem, "cham": k, "co_do": co_do,
            "so_luot_kh": sum(1 for t in ht["tin"] if not t["nv"]),
            "so_nv": len(nv_dem), "cum": ht["cum"], "nhom_qc": ht["nhom_qc"],
            "page": ht["page"], "bo_sot": ht["bo_sot"], "chi_bot": ht["chi_bot"],
            "gan_theo_qc": ht["gan_theo_qc"],
            "lead": I.cham_lead(ht, td, ma_o, rc, roi, k, nhiet, hs, moc_chot),
        })

    os.makedirs(a.ra, exist_ok=True)
    I.RA = a.ra                       # ghi_csv/gom_doc ghi vào đúng thư mục này
    I.ghi_csv(ban_ghi)
    ket = I.gom_doc(ban_ghi, a.ky, os.path.basename(a.file), pho, vi_sao)
    ket["so_ht_nguon"] = len(hts)
    ket["so_loai"] = len(loai)
    with open(os.path.join(a.ra, "doc-hoi-thoai.json"), "w", encoding="utf-8") as f:
        json.dump(ket, f, ensure_ascii=False, indent=1)

    nl = I.nguyen_lieu_chan_dung(ban_ghi, mau, td, a.ky, os.path.basename(a.file))
    nl["cum_dv"] = dict(Counter(r["cum"] for r in ban_ghi).most_common())
    nl["nhom_qc"] = dict(Counter(r["nhom_qc"] for r in ban_ghi).most_common())
    with open(os.path.join(a.ra, "nguyen-lieu-chan-dung.json"), "w", encoding="utf-8") as f:
        json.dump(nl, f, ensure_ascii=False, indent=1)

    with open(os.path.join(a.ra, "ban-ghi.json"), "w", encoding="utf-8") as f:
        json.dump({"ky": a.ky, "nguon": os.path.basename(a.file),
                   "so_ht_nguon": len(hts), "so_ht": len(ban_ghi),
                   "so_loai": len(loai), "ban_ghi": ban_ghi},
                  f, ensure_ascii=False, indent=1)

    L = ket["lead"]
    print("\nĐã ghi %s/doc-hoi-thoai.json · ban-ghi.json · nguyen-lieu-chan-dung.json"
          % os.path.basename(a.ra))
    print("  nhiệt id-D   :", ket["nhiet"])
    print("  nhóm gọi     :", " · ".join("%s %d" % (x["ma"], x["so"])
                                        for x in L["nhom_goi"]))
    bb = L["bat_bien"]
    print("  bất biến     :", "✓ đạt" if bb["dat"] else
          "⛔ GOI_NGAY thiếu SĐT %d · id-D HOT rơi KHONG %d"
          % (bb["goi_ngay_thieu_sdt"], bb["id_d_hot_roi_khong"]))
    print("  hàng chờ gọi : %d dòng" % len(L["hang_cho"]))
    print("  vì sao rơi   :", ket["nguyen_nhan_roi"])
    print("\n  Bước tiếp: python tools/id.py bao-cao --ky \"%s\"" % a.ky)


if __name__ == "__main__":
    if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    main()
