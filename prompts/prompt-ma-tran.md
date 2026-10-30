# prompt-ma-tran · dựng ma trận ưu tiên (CỔNG 1)

---

```
DỰNG MA TRẬN ƯU TIÊN

KỲ: <tu> → <den>

Theo id-G, dựng ba khối ĐÚNG THỨ TỰ:

① TĂNG HOT      tập: HT WARM đạt 3/5 tín hiệu (thường thiếu ② mốc thời gian ≤14 ngày
                hoặc ⑤ đồng ý khung giờ gọi)
② GIẢM COLD     tập: HT COLD của CD0 (ô dự trữ) + HT tin đầu chỉ hỏi giá / hỏi địa chỉ
③ TỐI ƯU WARM   tập: HT WARM đạt 2/5, có mã O rõ

Mỗi dòng một chân dung **đã duyệt ở CỔNG 0** (⛔ không tự thêm chân dung ở bước này), các cột:
  CD · tên · HT mới · HT trong tập · có SĐT · hệ số giá trị đơn · ĐIỂM · nấc ·
  hướng nội dung (một câu, cụ thể) · chọn hay không · số thứ tự ưu tiên

ĐIỂM = Σ (lead bỏ lỡ × hệ số giá trị đơn)
  hệ số: <5tr = 1 · 5–15tr = 2 · ≥15tr = 3 · chưa có giá = 1 ⚠
  Mọi ô dùng hệ số phải gắn ⚠ (ước từ bảng giá chuẩn, không phải doanh thu thật).

BA NHÓM KẾT LUẬN:
  ✅ ĐƯỢC CHỌN            điểm cao nhất trong khối, ≥5 HT mới
  🔧 SỬA VẬN HÀNH TRƯỚC   ≥50% HT của ô rơi do TRỰC PAGE
                          → ⛔ KHÔNG làm nội dung. Nội dung không gỡ được lỗi câu trả lời.
  👁 QUAN SÁT             <5 HT mới

SỐ Ô TỐI ĐA: khối ① 3 · khối ② 3 · khối ③ 2. ⛔ Quá 8 ô thì không ô nào làm tử tế.
Nhóm 🔧 không giới hạn, nhưng MỖI VIỆC PHẢI CÓ MỘT NGƯỜI TÊN THẬT.

In xong ghi:
TRẠNG THÁI: ⏳ CHỜ DUYỆT
và dừng. ⛔ Không viết hook. ⛔ Không sinh sổ tay.
```

---

## Sửa trước khi duyệt

```
SỬA <mã ô> <hướng mới>
```

## Duyệt

```
DUYỆT
```
Agent ghi `trang_thai: da_duyet` + ai duyệt + ngày duyệt, rồi chạy tiếp B6–B8.
