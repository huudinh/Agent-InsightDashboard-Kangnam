# id-E · ★ TỔ CHỨC ADS & ĐỌC CHỈ SỐ — FACEBOOK + GOOGLE

> Sổ này trả lời hai câu: **quảng cáo Kangnam được tổ chức thế nào** (để cắt số đúng chiều), và **đọc số ra kết luận gì** (để không chữa nhầm bệnh).
> Nguồn: sheet `5. Tổ chức Ads`, sheet `Giao ban`, và dashboard *"Kangnam – Hiệu quả quảng cáo Meta"*.

---

## 1. CHUỖI CHỈ SỐ — GIỮ ĐÚNG THỨ TỰ

```
CPM → CTR → CPI (Inbox) → CPL (Lead) → CPB (Booking) → Booking/Lead
```

Mỗi mắt xích hiện **ba thứ**: giá trị · so **mục tiêu** · so **kỳ trước**.

| Chỉ số | Công thức | Mục tiêu lấy từ đâu |
|---|---|---|
| **CPM** | chi ÷ hiển thị × 1.000 | TB 30 ngày của dịch vụ |
| **CTR** | click ÷ hiển thị | TB 30 ngày của dịch vụ |
| **CPI** | chi ÷ inbox | TB 30 ngày của dịch vụ |
| **CPL** | chi ÷ lead SĐT hợp lệ | TB 30 ngày của dịch vụ |
| **CPB** | chi ÷ booking | TB 30 ngày của dịch vụ |
| **Booking/Lead** | booking ÷ lead | so kỳ trước, tính bằng **điểm %** |

⚠️ Chưa đủ 30 ngày → ghi `⚠ chưa có mốc so sánh`. ⛔ **Không tự đặt mốc.**
⚠️ Ngày có **dưới 3 kết quả** thì ⛔ không vẽ điểm CPB/CPL của ngày đó — số đó là nhiễu, không phải tín hiệu.

### ★ LUẬT QUAN TRỌNG NHẤT — PHÂN RÃ TRƯỚC KHI KẾT LUẬN

```
CPL = (CPM/1000) ÷ ( CTR × click→inbox% × inbox→lead% )

⛔ KHÔNG KẾT LUẬN "CẦN LÀM THÊM NỘI DUNG" KHI THÀNH PHẦN XẤU ĐI KHÔNG PHẢI CTR.
```

| Thành phần xấu đi | Thật ra là việc của | Agent phải nói |
|---|---|---|
| **CTR** giảm | Nội dung | *"Đây là vấn đề nội dung"* |
| **CPM** tăng | Adnet — tệp, bid, lịch | *"Kỳ này KHÔNG phải vấn đề nội dung"* |
| **click→inbox** giảm | Kỹ thuật — điểm đến, lời chào tự động | *"Không phải nội dung"* |
| **inbox→lead** giảm | ★ **Trực page** — ca trực, thời gian phản hồi, cách xin số | *"Không phải nội dung"* → đẩy sang `id-F` |

★ Đây là chỗ agent này mạnh hơn mọi agent ads khác: **mắt xích `inbox→lead` được chứng minh bằng chính hội thoại**, không phải suy đoán. Khi `inbox→lead` giảm, agent chỉ thẳng ra bao nhiêu HT rơi do trực page và vì câu nào.

⚠️ Một agent quảng cáo luôn kết luận *"cần làm thêm content"* là một agent vô dụng. **Dám nói "không phải lỗi nội dung" là giá trị, không phải né việc.**

---

## 2. QUY ƯỚC TÊN CHIẾN DỊCH — 11 CHIỀU CẮT SỐ

Tên chiến dịch thật đang chạy có dạng:

```
kgs_knfb001_mb_{}_mui_ib_mofub_tuyetna_kq_thao nep mui_video_mof_hn lan can
 ①   ②     ③  ④   ⑤   ⑥   ⑦      ⑧      ⑨      ⑩         ⑪    ⑫     ⑬
```

| # | Vị trí | Nghĩa | Giá trị hay gặp |
|---|---|---|---|
| ① | `kgs` | Tiền tố hệ thống | ⚠ cần xác nhận nghĩa |
| ② | `knfb001` | **Tài khoản quảng cáo** | `knfb001` `knfb015` … |
| ③ | `mb` | **Khu vực** | `mb` Bắc · `mn` Nam · `allvn` · `mt` Miền Tây |
| ④ | `{}` | Ô động | |
| ⑤ | `mui` | **Dịch vụ** | `mui` `mat` `ham` `nguc` `da` … |
| ⑥ | `ib` | **Mục tiêu** | `ib` inbox · `lead` · `book` · `view` |
| ⑦ | `mofub` | **Phễu** | `tof` · `mof` · `bof` · `mofub` |
| ⑧ | `tuyetna` | ★ **Nhân viên chạy ads** | — |
| ⑨ | `kq` | **Góc nội dung** | `kq` kết quả · `feedback` · `talk bs` · `cn` công nghệ · `quyen loi` |
| ⑩ | `thao nep mui` | **Tên nội dung** | |
| ⑪ | `video` | **Format** | `video` · `banner` |
| ⑫ | `mof` | **Tầng nội dung** | khớp nấc 5A |
| ⑬ | `hn lan can` | **Địa phương hoá / mức local** | `hn bang` · `hcm lan can` · `hn lan can` |

> ⚠️ Bảng giải mã này **suy ra từ dữ liệu thật trong sheet Giao ban**, chưa được khối Ads xác nhận bằng văn bản. Ghi `⚠` khi dùng; thấy mẫu tên không khớp thì **báo lại**, ⛔ đừng ép vào khuôn.

### 16 chiều lọc của dashboard Meta hiện hành

`Khoảng thời gian` · `Chỉ số (Inbox·CPI / Lead·CPL / Booking·CPB)` · `Dịch vụ` · `Đối tượng KH` ·
`Loại tài khoản (Perform/Brand)` · `Tài khoản` · `Fanpage` · ★`Nhân viên` · `Phễu` ·
`Tầng nội dung` · `Góc nội dung` · `Địa phương hoá` · `Mức local` · `Khu vực` · `Chiến dịch`

★ Chiều **`Nhân viên`** là cầu nối duy nhất giữa số ads và `id-F`. ⚠️ **Cẩn thận:** `nhân viên` trong tên chiến dịch là **người chạy ads**, ⛔ **không phải** nhân viên trực page. Hai vai này ⛔ không được trộn vào một bảng điểm.

### Sáu line

`Kangnam All` · `KN PTTM` · `KN Beauty` · `KN Weightloss` · `KN Việt Kiều` · `KN Quốc tế (TA)`

⛔ Không so chéo CPL giữa hai line khác nhau — giá trị đơn khác nhau nên con số không cùng nghĩa.

---

## 3. MA TRẬN 10 Ô — VIEW × PERF

```
VIEW = ThruPlay/Reach : hút tệp mới + nuôi tệp ấm
PERF = Tin nhắn/Lead/Đặt lịch : đo bằng chi phí/kết quả

Luồng chạy theo ĐƯỜNG CHÉO: VIEW nấc n tạo tệp cho PERF nấc n+1.
Tách VIEW/PERF ở cấp CAMPAIGN. ⛔ Không trộn trong 1 CBO, ⛔ không tách tài khoản.
```

| Nấc | Ô VIEW | % NS | Ô PERF | % NS | CP mục tiêu / kết quả |
|---|---|---|---|---|---|
| `A1` | `V1` | 5% | `P1` — ⛔ **KHÔNG CHẠY** | 0% | người chưa biết vấn đề thì không mời nhắn tin |
| `A2` | `V2` | 3% | `P2` Tin nhắn (TOF) | 22% | 400.000 đ ⚠ |
| `A3` | `V3` | 1% | `P3` Tin nhắn / Lead (MOF) | 48% | 1.150.000 đ ⚠ |
| `A4` | `V4` | 0,5% | `P4` Đặt lịch (BOF) | 20% | 2.650.000 đ ⚠ |
| `A5` | `V5` | — | `P5` Cross-sell | — | — |

⚠️ Con số chi phí mục tiêu trong bảng là **GIẢ ĐỊNH của kế hoạch**, phải thay bằng số thực 3 tháng. Tỷ trọng gợi ý: PTTM VIEW ~25% / PERF ~75%; dịch vụ Entry (Da, Spa) VIEW ~35% / PERF ~65%. **Tổng VIEW + PERF phải = 100%.**

### Kho tệp — vào / loại trừ

| Mã tệp | Nguồn | Cửa sổ | Vào ô | Loại trừ ở ô |
|---|---|---|---|---|
| `LAL-CHOT` | Offline event Chốt (Caresoft) | 180 ngày | `V1` `P2` | — |
| `LAL-SDT` | Danh sách SĐT | 60 ngày | `V1` `P2` | — |
| `LAL-inb` | Đã inbox chuyên khoa | 30 ngày | `V1` `P2` | — |
| `BROAD-GEO` | Địa lý quanh 2 bệnh viện | — | `V1` `P2` | — |
| `VV25-DV` | Xem ≥25% video dịch vụ | 30–90 ngày | `V2` `P3` | `P2` |
| `VV95-N1` `VV95-N2` | Xem ≥95% creative nuôi | 30 ngày | `V3` `P3` | `V2` |
| `ENG` | Tương tác Page/IG | 30–90 ngày | `P3` | `P2` |
| `MSG` | Đã nhắn tin Page | 14–30 ngày | `P4` | `P2` `P3` `V2` `V3` |
| `LEAD-NB` | Lead chưa đặt lịch | 14–30 ngày | `P4` | `P2` `P3` `V2` `V3` |
| `BOOKED-NS` | Đặt lịch chưa đến | 14 ngày | `V4` | `P2` `P3` `P4` |
| `CUST` | Đã làm dịch vụ | 365 ngày | `V5` `P5` | mọi chiến dịch thu khách mới |

★ **Nguồn Lookalike phải là "đã chốt", ⛔ không dùng "đã nhắn".**
★ Giữ **10–15% tệp làm nhóm ĐỐI CHỨNG** (không cho xem VIEW nuôi) để đo được VIEW có tác dụng thật không.

---

## 4. CHẤM NỘI DUNG — 🟢🟡🔴 VÀ BỐN ĐƯỜNG CẢI TIẾN

| Chấm | Điều kiện | Cải tiến |
|---|---|---|
| 🟢 **TỐT** | CTR ≥ trung vị **và** CPL ≤ trung vị | **Nhân bản** — giữ hook, đổi chân dung/khu vực |
| 🟡 **TB** | Một trong hai đạt | **Biến thể** — đổi **đúng một** biến |
| 🔴 **KÉM** + mã `O` vẫn cao | CTR ≤ −30% trung vị, CPM trong ±15% | **Giữ ý — bỏ hook** |
| 🔴 **KÉM** + mã `O` thấp | | **Bỏ hẳn** |

⛔ **Không đổi ≥3 biến cùng lúc** — đổi ba biến thì dù kết quả tốt lên cũng không học được gì.

⚠️ **Luật port vùng miền:** nội dung 🟢 ở miền này ⛔ **không tự động 🟢** ở miền khác. Dữ liệu thật cho thấy nhiều nội dung TỐT ở Nam bị chấm KÉM khi port ra Bắc. Port thì phải quay lại hook bằng **giọng và bối cảnh của miền đó**.

---

## 5. GOOGLE ADS — 🔴 KHUNG CHỜ DỮ LIỆU

> Cột đầu vào ở `id-B` §4. Phần dưới là **cách đọc khi dữ liệu về**.

### Ba việc Google Ads làm được mà Facebook không

| # | Việc | Ra kết luận gì |
|---|---|---|
| ① | **Search term → mã `O`** | Khách gõ gì vào Google là insight trực tiếp. Map thẳng sang `O-01…O-12` cùng bảng với hội thoại |
| ② | **Truy vấn tốn tiền không chuyển đổi** | Cắt được trong ngày — tiết kiệm nhanh nhất trong cả hệ |
| ③ | **Truy vấn có người tìm mà Kangnam chưa có trang** | Lỗ hổng nội dung web → bàn giao `Agent-KN-GEO-Plant` |

### Ba bảng Google Ads trong dashboard

```
① Chuỗi chỉ số : CPC → CTR → CPL theo chiến dịch (cùng khuôn với Facebook)
② Search term  : truy vấn · chi · click · chuyển đổi · mã O gán được · quyết định (giữ/phủ định/mở trang)
③ So kênh      : cùng một mã O, Facebook tốn bao nhiêu / Google tốn bao nhiêu để ra 1 lead
```

⛔ Khi chưa có file: mọi ô để `null`, dashboard hiện `chưa có dữ liệu Google Ads`. ⛔ Không ước lượng, ⛔ không lấy số Facebook gán sang.

---

## 6. NỐI HỘI THOẠI ↔ NỘI DUNG ADS

| Nối theo | Cách làm | Độ tin |
|---|---|---|
| **Nội dung khách bấm vào** (ref/ad id trong hội thoại) | Chuẩn nhất | ✅ Cao |
| **Fanpage + khoảng ngày** | Khi không có ref | 🟡 Trung bình — ghi `⚠ suy ra` |
| **Dịch vụ khách hỏi** | Khi chỉ có hai thứ trên | 🔴 Thấp — chỉ dùng để tham khảo |

Gộp mọi ID cùng một nội dung về **một dòng theo TÊN NỘI DUNG**, bỏ tag cụm, mã người chạy, đuôi `_tối ưu` / `- Bản sao`; tên người mẫu thay bằng `[KH mẫu]`.

Mỗi dòng nội dung trong dashboard mang: `chi` · `inbox` (mới/cũ) · `deal` · `booking` · `CPI` · `CPL` · `CPB` · `đánh giá 🟢🟡🔴` · `khách hỏi gì · CD` · `cờ pháp chế`.

⚠️ **Chiến dịch nhiều mẫu** (một campaign chứa nhiều nội dung, không tách được chi) thì ⛔ không chia đều chi. Tách riêng một bảng *"chưa tách được chi cho từng nội dung"* và ghi rõ tổng.

---

## 7. TỰ KIỂM SỔ NÀY

- [ ] Đã **phân rã CPL** trước khi kết luận chưa?
- [ ] Có kết luận "cần thêm content" trong khi thành phần hỏng không phải CTR không?
- [ ] Mỗi chỉ số có đủ **ba thứ** (giá trị · mục tiêu · kỳ trước) không?
- [ ] Mốc nào chưa có đã ghi `⚠ chưa có mốc so sánh` chưa, hay đã tự đặt?
- [ ] Có so chéo CPL giữa hai line khác nhau không?
- [ ] `nhân viên chạy ads` có bị trộn với `nhân viên trực page` không?
- [ ] Ngày dưới 3 kết quả có bị vẽ lên đường CPB không?
