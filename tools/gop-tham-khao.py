#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gop-tham-khao.py · gộp 11 sổ tri thức thành một file để nạp lên nền tảng
chỉ cho phép ít file Knowledge.

    python tools/gop-tham-khao.py
→ goi/GOP-tri-thuc.md
"""
import os
import sys
from datetime import date

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NGUON = os.path.join(GOC, "knowledge")
DICH = os.path.join(GOC, "goi", "GOP-tri-thuc.md")


def main():
    files = sorted(f for f in os.listdir(NGUON) if f.endswith(".md"))
    if not files:
        sys.exit("⛔ knowledge/ rỗng.")
    os.makedirs(os.path.dirname(DICH), exist_ok=True)
    phan = ["# GÓI TRI THỨC · Agent-InsightDashboard-Kangnam",
            "",
            "> Bản gộp **sinh tự động** từ `knowledge/`. ⛔ Không sửa file này —",
            "> sửa file gốc rồi chạy lại `python tools/gop-tham-khao.py`.",
            "",
            "Gộp ngày %s · %d sổ" % (date.today().isoformat(), len(files)),
            "",
            "## Mục lục", ""]
    phan += ["- `%s`" % f for f in files]
    phan += ["", "---", ""]
    for f in files:
        with open(os.path.join(NGUON, f), encoding="utf-8") as fh:
            phan += ["<!-- ===== %s ===== -->" % f, "", fh.read().rstrip(), "", "---", ""]
    noi_dung = "\n".join(phan)
    with open(DICH, "w", encoding="utf-8") as fh:
        fh.write(noi_dung)
    print("  Đã gộp %d sổ → goi/GOP-tri-thuc.md (%s ký tự)" % (len(files), format(len(noi_dung), ",")))


if __name__ == "__main__":
    main()
