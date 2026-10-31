# id-B · ĐỌC ĐẦU VÀO — BA DÒNG DỮ LIỆU

> Agent nhận **ba dòng dữ liệu**. Dòng ① bắt buộc. Dòng ② nên có. Dòng ③ hiện **chưa có** — khung đã dựng sẵn, chờ cấp.

---

## 1. BA DÒNG

| Dòng | Nguồn | Trạng thái | Thiếu thì sao |
|---|---|---|---|
| ① **Hội thoại chat khách** | Caresoft › Messenger / Zalo OA / IG / bình luận FB | ✅ Có thật | ⛔ Không chạy được gì |
| ② **Chỉ số quảng cáo Facebook** | File *"Kangnam – Hiệu quả quảng cáo Meta"* | ✅ Có thật | Chạy được tab Phễu + Chấm điểm, ⛔ mất tab Marketing & Ma trận có điểm |
| ③ **Chỉ số Google Ads** | 🔴 **[CHỜ CẤP]** | ⛔ Chưa có | Tab Marketing ghi `⚠ chưa có dữ liệu Google Ads`, ⛔ không suy đoán |

---

## 2. DÒNG ① — HỘI THOẠI

### Khuôn file (bản xuất Caresoft, Markdown)

```
### <a id="ht-1"></a>1. <Tên khách>

_Cập nhật: 2026-10-13 14:46:52 · NV: <Tên nhân viên> · SĐT: Có|Không · ID: t_xxxxx_

- `10-13 14:26` **KH:** <nội dung>
- `10-13 14:29` **NV <Tên nhân viên>:** <nội dung>
```

| Trường | Bắt buộc | Dùng để |
|---|---|---|
| Mã hội thoại | ✅ | Truy ngược — mọi hook, mọi lỗi phải chỉ về được `HT-nnn` |
| Dấu thời gian từng tin | ✅ | SLA, tốc độ trả lời tin đầu, khung giờ |
| `KH:` / `NV <tên>:` | ✅ | Tách hai nửa hội thoại · gán nhân viên |
| SĐT có/không | ✅ | Chỉ số lõi `% có SĐT` |
| Page / nguồn quảng cáo | 🔶 nên có | Nối hội thoại ↔ nội dung ads (`id-E` §6) |
| Dịch vụ khách hỏi | ⬜ tự suy ra | Tín hiệu nóng ① · hệ số giá trị đơn. ⛔ **Không** dùng để gán chân dung (`id-C` §1) |

### ⛔ Tám thứ phải bỏ trước khi ghi ra bất cứ đâu

```
tên thật khách · số điện thoại · ảnh khách · email · địa chỉ nhà
link Facebook cá nhân · mã đơn hàng · tên người nhà khách nhắc tới
```
Trích dẫn trong báo cáo phải ở dạng **đã ẩn danh**, chỉ còn `HT-nnn` + nội dung câu hỏi.

### Chín ô tự suy ra, ⛔ không hỏi người dùng

`mức nóng` · `nấc 5A` · `mã O` · `rào cản` · `vì sao rơi` ·
`có chốt lịch trong chat không` · `tin đầu khách hỏi gì` · `khu vực khách tự nói` · `khách mới hay khách cũ`

⚠️ **`chân dung CD` KHÔNG nằm trong danh sách này.** Chân dung không suy ra được từ một ô dữ liệu: nó được **phác họa từ chữ của khách** rồi người dùng duyệt ở **CỔNG 0** (`id-C` §1–2). Trước khi duyệt, ô `cd` của mọi hội thoại để `null`.

---

## 3. DÒNG ② — CHỈ SỐ FACEBOOK ADS

Cột tối thiểu (khớp bản xuất Meta mà khối đang dùng):

| Cột | Kiểu | Ghi chú |
|---|---|---|
| `ngay` | ngày | |
| `chien_dich` | chữ | Tên theo quy ước ở `id-E` §2 |
| `tai_khoan` · `fanpage` | chữ | |
| `chi` | số (đ) | **Chỉ lấy cột Chi theo chiến dịch** |
| `hien_thi` · `click` | số | Để tính CTR |
| `inbox` | số | Hội thoại tin nhắn bắt đầu |
| `lead` | số | Lead SĐT hợp lệ |
| `booking` | số | |
| `nhan_vien_chay` | chữ | Người chạy ads — ⛔ **không phải** nhân viên trực page |

⚠️ **Tiền trong mọi bảng quy về NGHÌN ĐỒNG**, ghi rõ đơn vị ở đầu bảng.

### Chuỗi chỉ số bắt buộc giữ đúng thứ tự

```
Chi phí tổng → CPM → CTR → CPI (Inbox) → CPL (Lead) → CPB (Booking) → Booking/Lead
```
Mỗi mắt xích hiển thị **ba thứ**: giá trị · so **mục tiêu** · so **kỳ trước**.
Mốc mục tiêu lấy **trung bình 30 ngày của chính dịch vụ đó**; chưa đủ 30 ngày → `⚠ chưa có mốc so sánh`.

---

## 4. DÒNG ③ — GOOGLE ADS · 🔴 KHUNG CHỜ DỮ LIỆU

> Agent **đã có sẵn khối đọc**; chỉ thiếu file. Khi có, thả vào `du-lieu/google-ads.csv` đúng cột dưới đây là chạy được ngay.

| Cột | Kiểu | Khớp với cột Facebook |
|---|---|---|
| `ngay` | ngày | `ngay` |
| `chien_dich` | chữ | `chien_dich` |
| `nhom_quang_cao` | chữ | — |
| `tu_khoa` / `search_term` | chữ | ★ **không có đối ứng bên FB** — đây là giá trị riêng của Google |
| `loai_doi_sanh` | chữ | chính xác / cụm từ / rộng |
| `chi` | số (đ) | `chi` |
| `hien_thi` · `click` | số | `hien_thi` · `click` |
| `chuyen_doi` | số | ≈ `lead` |
| `loai_chuyen_doi` | chữ | cuộc gọi · form · chat · đặt lịch |
| `diem_chat_luong` | số 1–10 | — |
| `ty_le_hien_thi_top` | % | — |

### Ba câu Google Ads trả lời được mà Facebook không

```
① Khách gõ CHỮ GÌ vào Google trước khi vào — search term là insight trực tiếp,
   không phải suy ra từ hành vi xem video.
② Truy vấn nào đang tốn tiền mà không ra chuyển đổi — cắt được ngay.
③ Truy vấn nào có người tìm mà Kangnam chưa có trang trả lời — lỗ hổng nội dung web.
```
★ Khi dòng ③ về, **search term đổ thẳng vào bảng mã `O`** ở `id-D` §2 như một nguồn thứ hai bên cạnh hội thoại.

⛔ **Cho tới lúc đó:** mọi ô Google Ads trong dashboard để `null`, hiển thị `chưa có dữ liệu`. ⛔ Không ước lượng, không lấy số Facebook gán sang.

---

## 5. KIỂM ĐẦU VÀO — IN RA TRƯỚC KHI CHẠY

```
CỠ MẪU
  Đã đọc            : <n> hội thoại
  Loại khỏi phân tích: <n>  (lý do: <trùng · dưới 2 tin · page ngoài phạm vi · ngoài kỳ>)
  Còn lại           : <n>
  Khách mới / khách cũ: <n> / <n>

KỲ         : <tu> → <den>
NGUỒN      : <tên file / crawl lúc nào>
DÒNG ②     : có / không — nếu có: tên file, khoảng ngày
DÒNG ③     : ⚠ chưa có
MỐC SO SÁNH: kỳ trước <có/không> · mục tiêu 30 ngày <có/không>
```

⚠️ **Kỳ trước chồng lấn kỳ này** (ví dụ 19–22/10 nằm trong 19–25/10) thì vẫn so được nhưng phải ghi *"trùng x/y ngày — chỉ để tham khảo"*.

---

## 6. QUY ƯỚC MÃ — ⛔ KHÔNG ĐỔI

| Mã | Nghĩa | Định nghĩa ở |
|---|---|---|
| `HT-nnn` | Một hội thoại | sổ này |
| `CD0` | ★ Mã **dự trữ** — hội thoại không khớp dấu hiệu chân dung nào. ⛔ Không phác họa, ⛔ không đổi nghĩa | `id-C` §1 |
| `CD1 … CDn` | Chân dung **của từng kỳ**, phác họa từ hội thoại kỳ đó. Số lượng và tên thay đổi theo kỳ; mã giữ nguyên khi cùng nỗi sợ | `id-C` §1 · `out/chan-dung.json` |
| `A1 … A5` | Nấc hành trình 5A | `id-C` |
| `O-01 … O-12`, `O-00` | Mã phản đối / rào cản | `id-D` |
| `L01 … L16` | Format thể hiện | `id-H` |
| `N1 … N6` | Sáu nhóm tiêu chí chấm nhân viên | `id-F` |
| `CĐ-1 … CĐ-6` | Cờ đỏ trong hội thoại | `id-F` §5 |
| `V1–V5 / P1–P5` | Ô chiến dịch VIEW / PERF | `id-E` |

★ Các mã này **được tham chiếu chéo ở 30+ chỗ trong repo và ở hai agent khác**. Đổi tên mã = hỏng cả hệ.

⚠️ Ngoại lệ duy nhất là `CD1 … CDn`: **nội dung** của chúng đổi theo kỳ, chỉ **khuôn mã** là cố định. Gửi số liệu theo chân dung cho người khác thì gửi kèm `out/chan-dung.json` của kỳ, ⛔ không để người đọc tự đoán `CD2` nghĩa là gì.
