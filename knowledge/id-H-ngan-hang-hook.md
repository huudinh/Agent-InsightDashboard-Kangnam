# id-H · NGÂN HÀNG HOOK — 7 LOẠI HOOK × 16 FORMAT

> Chạy **sau CỔNG 1**. Mỗi hook phải gắn: **1 chân dung · 1 nấc 5A · 1 mã `O` · 1 `HT-nnn` truy ngược · 3 format**.
> ⛔ Hook không truy ngược được về một dòng hội thoại hoặc một con số là **hook bịa** — loại khỏi ngân hàng.

---

## 1. BẢY LOẠI HOOK

| Loại | Định nghĩa | Mục đích | Từ khoá nhận ra |
|---|---|---|---|
| **PHỦ ĐỊNH** | Bác bỏ một niềm tin phổ biến | Tò mò vì đi ngược số đông | *Đừng, Không nên, Dừng ngay, Chưa chắc* |
| **CON SỐ** | Lượng hoá vấn đề hoặc kết quả | Rõ ràng, cụ thể, dễ nhớ | *X ngày, X triệu, X điều, X%* |
| **GỌI TÊN NỖI SỢ** | Chỉ mặt đặt tên khuyết điểm, sự cố | Đánh trúng tự ti | *Bị [tình trạng], Sợ [sự cố], Hỏng, Lệch* |
| **NGHỊCH LÝ** | Hai thông tin tương phản trong một câu | Xung đột nhận thức | *Tuy… nhưng, Càng… lại càng* |
| **SO SÁNH A–B** | Đặt hai đối tượng lên bàn cân | Dễ cân đo, chọn lựa | *[A] hay [B], Khác gì nhau* |
| **TIẾT LỘ NỘI BỘ** | Bật mí sự thật, trải nghiệm thật | Củng cố niềm tin | *Bác sĩ hiếm khi nói, Sự thật đằng sau* |
| **CÂU HỎI THẦM** | Trăn trở khách đang phân vân | Cảm giác được tháo gỡ | *Có ai mỗi lần…? Liệu có…? Bao lâu…?* |

### Loại hook mạnh nhất theo nấc

| Nấc | Loại hook |
|---|---|
| `A1` | PHỦ ĐỊNH · NGHỊCH LÝ |
| `A2` | SO SÁNH A–B · CON SỐ |
| `A3` | GỌI TÊN NỖI SỢ · TIẾT LỘ NỘI BỘ |
| `A4` | CON SỐ · CÂU HỎI THẦM |
| `A5` | TIẾT LỘ NỘI BỘ · CON SỐ |

---

## 2. MƯỜI SÁU FORMAT `L01` – `L16`

> Thư viện chung — **giữ nguyên mã cho mọi dịch vụ** để so hiệu suất chéo tuyến. ⛔ Không có format "sáng tạo tự do".

| Mã | Tên | Thời lượng | Chỉ số đo chính |
|---|---|---|---|
| `L01` | Bác sĩ — Talk hỏi đáp | 25–35s | 3s-retention · share |
| `L02` | Bác sĩ — Talk chủ đề | 40–60s | Xem hết · bình luận chuyên môn |
| `L03` | Bác sĩ — Phân tích ca thật | 30–45s | Xem hết · lưu |
| `L04` | Khách hàng — Trước/sau | 10–15s | **CTR · tỷ lệ inbox** |
| `L05` | Khách hàng — Biến đổi theo mốc ngày | 15–25s | Bình luận / 1.000 view |
| `L06` | Khách hàng — Review | 0–45s | Lưu · share |
| `L07` | Khách hàng — Hành trình 1 ngày | 45–90s | **LƯU (cao nhất hệ)** |
| `L08` | Khách hàng — Kết quả | 20–35s | **Tỷ lệ inbox (cao nhất hệ)** |
| `L09` | Dịch vụ — Công nghệ | 15–30s | Share · 3s-retention |
| `L10` | Dịch vụ — Quy trình | 25–40s | Bình luận tích cực · lưu |
| `L11` | Dịch vụ — Giá / chính sách | 10–20s | Share · bình luận tích cực |
| `L12` | Local — Cơ sở / bác sĩ / công nghệ | 20–35s | **LƯU · giảm huỷ lịch** |
| `L13`–`L16` | ⚠ **Chưa có định nghĩa** | — | 🔴 `[CHỜ CẤP]` — Content Lead |

⚠️ `L13`–`L16` xuất hiện trong kế hoạch hook thật nhưng **chưa ai viết định nghĩa**. Agent được phép **gán** các mã này nếu kế hoạch đã dùng, nhưng phải ghi `⚠ chưa có định nghĩa format`.

---

## 3. BA CÁCH VIẾT HOOK — VÀ MỘT CÁCH SAI

### ✅ Cách 1 — CHÉP NGUYÊN *(tốt nhất)*

Lấy thẳng câu hỏi đầu tiên của khách.

```
HT-031: "mũi em nâng rồi mà đầu mũi bị bóng đỏ, giờ còn sửa được không ạ?"
     → hook: "Mũi đã nâng mà đầu mũi bóng đỏ — còn sửa lại được không?"
```

★ Hook này **không thể sai giọng khách**, vì nó chính là giọng khách.

### ✅ Cách 2 — GỘP TẦN SUẤT

12 người hỏi cùng một ý theo 12 cách → một câu gọi đúng tình trạng.

```
12 × O-04 → "Nâng mũi xong mấy ngày thì đi làm được mà không ai nhận ra?"
```

### ✅ Cách 3 — LẬT Ô TRỐNG

Ô trống trong ma trận `CD × 5A` + một mã `O` cao → hook mới cho đúng ô đó.

### ⛔ Cách SAI — "viết hook hay"

```
⛔ Tự nghĩ một câu nghe kêu rồi gán ngược cho một mã O.
   Dấu hiệu nhận ra: hook có TÍNH TỪ ("đẹp tự nhiên", "hoàn hảo", "đẳng cấp")
   mà không có TÌNH TRẠNG nào cụ thể.
```

★ **Luật một câu:** *hook gọi đúng **tình trạng**, không khen **tính từ**.*

---

## 4. KHUÔN MỘT DÒNG TRONG NGÂN HÀNG HOOK

| Cột | Bắt buộc | Ghi chú |
|---|---|---|
| `MÃ` | ✅ | `KN-<kỳ>-<nnn>` |
| `KHỐI` | ✅ | ① Tăng HOT · ② Giảm COLD · ③ Tối ưu WARM |
| `CD` · `NẤC` | ✅ | |
| `MÃ O` | ✅ | Mã phản đối hook này đóng |
| `INSIGHT LÕI` | ✅ | Khách đang tin gì / sợ gì — viết bằng chữ của khách |
| `HOOK 3 GIÂY` | ✅ | Lời thoại mở đầu, **đọc nguyên văn được** |
| `LOẠI HOOK` | ✅ | 1 trong 7 loại §1 |
| `FM1` `FM2` `FM3` | ✅ | 3 format `L01`–`L16` |
| `CTA CUỐI` | ✅ | |
| ★ `TRUY NGƯỢC` | ✅ | `HT-nnn` hoặc tên chỉ số. **Trống = loại khỏi kế hoạch** |
| `NHIỆT` | ✅ | Hot / Warm / Cold — tệp nhắm tới |
| `Ô CAMP` | 🔶 | `V1`–`V5` / `P1`–`P5` (`id-E` §3) |
| `CỜ PHÁP CHẾ` | ✅ | 🔴 🟡 🟢 theo `id-K` |
| `DUYỆT` | ⬜ | **Để trống** — BS + pháp chế điền, thứ Tư |

⛔ **Chỉ hook `DUYỆT = XANH` mới được lên ads.** Agent ⛔ không tự điền ô này.

---

## 5. LUẬT CÂN ĐỐI KỲ

```
① ≥ 1 ô CHALLENGER mỗi kỳ, kể cả kỳ số đẹp.
   Winner chết mà chưa có đồ thay là chậm 7–10 ngày.

② Mỗi khối của ma trận phải có ≥ 1 hook. ⛔ Không dồn hết vào khối ①.

③ Không quá 50% hook cùng một loại hook.
   Ngân hàng toàn CON SỐ thì khi Facebook siết số liệu là chết cả kho.

④ Mỗi chân dung được chọn phải có ≥ 1 hook nấc A3.
   A3 là điểm quyết định — bỏ A3 là bỏ chỗ khách rơi nhiều nhất.
```

---

## 6. ⛔ HOOK KHÔNG ĐƯỢC VIẾT

- ⛔ Hook nói với **người xem** rằng họ đang có khiếm khuyết → Facebook từ chối
- ⛔ Hook có **con số bảo hành** (`O-07` đang chặn)
- ⛔ Hook trả lời **bệnh nền / chống chỉ định** (`O-12`)
- ⛔ Hook gắn **chức danh, số năm, số ca của bác sĩ chưa đối chiếu chứng chỉ**
- ⛔ Hook có **giá dịch vụ ngoài mắt** khi chưa có bảng giá hiện hành
- ⛔ Hook hứa **đổi vận, tài lộc** (`CD5`) hoặc **tỷ lệ thành công** (`CD6`)
- ⛔ Hook **dìm đối thủ**
- ⛔ Hook lấy **số từ hook cũ** làm nguồn giá — hook cũ không phải nguồn giá

---

## 7. TỰ KIỂM SỔ NÀY

- [ ] Mỗi hook có `HT-nnn` hoặc chỉ số truy ngược không?
- [ ] Có hook nào chỉ có tính từ mà không có tình trạng không?
- [ ] Ba khối ma trận có hook đủ cả ba không?
- [ ] Có quá 50% hook cùng một loại không?
- [ ] Mỗi chân dung được chọn có hook nấc `A3` không?
- [ ] Cột `DUYỆT` có bị agent tự điền không?
- [ ] Có hook nào chạm `O-07` / `O-12` lọt ra không?
