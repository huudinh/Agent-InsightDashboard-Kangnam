# id-N · ★ CHỌN TỆP TẬP TRUNG & TẦNG NỘI DUNG — BỘ KF-64 v1.0

> Sổ **nhập từ ngoài**, như `id-L` và `id-M`: đây là văn bản KF-64 của khối Sale.
> ⛔ Repo không tự đặt thêm trục, trọng số hay ngưỡng nào.
>
> ★ **ĐANG CHẠY từ 02/11/2026.** Người dùng chốt **bỏ bước chờ anh UY duyệt**.
> Sổ này **thay** công thức xếp hạng chân dung của
> [`id-M` §7](id-M-thu-vien-chan-dung-kf62.md) — ⛔ không chạy song song.
>
> ⚠ **Bỏ duyệt ⛔ không trả lời được bốn chỗ KF-64 v1.0 để trống.** Repo đã tự
> chốt cả bốn, ghi ở **§2** — đọc chỗ đó trước khi dùng bất kỳ con số nào.

**Sổ này trả lời:** trong một dịch vụ thì **dồn lực vào chân dung nào**, và với
chân dung đó thì **làm nội dung tầng nào trước**.

### Ranh giới — ⛔ bốn sổ, bốn quyết định khác nhau

```
id-L     → GỌI AI TRƯỚC      · một HỘI THOẠI   · điểm × hệ số giá trị đơn
id-M §7  → ⛔ ĐÃ NGHỈ 02/11/2026 — thay bằng id-N
id-N     → DỒN SỨC VÀO AI + TẦNG NÀO · một CHÂN DUNG · ★ ĐANG CHẠY
id-G §3  → HỆ SỐ 1 · 2 · 3   · thành phần dùng chung
```

⚠ `id-M` §7 và `id-N` trả lời **cùng một câu hỏi**. Đó đúng là tình huống đã
làm hỏng `id-C` §4 (hai công thức cho một quyết định thì chắc chắn lệch nhau).
★ Nên khi bật `id-N`, bảng **«Cơ hội win» của `id-M` §7 đã bị gỡ khỏi dashboard**
và bản proxy lưu ở `_luu_co_hoi_win_idM7` của lớp phủ. ⛔ Một bảng, không hai.

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
| Trạng thái | ⛔ **đã nghỉ 02/11/2026** | ★ **đang chạy** |
| Cỡ mẫu | ≥30 HT **và** ≥5 booking | **y nguyên** |
| Gốc so sánh | TB **dịch vụ**; dịch vụ so TB hệ thống | **y nguyên** |

★ Nên đọc như vậy: **30:50 với 40:60 là cùng một tỷ lệ**, KF-64 chỉ chen thêm
trục Quy mô 20% vào trước. Và §6 của KF-64 tự đặt đúng câu hỏi đó thành A/B
test ①: `20/30/50` so với `0/40/60`, đo CPB sau 30 ngày.

⚠ Vì vậy ⛔ **đừng chạy hai bộ.** `id-N` **đã thay** `id-M` §7 từ 02/11/2026.

---

## 2. 🔴 BỐN CHỖ KF-64 v1.0 ĐỂ TRỐNG — REPO TỰ CHỐT

> Người dùng bỏ bước chờ duyệt, nhưng **bỏ duyệt ⛔ không trả lời được bốn câu
> này** — mà cả bốn đều **đổi kết quả**. Chốt ở đây để còn cãi lại được,
> ⛔ không chôn trong code. Mã: `tools/id.py` → `gom_kf64()`.

### ① Mẫu số «trung bình dịch vụ» = **tiền tố mã KF-62**

```
Chọn  : 18 dịch vụ của thư viện KF-62   (FILLER · SACTO · SEO · TREHOA …)
⛔ Bỏ : 11 nhóm của cột `dich_vu`        (id-G §3 — chỗ lấy hệ số 1/2/3)
```

**Vì sao:** chân dung được **định nghĩa bên trong** dịch vụ KF-62 (`id-M` §2).
Lấy mẫu số kia thì một chân dung bị so với những chân dung ⛔ không cùng dịch vụ.

**Đổi mẫu số là đổi kết luận** — số thật của kỳ 24–29/10:

| | theo cột `dich_vu` | theo tiền tố KF-62 |
|---|---|---|
| `FILLER-BOTOX_LAN_DAU` Quy mô | **1,87** → «lớn» | **0,85** → ⛔ không «lớn» |

★ Cột `dich_vu` ⛔ **không bỏ** — nó vẫn là chỗ lấy hệ số giá trị đơn.

### ② `%Hot` của cả dịch vụ bằng 0 → **bỏ chỉ số đó**

```
Chất lượng = trung bình các chỉ số ĐO ĐƯỢC, ⛔ không tính %Hot thành 0.
Mẫu số bằng 0 thì tỷ lệ là KHÔNG XÁC ĐỊNH — ⛔ không phải bằng không.
```

Kỳ này có **3 HOT trên 494**, nên 4/6 dịch vụ có chân dung rơi vào đúng cảnh đó.
Tính `%Hot` thành 0 là **chia đôi Chất lượng của mọi chân dung** trong dịch vụ:

| Mã | đọc theo đúng chữ KF-64 | chốt như trên |
|---|---|---|
| `FILLER-LAM_DAY_LAN_DAU` | **76** · THẤP | **106,3** · TRUNG BÌNH |
| `FILLER-BOTOX_LAN_DAU` | **64** · THẤP | **93,7** · TRUNG BÌNH |

### ③ `điểm hiệu quả` — chuẩn hoá lại trên trục đo được

KF-64 cho bản dự phòng cho *Chỉ số tập trung* (`0,4/0,6`) nhưng ⛔ **không cho**
*điểm hiệu quả*, mà Chuyển đổi chiếm **62,5%** của nó. Làm đúng cách KF-64 đã
làm ở chỗ kia: chuẩn hoá lại trên trục đo được → **hiệu quả = Chất lượng**.

⚠ **Hệ quả phải nói ra:** ô ③ lúc này đọc là *«đông nhưng **NGUỘI**»*, ⛔ chưa
phải *«đông nhưng **YẾU**»*. Hai chẩn đoán khác nhau dẫn tới hai việc khác nhau.
Mọi dòng gắn `tam = true`.

⛔ **Và ô ma trận kỳ này VẪN chưa chốt được** — xem §6.

### ④ Tên tầng: `T1…T4`, giữ nguyên `5A` của `id-D`

```
Cùng 494 hội thoại:  A2 theo id-D §3 =   1 HT
                     A2 theo KF-64    = 324 HT
⛔ Một nhãn hai nghĩa thì không bảng nào đọc được.
```

| KF-64 | Phễu | Quy đổi sang `id-D` §3 |
|---|---|---|
| `T1` | TOF | `A1` |
| `T2` | TOF→MOF | ⚠ **đo ở cấp dịch vụ**, ⛔ không có ở cấp hội thoại |
| `T3` | MOF | `A2` + `A3` |
| `T4` | BOF | `A4` |

★ Nấc `5A` của `id-D` ⛔ **không đổi** — tab Phễu và mốc so sánh giữa các kỳ giữ nguyên.

### Chỉ số tạm khi chưa có CRM

```
Chỉ số tạm = 100 × (0,4 × Quy mô + 0,6 × Chất lượng)      ← ghi rõ "TẠM"
⛔ Chỉ dùng để chọn nhóm LÀM THỬ, ⛔ không để dồn ngân sách lớn.
```

★ Cái này **chạy được ngay** trên dữ liệu đang có, và tốt hơn bản proxy của
`id-M` §7 ở một điểm: nó ⛔ không dùng `% có SĐT` làm thế thân cho booking.

---

## 3. MA TRẬN QUY MÔ × HIỆU QUẢ — ⚠ VẼ ĐƯỢC NHƯNG ⛔ CHƯA CHỐT ĐƯỢC

```
Quy mô "lớn"   : chỉ số Quy mô ≥ 1,0 (từ mức chia đều trở lên)
Hiệu quả "tốt" : điểm hiệu quả ≥ 100
                 điểm hiệu quả = 100 × (0,375 × Chất lượng + 0,625 × Chuyển đổi)
```

| Ô | Điều kiện | Chiến lược | TOF / MOF / BOF |
|---|---|---|---|
| **① Trụ cột** | Lớn + Tốt | Scale có kiểm soát `+15–20%/3 ngày` (KF-49), giữ chất lượng | 30 / 40 / 30 |
| **② Ngách hiệu quả** | Nhỏ + Tốt | Mở rộng tệp: tăng TOF/`T2` kéo thêm **đúng** người | 45 / 35 / 20 |
| **③ Đông nhưng yếu** | Lớn + Chưa tốt | ⛔ **Không tăng ngân sách kéo khách.** Sửa MOF, kịch bản, tốc độ Sale | 15 / 55 / 30 |
| **④ Duy trì tối thiểu** | Nhỏ + Chưa tốt | Giữ remarketing + nội dung nền, xem lại sau 30 ngày | 20 / 40 / 40 |

Ràng buộc KF-50: **BOF ≥ 10%** và **remarketing ≤ 40%** tổng chi của dịch vụ.
Thứ tự dồn lực xếp theo Chỉ số tập trung, nhưng **mỗi dịch vụ giữ ít nhất một
chân dung ở ô ②** để không bỏ lỡ nhóm đang lên.

### ⛔ VÌ SAO KỲ NÀY VẪN CHƯA CHỐT ĐƯỢC Ô NÀO

Theo §2 ③ thì `hiệu quả` chuẩn hoá lại còn **một trục: Chất lượng**. Vẽ được —
nhưng đo ra thì **cả 3/3 chân dung được xếp hạng đều nằm sát mốc 100**:

| Mã | Quy mô | Hiệu quả | Ô | Lệch mốc |
|---|---|---|---|---|
| `SACTO-NAM_LAN_DAU` | 2,00 | **102,1** | ① Trụ cột | **+2,1** |
| `FILLER-LAM_DAY_LAN_DAU` | 1,15 | **100,2** | ① Trụ cột | **+0,2** |
| `FILLER-BOTOX_LAN_DAU` | 0,85 | **99,8** | ④ Duy trì tối thiểu | **−0,2** |

★ **Lệch 0,2 điểm là đổi chiến lược hẳn:** ô ① bảo *scale +15–20%/3 ngày*, ô ④
bảo *duy trì tối thiểu, ngân sách thấp*. ⛔ Không ai ra quyết định ngân sách
trên một con số lung lay 0,2 điểm.

⚠ **Và đây ⛔ không phải lỗi của mốc 100.** Nó là hệ quả số học: `hiệu quả` chỉ
còn Chất lượng, mà Chất lượng của mỗi chân dung **so với trung bình của chính
dịch vụ mình**. Dịch vụ `FILLER` có 2 chân dung → hai tỷ lệ của chúng **buộc
phải kẹp quanh 1,0**. Thêm chân dung cũng không chữa được: chỉ **trục Chuyển
đổi** mới kéo các chỉ số ra xa nhau.

```
⛔ ĐỪNG dùng ô ma trận để chia ngân sách trước khi CRM gắn mã chân dung (§10 ①).
★  Báo cáo tự bật cờ: mọi dòng |hiệu quả − 100| < 5 gắn `o_sat_moc`, và kỳ nào
   có dòng như vậy thì `canh_bao` mọc một dòng đỏ — ⛔ không im lặng.
```

---

## 4. NĂM TẦNG × PHỄU — ✅ ĐÃ ĐỔI TÊN THÀNH `T1…T4`

> ✅ **Đã chốt ở §2 ④:** trục phễu của KF-64 mang tên `T1…T4`; nấc `5A` của
> `id-D` §3 ⛔ không đổi. Bảng dưới giữ nguyên văn KF-64 để đối chiếu.

| Tầng KF-64 | Phễu | KF-64 nói khách đang ở đâu | `id-D` §3 nói gì ở nhãn trùng tên |
|---|---|---|---|
| **`T1`** *(A1 của KF-64)* | TOF | Chưa biết vấn đề có giải pháp, hoặc chưa biết Kangnam | `A1` — có vấn đề nhưng **chưa gọi tên** |
| **`T2`** *(A2 của KF-64)* | TOF→MOF | **Có nhắn tin nhưng chưa nói rõ nhu cầu** | `A2` — **đang so phương pháp** ⛔ khác hẳn |
| **`T3`** *(A3 của KF-64)* | MOF | Đã nói nhu cầu, **đang so sánh**, có rào cản | `A2` + `A3` gộp lại |
| **`T4`** *(A4 của KF-64)* | BOF | Nóng nhưng chưa chốt lịch, chưa đến | `A4` — đã inbox/đặt lịch |
| — | sau dịch vụ | Đã làm — CDP, ⛔ không phải ads kéo khách | `A5` — đã làm, lo hậu phẫu |

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

✅ **Đã chọn ⓐ.** Lý do: `5A` của `id-D` đọc từ **câu hỏi đầu tiên**, một hội
thoại một nấc, truy ngược được. `T2` của KF-64 ⛔ không đọc được ở cấp hội thoại
— chính KF-64 §4.2 nói nó phải đo ở **cấp dịch vụ**. Hai thứ ở hai cấp khác nhau
thì ⛔ không được trùng tên.

⚠ Đây là quyết định của **repo**, ⛔ không phải của khối Sale — báo lại để họ
xác nhận hoặc đổi (§10 việc ①).

---

## 5. LUẬT `T2` CẤP DỊCH VỤ — ★ ĐANG CHẠY, VIỆC DÙNG ĐƯỢC NGAY

> KF-64 §4.2: tỷ lệ hội thoại **chưa rõ nhu cầu** ≥ **30%** → dịch vụ đó ưu tiên
> **`T2` (TOF→MOF)**: nội dung tự phân loại *"bạn thuộc kiểu nào"*, hook đúng chân
> dung, đưa **câu hỏi vàng** lên ads.

★ Luật này nối thẳng vào hai mã dự trữ của `id-M`: `<DV>-CHUA_XAC_DINH` và
`KHONG_XAC_DINH_DV` **chính là** tử số của nó. Nhờ vậy nó ⛔ không cần CRM, ⛔
không cần booking, và đo được từ kỳ đầu tiên.

### Kết quả đo — kỳ 24–29/10/2026, 494 hội thoại

| Dịch vụ KF-62 | HT | Chưa rõ | % | KF-64 nói |
|---|---|---|---|---|
| Tiêm filler & botox | 176 | 105 | **59,7%** | ★ ƯU TIÊN `T2` |
| Điều trị nám & sắc tố | 139 | 57 | **41,0%** | ★ ƯU TIÊN `T2` |
| Trẻ hoá & nâng cơ | 35 | 27 | **77,1%** | ★ ƯU TIÊN `T2` |
| Điều trị sẹo | 31 | 23 | **74,2%** | ★ ƯU TIÊN `T2` |
| Thẩm mỹ hàm mặt | 4 | 3 | 75,0% | ★ ƯU TIÊN `T2` *(mẫu nhỏ)* |
| Nâng ngực · Cắt mí · Mũi · Hút mỡ | 7 | 7 | 100% | ★ *(mẫu quá nhỏ)* |
| `KHONG_XAC_DINH_DV` | 102 | 102 | — | ⛔ không phải dịch vụ |
| **TOÀN KỲ** | **494** | **324** | **65,6%** | |

★ **9/10 dịch vụ vượt ngưỡng, 6/10 vượt 70%.** Nên kết luận của KF-64 cho kỳ này
là một câu duy nhất: **làm `T2` trước, ở gần như mọi dịch vụ.**

★ **Con số 65,6% không mới** — nó đúng bằng tỷ lệ `id-M` §5 ghi là **cổng ① của
KF-62 chưa đạt** (yêu cầu 70% xếp được chân dung). Hai sổ, hai cách đo độc lập,
cùng một con số: khách gõ **tên dịch vụ rồi hỏi giá** (trung vị 44 ký tự), ⛔ chứ
không tả tình trạng.

⚠ Và đó là chỗ hai sổ đọc cùng một số theo **hai nghĩa trái nhau**:

```
id-M §5  →  65,6% là THƯ VIỆN ĐANG HỤT   → việc: bổ sung từ nhận dạng
id-N §5  →  65,6% là PHỄU ĐANG RÒ Ở T2   → việc: làm nội dung tự phân loại
```

★ **Cả hai đều đúng, và ⛔ không thay nhau được.** Thư viện có thêm từ thì xếp
được nhiều hơn một ít; nhưng khách **không viết** tình trạng thì không từ nào
đọc ra được. Việc thật nằm ở `T2`: làm khách **nói ra** trước đã.

---

## 6. NĂM BƯỚC CHUYỂN TẦNG — ⛔ CHỈ ĐO ĐƯỢC BA

Mỗi tỷ lệ so với **TB dịch vụ** (⛔ không tính `CHUA_XAC_DINH`) → ra chỉ số tương đối.

| # | Bước | Tỷ lệ | Yếu nhất → tầng ưu tiên | Đo được? |
|---|---|---|---|---|
| `S1` | Quy mô | chỉ số Quy mô | **`T1` · TOF** — mở tệp | ✅ |
| 🔴 `S2` | — | — | — | ⛔ **văn bản KF-64 không có** |
| `S3` | Tương tác | `(Warm+Hot) ÷ HT` | **`T3` · MOF** — gỡ rào cản chính | ✅ |
| `S4` | Nóng lên | `Hot ÷ (Warm+Hot)` | **`T3` · MOF** — bác sĩ, ca thật, so sánh | ⚠ xem dưới |
| `S5` | Hot → booking | `Booking ÷ Hot` | **`T4` · BOF** + cờ Vận hành/Sale | ⛔ chưa có CRM |
| `S6` | Booking → đến khám | `Đến khám ÷ Booking` | **`T4` · BOF** + cờ Vận hành | ⛔ chưa có CRM |

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

### ⚠ Kỳ 24–29/10: ⛔ KHÔNG chân dung nào ra được tầng ưu tiên

```
Không bước nào tụt dưới 0,8 so với trung bình dịch vụ → theo luật ② thì
«giữ cơ cấu theo ô ma trận». Nhưng ⛔ ĐỪNG đọc thành «phễu không nghẽn»:
hai bước hay nghẽn nhất — S5 (Hot→booking) và S6 (booking→đến khám) —
⛔ CHƯA ĐO ĐƯỢC vì thiếu CRM. Ba bước còn lại đều nằm TRƯỚC chỗ nghẽn.
```

★ Vì vậy cờ **«Vận hành/Sale»** của luật ③ **chưa bao giờ bật được** — mà theo
`id-D` §6 và `id-G` thì đó chính là ô đang chứa nhiều việc nhất của kỳ này
(217/494 HT rơi do trực page). ⛔ KF-64 ở cấp chân dung **chưa nhìn thấy** phần
đó. Báo cáo tự bật một dòng `canh_bao` nói đúng điều này.

★ Nên việc dùng được của KF-64 kỳ này vẫn là **§5 — luật `T2` cấp dịch vụ**.

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

## 7. ★ KẾT QUẢ ĐO — CHỈ SỐ TẠM, KỲ 24–29/10/2026 *(máy sinh)*

> Gom theo **trục dịch vụ KF-62** (18 dịch vụ), ⛔ không theo cột `dich_vu` —
> xem §2 ① về vì sao. ★ Từ 02/11/2026 bảng này **máy sinh** vào khối `kf64` của
> file kỳ, ⛔ không còn chép tay vào sổ.

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

## 8. ✅ "TRUNG BÌNH DỊCH VỤ" — ĐÃ CHỐT LÀ TIỀN TỐ KF-62

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

✅ **Đã chốt: dùng tiền tố KF-62** (§2 ①), vì chân dung được **định nghĩa bên
trong** dịch vụ đó (`id-M` §2). Cài ở `_kf64_dv()` của `tools/id.py`.

⚠ Đây là quyết định của **repo**, ⛔ không phải của khối Sale — và nó là mẫu số
của **mọi** con số trong KF-64. Báo lại để xác nhận (§10 việc ①).

⚠ Cột `dich_vu` thì ⛔ **không bỏ được** — nó vẫn là chỗ lấy hệ số 1/2/3.

---

## 9. BRIEF NỘI DUNG

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

## 10. ĐIỀU KIỆN ĐỂ KF-64 CHẠY ĐƯỢC

| # | Điều kiện | Trạng thái 02/11 |
|---|---|---|
| ① | **Mã chân dung trong CRM** — thêm trường vào Caresoft | ⛔ chưa có → trục Chuyển đổi 50% trống |
| ② | Cửa sổ **30 ngày**, ≥30 HT/chân dung | ⛔ kỳ đang chạy 6 ngày → 3/85 mã đạt |
| ③ | Chốt **mẫu số "dịch vụ"** | ✅ §2 ① — tiền tố KF-62 |
| ④ | Chốt cách xử lý `%Hot = 0` | ✅ §2 ② — bỏ chỉ số đó |
| ⑤ | Chốt bản dự phòng cho **điểm hiệu quả** | ✅ §2 ③ — nhưng ⛔ ô vẫn chưa chốt được, xem §6 |
| ⑥ | Chốt xung đột tên `A2` với `id-D` §3 | ✅ §2 ④ — trục KF-64 đổi thành `T1…T4` |
| ⑦ | Chi phí QC tách theo chân dung | ⛔ chưa có — KF-64 §7 nói vẫn chạy được, chỉ thiếu CPL/CPB |

★ ③④⑤⑥ đã chốt ở **§2**. ①②⑦ vẫn là **chờ dữ liệu** — ⛔ không ai chốt thay
được, phải có CRM và phải có 30 ngày.

⚠ **Baseline T10 của NV đo theo cách riêng, ⛔ không chuẩn KF-60.** Tab 3 của
Driver để làm ví dụ. ⛔ Không ra quyết định từ số đó.

---

## 11. CHẠY Ở ĐÂU

| Thứ | Chỗ |
|---|---|
| Bộ chấm | `tools/id.py` → `gom_kf64()` · `_kf64_dv()` · `_kf64_ti()` |
| Hằng số | `KF64_TS` · `KF64_TS_TAM` · `KF64_TRAN` · `KF64_MIN_HT` · `KF64_NGHEN` · `KF64_MOC` · `KF64_SAT_MOC` |
| Trục phễu | `KF64_TANG` (`T1…T4`) · ô ma trận `KF64_O` |
| Đầu ra | khối **`kf64`** của file kỳ — `schema insight-dashboard-kangnam/3` |
| Màn hình | tab **Chân dung & insight** — hai bảng: *tầng `T2` theo dịch vụ* và *dồn sức vào chân dung nào* |
| Đã gỡ | bảng «Cơ hội win» của `id-M` §7 · `chan_dung.co_hoi_win` nay để rỗng |

⚠ `id-N` có **bản sinh đôi trong `tools/id.py`** như `id-L` — sửa trọng số hay
ngưỡng thì phải sửa **cả hai chỗ**, lệch nhau là không ai biết đang chấm theo bản nào.

---

## 12. TỰ KIỂM SỔ NÀY

- [ ] Có bảng «Cơ hội win» của `id-M` §7 nào còn hiện ra không? ⛔ Nó đã nghỉ.
- [ ] Có ai dùng **ô ma trận** để chia ngân sách chưa? ⛔ Kỳ này 3/3 dòng sát mốc (§3).
- [ ] Bốn quyết định §2 đã gửi khối Sale xác nhận chưa? ⛔ Repo tự chốt, không phải họ.
- [ ] Mọi dòng chỉ số tạm có gắn chữ **TẠM** không?
- [ ] Chân dung < 30 HT có bị xếp hạng không? ⛔ Phải ghi «chưa đủ dữ liệu».
- [ ] `<DV>-CHUA_XAC_DINH` và `KHONG_XAC_DINH_DV` có bị tính vào **TB dịch vụ** không? ⛔ Không được.
- [ ] Mẫu số "dịch vụ" dùng tiền tố KF-62 hay cột `dich_vu` — đã ghi rõ chưa? (§2 ①)
- [ ] Bảng nào còn nhãn `A2` của KF-64 không? ⛔ Trục đó nay là `T1…T4` (§2 ④).
- [ ] Bước yếu nhất là `S5`/`S6` → đã gắn cờ **Vận hành/Sale** chưa, hay lại đi làm nội dung BOF?
- [ ] Ba điều kiện chờ dữ liệu ở §10 (①②⑦) đã ai theo chưa?

---

### Nhật ký duyệt

| Khi nào | Ai | Duyệt gì |
|---|---|---|
| **02/11/2026** | **người dùng** | ★ **Bỏ bước chờ anh UY duyệt.** KF-64 v1.0 thành bản chạy, **thay** `id-M` §7. |
| **02/11/2026** | **repo** | Tự chốt bốn chỗ KF-64 để trống — **§2** ①②③④. ⚠ Đây ⛔ không phải quyết định của khối Sale; báo lại để họ xác nhận hoặc đổi. |

⚠ **Duyệt để CHẠY, ⛔ không phải duyệt là ĐÚNG.** Trục Chuyển đổi (50% của bản
đủ) vẫn trống, và ô ma trận vẫn chưa chốt được — xem §6.

### ⚠ Việc còn phải làm

| # | Việc | Ai |
|---|---|---|
| ① | **Xác nhận hoặc đổi bốn quyết định §2b** — repo tự chốt, ⛔ chưa ai bên Sale xem | khối Sale |
| ② | Thêm trường **mã chân dung KF-62** vào Caresoft — ⛔ không có nó thì trục Chuyển đổi mãi trống | Sale Admin |
| ③ | Gửi lại số §4: **9/10 dịch vụ vượt ngưỡng `T2`** — kết luận dùng được ngay, ⛔ không chờ CRM | MKT Lead |
| ④ | ⛔ **Đừng dùng ô ma trận để chia ngân sách** tới khi có CRM — §6 nói vì sao | MKT Lead |
| ⑤ | Bổ sung `S2` vào bảng 5 bước của KF-64 (§5) | khối Sale |

---

### Liên quan

`id-M` §7 (xếp hạng chân dung — **bản đang chạy**) · §2 (dịch vụ → chân dung) ·
§5 (cổng ①) · §8 (thông điệp) · `id-D` §3 (nấc `5A` — ⚠ xung đột tên `A2`) ·
§1 (mã `O`) · §5 (rào cản) · §6 (bảng giao bốn ô) · `id-L` (nhiệt độ · nhóm gọi) ·
`id-G` §3 (hệ số 1/2/3) · `id-H` (hook · format) · `id-K` §3 (pháp chế đang chặn) ·
KF-57/KF-50 (định nghĩa tầng · ràng buộc ngân sách) · KF-49 (scale `+15–20%/3 ngày`) ·
KF-61/62 (tương quan 40:60 gốc) · KF-21/34 (CDP · nhắc lịch D02)
