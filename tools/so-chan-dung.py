#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
so-chan-dung.py · sinh phần BẢNG của sổ id-M từ tools/chan_dung_kf62.json

    python tools/so-chan-dung.py
→ ghi đè khối giữa hai mốc trong knowledge/id-M-thu-vien-chan-dung-kf62.md

⛔ Vì sao phải sinh tự động: bài học của `id-L`. Thang điểm KF-60 nằm ở cả sổ
   lẫn code nên phải nhắc nhau sửa hai chỗ. Danh mục 85 chân dung thì ⛔ KHÔNG
   chép tay lần hai — sổ đọc thẳng từ file máy dùng, nên hai bên không thể lệch.

★ Phần VĂN của sổ (vì sao, ranh giới, cổng, rủi ro) viết tay, nằm NGOÀI hai mốc
  và ⛔ không bị lệnh này đụng tới.
"""
import io
import json
import os
import sys

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TV = os.path.join(GOC, "tools", "chan_dung_kf62.json")
SO = os.path.join(GOC, "knowledge", "id-M-thu-vien-chan-dung-kf62.md")
BAT = "<!-- BANG-TU-DONG:bat -->"
KET = "<!-- BANG-TU-DONG:ket -->"


def dong_dv(ma, dv):
    cds = [c for c in dv["chan_dung"] if not c["ma"].endswith("CHUA_XAC_DINH")]
    rieng = sum(1 for c in cds if c.get("hanh_dong"))
    return len(cds), rieng


def main():
    with open(TV, encoding="utf-8") as f:
        tv = json.load(f)
    dvs = tv["dich_vu"]
    r = ["> ⚙ Phần dưới đây **sinh tự động** từ `tools/chan_dung_kf62.json` bằng",
         "> `python tools/so-chan-dung.py`. ⛔ Đừng sửa tay — sửa file JSON rồi chạy lại.", ""]

    # ── bảng khối ────────────────────────────────────────────────────────
    khois = []
    for ma, dv in dvs.items():
        if dv["khoi"] not in khois:
            khois.append(dv["khoi"])
    r += ["### Năm khối · %d dịch vụ · %d chân dung" % (
        len(dvs), sum(dong_dv(m, d)[0] for m, d in dvs.items())), "",
        "| Khối | Dịch vụ | Chân dung | Đã khai kịch bản riêng |", "|---|---|---:|---:|"]
    for k in khois:
        ds = [(m, d) for m, d in dvs.items() if d["khoi"] == k]
        tong = sum(dong_dv(m, d)[0] for m, d in ds)
        rieng = sum(dong_dv(m, d)[1] for m, d in ds)
        r.append("| **%s** | %s | %d | %s |" % (
            k, " · ".join("`%s`" % m for m, _ in ds), tong,
            "**%d**" % rieng if rieng else "⚠ 0 — dùng lời mặc định"))
    r.append("")

    # ── thẻ ngữ cảnh ─────────────────────────────────────────────────────
    r += ["### 12 thẻ ngữ cảnh — dùng chung mọi dịch vụ, tối đa 3 thẻ một hội thoại", "",
          "| Mã | Thẻ | Cách xử lý |", "|---|---|---|"]
    for ma, t in tv["the_ngu_canh"].items():
        r.append("| `%s` | %s | %s |" % (ma, t["ten"], t["xu_ly"]))
    r.append("")

    # ── nối KF-60 ────────────────────────────────────────────────────────
    lk = tv.get("lien_ket_kf60") or {}
    if lk:
        r += ["### Nối với lead scoring (`id-L`)", "",
              "| Nhóm gọi KF-60 v1.1 | Tên cũ trong KF-62 | Ai làm | SLA |",
              "|---|---|---|---|"]
        for ma, q in lk["quy_doi"].items():
            r.append("| `%s` | %s | %s | %s |" % (ma, q["kf62_v1_0"], q["ai_lam"], q["sla"]))
        r += ["", "⚠ Chân dung chưa khai `hanh_dong` thì dùng `lien_ket_kf60.mac_dinh` — "
              "đủ để chạy, ⛔ nhưng không phải lời của KF-62 cho chân dung đó.", ""]

    # ── trạng thái lead ──────────────────────────────────────────────────
    r += ["### Ngoài chân dung", "", "| Mã | Nghĩa |", "|---|---|"]
    for ma, t in (tv.get("trang_thai_lead") or {}).items():
        r.append("| `%s` | %s |" % (ma, t["ten"]))
    r.append("| `KHONG_XAC_DINH_DV` | Đến DỊCH VỤ cũng chưa biết — mã dự trữ |")
    r.append("")

    # ── danh mục từng dịch vụ ────────────────────────────────────────────
    r += ["### Danh mục chân dung theo thứ tự kiểm tra", "",
          "> Câu **«Có» đầu tiên** quyết định. ⛔ Không chấm điểm, không lấy cái trúng",
          "> nhiều từ nhất — thứ tự là một phần của luật.", ""]
    for k in khois:
        r.append("#### Khối %s" % k)
        r.append("")
        for ma, dv in dvs.items():
            if dv["khoi"] != k:
                continue
            tong, rieng = dong_dv(ma, dv)
            r.append("**`%s` · %s** — %d chân dung%s" % (
                ma, dv["ten"], tong, "" if rieng == tong else
                " · ⚠ %d/%d đã khai kịch bản" % (rieng, tong)))
            r.append("")
            r.append("| # | Mã | Chân dung |")
            r.append("|---:|---|---|")
            for c in sorted(dv["chan_dung"], key=lambda x: x["thu_tu"]):
                if c["ma"].endswith("CHUA_XAC_DINH"):
                    r.append("| — | `%s` | *%s* |" % (c["ma"], c["ten"]))
                else:
                    r.append("| %d | `%s`%s | %s |" % (
                        c["thu_tu"], c["ma"], "" if c.get("hanh_dong") else " ⚠", c["ten"]))
            r.append("")
    r.append("⚠ = chưa khai kịch bản riêng theo nhóm gọi.")

    s = io.open(SO, encoding="utf-8").read()
    if s.count(BAT) != 1 or s.count(KET) != 1:
        sys.exit("⛔ %s thiếu mốc BANG-TU-DONG" % os.path.basename(SO))
    dau, cuoi = s.index(BAT) + len(BAT), s.index(KET)
    s = s[:dau] + "\n\n" + "\n".join(r) + "\n\n" + s[cuoi:]
    io.open(SO + ".tmp", "w", encoding="utf-8", newline="").write(s)
    os.replace(SO + ".tmp", SO)
    print("  Đã sinh bảng id-M: %d dịch vụ · %d chân dung · %d thẻ"
          % (len(dvs), sum(dong_dv(m, d)[0] for m, d in dvs.items()),
             len(tv["the_ngu_canh"])))


if __name__ == "__main__":
    if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    main()
