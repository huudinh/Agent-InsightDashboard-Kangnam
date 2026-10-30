#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dem-ngan.py · canh giới hạn 8.000 ký tự của ô Instructions trong ChatGPT Custom GPT.

    python tools/dem-ngan.py
"""
import os
import sys

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRAN = 8000


def main():
    for ten, tran in (("SYSTEM-PROMPT-NGAN.md", TRAN), ("SYSTEM-PROMPT.md", None)):
        p = os.path.join(GOC, ten)
        if not os.path.exists(p):
            print("  ⛔ thiếu %s" % ten)
            continue
        with open(p, encoding="utf-8") as f:
            n = len(f.read())
        if tran is None:
            print("  %-24s %7s ký tự" % (ten, format(n, ",")))
        elif n <= tran:
            print("  %-24s %7s ký tự  ✅ còn dư %s" % (ten, format(n, ","), format(tran - n, ",")))
        else:
            print("  %-24s %7s ký tự  ⛔ VƯỢT %s — phải cắt" % (ten, format(n, ","), format(n - tran, ",")))
            sys.exit(1)


if __name__ == "__main__":
    # Console Windows mặc định cp1252 — không in nổi ★ ⛔ ✅. Chuyển sang UTF-8.
    if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    main()
