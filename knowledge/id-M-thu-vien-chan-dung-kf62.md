# id-M · ★★ THƯ VIỆN CHÂN DUNG KHÁCH HÀNG — BỘ KF-62 v2.2

> Sổ **nhập từ ngoài**, như `id-L`: đây là thư viện KF-62 của khối Sale.
> ⛔ Repo không tự đặt thêm chân dung nào. Thiếu thì **báo lại để bổ sung ở bản sau**.
>
> ★ Sổ này **thay hẳn `id-C`** (đã bỏ 02/11/2026). Phần chân dung về đây;
> nấc `5A`, ma trận chân dung × `5A` và đầu ra bước B3 về `id-D` §3, §6, §9.

**Sổ này trả lời:** khách đang nhắn là **ai**, và nói gì với người đó.

---

## 1. ĐỔI LUẬT GỐC — 02/11/2026

Trước đây repo **cấm** có bộ chân dung dựng sẵn: mỗi kỳ agent phác họa `CD1…CDn`
từ chính hội thoại của kỳ, người dùng duyệt ở **CỔNG 0**. Luật đó đã **bỏ**.

| | Trước | Nay |
|---|---|---|
| Nguồn | Agent phác họa từ hội thoại của kỳ | `tools/chan_dung_kf62.json` — **cố định** |
| Mã | `CD1 … CDn`, **đổi nghĩa mỗi kỳ** | `SACTO-NAM_TAI_PHAT` — đọc được, cố định |
| Duyệt | CỔNG 0, **mỗi kỳ** | Một lần ở cấp KF-62 · ⛔ **không còn CỔNG 0** |
| So giữa các kỳ | ⛔ không | ✅ được |
| Dùng chung với Sale, pháp chế | ⛔ không | ✅ cùng một bộ mã |

★ **Vì sao đổi.** Mã đổi nghĩa mỗi kỳ thì `CD3` của tháng 10 và `CD3` của tháng 11
là hai thứ khác nhau — không vẽ được xu hướng, không bàn giao được cho ai.

⚠ **Cái mất khi đổi.** Chân dung phác họa theo kỳ **bám sát tệp thật** vì nó sinh
ra từ tệp đó; thư viện cố định thì không. Đó chính là lý do có **cổng ① ở §4** —
và kỳ đầu tiên đã trượt cổng đó (§5).

---

## 2. KIẾN TRÚC — BA NHÃN CHO MỘT HỘI THOẠI

```
CHÂN DUNG        × THẺ NGỮ CẢNH      × NHÃN NÓNG        → HÀNH ĐỘNG
(id-M, đúng 1)     (tối đa 3 thẻ)      (id-D §2, 1 nhãn)   (nhóm gọi id-L)

khách LÀ AI        khách đang         khách nóng          gọi ai trước ·
                   vướng gì           tới đâu             ai gọi · nói gì
```

⛔ **Ba thứ này ⛔ KHÔNG phải chân dung** — đây là lỗi hay gặp nhất:

| Khách nói | Trước xếp là | Thật ra là |
|---|---|---|
| *"em ở tỉnh"* | chân dung CD6 | **thẻ `AR02`** |
| *"đang tham khảo giá"* | chân dung CD2 | **thẻ `AR06`** |
| *"giá bao nhiêu"* rồi im | chân dung CD7 | **trạng thái lead `CHI_HOI_GIA`** |

★ Gộp chúng vào chân dung là trộn **khách là ai** với **khách đang ở đâu trong
phễu**. Hai câu hỏi khác nhau, hai cách xử lý khác nhau.

### Luật phân loại — thứ tự là một phần của luật

```
Mỗi dịch vụ có tối đa 5 câu hỏi Có/Không, chạy theo THỨ TỰ KIỂM TRA.
Câu «Có» ĐẦU TIÊN quyết định chân dung. ⛔ Không chấm điểm, ⛔ không lấy
cái trúng nhiều từ nhất.

① Tiền sử can thiệp · làm hỏng · vấn đề y khoa   ← hỏi TRƯỚC
② Mục tiêu thẩm mỹ                               ← hỏi SAU

Không câu nào «Có» → <DV>-CHUA_XAC_DINH, nhân viên hỏi 2 CÂU HỎI VÀNG.
```

⚠ **Đảo thứ tự là xếp ca sửa hỏng thành ca làm lần đầu** — rồi tư vấn sai, báo
giá sai, và mất một khách đã từng bị hỏng một lần.

⛔ Thứ tự này **để nhận diện đúng**, ⛔ không phải thứ tự ưu tiên kinh doanh.

### Ưu tiên chỉ tính từ dữ liệu

> Anh UY chốt 02/11/2026: ⛔ **không chân dung, không dịch vụ nào được gán ưu
> tiên trước.** Chỉ số ưu tiên = nhiệt độ trung bình (`id-L`, 40%) + tỷ lệ booking
> thực tế trên CRM (60%). Dưới 30 hội thoại hoặc dưới 5 booking → ghi
> *"chưa đủ dữ liệu"*, ⛔ không xếp hạng.

⚠ Mức ưu tiên dùng để chia **ngân sách, nội dung, đào tạo kịch bản** —
⛔ không đổi SLA phản hồi khách. SLA theo nhóm gọi của `id-L`.

---

## 3. CHẠY Ở ĐÂU

| Thứ | Chỗ |
|---|---|
| Thư viện (bản máy dùng) | `tools/chan_dung_kf62.json` — ★ **bản gốc, sửa tay** |
| Phân loại | `tools/id.py` → `gan_dich_vu_kf62()` · `gan_chan_dung_kf62()` · `gan_the()` |
| Nối lead scoring | `tools/id.py` → `viec_cua()` · khối `lien_ket_kf60` của thư viện |
| Sinh lại bảng của sổ này | `python tools/so-chan-dung.py` |
| Đầu ra | `chan_dung.tep` của file kỳ · cột `cd` và `the` của hàng chờ gọi |

⛔ **Đừng chép danh mục chân dung sang chỗ thứ hai.** Bảng ở §9 sinh thẳng từ
file JSON nên hai bên không thể lệch — đó là bài học của `id-L`, nơi thang điểm
nằm hai chỗ và phải nhắc nhau sửa cả hai.

---

## 4. NĂM CỔNG ĐÁNH GIÁ — KF-62 §4

Thư viện của **một dịch vụ** chỉ được coi là ổn định khi đạt **cả năm**:

| # | Cổng | Ngưỡng |
|---|---|---|
| ① | Tỷ lệ *"Chưa xác định"* | ≤ **15%** |
| ② | AI khớp nhãn trưởng nhóm Sale | ≥ **80%** |
| ③ | Không chân dung nào có độ khớp | < **70%** |
| ④ | Chỉ số ưu tiên giữa các chân dung chênh nhau | ≥ **20 điểm** |
| ⑤ | Không chân dung nào chiếm | < **5%** số hội thoại |

Không đạt → **gộp hoặc tách chân dung, sửa câu hỏi phân loại, chạy lại 2 tuần.**

⛔ **Chưa qua cổng ① thì ⛔ không dùng bảng chân dung để chia ngân sách.**
Báo cáo tự gắn cờ đỏ việc này ở đầu trang (`id-J` §2).

---

## 5. ★ KẾT QUẢ ĐO THẬT — KỲ 24–29/10/2026, 494 HỘI THOẠI

| Cổng | Ngưỡng | Đo được | |
|---|---|---|---|
| ① Chưa xác định | ≤15% | **65,6%** | ⛔ **TRƯỢT** |
| ⑤ Không chân dung nào <5% | — | lớn nhất 15,6% | ⛔ **TRƯỢT** |

**Nguyên nhân — đã kiểm, ⛔ không phải lỗi từ khoá:**

```
Trung vị chữ khách nói, CẢ hội thoại  :  44 ký tự
Nhóm chưa xếp được dịch vụ            :  18 ký tự
Mẫu thật: "Cấy HA giá bao nhieu" · "Mìn cần tư vấn ạ" · "(trống)"
```

★ Khách gõ **tên thủ thuật rồi hỏi giá**, ⛔ không tả tình trạng. Mà KF-62 phân
loại theo *tiền sử can thiệp × mục tiêu × hoàn cảnh mua* — ba thứ khách chưa nói.

→ **Việc chặn là tuần 1 của KF-62: áp 2 câu hỏi vàng cho mọi page.** Số liệu
chứng minh đúng thứ tự đó. ⛔ Thêm từ khoá nữa là ép dữ liệu, không phải sửa.

⚠ Bốn trong bảy chân dung cũ **không remap được** sang KF-62 (xem `_doi_chieu`
trong `dashboard/data/24-29-10.nguoi.json`). `CD1 · khách nói tiếng nước ngoài`
(29 HT) ⛔ **không có chỗ** trong KF-62 — cần báo lại để bổ sung thẻ.

---

## 6. RỦI RO — KF-62 §6

```
① DỮ LIỆU SỨC KHOẺ. Tiền sử điều trị là dữ liệu sức khoẻ (Luật 91/2025/QH15).
   Chỉ lưu NHÃN + câu bằng chứng ngắn · giới hạn người xem · cần đồng ý xử lý.

② AN TOÀN TRƯỚC BÁN HÀNG. Có dấu hiệu an toàn của dịch vụ → chuyển bác sĩ,
   ⛔ không tư vấn bán. Đã làm TẠI Kangnam/HCI và đang phàn nàn → luồng N4.

③ PHÁP LÝ. Toàn bộ dịch vụ tế bào gốc mang mã L8, ⛔ không hứa chữa bệnh.
   ⛔ KHÔNG dùng thẻ AR08 (nhân tướng/phong thuỷ) trong quảng cáo hay tin Zalo.

④ MỘT HỘI THOẠI HỎI NHIỀU DỊCH VỤ. Chọn dịch vụ khách hỏi SÂU NHẤT, ghi các
   dịch vụ còn lại để bán chéo. ⛔ Không tách thành hai hội thoại.

⑤ CÁC ĐIỂM [CẦN XÁC MINH] trong thư viện phải được chuyên môn và pháp chế
   xác nhận TRƯỚC khi dùng kịch bản liên quan.
```

⚠ `AR08` được phép dùng **trong tư vấn 1-1** để hiểu động cơ khách, ⛔ nhưng
không bao giờ xuất hiện trong nội dung phát ra ngoài.

---

## 7. ★ XẾP HẠNG CHÂN DUNG — DỒN SỨC VÀO ĐÂU

Bảng chân dung nói *có những ai*. Nó ⛔ không nói *làm ai trước*. Xếp theo số HT
là xếp theo nhóm **đông nhất**, ⛔ không phải nhóm **đáng làm nhất**.

### Công thức chính thức — anh UY chốt 02/11/2026 · ★ BẢN ĐANG CHẠY

```
Chỉ số ưu tiên = nhiệt độ trung bình (id-L) × 40%  +  tỷ lệ booking CRM × 60%

Mỗi chân dung so với TRUNG BÌNH CỦA DỊCH VỤ nó thuộc về (⛔ không tính CHUA_XAC_DINH).
Mỗi dịch vụ   so với TRUNG BÌNH TOÀN HỆ THỐNG.

≥110 CAO · 90–109 TRUNG BÌNH · <90 THẤP
Dưới 30 hội thoại HOẶC dưới 5 booking → ghi «chưa đủ dữ liệu», ⛔ không xếp hạng.
```

⚠️ **Chưa chạy được**: chưa có dòng CRM nào về. Mốc có số thật là tuần 3–4 (§10).

🔴 **Đã có bản kế tiếp đang chờ duyệt.** KF-64 ([`id-N`](id-N-chon-tep-tang-noi-dung-kf64.md))
chen thêm trục **Quy mô 20%** vào trước, thành `20/30/50` — và chính nó khai
rằng `30:50` giữ đúng tương quan `40:60` ở đây. Khi anh UY duyệt thì KF-64
**thay** công thức này, ⛔ không chạy song song. Đến lúc đó ⛔ đừng để hai
bảng xếp hạng cùng sống — đúng lỗi đã làm phải bỏ `id-C` §4.

### Bản tạm khi chưa có CRM — ⚠ là PROXY, ⛔ không phải bản chính

```
Điểm win = lead đang bỏ lỡ × hệ số giá trị đơn × tỷ lệ ĐANG CHỐT ĐƯỢC của nhóm
```

| Thành phần | Là gì | Lấy ở đâu |
|---|---|---|
| **lead đang bỏ lỡ** | HT của nhóm **chưa có SĐT** — phần còn lấy lại được | bảng chân dung |
| **hệ số giá trị đơn** | 1 · 2 · 3 theo **dịch vụ khách hỏi** | `id-G` §3 |
| **tỷ lệ đang chốt được** | `% có SĐT` quan sát được của chính nhóm đó | bảng chân dung |

⚠️ **`% có SĐT` chỉ là proxy của booking** — và đó chính là lý do anh UY đổi sang
công thức có CRM. Cho số điện thoại ⛔ không phải đã đặt lịch. Dùng bản tạm thì
mọi dòng phải gắn `⚠ proxy`, ⛔ không trình bày như kết quả đã đo.

★ **Cả ba thành phần đều là số ĐÃ ĐO của kỳ** — ⛔ không hệ số nào tự đặt. Đó là
điều kiện để bảng này còn **cãi được**.

★ **Vì sao nhân với tỷ lệ đang chốt được.** Nhóm đã chốt tốt là nhóm mà công sức
bỏ thêm sinh lời nhanh nhất. Nhóm chốt kém **vì câu trả lời của trực page** thì
điểm thấp là ĐÚNG — việc của nó nằm ở ô `🔧 sửa vận hành` của ma trận
(`id-D` §6): **sửa câu trả lời trước, làm nội dung sau.** Hai việc khác nhau,
⛔ không trộn vào một bảng xếp hạng.

### Ba luật giữ nguyên

```
⛔ Dòng CHUA_XAC_DINH và KHONG_XAC_DINH_DV KHÔNG được xếp hạng — không phải
   chân dung. Vẫn để trong bảng để tổng còn khớp, nhưng luôn nằm cuối.

★  Thẻ insight xếp theo ĐÚNG thứ hạng này, mỗi thẻ mang theo hạng của mình.
   Người đọc lướt từ trên xuống là đang đọc theo thứ tự đáng làm.

⚠  Chỉ số ưu tiên là ĐỀ XUẤT thứ tự, ⛔ không thay CỔNG 1. Ma trận ưu tiên
   vẫn do người dùng duyệt. Và nó ⛔ KHÔNG đổi SLA phản hồi khách — SLA theo
   nhóm gọi của `id-L`.
```

⛔ **Ba công thức, ba việc khác nhau — đừng trộn:**

| Sổ | Công thức | Cho cái gì |
|---|---|---|
| `id-L` | điểm × hệ số giá trị đơn | **một hội thoại** — thứ tự gọi trong nhóm |
| `id-M` §5 | nhiệt độ TB 40% + booking 60% | **một chân dung** — chia ngân sách, nội dung |
| `id-G` §3 | hệ số 1 · 2 · 3 | **thành phần dùng chung** của cả hai |

---

## 8. THÔNG ĐIỆP — THƯ VIỆN CÓ SẴN, NHƯNG ⛔ KHÔNG CÂU NÀO CŨNG DÙNG ĐƯỢC

⚠ **Luật cũ đã đảo.** `id-C` trước đây cấm lấy thông điệp từ kho, vì kho chở
theo đúng những câu `id-K` đang chặn (*trọn đời* · *tỷ lệ thành công* · *đổi
vận*). Nay KF-62 **chính là cái kho đó** — mỗi chân dung mang sẵn một *Thông
điệp (bản an toàn)*. Nên luật đổi thành:

```
Mỗi thông điệp của thư viện mang theo TRẠNG THÁI DUYỆT.
✅ «Đã duyệt»                       → phát được.
⛔ «Đề xuất – chưa duyệt» · «Chờ pháp chế duyệt»  → KHÔNG phát ra ngoài.
⚠  «Chưa có thông điệp – chờ dữ liệu NV»         → tự viết, theo khuôn dưới.
```

### Khuôn một thông điệp dựng tại kỳ

```
<điều khách sợ, bằng chữ của khách>  →  <điều mình làm khác>  →  <bằng chứng>
```

| Phải có | ⛔ Phải không có |
|---|---|
| Một `HT-nnn` truy ngược | Con số bảo hành (`id-K` §3) |
| Chữ khách dùng, ⛔ không phải tính từ | Cam kết kết quả chắc chắn |
| Một điều mình làm khác được | Hứa đổi vận, tài lộc, tỷ lệ thành công |
| Qua **CỔNG 2** trước khi phát | Giá dịch vụ chưa có bảng hiện hành |

★ Viết bằng **chữ của khách**. Khách không tìm *"đẹp tự nhiên"* — khách tìm
*"đầu mũi bóng đỏ"*.

⚠ Thông điệp dán sẵn làm hai việc sai cùng lúc: **nói hộ khách**, và **chở theo
câu đang bị chặn**. Thư viện đỡ được việc thứ nhất — 85 câu đều viết từ chính
lời khách. Việc thứ hai thì **chỉ trạng thái duyệt chặn được**, nên nó là thứ
⛔ không được bỏ qua khi lấy câu ra dùng.

---

## 9. DANH MỤC — sinh tự động từ `tools/chan_dung_kf62.json`

<!-- BANG-TU-DONG:bat -->

> ⚙ Phần dưới đây **sinh tự động** từ `tools/chan_dung_kf62.json` bằng
> `python tools/so-chan-dung.py`. ⛔ Đừng sửa tay — sửa file JSON rồi chạy lại.

### Năm khối · 18 dịch vụ · 85 chân dung

| Khối | Dịch vụ | Chân dung | Đã khai kịch bản riêng |
|---|---|---:|---:|
| **PTTM** | `MUI` · `MAT` · `HAM` · `NGUC` · `CAYMO` | 24 | ⚠ 0 — dùng lời mặc định |
| **Weightloss** | `GIAMBEO` · `HUTMO` · `BEOPHI` | 14 | ⚠ 0 — dùng lời mặc định |
| **Beauty & Spa** | `TREHOA` · `SACTO` · `FILLER` · `SEO` | 18 | **18** |
| **Dental** | `RANGSU` · `NIENG` · `IMPLANT` | 15 | ⚠ 0 — dùng lời mặc định |
| **Wellness** | `TBG` · `LONGEVITY` · `TIEMKHOP` | 14 | ⚠ 0 — dùng lời mặc định |

### 12 thẻ ngữ cảnh — dùng chung mọi dịch vụ, tối đa 3 thẻ một hội thoại

| Mã | Thẻ | Cách xử lý |
|---|---|---|
| `AR01` | Cần gấp / có sự kiện | Tính lịch hồi phục ngược từ ngày sự kiện; nói thật nếu không đủ thời gian |
| `AR02` | Việt kiều / ở xa có lịch về | Tư vấn online trước, chốt lịch theo ngày về, hỗ trợ lưu trú, tái khám từ xa |
| `AR03` | Nam giới | Phương án phù hợp nam giới, riêng tư |
| `AR04` | Trên 40 / kết hợp trẻ hoá | Tư vấn hài hoà theo tuổi; gợi mở trẻ hoá/wellness |
| `AR05` | Người trả tiền / quyết định khác người dùng | Mời người quyết định cùng tư vấn; trang bị câu nói cho người thân |
| `AR06` | So sánh giá / săn ưu đãi | Tách giá theo cấu phần, nói rõ giá trị |
| `AR07` | Cẩn trọng, cần kiểm chứng bác sĩ | Hồ sơ bác sĩ đã xác minh; hẹn gặp bác sĩ |
| `AR08` | Động cơ nhân tướng / phong thuỷ | ⛔ Không hứa tài lộc (cấm nội dung mê tín); chuyển về hài hoà |
| `AR09` | Khách cũ Kangnam / HCI | Ưu đãi khách thân thiết, cross-sell |
| `AR10` | Phụ huynh hỏi cho con | Chỉ tư vấn dịch vụ hợp lệ cho trẻ; PTTM dưới 18 tuổi → N5 |
| `AR11` | Lên hình / làm nội dung (KOC, TikToker) | Clip hồi phục theo mốc, nói rõ giới hạn; ⛔ không hứa mốc chưa được BS xác nhận |
| `AR12` | Bận rộn / quỹ nghỉ ngắn | Lịch cụ thể, số buổi và thời lượng thật, chính sách đổi lịch |

### Nối với lead scoring (`id-L`)

| Nhóm gọi KF-60 v1.1 | Tên cũ trong KF-62 | Ai làm | SLA |
|---|---|---|---|
| `GOI_NGAY` | HOT | Sale | gọi ≤15 phút |
| `XIN_SO` | HOT_CHUA_SO | Trực page | xin số ≤15 phút |
| `NUOI` | WARM | Sale/CSKH online | 24–72h |
| `KHONG` | COLD | Marketing (CDP) | tự động |

⚠ Chân dung chưa khai `hanh_dong` thì dùng `lien_ket_kf60.mac_dinh` — đủ để chạy, ⛔ nhưng không phải lời của KF-62 cho chân dung đó.

### Ngoài chân dung

| Mã | Nghĩa |
|---|---|
| `CHI_HOI_GIA` | Chỉ hỏi giá — chưa nói tình trạng |
| `CHUA_XAC_DINH` | Chưa xác định — chưa đủ dữ kiện xếp chân dung |
| `KHONG_XAC_DINH_DV` | Đến DỊCH VỤ cũng chưa biết — mã dự trữ |

### Danh mục chân dung theo thứ tự kiểm tra

> Câu **«Có» đầu tiên** quyết định. ⛔ Không chấm điểm, không lấy cái trúng
> nhiều từ nhất — thứ tự là một phần của luật.

#### Khối PTTM

**`MUI` · Thẩm mỹ mũi** — 5 chân dung · ⚠ 0/5 đã khai kịch bản

| # | Mã | Chân dung |
|---:|---|---|
| 1 | `MUI-SUA_HONG` ⚠ | Sửa mũi hỏng / làm lại |
| 2 | `MUI-CHUC_NANG_DI_TAT` ⚠ | Chức năng & dị tật — ngạt, vẹo vách ngăn, sứt môi, tai nạn |
| 3 | `MUI-FILLER_SANG_PT` ⚠ | Đã tiêm filler/chỉ — muốn chuyển sang phẫu thuật |
| 4 | `MUI-CHINH_CHI_TIET` ⚠ | Chỉnh chi tiết — cánh/đầu mũi to, gồ, hếch |
| 5 | `MUI-NANG_LAN_DAU` ⚠ | Nâng mũi lần đầu — muốn cao, thon, tự nhiên |
| — | `MUI-CHUA_XAC_DINH` | *Chưa xác định — hỏi 2 câu hỏi vàng* |

**`MAT` · Cắt mí & thẩm mỹ mắt** — 5 chân dung · ⚠ 0/5 đã khai kịch bản

| # | Mã | Chân dung |
|---:|---|---|
| 1 | `MAT-SUA_HONG` ⚠ | Sửa mí hỏng / làm lại mắt |
| 2 | `MAT-SUP_MI_CHUC_NANG` ⚠ | Da chùng/sụp che tầm nhìn — cần khám chức năng |
| 3 | `MAT-MI_DUOI_CUNG_MAY` ⚠ | Can thiệp đúng vùng — mí dưới, bọng dưới, cung mày, combo |
| 4 | `MAT-TRE_HOA_MI_TREN` ⚠ | Trẻ hoá mí trên — sụp sớm, nhìn mệt |
| 5 | `MAT-MOT_MI_LAN_DAU` ⚠ | Một mí/mí lót — lần đầu, muốn tạo nếp tự nhiên |
| — | `MAT-CHUA_XAC_DINH` | *Chưa xác định — hỏi 2 câu hỏi vàng* |

**`HAM` · Thẩm mỹ hàm mặt** — 5 chân dung · ⚠ 0/5 đã khai kịch bản

| # | Mã | Chân dung |
|---:|---|---|
| 1 | `HAM-CA_KHO_SUA_LAI` ⚠ | Ca khó & sửa lại: đã mổ nơi khác, di chứng, khe hở môi–vòm |
| 2 | `HAM-DANG_NIENG` ⚠ | Đang/đã niềng — cần ý kiến thứ hai |
| 3 | `HAM-MOM_LECH` ⚠ | Móm / khớp cắn ngược / lệch hàm — lần đầu |
| 4 | `HAM-HO_LAN_DAU` ⚠ | Hô — «răng hay hàm?», lần đầu |
| 5 | `HAM-GOT_HAM_VLINE` ⚠ | Gọt hàm/V-line, gò má, cằm — khớp cắn bình thường |
| — | `HAM-CHUA_XAC_DINH` | *Chưa xác định — hỏi 2 câu hỏi vàng* |

**`NGUC` · Nâng ngực** — 4 chân dung · ⚠ 0/4 đã khai kịch bản

| # | Mã | Chân dung |
|---:|---|---|
| 1 | `NGUC-THAY_TUI_SUA_LAI` ⚠ | Đã can thiệp ngực — thay/tháo túi, bao xơ, sửa lại |
| 2 | `NGUC-LECH_QUA_TO` ⚠ | Ngực lệch, dị dạng hoặc quá to — chỉnh hình dạng/kích thước |
| 3 | `NGUC-SAU_SINH` ⚠ | Ngực sau sinh/cho con bú — xẹp, chảy xệ |
| 4 | `NGUC-NANG_LAN_DAU` ⚠ | Nâng ngực lần đầu — ngực nhỏ/lép, muốn đầy tự nhiên |
| — | `NGUC-CHUA_XAC_DINH` | *Chưa xác định — hỏi 2 câu hỏi vàng* |

**`CAYMO` · Cấy mỡ tự thân** — 5 chân dung · ⚠ 0/5 đã khai kịch bản

| # | Mã | Chân dung |
|---:|---|---|
| 1 | `CAYMO-LAP_LOM_SUA_BODY` ⚠ | Lấp lõm & sửa body: lõm sau hút mỡ, sẹo lõm, chấn thương |
| 2 | `CAYMO-DA_LAM_DAY` ⚠ | Đã làm đầy/trẻ hoá mặt chưa ưng — «lần này khác gì?» |
| 3 | `CAYMO-VUNG_MAT` ⚠ | Vùng mắt: mắt trũng, rãnh lệ — «cắt hay cấy, BS chọn giúp» |
| 4 | `CAYMO-BODY` ⚠ | Body: ngực/mông/hông, sau sinh, kết hợp hút mỡ |
| 5 | `CAYMO-MAT_HOP_LAN_DAU` ⚠ | Mặt hóp lần đầu — «mình có làm nổi không?» |
| — | `CAYMO-CHUA_XAC_DINH` | *Chưa xác định — hỏi 2 câu hỏi vàng* |

#### Khối Weightloss

**`GIAMBEO` · Giảm béo không phẫu thuật** — 4 chân dung · ⚠ 0/4 đã khai kịch bản

| # | Mã | Chân dung |
|---:|---|---|
| 1 | `GIAMBEO-DA_THU_NOI_KHAC` ⚠ | Đã thử giảm béo nơi khác không hiệu quả, sợ bị ép thẻ |
| 2 | `GIAMBEO-SAU_SINH` ⚠ | Mẹ sau sinh muốn lấy lại vóc dáng không phẫu thuật |
| 3 | `GIAMBEO-SO_PHAU_THUAT` ⚠ | Sợ phẫu thuật — cân nhắc giữa hút mỡ và làm máy |
| 4 | `GIAMBEO-MO_KHU_TRU` ⚠ | Mỡ khu trú cứng đầu — cân nặng ổn, muốn gọn vùng |
| — | `GIAMBEO-CHUA_XAC_DINH` | *Chưa xác định — hỏi 2 câu hỏi vàng* |

**`HUTMO` · Hút mỡ & tạo hình vóc dáng** — 5 chân dung · ⚠ 0/5 đã khai kịch bản

| # | Mã | Chân dung |
|---:|---|---|
| 1 | `HUTMO-SUA_HONG` ⚠ | Sửa hút mỡ hỏng / làm lại sau tạo hình nơi khác |
| 2 | `HUTMO-DA_CHUNG_SAU_GIAM_CAN` ⚠ | Da chùng sau giảm cân lớn — muốn tái tạo body |
| 3 | `HUTMO-BUNG_SAU_SINH` ⚠ | Mẹ sau sinh — bụng vừa mỡ vừa da nhão |
| 4 | `HUTMO-NHIEU_VUNG_LIPO360` ⚠ | Nhiều vùng/toàn thân, muốn làm một lần (Lipo 360) |
| 5 | `HUTMO-1_2_VUNG_LAN_DAU` ⚠ | Hút mỡ lần đầu một–hai vùng mỡ cứng đầu |
| — | `HUTMO-CHUA_XAC_DINH` | *Chưa xác định — hỏi 2 câu hỏi vàng* |

**`BEOPHI` · Chống béo phì & kiểm soát cân nặng y khoa** — 5 chân dung · ⚠ 0/5 đã khai kịch bản

| # | Mã | Chân dung |
|---:|---|---|
| 1 | `BEOPHI-PHU_HUYNH_CHO_CON` ⚠ | Phụ huynh tìm chương trình kiểm soát cân nặng cho con |
| 2 | `BEOPHI-THUOC_YOYO` ⚠ | Đã dùng thuốc/tiêm giảm cân hoặc yo-yo nhiều lần |
| 3 | `BEOPHI-BENH_CHUYEN_HOA` ⚠ | Thừa cân kèm bệnh chuyển hóa — được dặn phải giảm cân |
| 4 | `BEOPHI-BEO_PHI_NANG` ⚠ | Béo phì nặng — cần giảm nhiều chục kg |
| 5 | `BEOPHI-THUA_CAN_VUA` ⚠ | Thừa cân mức vừa — muốn giảm cân y khoa bài bản |
| — | `BEOPHI-CHUA_XAC_DINH` | *Chưa xác định — hỏi 2 câu hỏi vàng* |

#### Khối Beauty & Spa

**`TREHOA` · Trẻ hoá & nâng cơ** — 4 chân dung

| # | Mã | Chân dung |
|---:|---|---|
| 1 | `TREHOA-SUA_BIEN_CHUNG` | Biến chứng/kết quả hỏng sau trẻ hoá – nâng cơ – căng chỉ |
| 2 | `TREHOA-CANG_DA_PT` | Chảy xệ nhiều — cân nhắc căng da phẫu thuật |
| 3 | `TREHOA-NANG_CO_KHONG_PT` | Chảy xệ, nhăn sâu — muốn nâng cơ không phẫu thuật |
| 4 | `TREHOA-CHONG_LAO_HOA_SOM` | Chống lão hoá sớm — da xuống sắc, nếp nhăn nhỏ |
| — | `TREHOA-CHUA_XAC_DINH` | *Chưa xác định — hỏi 2 câu hỏi vàng* |

**`SACTO` · Điều trị nám & sắc tố** — 5 chân dung

| # | Mã | Chân dung |
|---:|---|---|
| 1 | `SACTO-HONG_DA_KEM_TRON` | Da tổn thương do kem trộn hoặc biến chứng laser/peel |
| 2 | `SACTO-BOT_BAM_SINH` | Bớt sắc tố bẩm sinh — bớt xanh, bớt nâu, bớt Ota |
| 3 | `SACTO-NAM_TAI_PHAT` | Nám điều trị nhiều nơi, tái phát hoặc không đỡ |
| 4 | `SACTO-NAM_LAN_DAU` | Nám, tàn nhang, đồi mồi — điều trị lần đầu |
| 5 | `SACTO-SANG_DA` | Da xỉn, không đều màu — muốn sáng da |
| — | `SACTO-CHUA_XAC_DINH` | *Chưa xác định — hỏi 2 câu hỏi vàng* |

**`FILLER` · Tiêm filler & botox** — 4 chân dung

| # | Mã | Chân dung |
|---:|---|---|
| 1 | `FILLER-SUA_HONG` | Tiêm filler/botox hỏng — vón, lệch, muốn tiêu/sửa |
| 2 | `FILLER-TIEM_DUY_TRI` | Đã tiêm ổn — muốn tiêm lại, dặm, duy trì |
| 3 | `FILLER-BOTOX_LAN_DAU` | Xóa nhăn, gọn hàm bằng botox — lần đầu |
| 4 | `FILLER-LAM_DAY_LAN_DAU` | Làm đầy filler lần đầu — môi, cằm, má, rãnh |
| — | `FILLER-CHUA_XAC_DINH` | *Chưa xác định — hỏi 2 câu hỏi vàng* |

**`SEO` · Điều trị sẹo** — 5 chân dung

| # | Mã | Chân dung |
|---:|---|---|
| 1 | `SEO-DIEU_TRI_LAI` | Điều trị sẹo nơi khác không đỡ hoặc nặng hơn |
| 2 | `SEO-PT_BONG_CO_KEO` | Sẹo sau phẫu thuật, bỏng, chấn thương — diện rộng, co kéo |
| 3 | `SEO-LOI` | Sẹo lồi, sẹo phì đại |
| 4 | `SEO-RO_LOM` | Sẹo rỗ, sẹo lõm sau mụn/thủy đậu |
| 5 | `SEO-THAM` | Thâm sau mụn/vết thương — da phẳng |
| — | `SEO-CHUA_XAC_DINH` | *Chưa xác định — hỏi 2 câu hỏi vàng* |

#### Khối Dental

**`RANGSU` · Răng sứ & dán sứ (veneer)** — 5 chân dung · ⚠ 0/5 đã khai kịch bản

| # | Mã | Chân dung |
|---:|---|---|
| 1 | `RANGSU-SU_HONG_LAM_LAI` ⚠ | Sứ hỏng / làm lại — đen viền, hở, ê buốt, bể |
| 2 | `RANGSU-PHUC_HOI_RANG_VO` ⚠ | Răng vỡ lớn, sâu nhiều, đã chữa tủy — cần mão sứ |
| 3 | `RANGSU-BOC_SU_THAY_NIENG` ⚠ | Muốn bọc sứ để hết hô/lệch — có thể chỉ cần niềng |
| 4 | `RANGSU-SO_MAI_RANG` ⚠ | Lo mài răng thật — cân nhắc dán sứ veneer hay bọc sứ |
| 5 | `RANGSU-TRANG_DEU_NHANH` ⚠ | Muốn răng trắng đều nhanh — ố, mẻ, thưa nhẹ |
| — | `RANGSU-CHUA_XAC_DINH` | *Chưa xác định — hỏi 2 câu hỏi vàng* |

**`NIENG` · Niềng răng** — 5 chân dung · ⚠ 0/5 đã khai kịch bản

| # | Mã | Chân dung |
|---:|---|---|
| 1 | `NIENG-HONG_DO_DANG` ⚠ | Niềng hỏng, niềng dở dang hoặc tái phát |
| 2 | `NIENG-PHU_HUYNH_CHO_CON` ⚠ | Phụ huynh hỏi niềng cho con |
| 3 | `NIENG-HO_MOM_XUONG` ⚠ | Hô, móm, lệch hàm nghi do xương |
| 4 | `NIENG-KIN_DAO` ⚠ | Ngại lộ khí cụ — khay trong suốt, mắc cài sứ/mặt trong |
| 5 | `NIENG-LAN_DAU` ⚠ | Niềng lần đầu — răng lệch, chen chúc, thưa, hô nhẹ |
| — | `NIENG-CHUA_XAC_DINH` | *Chưa xác định — hỏi 2 câu hỏi vàng* |

**`IMPLANT` · Cấy ghép Implant** — 5 chân dung · ⚠ 0/5 đã khai kịch bản

| # | Mã | Chân dung |
|---:|---|---|
| 1 | `IMPLANT-HONG_LAM_LAI` ⚠ | Implant hỏng / làm lại — trụ lung lay, viêm quanh trụ |
| 2 | `IMPLANT-MAT_NHIEU_RANG_NGUOI_GIA` ⚠ | Mất nhiều răng/cả hàm, người lớn tuổi — con hỏi cho bố mẹ |
| 3 | `IMPLANT-VIET_KIEU` ⚠ | Việt kiều / ở nước ngoài về Việt Nam làm implant |
| 4 | `IMPLANT-HAY_CAU_RANG` ⚠ | Cân nhắc implant hay cầu răng |
| 5 | `IMPLANT-MAT_1_VAI_RANG` ⚠ | Mất 1–vài răng — muốn trồng lại bằng implant |
| — | `IMPLANT-CHUA_XAC_DINH` | *Chưa xác định — hỏi 2 câu hỏi vàng* |

#### Khối Wellness

**`TBG` · Tế bào gốc & liệu pháp tái tạo** — 4 chân dung · ⚠ 0/4 đã khai kịch bản

| # | Mã | Chân dung |
|---:|---|---|
| 1 | `TBG-DA_LAM_NOI_KHAC` ⚠ | Đã làm tế bào gốc nơi khác — không hiệu quả, lo biến chứng |
| 2 | `TBG-CHUA_BENH_KHOP` ⚠ | Tìm tế bào gốc để chữa bệnh/khớp cho mình hoặc bố mẹ |
| 3 | `TBG-DA_MAT` ⚠ | Muốn tế bào gốc/exosome cho da mặt — nám, nhăn, lỗ chân lông |
| 4 | `TBG-TRE_HOA_TOAN_THAN` ⚠ | Muốn truyền tế bào gốc toàn thân để trẻ hoá |
| — | `TBG-CHUA_XAC_DINH` | *Chưa xác định — hỏi 2 câu hỏi vàng* |

**`LONGEVITY` · Longevity & chống lão hoá chủ động** — 5 chân dung · ⚠ 0/5 đã khai kịch bản

| # | Mã | Chân dung |
|---:|---|---|
| 1 | `LONGEVITY-DA_TRUYEN_NOI_TIET` ⚠ | Đã truyền dịch/dùng nội tiết nơi khác — lo tác dụng phụ |
| 2 | `LONGEVITY-QUANH_PHAU_THUAT` ⚠ | Chuẩn bị hoặc phục hồi quanh phẫu thuật thẩm mỹ |
| 3 | `LONGEVITY-NOI_TIET_TRUNG_NIEN` ⚠ | Nội tiết tuổi trung niên — tiền mãn kinh, giảm testosterone |
| 4 | `LONGEVITY-MUA_CHO_BO_ME` ⚠ | Con/người nhà mua gói tầm soát, chăm sóc cho bố mẹ |
| 5 | `LONGEVITY-TU_CHONG_LAO_HOA` ⚠ | Tự chủ động chống lão hoá — mệt mỏi, tuổi sinh học, IV/NAD+ |
| — | `LONGEVITY-CHUA_XAC_DINH` | *Chưa xác định — hỏi 2 câu hỏi vàng* |

**`TIEMKHOP` · Tiêm khớp (PRP, tiêm dưới siêu âm)** — 5 chân dung · ⚠ 0/5 đã khai kịch bản

| # | Mã | Chân dung |
|---:|---|---|
| 1 | `TIEMKHOP-CHI_DINH_THAY_KHOP` ⚠ | Đã được chỉ định mổ thay khớp — tìm ý kiến thứ hai |
| 2 | `TIEMKHOP-DA_TIEM_NOI_KHAC` ⚠ | Đã tiêm khớp nơi khác — đỡ rồi đau lại |
| 3 | `TIEMKHOP-CHAN_THUONG_THE_THAO` ⚠ | Chấn thương khớp do thể thao, vận động — đau tái phát |
| 4 | `TIEMKHOP-CON_HOI_CHO_BO_ME` ⚠ | Con hỏi cho bố mẹ đau khớp |
| 5 | `TIEMKHOP-TU_DAU_TU_CHUA` ⚠ | Tự đau khớp lâu ngày hoặc mới đau sớm — đang tự chữa |
| — | `TIEMKHOP-CHUA_XAC_DINH` | *Chưa xác định — hỏi 2 câu hỏi vàng* |

⚠ = chưa khai kịch bản riêng theo nhóm gọi.

<!-- BANG-TU-DONG:ket -->

---

## 10. TRIỂN KHAI — KF-62 §5

| Tuần | Việc |
|---|---|
| 1 | ★ **Áp 2 câu hỏi vàng cho mọi page dịch vụ.** Lấy ~100 hội thoại mỗi dịch vụ; 2 trưởng nhóm Sale gắn nhãn độc lập |
| 2 | AI phân loại cùng bộ hội thoại, so khớp; sửa câu hỏi và dấu hiệu ở chỗ hay nhầm |
| 3–4 | Chạy thực tế cùng `id-L`, đối chiếu booking trên CRM; lần đầu tính chỉ số ưu tiên |
| Mỗi 2 tuần | Cập nhật chỉ số ưu tiên → điều chỉnh ngân sách ads, nội dung, đào tạo kịch bản |

**A/B test:** kịch bản theo chân dung so với kịch bản chung (tỷ lệ xin số, booking) ·
hỏi 2 câu vàng ở tin **thứ 1** so với tin **thứ 3**.

---

## 11. TỰ KIỂM SỔ NÀY

- [ ] Mỗi hội thoại có **đúng một** chân dung, **tối đa ba** thẻ không?
- [ ] Có thẻ nào bị xếp nhầm thành chân dung không (`AR02` ở tỉnh, `AR06` so giá)?
- [ ] *"Chỉ hỏi giá, chưa nói tình trạng"* có bị gán chân dung không? ⛔ Phải là trạng thái lead.
- [ ] Tỷ lệ *"Chưa xác định"* của từng dịch vụ có vượt 15% không? Vượt thì đã **báo cờ đỏ** chưa?
- [ ] Tổng cột `ht` của bảng chân dung có **bằng đúng** cỡ mẫu không?
- [ ] Chân dung nào chưa khai `hanh_dong` mà đã lên hàng chờ? Dòng đó có gắn nhãn **«lời mặc định»** chưa?
- [ ] Có ai tự thêm chân dung ngoài KF-62 không? ⛔ Phải báo lại, ⛔ không tự đặt.
- [ ] Xếp hạng chân dung dùng công thức CRM (§7) hay bản tạm? Dùng bản tạm thì mọi dòng đã gắn `⚠ proxy` chưa?
- [ ] Có bảng nào xếp hạng theo KF-64 (`id-N`) chưa? ⛔ Sổ đó **chưa duyệt** — bản chạy là §7.
- [ ] Bảng §9 có khớp `tools/chan_dung_kf62.json` không — đã chạy lại `so-chan-dung.py` chưa?
- [ ] Thông điệp phát ra ngoài có câu nào còn «chưa duyệt» / «chờ pháp chế» không? (§8)
- [ ] Thẻ `AR08` có lọt ra nội dung quảng cáo hay tin Zalo không?

---

### Liên quan

`id-D` §3 (nấc `5A`) · §6 (ma trận chân dung × `5A`) · §2 (nhãn nóng) ·
`id-L` (lead scoring · nhóm gọi · `lien_ket_kf60`) · `id-G` §3 (hệ số giá trị đơn) ·
`id-J` §2b (khối `lead` · cột `viec_chi_tiet`) · `id-K` (pháp chế) ·
KF-61 (khung thí điểm Mũi) · KF-24 (mã pháp lý `L0–L9`)
