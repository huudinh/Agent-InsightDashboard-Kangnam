# prompt-cham-diem · chấm điểm & phân loại nhân viên trực page

> ⚠ Đọc `id-F` §1 và §7 trước khi dùng. Prompt này tạo ra con số gắn với tên một con người.

---

```
CHẤM ĐIỂM TRỰC PAGE

FILE HỘI THOẠI: <tên file>
KỲ: <tu> → <den>

Theo id-F, chấm hai tầng:

TẦNG 1 — từng hội thoại, 22 tiêu chí N1.1 … N6.3, mỗi tiêu chí ✓ / ✗ / —
   ✓ có bằng chứng trong hội thoại
   ✗ có bằng chứng là KHÔNG làm hoặc LÀM SAI — phải trích được nguyên văn
   — tình huống không phát sinh, HOẶC lỗi hệ thống
   Điểm = (tổng điểm ✓) ÷ (tổng điểm các tiêu chí không phải "—") × 100

TẦNG 2 — từng nhân viên
   Điểm = trung bình điểm các hội thoại của người đó
   Phân loại A ≥85 · B 70–84 · C 55–69 · D <55
   ⛔ Dưới 10 hội thoại: KHÔNG cho điểm tổng, KHÔNG phân loại. Ghi "chưa đủ mẫu".
   Một cờ đỏ → trần 49 điểm cho hội thoại đó, và người đó ⛔ không được xếp loại A.

IN RA SÁU KHỐI:
① PHÂN BỐ        A/B/C/D + số người chưa đủ mẫu
② CHỈ SỐ ĐỘI     % đạt từng nhóm N1…N6 và từng tiêu chí
③ BẢNG CÁ NHÂN   tên · số HT · điểm · loại · nhóm yếu nhất · nhóm mạnh nhất
                 ⛔ Khối này CHỈ vào sổ tay riêng và bản trưởng nhóm.
④ CỜ ĐỎ          mã · ai · HT-nnn · NGUYÊN VĂN câu nói · người xử lý đích danh
⑤ VIỆC HỆ THỐNG  các ô "—" do lỗi hệ, gom theo nguyên nhân
⑥ BA TIÊU CHÍ YẾU NHẤT CỦA KHỐI → nội dung đào tạo 15 phút kỳ sau

BỐN RÀO AN TOÀN — kiểm lại trước khi trả lời:
① Mọi ✗ có HT-nnn + nguyên văn chưa? Không có thì đổi thành "—".
② Có ô nào là LỖI HỆ mà bị chấm ✗ không? (thiếu bảng giá, page không có
   dịch vụ khách hỏi, ngoài giờ, công cụ lỗi) → phải là "—".
③ "—" có bị cộng vào mẫu số không?
④ Có bảng xếp hạng cá nhân nào nằm ngoài sổ tay riêng không?

Chân mọi bảng điểm phải có câu:
"Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay xếp hạng công khai."
```

---

## Chấm một người

```
CHẤM RIÊNG: <tên nhân viên>
Liệt kê từng hội thoại của người này: HT-nnn · chân dung · 22 ô ✓/✗/— ·
điểm · câu đáng chú ý (một câu làm tốt, một câu làm hỏng, nguyên văn).
```
