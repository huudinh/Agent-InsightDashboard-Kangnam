# id-N · ★ CHỌN TỆP TẬP TRUNG & TẦNG NỘI DUNG — BỘ KF-64 v1.0

> Sổ **nhập từ ngoài**, như `id-L` và `id-M`: đây là văn bản KF-64 của khối Sale.
> ⛔ Repo không tự đặt thêm trục, trọng số hay ngưỡng nào.
>
> 🔴 **BẢN ĐỀ XUẤT — CHƯA ANH UY DUYỆT (02/11/2026).** Khác hẳn `id-L` và `id-M`:
> hai sổ kia có dòng duyệt, sổ này chưa. Nên mọi con số ở đây là **đề xuất**,
> ⛔ không phải luật. Công thức **đang có hiệu lực** để xếp hạng chân dung vẫn là
> [`id-M` §7](id-M-thu-vien-chan-dung-kf62.md) — xem §2 dưới.

**Sổ này trả lời:** trong một dịch vụ thì **dồn lực vào chân dung nào**, và với
chân dung đó thì **làm nội dung tầng nào trước**.

### Ranh giới — ⛔ bốn sổ, bốn quyết định khác nhau

```
id-L     → GỌI AI TRƯỚC      · một HỘI THOẠI   · điểm × hệ số giá trị đơn
id-M §7  → DỒN SỨC VÀO AI    · một CHÂN DUNG   · ★ ĐANG CÓ HIỆU LỰC
id-N     → DỒN SỨC + TẦNG NÀO· một CHÂN DUNG   · 🔴 đề xuất, mở rộng id-M §7
id-G §3  → HỆ SỐ 1 · 2 · 3   · thành phần dùng chung
```

⚠ `id-M` §7 và `id-N` §2 trả lời **cùng một câu hỏi**. Đó đúng là tình huống đã
làm hỏng `id-C` §4 (hai công thức cho một quyết định thì chắc chắn lệch nhau).
Lần này ⛔ không để hai bản cùng sống: `id-M` §7 là bản chạy, `id-N` là bản chờ.

---

## 1. ĐỔI GÌ SO VỚI `id-M` §7

`id-M` §7 (anh UY chốt 02/11) và KF-64 §3.1 **không phải hai thứ khác nhau** —
KF-64 là bản mở rộng, và chính nó khai điều đó: *"tỷ lệ Chất lượng : Chuyển đổi
= 30 : 50 giữ đúng tương quan 40 : 60 mà anh đã chốt"*.

| | `id-M` §7 — đang chạy | KF-64 §3.1 — đề xuất |
|---|---|---|
| Quy mô | ⛔ không có | **20%** ← phần mới |
| Chất lượng (nhiệt độ) | 40% | 30% |
| Chuyển đổi (booking CRM) | 60% | 50% |
| Mốc đọc | ≥110 CAO · 90–109 TB · <90 THẤP | **y nguyên** |
| Cỡ mẫu | ≥30 HT **và** ≥5 booking | **y nguyên** |
| Gốc so sánh | TB **dịch vụ**; dịch vụ so TB hệ thống | **y nguyên** |

★ Nên đọc như vậy: **30:50 với 40:60 là cùng một tỷ lệ**, KF-64 chỉ chen thêm
trục Quy mô 20% vào trước. Và §6 của KF-64 tự đặt đúng câu hỏi đó thành A/B
test ①: `20/30/50` so với `0/40/60`, đo CPB sau 30 ngày.

⚠ Vì vậy ⛔ **đừng nhập KF-64 như một bộ thứ hai.** Khi anh UY duyệt thì nó
**thay** `id-M` §7, không chạy song song.

### Chỉ số tạm khi chưa có CRM

```
Chỉ số tạm = 100 × (0,4 × Quy mô + 0,6 × Chất lượng)      ← ghi rõ "TẠM"
⛔ Chỉ dùng để chọn nhóm LÀM THỬ, ⛔ không để dồn ngân sách lớn.
```

★ Cái này **chạy được ngay** trên dữ liệu đang có, và tốt hơn bản proxy của
`id-M` §7 ở một điểm: nó ⛔ không dùng `% có SĐT` làm thế thân cho booking.

---

## 2. MA TRẬN QUY MÔ × HIỆU QUẢ — 🔴 ⛔ CHƯA VẼ ĐƯỢC

```
Quy mô "lớn"   : chỉ số Quy mô ≥ 1,0 (từ mức chia đều trở lên)
Hiệu quả "tốt" : điểm hiệu quả ≥ 100
                 điểm hiệu quả = 100 × (0,375 × Chất lượng + 0,625 × Chuyển đổi)
```

| Ô | Điều kiện | Chiến lược | TOF / MOF / BOF |
|---|---|---|---|
| **① Trụ cột** | Lớn + Tốt | Scale có kiểm soát `+15–20%/3 ngày` (KF-49), giữ chất lượng | 30 / 40 / 30 |
| **② Ngách hiệu quả** | Nhỏ + Tốt | Mở rộng tệp: tăng TOF/A2 kéo thêm **đúng** người | 45 / 35 / 20 |
| **③ Đông nhưng yếu** | Lớn + Chưa tốt | ⛔ **Không tăng ngân sách kéo khách.** Sửa MOF, kịch bản, tốc độ Sale | 15 / 55 / 30 |
| **④ Duy trì tối thiểu** | Nhỏ + Chưa tốt | Giữ remarketing + nội dung nền, xem lại sau 30 ngày | 20 / 40 / 40 |

Ràng buộc KF-50: **BOF ≥ 10%** và **remarketing ≤ 40%** tổng chi của dịch vụ.
Thứ tự dồn lực xếp theo Chỉ số tập trung, nhưng **mỗi dịch vụ giữ ít nhất một
chân dung ở ô ②** để không bỏ lỡ nhóm đang lên.

### 🔴 Lỗ hổng của chính văn bản KF-64

```
Chỉ số tập trung  CÓ bản dự phòng khi thiếu CRM  → "chỉ số tạm" (0,4/0,6)
Điểm hiệu quả     ⛔ KHÔNG có bản dự phòng nào
                  mà Chuyển đổi chiếm 62,5% của nó.
```

⚠ Hệ quả đo được: **ma trận bốn ô ⛔ không vẽ được dòng nào** cho kỳ 24–29/10.
⛔ Và ⛔ **không được tự lấy Chất lượng làm «hiệu quả»** để lấp — KF-64 không cho
phép, và làm thế thì ô ③ *"đông nhưng yếu"* biến thành *"đông nhưng nguội"*, là
hai chẩn đoán khác nhau dẫn tới hai việc khác nhau.

★ Đây là **câu hỏi phải gửi lại khối Sale**, ⛔ không phải chỗ repo tự quyết.

---

## 3. NĂM TẦNG × PHỄU — 🔴 ĐỤNG NẤC `5A` CỦA `id-D` §3

| Tầng | Phễu | KF-64 nói khách đang ở đâu | `id-D` §3 nói |
|---|---|---|---|
| **A1** | TOF | Chưa biết vấn đề có giải pháp, hoặc chưa biết Kangnam | Có vấn đề nhưng **chưa gọi tên** |
| **A2** | TOF→MOF | 🔴 **Có nhắn tin nhưng chưa nói rõ nhu cầu** | 🔴 **Đang so phương pháp, lập shortlist** |
| **A3** | MOF | 🔴 Đã nói nhu cầu, **đang so sánh**, có rào cản | Điểm quyết định — nỗi sợ đạt đỉnh |
| **A4** | BOF | Nóng nhưng chưa chốt lịch, chưa đến | Đã inbox/đặt lịch, còn có thể huỷ |
| A5 | sau dịch vụ | Đã làm — CDP, ⛔ không phải ads kéo khách | Đã làm, lo hậu phẫu |

### ⛔ `A2` là HAI thứ khác nhau dưới cùng một tên

```
KF-64 : A2 = CHƯA NÓI RÕ NHU CẦU         → đo ở CẤP DỊCH VỤ, §4.2
id-D  : A2 = ĐANG SO PHƯƠNG PHÁP         → đọc câu hỏi ĐẦU TIÊN của khách

Đo trên cùng 494 hội thoại kỳ 24–29/10:
   A2 theo id-D   →     1 hội thoại
   A2 theo KF-64  →   324 hội thoại
```

★ **Một nhãn, 1 với 324.** Cái mà KF-64 gọi là `A2` thì `id-D` xếp phần lớn vào
`A1` (329 HT). Và cái `id-D` gọi là `A2` thì KF-64 nhập vào `A3`
(*"đã nói nhu cầu, đang so sánh"*).

⛔ **Không được để hai định nghĩa cùng tên.** Hai đường ra, phải chọn một:

| | Cách | Được gì | Mất gì |
|---|---|---|---|
| ⓐ | Giữ `5A` của `id-D`, KF-64 dùng **tên khác** cho trục phễu (`T1…T4`) | ⛔ không phải chấm lại 494 HT; tab Phễu giữ nguyên | Hai bộ tên song song, phải có bảng quy đổi |
| ⓑ | Đổi `5A` theo KF-64 | một bộ tên duy nhất, khớp KF-57 | Chấm lại toàn bộ; ⛔ mất mốc so sánh với kỳ 19–25/10 |

★ Tôi nghiêng về **ⓐ**: `5A` của `id-D` đọc từ **câu hỏi đầu tiên**, một hội
thoại một nấc, truy ngược được. `A2` của KF-64 ⛔ không đọc được ở cấp hội thoại
— chính KF-64 §4.2 nói nó phải đo ở **cấp dịch vụ**. Hai thứ ở hai cấp khác nhau
thì ⛔ không nên trùng tên. Nhưng đây là **việc của khối Sale chốt**, không phải
của repo.

---

## 4. LUẬT `A2` CẤP DỊCH VỤ — ★ CHẠY ĐƯỢC NGAY

> KF-64 §4.2: tỷ lệ hội thoại **chưa rõ nhu cầu** ≥ **30%** → dịch vụ đó ưu tiên
> **A2 (TOF→MOF)**: nội dung tự phân loại *"bạn thuộc kiểu nào"*, hook đúng chân
> dung, đưa **câu hỏi vàng** lên ads.

★ Luật này nối thẳng vào hai mã dự trữ của `id-M`: `<DV>-CHUA_XAC_DINH` và
`KHONG_XAC_DINH_DV` **chính là** tử số của nó. Nhờ vậy nó ⛔ không cần CRM, ⛔
không cần booking, và đo được từ kỳ đầu tiên.

### Kết quả đo — kỳ 24–29/10/2026, 494 hội thoại

| Dịch vụ KF-62 | HT | Chưa rõ | % | KF-64 nói |
|---|---|---|---|---|
| Tiêm filler & botox | 176 | 105 | **59,7%** | ★ ƯU TIÊN A2 |
| Điều trị nám & sắc tố | 139 | 57 | **41,0%** | ★ ƯU TIÊN A2 |
| Trẻ hoá & nâng cơ | 35 | 27 | **77,1%** | ★ ƯU TIÊN A2 |
| Điều trị sẹo | 31 | 23 | **74,2%** | ★ ƯU TIÊN A2 |
| Thẩm mỹ hàm mặt | 4 | 3 | 75,0% | ★ ƯU TIÊN A2 *(mẫu nhỏ)* |
| Nâng ngực · Cắt mí · Mũi · Hút mỡ | 7 | 7 | 100% | ★ *(mẫu quá nhỏ)* |
| `KHONG_XAC_DINH_DV` | 102 | 102 | — | ⛔ không phải dịch vụ |
| **TOÀN KỲ** | **494** | **324** | **65,6%** | |

★ **9/10 dịch vụ vượt ngưỡng, 6/10 vượt 70%.** Nên kết luận của KF-64 cho kỳ này
là một câu duy nhất: **làm `A2` trước, ở gần như mọi dịch vụ.**

★ **Con số 65,6% không mới** — nó đúng bằng tỷ lệ `id-M` §5 ghi là **cổng ① của
KF-62 chưa đạt** (yêu cầu 70% xếp được chân dung). Hai sổ, hai cách đo độc lập,
cùng một con số: khách gõ **tên dịch vụ rồi hỏi giá** (trung vị 44 ký tự), ⛔ chứ
không tả tình trạng.

⚠ Và đó là chỗ hai sổ đọc cùng một số theo **hai nghĩa trái nhau**:

```
id-M §5  →  65,6% là THƯ VIỆN ĐANG HỤT   → việc: bổ sung từ nhận dạng
id-N §4  →  65,6% là PHỄU ĐANG RÒ Ở A2   → việc: làm nội dung tự phân loại
```

★ **Cả hai đều đúng, và ⛔ không thay nhau được.** Thư viện có thêm từ thì xếp
được nhiều hơn một ít; nhưng khách **không viết** tình trạng thì không từ nào
đọc ra được. Việc thật nằm ở `A2`: làm khách **nói ra** trước đã.

---

## 5. NĂM BƯỚC CHUYỂN TẦNG — ⛔ CHỈ ĐO ĐƯỢC BA

Mỗi tỷ lệ so với **TB dịch vụ** (⛔ không tính `CHUA_XAC_DINH`) → ra chỉ số tương đối.

| # | Bước | Tỷ lệ | Yếu nhất → tầng ưu tiên | Đo được? |
|---|---|---|---|---|
| `S1` | Quy mô | chỉ số Quy mô | **A1 · TOF** — mở tệp | ✅ |
| 🔴 `S2` | — | — | — | ⛔ **văn bản KF-64 không có** |
| `S3` | Tương tác | `(Warm+Hot) ÷ HT` | **A3 · MOF** — gỡ rào cản chính | ✅ |
| `S4` | Nóng lên | `Hot ÷ (Warm+Hot)` | **A3 · MOF** — bác sĩ, ca thật, so sánh | ⚠ xem dưới |
| `S5` | Hot → booking | `Booking ÷ Hot` | **A4 · BOF** + cờ Vận hành/Sale | ⛔ chưa có CRM |
| `S6` | Booking → đến khám | `Đến khám ÷ Booking` | **A4 · BOF** + cờ Vận hành | ⛔ chưa có CRM |

🔴 **Bảng của KF-64 đánh số `S1 · S3 · S4 · S5 · S6` — thiếu `S2`.** Đọc §4.2 thì
`S2` gần như chắc là *"nói rõ nhu cầu"*, nhưng nó được mô tả ở **cấp dịch vụ**
nên không có dòng trong bảng cấp chân dung. ★ Phải hỏi lại khối Sale: `S2` là
bước bị bỏ quên, hay cố ý để ở cấp dịch vụ?

### Quy tắc chọn

```
① Tầng ưu tiên = bước có chỉ số tương đối THẤP NHẤT và < 0,8
② Không bước nào < 0,8 → giữ cơ cấu theo ô ma trận, A/B ở tầng đang chi lớn nhất
③ Yếu nhất là S5 hoặc S6 → gắn cờ "VẬN HÀNH/SALE": lỗi tốc độ gọi, kịch bản,
  giá, nhắc lịch — ⛔ KHÔNG phải lỗi nội dung. Sửa vận hành trước, làm BOF sau.
④ Tầng ưu tiên quyết định NỘI DUNG SẢN XUẤT TRƯỚC.
  Ô ma trận quyết định CƠ CẤU NGÂN SÁCH.
  Phễu của tầng ưu tiên +10 điểm %, trừ đều theo tỷ lệ từ hai phễu còn lại.
```

★ Luật ③ là **cùng một luật** với ô `🔧 sửa vận hành` của `id-G`, và với ô ③ của
bảng giao `id-D` §6: *sửa câu trả lời trước, làm nội dung sau.* Ba sổ nói cùng
một câu — đó là dấu hiệu luật này đúng, ⛔ không phải dấu hiệu trùng lặp.

### ⚠ `S4` gần như vô dụng trên tệp này

```
Cả kỳ 24–29/10 có ĐÚNG 3 hội thoại HOT trên 494  (0,6%).
6/10 dịch vụ có %Hot = 0 → mẫu số của S4 bằng 0 cho cả dịch vụ.
```

⚠ Chỗ này KF-64 §3.1 còn **nhập nhằng và nó đổi kết luận**. Văn bản ghi *"trung
bình hai chỉ số… chưa có nhiệt độ thì dùng % Hot"* — nhưng ở đây **ngược lại**:
có nhiệt độ, ⛔ không có HOT. Hai cách đọc cho hai hạng khác nhau:

| Mã | Đọc theo đúng chữ *(lấy TB hai chỉ số, %Hot tính là 0)* | Bỏ `%Hot` khi dịch vụ không có HOT |
|---|---|---|
| `FILLER-LAM_DAY_LAN_DAU` | Chất lượng 0,50 → **TẠM 76** · THẤP | Chất lượng 1,00 → **TẠM 106** · TRUNG BÌNH |
| `FILLER-BOTOX_LAN_DAU` | Chất lượng 0,50 → **TẠM 64** · THẤP | Chất lượng 1,00 → **TẠM 94** · TRUNG BÌNH |

★ **Một dòng chữ không rõ làm lệch hạng tới 30 điểm** và đổi cả nhãn CAO/TB/THẤP.
⛔ Repo không tự chọn. Phải hỏi: khi `%Hot` của **cả dịch vụ** bằng 0 thì bỏ chỉ
số đó, hay vẫn tính là 0?

---

## 6. ★ KẾT QUẢ ĐO — CHỈ SỐ TẠM, KỲ 24–29/10/2026

> Gom theo **trục dịch vụ KF-62** (18 dịch vụ), ⛔ không theo cột `dich_vu` —
> xem §7 về vì sao.

| Dịch vụ | Mã | HT | Quy mô | Nhiệt TB | TẠM | Cỡ mẫu |
|---|---|---|---|---|---|---|
| Nám & sắc tố | `SACTO-NAM_LAN_DAU` | 77 | 2,00 | 17,7 | **141,2** | ✅ |
| Filler & botox | `FILLER-LAM_DAY_LAN_DAU` | 41 | 1,15 | 11,8 | **106,3** | ✅ |
| Filler & botox | `FILLER-BOTOX_LAN_DAU` | 30 | 0,85 | 11,8 | **93,7** | ✅ |
| Trẻ hoá & nâng cơ | `TREHOA-NANG_CO_KHONG_PT` | 6 | 1,50 | 16,0 | 129,8 | ⛔ <30 |
| Điều trị sẹo | `SEO-LOI` | 3 | 1,50 | 23,5 | 134,1 | ⛔ <30 |
| Điều trị sẹo | `SEO-THAM` | 3 | 1,50 | 17,3 | 114,3 | ⛔ <30 |
| Nám & sắc tố | `SACTO-NAM_TAI_PHAT` | 1 | 0,05 | 35,7 | 61,1 | ⛔ <30 |
| *(6 mã còn lại)* | | 1–3 | | | 40–101 | ⛔ <30 |

```
Mã có khách trong kỳ               13 / 85
Mã đạt ngưỡng 30 HT                 3 / 85   ← chỉ số TẠM dùng được
Mã đạt ngưỡng chính thức            0 / 85   ← cần thêm ≥5 booking CRM
Dịch vụ ⛔ không xếp được mã nào     4 / 10   (Ngực · Mắt · Mũi · Hút mỡ)
```

⚠ **KF-64 ở cấp chân dung gần như bất động trên một kỳ 6 ngày.** Nó đòi cửa sổ
**30 ngày** — và §7 của chính nó đã nói cách chữa: gộp 2 tháng, hoặc **chỉ đánh
giá ở cấp dịch vụ**. ★ Vậy phần dùng được ngay của KF-64 là §4 (luật `A2` cấp
dịch vụ), ⛔ không phải §3 (xếp hạng chân dung).

★ `SACTO-NAM_TAI_PHAT` lại đáng để ý: **nhiệt TB 35,7 — cao nhất mọi mã**, mà chỉ
**1 hội thoại**. Chân dung KF-62 kỳ vọng nhiều nhất gần như không xuất hiện. Một
HT thì ⛔ không kết luận được gì, nhưng là chỗ đáng theo dõi kỳ sau.

---

## 7. 🔴 "TRUNG BÌNH DỊCH VỤ" LÀ DỊCH VỤ NÀO — CÂU HỎI CHẶN

Mọi chỉ số của KF-64 đều là *"so với trung bình **dịch vụ**"*. Nhưng hệ đang có
**hai cách chia dịch vụ**, và chúng ⛔ không trùng nhau:

| Trục | Ở đâu | Dùng để | Số nhóm |
|---|---|---|---|
| cột `dich_vu` | `id-G` §3 · `gan_dich_vu()` | lấy **hệ số giá trị đơn 1/2/3** | 11 nhóm trong kỳ |
| tiền tố mã KF-62 | `tools/chan_dung_kf62.json` | **chân dung nằm trong dịch vụ nào** | 18 dịch vụ |

```
392 / 494 hội thoại có tiền tố mã KHÁC tên ở cột dich_vu. Ví dụ:

  KF-62 «Tiêm filler & botox»     gộp  id-G «Trẻ hóa — Làm đầy» + «Trẻ hóa — Botox»
  KF-62 «Điều trị nám & sắc tố»   gộp  id-G «Nám & sắc tố» + «Tàn nhang»
```

⚠ **Mẫu số khác thì mọi chỉ số khác.** Ví dụ thật: `FILLER-BOTOX_LAN_DAU` có
Quy mô **1,87** nếu chia theo `dich_vu` (*Botox*, 53 HT) nhưng **0,85** nếu chia
theo tiền tố KF-62 (*Filler & botox*, 176 HT) — vượt mốc "lớn" ở cách thứ nhất,
⛔ không vượt ở cách thứ hai. Đổi mẫu số là đổi ô ma trận.

★ **Sổ này dùng tiền tố KF-62**, vì chân dung được **định nghĩa bên trong** dịch
vụ đó (`id-M` §2) và `id-M` §7 đã so theo trục ấy. ⛔ Nhưng phải hỏi lại khối
Sale để chốt, vì đây là mẫu số của mọi con số trong KF-64.

⚠ Cột `dich_vu` thì ⛔ **không bỏ được** — nó vẫn là chỗ lấy hệ số 1/2/3.

---

## 8. BRIEF NỘI DUNG

```
Brief = CHÂN DUNG × TẦNG ƯU TIÊN × RÀO CẢN CHÍNH
```

| Thành phần | Lấy ở đâu |
|---|---|
| Chân dung | `id-M` §9 — mã thư viện + tên |
| Tầng ưu tiên | §5 sổ này — bước yếu nhất < 0,8 |
| Rào cản chính | `id-D` §5 (rào cản) · `id-D` §1 (mã `O`) |
| Hook · format · CTA | `id-M` §9 cột hành động · `id-H` (7 loại × 16 format) |
| Thông điệp | `id-M` §8 — ⛔ phải qua trạng thái duyệt |

⛔ **Mọi thông điệp ra ngoài vẫn qua `id-K` và CỔNG 2.** KF-64 ⛔ không nói gì về
pháp chế, nên ⛔ không được hiểu là nó miễn trừ: *ưu đãi có hạn* của tầng `A4`
và *so sánh phương án* của `A3` đều là chỗ `id-K` §3 đang chặn.

⚠ Hai ví dụ trong Driver KF-64 (`MUI-NANG_LAN_DAU`, `MUI-FILLER_SANG_PT`) là **số
giả lập**, chính văn bản ghi vậy. ⛔ Không trích như kết quả đo.

---

## 9. ĐIỀU KIỆN ĐỂ KF-64 CHẠY ĐƯỢC

| # | Điều kiện | Trạng thái 02/11 |
|---|---|---|
| ① | **Mã chân dung trong CRM** — thêm trường vào Caresoft | ⛔ chưa có → trục Chuyển đổi 50% trống |
| ② | Cửa sổ **30 ngày**, ≥30 HT/chân dung | ⛔ kỳ đang chạy 6 ngày → 3/85 mã đạt |
| ③ | Chốt **mẫu số "dịch vụ"** (§7) | 🔴 chưa chốt |
| ④ | Chốt cách xử lý `%Hot = 0` (§5) | 🔴 chưa chốt — lệch tới 30 điểm |
| ⑤ | Chốt bản dự phòng cho **điểm hiệu quả** (§2) | 🔴 chưa chốt → ma trận không vẽ được |
| ⑥ | Chốt xung đột tên `A2` với `id-D` §3 (§3) | 🔴 chưa chốt |
| ⑦ | Chi phí QC tách theo chân dung | ⛔ chưa có — KF-64 §7 nói vẫn chạy được, chỉ thiếu CPL/CPB |

★ ①②⑦ là **chờ dữ liệu**. ③④⑤⑥ là **chờ người chốt** — và cả bốn đều đổi kết
luận, ⛔ không phải chi tiết kỹ thuật.

⚠ **Baseline T10 của NV đo theo cách riêng, ⛔ không chuẩn KF-60.** Tab 3 của
Driver để làm ví dụ. ⛔ Không ra quyết định từ số đó.

---

## 10. CHƯA CHẠY Ở ĐÂU

| Thứ | Trạng thái |
|---|---|
| `tools/id.py` | ⛔ **chưa cài** — sổ này còn chờ duyệt |
| Khối trong file kỳ | ⛔ chưa có |
| Tab dashboard | ⛔ chưa có |
| Đo tay kỳ 24–29/10 | ✅ §4 và §6 — số trong sổ này |

★ Cố ý chưa cài. Cài một bộ xếp hạng thứ hai khi `id-M` §7 đang là bản duyệt thì
lặp lại đúng lỗi của `id-C` §4.

---

## 11. TỰ KIỂM SỔ NÀY

- [ ] Có ai dùng công thức `20/30/50` để ra quyết định thật chưa? ⛔ Chưa duyệt.
- [ ] Bảng xếp hạng chân dung đang lấy từ `id-M` §7, ⛔ không phải sổ này?
- [ ] Mọi dòng chỉ số tạm có gắn chữ **TẠM** không?
- [ ] Chân dung < 30 HT có bị xếp hạng không? ⛔ Phải ghi «chưa đủ dữ liệu».
- [ ] `<DV>-CHUA_XAC_DINH` và `KHONG_XAC_DINH_DV` có bị tính vào **TB dịch vụ** không? ⛔ Không được.
- [ ] Mẫu số "dịch vụ" dùng tiền tố KF-62 hay cột `dich_vu` — đã ghi rõ chưa? (§7)
- [ ] Nhãn `A2` trong một bảng là `A2` của ai — `id-D` §3 hay KF-64 §4.1? (§3)
- [ ] Bước yếu nhất là `S5`/`S6` → đã gắn cờ **Vận hành/Sale** chưa, hay lại đi làm nội dung BOF?
- [ ] Sáu câu hỏi ở §9 đã gửi khối Sale chưa?

---

### Nhật ký duyệt

| Khi nào | Ai | Duyệt gì |
|---|---|---|
| — | — | 🔴 **Chưa có dòng nào.** KF-64 v1.0 là bản đề xuất 02/11/2026. |

### ⚠ Việc còn phải làm

| # | Việc | Ai |
|---|---|---|
| ① | Trả lời bốn câu chốt ③④⑤⑥ của §9 — cả bốn đổi kết luận | khối Sale |
| ② | Thêm trường **mã chân dung KF-62** vào Caresoft | Sale Admin |
| ③ | Khi duyệt: `id-M` §7 **bị thay**, ⛔ không chạy song song | QL Sale + repo |
| ④ | Gửi lại số §4: **9/10 dịch vụ vượt ngưỡng `A2`** — đây là kết luận dùng được ngay, ⛔ không chờ CRM | MKT Lead |

---

### Liên quan

`id-M` §7 (xếp hạng chân dung — **bản đang chạy**) · §2 (dịch vụ → chân dung) ·
§5 (cổng ①) · §8 (thông điệp) · `id-D` §3 (nấc `5A` — ⚠ xung đột tên `A2`) ·
§1 (mã `O`) · §5 (rào cản) · §6 (bảng giao bốn ô) · `id-L` (nhiệt độ · nhóm gọi) ·
`id-G` §3 (hệ số 1/2/3) · `id-H` (hook · format) · `id-K` §3 (pháp chế đang chặn) ·
KF-57/KF-50 (định nghĩa tầng · ràng buộc ngân sách) · KF-49 (scale `+15–20%/3 ngày`) ·
KF-61/62 (tương quan 40:60 gốc) · KF-21/34 (CDP · nhắc lịch D02)
