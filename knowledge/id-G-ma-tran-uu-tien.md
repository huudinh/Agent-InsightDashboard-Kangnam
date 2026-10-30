# id-G · ★ MA TRẬN ƯU TIÊN — CHỌN VIỆC CHO KỲ TỚI

> Đây là **CỔNG 1**. Agent dừng ở đây, in ma trận ra, chờ người dùng gõ `DUYỆT`.
> ⛔ Chưa duyệt thì ⛔ không viết hook, ⛔ không sinh sổ tay.

---

## 1. VÌ SAO PHẢI CÓ MA TRẬN

Một kỳ đọc 300 hội thoại sẽ đẻ ra 40–60 việc đáng làm. Khối chỉ làm được 8–15 việc. Không có ma trận thì việc được chọn theo **ai nói to nhất**, chứ không theo **đâu mất nhiều lead nhất**.

> Ma trận trả lời đúng một câu: **nếu chỉ làm được 5 việc trong kỳ tới thì làm 5 việc nào.**

---

## 2. BA KHỐI — ĐI THEO ĐÚNG THỨ TỰ

| # | Khối | Mục tiêu | Tập lead xét |
|---|---|---|---|
| ① | **TĂNG HOT** | Kéo WARM sát HOT lên HOT | HT `WARM` đạt **3/5 tín hiệu** — thường thiếu ② mốc thời gian hoặc ⑤ khung giờ gọi |
| ② | **GIẢM COLD** | Làm khách nói được tình trạng ngay từ quảng cáo | HT `COLD` của `CD0` + HT tin đầu chỉ hỏi giá/địa chỉ |
| ③ | **TỐI ƯU WARM** | Gỡ rào cản làm WARM đứng lại | HT `WARM` đạt 2/5, có mã `O` rõ |

★ **Thứ tự này không đảo được.** Khối ① rẻ nhất (lead đã gần chín), khối ② đông nhất nhưng chậm, khối ③ là phần còn lại. Làm ② trước ① là bỏ tiền kéo người lạ trong khi người sắp mua đang đứng ngay đó.

---

## 3. CÔNG THỨC ĐIỂM

```
Điểm một ô = Σ ( lead bỏ lỡ trong ô × hệ số giá trị đơn )
```

### Hệ số giá trị đơn — theo dịch vụ chính khách hỏi

| Bậc | Giá trị đơn ước tính | Hệ số |
|---|---|---|
| Thấp | < 5 triệu | **1** |
| Trung | 5 – 15 triệu | **2** |
| Cao | ≥ 15 triệu | **3** |
| ⚠ Chưa có giá hoặc khách không nêu dịch vụ | | **1** ⚠ |

⚠️ Giá trị đơn **ước từ bảng giá chuẩn**, không phải doanh thu thật. Mọi ô dùng hệ số đều gắn `⚠`. Khi hệ thống cấp bảng giá hiện hành (`id-K` §3), thay số thật vào và ghi lại ở `doc/CHANGELOG.md`.

### Ví dụ đọc một dòng

```
CD3 · Sửa lại · khối ① Tăng HOT
  HT mới trong kỳ        : 42
  HT trong tập (WARM 3/5): 11
  Có SĐT                 : 6
  Hệ số giá trị đơn      : 3  (sửa mũi ≥15tr)
  Điểm                   : 11 × 3 = 33
  Dừng ở                 : A3 (7 HT) · A2 (4 HT)
  → Ưu tiên 1 của khối ①, làm nội dung nấc A3
```

---

## 4. BA NHÓM KẾT LUẬN

| Nhóm | Khi nào | Việc |
|---|---|---|
| ✅ **ĐƯỢC CHỌN** | Điểm cao nhất trong khối, ≥ 5 HT mới | Vào kế hoạch nội dung, có số thứ tự ưu tiên |
| 🔧 **SỬA VẬN HÀNH TRƯỚC** | ≥ 50% HT của ô rơi do **trực page** | ⛔ **Không làm nội dung.** Nội dung không gỡ được lỗi người trả lời. Đẩy sang `id-F` / `id-I` |
| 👁 **QUAN SÁT** | < 5 HT mới | Ghi tên, chờ kỳ sau |

⚠️ Nhóm 🔧 là nhóm quan trọng nhất mà các agent nội dung hay bỏ qua: **ô có nhiều lead nhưng lead rơi do câu trả lời của người, không phải do thiếu clip**. Làm clip cho ô này là ném tiền.

---

## 5. SỐ VIỆC TỐI ĐA MỖI KỲ

| Khối | Số ô được chọn |
|---|---|
| ① Tăng HOT | tối đa **3** |
| ② Giảm COLD | tối đa **3** |
| ③ Tối ưu WARM | tối đa **2** |
| 🔧 Sửa vận hành | không giới hạn — nhưng **mỗi việc phải có một người tên thật** |

⛔ Quá 8 ô nội dung một kỳ thì không ô nào được làm tử tế. Thà làm 5 ô xong hẳn.

---

## 6. KHUÔN IN RA Ở CỔNG 1

```
MA TRẬN ƯU TIÊN — KỲ <tu> → <den>          TRẠNG THÁI: ⏳ CHỜ DUYỆT

① TĂNG HOT        mục tiêu: kéo WARM 3/5 lên HOT    tập: <n> HT
┌────┬─────┬──────────────┬─────┬──────┬──────┬───────┬──────┬─────┬─────────────────┐
│ #  │ CD  │ Chân dung    │ HT  │ Tập  │ SĐT  │ Hệ số │ Điểm │ Nấc │ Hướng nội dung  │
└────┴─────┴──────────────┴─────┴──────┴──────┴───────┴──────┴─────┴─────────────────┘

② GIẢM COLD       …
③ TỐI ƯU WARM     …

🔧 SỬA VẬN HÀNH TRƯỚC — chưa làm nội dung
┌─────┬──────────────┬─────┬──────────────┬────────────────────────────┐
│ CD  │ Chân dung    │ HT  │ Rơi do trực  │ Lý do                      │
└─────┴──────────────┴─────┴──────────────┴────────────────────────────┘

👁 QUAN SÁT — dưới 5 HT mới: CD2 (3) · CD5 (2)

───────────────────────────────────────────────────────────────────────
Gõ DUYỆT để agent viết ngân hàng hook và sinh sổ tay.
Gõ SỬA <mã ô> <hướng mới> để đổi trước khi duyệt.
```

---

## 7. SAU KHI DUYỆT

Agent ghi vào dữ liệu kỳ:

```json
"ma_tran": {
  "trang_thai": "da_duyet",
  "duyet_boi": "<ai>",
  "duyet_luc": "<ngày>"
}
```

⛔ Chừng nào `trang_thai` còn là `cho_duyet`, tab **Ngân hàng hook** và tab **Sổ tay** của dashboard hiển thị *"chưa viết — ma trận chưa được duyệt"*, ⛔ không hiện nội dung rỗng.

---

## 8. TỰ KIỂM SỔ NÀY

- [ ] Ba khối có đi **đúng thứ tự** ① → ② → ③ không?
- [ ] Mỗi ô được chọn có ghi rõ **điểm** và **cách ra điểm** không?
- [ ] Hệ số giá trị đơn có gắn `⚠` không?
- [ ] Ô nào ≥50% rơi do trực page có bị đẩy nhầm sang làm nội dung không?
- [ ] Tổng số ô nội dung được chọn có vượt 8 không?
- [ ] Có dừng chờ duyệt thật không, hay đã tự chạy tiếp?
