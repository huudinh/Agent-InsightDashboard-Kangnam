#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
so_tay.py · Agent-InsightDashboard-Kangnam

Sinh SỔ TAY THỰC THI theo khuôn id-I:
  ST-CN · một bản cho mỗi nhân viên trực page   (1 trang)
  ST-TN · một bản cho trưởng nhóm               (cả nhóm)
  ST-ND · một bản cho người làm nội dung        (⛔ không có tên nhân viên)

Script điền phần ĐẾM ĐƯỢC và chừa chỗ `«agent điền: …»` cho phần ĐỌC HIỂU
— câu mẫu, insight, câu hỏi ngầm. ⛔ Script không nghĩ hộ.

    python tools/so_tay.py --ky 19-25/10
"""

import argparse
import csv
import json
import os
import re
import sys
from collections import Counter, defaultdict

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RA = os.path.join(GOC, "out")
THU_MUC = os.path.join(RA, "so-tay")

TEN_NHOM = {"N1": "Phản hồi & SLA", "N2": "Khai thác tình trạng",
            "N3": "Trả lời đúng & minh bạch", "N4": "Xử lý rào cản",
            "N5": "Xin số & chốt", "N6": "Ngôn từ & thái độ"}

# Việc mẫu theo nhóm yếu nhất — viết như HÀNH ĐỘNG, không phải phẩm chất (id-I §6).
VIEC = {
    "N1": ("Nhắn lại một câu hỏi về tình trạng khi khách im quá 30 phút",
           ["Chị ơi, mũi mình hiện đang thấp sống hay to cánh ạ? Chị tả giúp em một câu thôi.",
            "Em vẫn ở đây ạ. Chị gửi em tấm ảnh nghiêng, em nhờ bác sĩ xem giúp chị nhé."],
           ("Kangnam chào chị ạ", "khách đã được chào rồi — câu này không mở được gì")),
    "N2": ("Hỏi MỘT câu về tình trạng trước khi gõ câu xin số",
           ["Trước đây mình đã can thiệp vùng mũi lần nào chưa ạ?",
            "Chị đang muốn cải thiện phần sống mũi hay phần đầu – cánh mũi ạ?"],
           ("Chị cho em xin số điện thoại", "gõ ngay khi chưa biết khách cần gì")),
    "N3": ("Nêu khung giá ngay khi khách hỏi giá, hoặc nói rõ vì sao chưa nêu được",
           ["Dịch vụ này đang ở khoảng «…», tuỳ tình trạng cụ thể của chị ạ.",
            "Mức giá phụ thuộc vào tình trạng nên em xin chị một tấm ảnh để báo đúng, tránh báo hớ ạ."],
           ("Dạ về chi phí trợ lý bác sĩ mới nắm rõ ạ", "né hẳn câu hỏi, khách dừng ngay")),
    "N4": ("Trả lời đúng tầng khách đang lo, không đổi sang tầng khác",
           ["Chị đang lo chi phí phát sinh đúng không ạ — gói này gồm «…», ngoài ra không phát sinh.",
            "Chị sợ sửa lần hai càng hỏng — với ca đã nâng rồi, bác sĩ sẽ xem cấu trúc cũ trước khi quyết."],
           ("Bên em là bệnh viện uy tín hàng đầu ạ", "khách lo GIÁ mà trả lời bằng CHẤT LƯỢNG — lệch tầng")),
    "N5": ("Hỏi khung giờ nghe máy ngay sau khi khách cho số",
           ["Chị tiện nghe máy khung giờ nào ạ, em để bác sĩ gọi đúng giờ đó.",
            "Chiều mai 15h em giữ chỗ cho chị nhé, chị xác nhận giúp em một câu ạ."],
           ("Khi nào rảnh chị qua nhé", "không có ngày giờ thì không phải một lời mời lịch")),
    "N6": ("Cắt đoạn dán dài, trả lời đúng điều khách vừa hỏi trước",
           ["Dạ câu này em trả lời ngay: «…». Chi tiết còn lại em gửi chị sau ạ."],
           ("<khối giới thiệu công nghệ 500 chữ>", "khách chỉ hỏi một câu, đoạn dán không trả lời câu đó")),
}

CHUNG_KHONG = [
    "⛔ Không nêu con số bảo hành — nói «chính sách bảo hành bằng văn bản»",
    "⛔ Không trả lời câu bệnh nền — chuyển «trường hợp này cần bác sĩ khám trực tiếp đánh giá»",
    "⛔ Không cam kết kết quả chắc chắn",
]
GHI_CHU_DIEM = ("> Điểm dùng để phân việc kèm cặp. "
                "Không phải căn cứ kỷ luật hay xếp hạng công khai.")

SO_VIEC = {"A": 1, "B": 1, "C": 2, "D": 1}


def ten_file(s):
    s = re.sub(r'[^\w\s-]', '', s, flags=re.U).strip()
    return re.sub(r'\s+', '-', s) or "khong-ro"


def nap():
    f = os.path.join(RA, "doc-hoi-thoai.json")
    if not os.path.exists(f):
        sys.exit("⛔ Chưa có out/doc-hoi-thoai.json. Chạy `id.py doc` trước.")
    with open(f, encoding="utf-8") as fh:
        D = json.load(fh)
    rows = []
    c = os.path.join(RA, "cham-hoi-thoai.csv")
    if os.path.exists(c):
        with open(c, encoding="utf-8-sig") as fh:
            rows = list(csv.DictReader(fh))
    return D, rows


def pct(a, b):
    return round(a / b * 100, 1) if b else None


def so_cn(nv, D, rows, ky):
    rs = [r for r in rows if r["nv"] == nv["ten"]]
    n = len(rs)
    loai = nv["loai"]
    yeu, manh = nv["yeu_nhat"], nv["manh_nhat"]
    # Việc được chọn theo nhóm MẤT NHIỀU ĐIỂM NHẤT, không phải nhóm dễ sửa nhất (id-I §2).
    cot = {g: [c for c in rs[0].keys() if c.startswith(g + ".")] for g in TEN_NHOM} if rs else {}
    xep = sorted([g for g in TEN_NHOM if _pct_nhom(rs, g, cot.get(g, [])) is not None],
                 key=lambda g: _pct_nhom(rs, g, cot.get(g, [])))
    chon = xep[:SO_VIEC.get(loai, 1)] or [yeu]
    cot_yeu = cot.get(yeu, [])

    cd_chinh = Counter(r["cd"] for r in rs).most_common(1)
    o_chinh = Counter(o for r in rs for o in (r["ma_o"] or "").split()
                      if o.startswith("O-")).most_common(1)

    pct_yeu = _pct_nhom(rs, yeu, cot_yeu)
    khoi_yeu = next((g["pct_dat"] for g in D["nhan_vien"]["nhom"] if g["ma"] == yeu), None)
    cot_manh = [c for c in rs[0].keys() if c.startswith(manh + ".")] if rs else []

    L = []
    a = L.append
    a("# SỔ TAY THỰC THI · %s" % nv["ten"])
    a("Kỳ %s · %d hội thoại · %s/100 · loại **%s**"
      % (ky, n, nv["diem"] if nv["diem"] is not None else "—", loai))
    a("")
    a(GHI_CHU_DIEM)
    a("")
    a("## 1 · KỲ NÀY BẠN LÀM TỐT NHẤT ĐIỀU GÌ")
    a("**%s · %s** — %s%% đạt  *(cả khối: %s%%)*"
      % (manh, TEN_NHOM.get(manh, ""), _pct_nhom(rs, manh, cot_manh),
         next((g["pct_dat"] for g in D["nhan_vien"]["nhom"] if g["ma"] == manh), "—")))
    a("")
    a("«agent điền: một câu nguyên văn của chính người này làm tốt, kèm HT-nnn»")
    a("")
    a("## 2 · ★ %s VIỆC CỦA KỲ TỚI" % ({1: "MỘT", 2: "HAI"}.get(len(chon), str(len(chon)))))
    for i, g in enumerate(chon):
        viec, cau_dung, (cau_sai, ly_do) = VIEC.get(g, VIEC["N2"])
        p_g = _pct_nhom(rs, g, cot.get(g, []))
        khoi_g = next((x["pct_dat"] for x in D["nhan_vien"]["nhom"] if x["ma"] == g), None)
        a("")
        a("### %s. %s" % (i + 1, viec))
        a("")
        a("Vì sao: nhóm **%s · %s** đạt **%s%%** trên %d hội thoại áp dụng  *(cả khối %s%%)*."
          % (g, TEN_NHOM.get(g, ""), p_g, n, khoi_g))
        a("")
        bc = [r for r in rs if any(r.get(c) == "✗" for c in cot.get(g, []))][:2]
        if bc:
            a("Bằng chứng — hội thoại của chính bạn:")
            for r in bc:
                tr = [c for c in cot.get(g, []) if r.get(c) == "✗"]
                a("- `%s` · trượt %s · khách thuộc %s · %s"
                  % (r["ma"], ", ".join(tr), r["cd"], r["vi_sao_roi"]))
            a("")
        a("Làm thế nào — câu dùng được ngay:")
        for c in cau_dung:
            a("- ✅ *%s*" % c)
        a("- ⛔ *%s* — %s" % (cau_sai, ly_do))
        a("")
        a("Đo thế nào ở kỳ sau: **%s** từ %s%% lên **%s%%**"
          % (g, p_g, min(100, round((p_g or 0) + 15))))
    a("")
    a("## 3 · KHÁCH CỦA BẠN LÀ AI")
    if cd_chinh:
        a("Chân dung gặp nhiều nhất: **%s** — %d/%d hội thoại"
          % (cd_chinh[0][0], cd_chinh[0][1], n))
    if o_chinh:
        a("Họ đang sợ: **%s** — %d lần" % (o_chinh[0][0], o_chinh[0][1]))
    a("")
    a("Câu hỏi ngầm: «agent điền: dịch câu khách gõ thành điều khách thật sự muốn biết»")
    a("")
    a("Ba câu trả lời sẵn cho tệp này:")
    a("1. «agent điền»")
    a("2. «agent điền»")
    a("3. «agent điền»")
    a("")
    a("## 4 · ⛔ BA ĐIỀU TUYỆT ĐỐI KHÔNG")
    for x in CHUNG_KHONG:
        a("- %s" % x)
    if nv.get("co_do"):
        a("")
        a("🔴 **Kỳ này bạn có cờ đỏ:** %s" % " · ".join(nv["co_do"]))
        for c in D["nhan_vien"]["co_do"]:
            if c["nguoi"] == nv["ten"]:
                a("- `%s` · %s · trích: «%s»" % (c["ht"], c["ma"], c["trich"]))
        a("")
        a("⚠️ Cờ đỏ phải ngồi lại với trưởng nhóm trong 48 giờ.")
    a("")
    a("## 5 · KIỂM TRƯỚC KHI ĐÓNG MỖI HỘI THOẠI")
    a("- [ ] Đã hỏi tình trạng **trước khi** xin số chưa?")
    a("- [ ] Đã nêu được khung giá, hoặc nói rõ vì sao chưa nêu được chưa?")
    a("- [ ] Đã hỏi khung giờ nghe máy chưa?")
    a("- [ ] Đã mời lịch có **ngày + giờ** cụ thể chưa?")
    for g in chon:
        a("- [ ] %s" % VIEC.get(g, VIEC["N2"])[0])
    a("")
    return "\n".join(L)


def _pct_nhom(rs, ma, cot):
    dat = sum(1 for r in rs for c in cot if r.get(c) == "✓")
    chua = sum(1 for r in rs for c in cot if r.get(c) == "✗")
    return pct(dat, dat + chua)


def so_tn(D, rows, ky):
    V = D["nhan_vien"]
    pb = V["phan_bo"]
    nhom_xep = sorted([g for g in V["nhom"] if g["pct_dat"] is not None],
                      key=lambda g: g["pct_dat"])
    A = [c for c in V["ca_nhan"] if c["loai"] == "A"]
    D_ = [c for c in V["ca_nhan"] if c["loai"] == "D"]

    L = ["# SỔ TAY TRƯỞNG NHÓM · trực page", "Kỳ %s" % ky, "", GHI_CHU_DIEM, "",
         "## 1 · PHÂN BỐ NHÓM",
         " · ".join("%s: %d" % (k, v) for k, v in sorted(pb.items())), "",
         "## 2 · BA TIÊU CHÍ YẾU NHẤT CỦA KHỐI",
         "*Đây là nội dung buổi đào tạo 15 phút kỳ tới.*", ""]
    for g in nhom_xep[:3]:
        tc = sorted([c for c in g["tieu_chi"] if c["pct_dat"] is not None],
                    key=lambda c: c["pct_dat"])[:1]
        for c in tc:
            L.append("- **%s · %s** — %s%% đạt, %d HT không áp dụng"
                     % (c["ma"], c["ten"], c["pct_dat"], c["khong_ap_dung"]))
    L += ["", "## 3 · AI KÈM AI"]
    if A and D_:
        for i, d in enumerate(D_):
            a = A[i % len(A)]
            L.append("- **%s** kèm **%s** — về nhóm %s" % (a["ten"], d["ten"], d["yeu_nhat"]))
    else:
        L.append("- ⚠ Kỳ này không có người loại A để kèm. Trưởng nhóm kèm trực tiếp %d người loại D."
                 % len(D_))
    L += ["", "## 4 · CỜ ĐỎ CẦN XỬ TRONG 48 GIỜ"]
    if V["co_do"]:
        for c in V["co_do"]:
            L.append("- `%s` · **%s** · %s · trích: «%s» → *«agent điền: xử thế nào»*"
                     % (c["ma"], c["nguoi"], c["ht"], c["trich"]))
    else:
        L.append("- Không có cờ đỏ trong kỳ.")
    L += ["", "## 5 · VIỆC KHÔNG PHẢI CỦA NHÓM BẠN",
          "*Các ô chấm «—» do lỗi hệ thống — đã đẩy lên mục việc hệ thống của dashboard, "
          "⛔ không trừ điểm nhân viên.*", ""]
    for g in V["nhom"]:
        for c in g["tieu_chi"]:
            if c["khong_ap_dung"] >= max(3, len(rows) // 10):
                L.append("- `%s · %s` — %d HT không áp dụng" % (c["ma"], c["ten"], c["khong_ap_dung"]))
    L += ["", "## 6 · BẢNG ĐIỂM CẢ NHÓM", "",
          "| Nhân viên | HT | Điểm | Loại | Nhóm yếu nhất | Nhóm mạnh nhất |",
          "|---|---:|---:|---|---|---|"]
    for c in V["ca_nhan"]:
        L.append("| %s | %d | %s | %s | %s | %s |"
                 % (c["ten"], c["ht"], c["diem"] if c["diem"] is not None else "—",
                    c["loai"], c["yeu_nhat"], c["manh_nhat"]))
    L += ["", "⛔ Bảng này ⛔ không phát ra ngoài nhóm, ⛔ không dán lên màn hình chung "
              "(rào an toàn ④ của `id-F §7`).", ""]
    return "\n".join(L)


def so_nd(D, ky):
    M = D.get("ma_tran") or {}
    L = ["# SỔ TAY NỘI DUNG · kỳ %s" % ky, "",
         "⛔ Sổ này ⛔ không chứa tên nhân viên trực page nào.", "",
         "## 1 · Ô ĐƯỢC CHỌN"]
    if M.get("trang_thai") != "da_duyet":
        L.append("⏳ **Ma trận chưa được duyệt** — chưa chốt ô nào. Xem `id-G`.")
    else:
        L.append("«agent điền: bảng ô được chọn theo khuôn id-G §6»")
    L += ["", "## 2 · NGÂN HÀNG HOOK KỲ NÀY",
          "«agent điền: bảng hook theo khuôn id-H §4 — mỗi hook phải có cột TRUY NGƯỢC»", "",
          "## 3 · NỘI DUNG PHẢI DỪNG",
          "«agent điền: nội dung 🔴 KÉM + mã O thấp → bỏ hẳn»", "",
          "## 4 · Ô ĐANG PHÍ",
          "«agent điền: ô ③ của ma trận CD×5A — nhiều nội dung, ít người hỏi»", "",
          "## 5 · ⛔ CỜ PHÁP CHẾ TRƯỚC KHI SẢN XUẤT",
          "- ⛔ Con số bảo hành — chưa có văn bản (`id-K §3①`)",
          "- ⛔ Giá dịch vụ ngoài mắt — chưa có bảng giá hiện hành (`id-K §3②`)",
          "- ⛔ Chức danh / số năm / số ca của bác sĩ chưa đối chiếu chứng chỉ (`id-K §3③`)",
          "- ⛔ Ảnh / video khách chưa có consent đúng mục đích quảng cáo", ""]
    return "\n".join(L)


def main():
    p = argparse.ArgumentParser(description="Sinh sổ tay thực thi theo khuôn id-I")
    p.add_argument("--ky", required=True)
    p.add_argument("--chi", help="chỉ sinh cho một nhân viên")
    args = p.parse_args()

    D, rows = nap()
    os.makedirs(THU_MUC, exist_ok=True)
    V = D["nhan_vien"]

    da = 0
    for nv in V["ca_nhan"]:
        if args.chi and nv["ten"] != args.chi:
            continue
        if nv["loai"] == "chưa đủ mẫu":
            continue
        fp = os.path.join(THU_MUC, "ST-CN_%s.md" % ten_file(nv["ten"]))
        with open(fp, "w", encoding="utf-8") as f:
            f.write(so_cn(nv, D, rows, args.ky))
        da += 1

    with open(os.path.join(THU_MUC, "ST-TN_truong-nhom.md"), "w", encoding="utf-8") as f:
        f.write(so_tn(D, rows, args.ky))
    with open(os.path.join(THU_MUC, "ST-ND_noi-dung.md"), "w", encoding="utf-8") as f:
        f.write(so_nd(D, args.ky))

    chua = V["phan_bo"].get("chưa đủ mẫu", 0)
    print("")
    print("  Đã sinh %d sổ tay cá nhân + 1 sổ trưởng nhóm + 1 sổ nội dung" % da)
    print("  Thư mục: out/so-tay/")
    if chua:
        print("  ⚠ %d người chưa đủ 10 hội thoại — ⛔ không phân loại, ⛔ không sinh sổ (id-F §6)" % chua)
    print("  ⚠ Còn «agent điền: …» ở phần đọc hiểu — agent phải viết trước khi phát.")
    print("  ⛔ Phát riêng từng người. ⛔ Không gửi vào nhóm chat chung.")
    print("")


if __name__ == "__main__":
    if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    main()
