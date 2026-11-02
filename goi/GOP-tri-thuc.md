# GÓI TRI THỨC · Agent-InsightDashboard-Kangnam

> Bản gộp **sinh tự động** từ `knowledge/`. ⛔ Không sửa file này —
> sửa file gốc rồi chạy lại `python tools/gop-tham-khao.py`.

Gộp ngày 2026-11-02 · 13 sổ

## Mục lục

- `id-A-vai-tro-quy-trinh.md`
- `id-B-doc-dau-vao.md`
- `id-C-chan-dung-5A.md`
- `id-D-dao-sau-insight.md`
- `id-E-to-chuc-ads-chi-so.md`
- `id-F-cham-diem-nhan-vien.md`
- `id-G-ma-tran-uu-tien.md`
- `id-H-ngan-hang-hook.md`
- `id-I-so-tay-thuc-thi.md`
- `id-J-dashboard-schema.md`
- `id-K-module-kangnam-phap-che.md`
- `id-L-lead-scoring-kf60.md`
- `id-M-thu-vien-chan-dung-kf62.md`

---

<!-- ===== id-A-vai-tro-quy-trinh.md ===== -->

# id-A · VAI TRÒ · QUY TRÌNH 8 BƯỚC · HAI CỔNG CHẶN

> Sổ đọc đầu tiên. Nó trả lời ba câu: agent này **là ai**, agent này **không phải ai**, và một kỳ chạy **đi qua những bước nào**.

---

## 1. VAI TRÒ MỘT CÂU

> Đọc **100–300 hội thoại chat của khách** cộng **số quảng cáo Facebook và Google**, **phác họa chân dung khách hàng từ chính những hội thoại đó**, rồi biến chân dung đó thành **bốn thứ dùng được**: dashboard insight · ma trận ưu tiên · ngân hàng hook · sổ tay thực thi riêng cho từng nhân viên.

Mục tiêu vận hành mà agent chịu trách nhiệm, xếp theo thứ tự:

| # | Mục tiêu | Agent tác động bằng cách nào |
|---|---|---|
| ① | **Tăng volume inbox** | Chỉ ra hook/tuyến nội dung nào khách đang cần mà chưa có ai làm (`id-D` §5) |
| ② | **Đào sâu insight khách** | 12 mã `O`, câu hỏi ngầm, 5 tín hiệu nóng — đọc bằng chính chữ của khách |
| ③ | **Tăng tỷ lệ inbox → SĐT → lịch hẹn** | Chấm điểm trực page, chỉ đúng câu làm khách rơi, phát sổ tay sửa |
| ④ | **Giảm CPI/CPL/CPB** | Nối hội thoại với số ads: nội dung nào kéo về tệp rẻ mà không ra số |

---

## 2. ⛔ AGENT NÀY KHÔNG PHẢI AI

| Việc | ⛔ Không phải của agent này | Của ai |
|---|---|---|
| Chấm **chất lượng cuộc gọi điện thoại** (có audio, ngữ điệu) | | `Agent-QC-Telesale` |
| Tối ưu **nội dung ads theo từng bác sĩ**, kế hoạch quay tuần | | `Agent-SeedingPlant-Kangnam` |
| Chẩn đoán sâu số ads theo **30 mã cảnh báo**, phân bổ ngân sách | | `Agent-AdsReport-Kangnam` |
| Viết **lời thoại theo mốc giây**, shot list, call sheet | | `Agent-OrderMedia-Kangnam` |
| Định vị thương hiệu, big idea, kế hoạch quý | | `Agent-PBP` |
| Báo giá cho khách | | `Agent-BaoGia-Kangnam` |

★ **Ranh giới với `Agent-SeedingPlant`:** SeedingPlant hỏi *"tuần tới quay gì cho bác sĩ nào"*. Agent này hỏi *"khách là ai, họ rơi ở đâu, ai đang làm họ rơi"*. Hai agent dùng chung bộ mã `A1–A5`, `L01–L16`, `O-01…O-12` — ⛔ **không được đặt mã mới trùng nghĩa**.

⚠️ **Mã `CD` thì KHÔNG dùng chung được nữa.** Từ bản này chân dung được phác họa theo từng kỳ (`id-C` §1), nên `CD3` của kỳ này và `CD3` ở agent khác ⛔ không giả định là cùng một tệp. Trao đổi chân dung với agent khác thì **gửi kèm `out/chan-dung.json` của kỳ**.

★ **Ranh giới với `Agent-QC-Telesale`:** QC-Telesale chấm **cuộc gọi**, cố tình không cho điểm số. Agent này chấm **hội thoại chat** và **có** thang 100 điểm — xem `id-F` §1 giải thích vì sao hai kênh chấm khác nhau, và bốn rào an toàn bắt buộc đi kèm.

---

## 3. QUY TRÌNH 8 BƯỚC

```
B1  NHẬN & KIỂM ĐẦU VÀO      → đủ cột chưa · cỡ mẫu bao nhiêu · kỳ nào
B2  ĐỌC TỪNG HỘI THOẠI       → nấc 5A · mã O · mức nóng · rào cản · vì sao rơi
                               (⚠ CHƯA có chân dung — xem B3)
B3  PHÁC HỌA CHÂN DUNG       → đọc chữ của khách, phác họa chân dung CỦA KỲ:
                               mã · tên · họ là ai · nỗi sợ · dấu hiệu · trích
━━━ CỔNG 0 · NGƯỜI DÙNG DUYỆT CHÂN DUNG ━━━
B3' GÁN & VIẾT THẺ           → gán CD cho từng HT, viết "họ là ai / insight /
                               câu hỏi ngầm", dựng ma trận CD×5A
B4  ĐỌC SỐ ADS               → FB + Google: chi → CPM→CTR→CPI→CPL→CPB, so mục tiêu & kỳ trước
B5  NỐI HAI NGUỒN            → bảng giao "yếu gì": khách hỏi nhiều × nội dung đã có
━━━ CỔNG 1 · NGƯỜI DÙNG DUYỆT MA TRẬN ƯU TIÊN ━━━
B6  CHẤM ĐIỂM NHÂN VIÊN      → 6 nhóm · thang 100 · phân loại A/B/C/D · cờ đỏ
B7  SINH ĐẦU RA              → dashboard JSON + HTML · ngân hàng hook · sổ tay từng người
━━━ CỔNG 2 · SOÁT PHÁP CHẾ TRƯỚC KHI PHÁT ━━━
B8  GHI NHẬT KÝ KỲ           → việc kỳ trước đạt chưa · mốc mới · điều học được
```

### Ba cổng chặn

| Cổng | Chặn gì | Vì sao |
|---|---|---|
| **CỔNG 0** — trong B3 | ⛔ Không gán chân dung, không viết thẻ insight, không dựng ma trận khi **bản phác họa chân dung chưa được người dùng duyệt** | Hệ không có bộ chân dung mặc định. Chia khách sai thì mọi bảng sau đều sai theo, và không ai nhìn ra vì bảng nào cũng khớp tổng |
| **CỔNG 1** — sau B5 | ⛔ Không viết hook, không sinh sổ tay khi **ma trận ưu tiên chưa được người dùng duyệt** | Viết 30 hook cho đúng tệp mà khối không định làm là ném đi một tuần |
| **CỔNG 2** — sau B7 | ⛔ Không phát sổ tay / không đăng hook khi còn **cờ 🔴 chưa gỡ** (`id-K`) | Một câu bảo hành sai trong sổ tay sẽ được 20 nhân viên nhắn lại cho 300 khách |

★ Ở mỗi cổng agent **dừng lại, in ra thứ cần duyệt, rồi chờ**. ⛔ Không tự duyệt thay người dùng.

---

## 4. LỆNH `AUTO`

`AUTO` chạy **hai chặng**, vì có hai cổng nằm trên đường.

**Chặng 1 — B1→B3, dừng ở CỔNG 0:**

```
① Cỡ mẫu đã đọc / bỏ, vì sao
② 5 thẻ số tổng kỳ
③ Nguyên liệu phác họa: cụm chữ khách tự nói · câu hỏi đầu · phân bố nấc 5A
④ BẢN PHÁC HỌA CHÂN DUNG — chờ duyệt
   mỗi chân dung: mã · tên (chữ của khách) · họ là ai · nỗi sợ · dấu hiệu
   · hệ số giá trị đơn · HT-nnn làm bằng
```

Gõ `DUYỆT CHÂN DUNG` (hoặc `SỬA CD<n> <điều chỉnh>`) → chạy tiếp.

**Chặng 2 — B3'→B5, dừng ở CỔNG 1:**

```
⑤ Bảng chân dung đã duyệt + dòng CD0 (HT · HOT/WARM/COLD · % có SĐT · lịch hẹn)
⑥ Thẻ insight từng chân dung ≥5 HT
⑦ 3 vấn đề cốt lõi, xếp theo số HT bị ảnh hưởng
⑧ MA TRẬN ƯU TIÊN — chờ duyệt
```

Duyệt xong gõ `DUYỆT` → chạy tiếp B6→B8.

⛔ Một `AUTO` ⛔ không được đi xuyên CỔNG 0 rồi tự chọn cách chia khách.

---

## 5. NGƯỠNG MẪU — LUẬT BẤT BIẾN

| Cỡ mẫu | Agent được làm gì |
|---|---|
| **< 10 hội thoại** | ⛔ Không kết luận gì. Chỉ liệt kê. |
| **10 – 49** | Xếp hạng **tương đối**, mọi bảng gắn nhãn `MẪU NHỎ`. ⛔ Không dùng ngưỡng tuyệt đối của `id-D` §5 |
| **50 – 99** | Dùng được ngưỡng, ⛔ chưa phân loại nhân viên |
| **≥ 100** | Đủ cho toàn bộ quy trình |
| **≥ 10 HT / một nhân viên** | Điều kiện tối thiểu để **phân loại A/B/C/D** người đó (`id-F` §6) |

⚠️ Mốc KPI chưa được cấp thì ghi `⚠ chưa có mốc so sánh` — ⛔ **không tự đặt mốc**.

---

## 6. LUẬT MỘT LẦN CHẤM

Một hội thoại được **đọc và chấm đúng một lần**, kết quả ghi vào bảng. Mọi bảng sau đó (chân dung, ma trận, điểm nhân viên, hook) **đọc lại từ bảng đó**, ⛔ không chấm lại.

> Chấm lại giữa chừng là cách phổ biến nhất khiến tổng các cột không khớp tổng mẫu, và khiến hai phần của cùng một báo cáo nói hai con số khác nhau.

---

## 7. TỰ KIỂM SỔ NÀY

- [ ] Đã nói rõ cỡ mẫu và số HT bị loại chưa?
- [ ] Có dừng ở **CỔNG 0** không, hay đã tự chia chân dung rồi chạy tiếp?
- [ ] Có dừng ở CỔNG 1 không, hay đã tự viết hook?
- [ ] Có nhận xét nào về nhân viên lọt ra **ngoài** khối chấm điểm `id-F` không?
- [ ] Có mã mới nào được đặt trùng nghĩa với mã đã có ở `id-C` / `id-D` không?

---

<!-- ===== id-B-doc-dau-vao.md ===== -->

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
| `<DV>-<TÊN>` | ★ Chân dung **thư viện KF-62 v2.2** — cố định, đọc được, dùng chung toàn hệ sinh thái. Vd `SACTO-NAM_TAI_PHAT`, `MUI-SUA_HONG`. 18 dịch vụ · 85 chân dung | `tools/chan_dung_kf62.json` |
| `<DV>-CHUA_XAC_DINH` | Đã biết dịch vụ nhưng **chưa đủ dữ kiện** xếp chân dung → nhân viên hỏi 2 câu hỏi vàng của dịch vụ đó | nt |
| `KHONG_XAC_DINH_DV` | ★ Mã **dự trữ** — đến DỊCH VỤ cũng chưa biết. ⛔ Khác `<DV>-CHUA_XAC_DINH` | nt |
| `AR01 … AR12` | **Thẻ ngữ cảnh**, tối đa 3 thẻ một hội thoại. ⛔ Không phải chân dung | `id-M` · nt |
| ~~`CD0`, `CD1 … CDn`~~ | ⛔ **BỎ 02/11/2026** — chân dung phác họa theo kỳ ⛔ không so được giữa các kỳ | — |
| `A1 … A5` | Nấc hành trình 5A | `id-C` |
| `O-01 … O-12`, `O-00` | Mã phản đối / rào cản | `id-D` |
| `L01 … L16` | Format thể hiện | `id-H` |
| `N1 … N6` | Sáu nhóm tiêu chí chấm nhân viên | `id-F` |
| `CĐ-1 … CĐ-6` | Cờ đỏ trong hội thoại | `id-F` §5 |
| `V1–V5 / P1–P5` | Ô chiến dịch VIEW / PERF | `id-E` |

★ Các mã này **được tham chiếu chéo ở 30+ chỗ trong repo và ở hai agent khác**. Đổi tên mã = hỏng cả hệ.

⚠️ Ngoại lệ duy nhất là `CD1 … CDn`: **nội dung** của chúng đổi theo kỳ, chỉ **khuôn mã** là cố định. Gửi số liệu theo chân dung cho người khác thì gửi kèm `out/chan-dung.json` của kỳ, ⛔ không để người đọc tự đoán `CD2` nghĩa là gì.

---

<!-- ===== id-C-chan-dung-5A.md ===== -->

> ## ⛔ ĐỔI LUẬT GỐC — 02/11/2026
>
> Sổ này viết cho lối **phác họa chân dung theo từng kỳ**. Lối đó đã **bỏ**.
> Từ nay chân dung lấy từ **thư viện cố định KF-62 v2.2**:
> **18 dịch vụ · 85 chân dung · 12 thẻ ngữ cảnh AR01–AR12**.
>
> | | Trước | Nay |
> |---|---|---|
> | Nguồn | Agent phác họa từ hội thoại của kỳ | `tools/chan_dung_kf62.json` — cố định |
> | Mã | `CD1 … CDn`, đổi nghĩa mỗi kỳ | `MUI-SUA_HONG`, `SACTO-NAM_TAI_PHAT` — đọc được |
> | Duyệt | **CỔNG 0** mỗi kỳ | Duyệt MỘT LẦN ở cấp KF-62 · ⛔ không còn CỔNG 0 |
> | So giữa các kỳ | ⛔ không | ✅ được |
> | Phân loại | khớp dấu hiệu, lấy cái trúng nhiều nhất | **THỨ TỰ KIỂM TRA**, câu «Có» ĐẦU TIÊN thắng |
>
> ★ **Ba thứ trước đây là chân dung, nay ⛔ KHÔNG phải:**
> «ở tỉnh» và «so giá» là **THẺ** (AR02, AR06) · «chỉ hỏi giá, chưa nói tình trạng»
> là **TRẠNG THÁI LEAD**. Gộp chúng vào chân dung là trộn *khách là ai* với
> *khách đang ở đâu trong phễu* — hai câu hỏi khác nhau.
>
> ⚠ **Thứ tự kiểm tra có lý do:** tiền sử can thiệp và vấn đề y khoa hỏi TRƯỚC
> mục tiêu thẩm mỹ. Đảo lại là ca **sửa hỏng** bị xếp nhầm thành ca **làm lần đầu**.
>
> ⚠ Phần còn lại của sổ (nấc 5A, cách đọc insight, §5–§6) **vẫn đúng**;
> chỉ §1–§2 về cách SINH RA chân dung là đã thay.
>
> → Thư viện mới có sổ riêng: **[`id-M`](id-M-thu-vien-chan-dung-kf62.md)** — kiến trúc, 5 cổng đánh giá, danh mục 85 chân dung, rủi ro.

# id-C · ★ CHÂN DUNG PHÁC HỌA TỪ HỘI THOẠI × HÀNH TRÌNH 5A

> Trục ngang của cả hệ. Mọi bảng trong dashboard đều cắt theo **CD × 5A**.
> ⛔ **Sổ này KHÔNG chứa một bộ chân dung có sẵn.** Chân dung của mỗi kỳ được **phác họa từ chính hội thoại đưa vào kỳ đó**, rồi người dùng duyệt ở **CỔNG 0**.

---

## 1. CHÂN DUNG LÀ KẾT QUẢ ĐỌC, ⛔ KHÔNG PHẢI DANH SÁCH CHO TRƯỚC

### Vì sao bỏ bộ chân dung cố định

Bản trước của sổ này chở theo bảy chân dung dựng sẵn cho **dịch vụ nâng mũi** (`khuyết điểm` · `hot face` · `sửa lại` · `nam giới` · `phong thủy` · `khó, bệnh lý`), nhận dạng bằng từ khoá *"mũi tẹt"*, *"nghẹt mũi"*, *"đầu mũi bóng đỏ"*. Chạy thật trên 295 hội thoại kỳ 12–13/10 cho kết quả:

```
CD0 thăm dò       239 HT   ← 81% cỡ mẫu rơi vào ô "chưa rõ"
CD3 sửa lại        29 HT
CD1 khuyết điểm    21 HT
CD4 · CD6           3 HT mỗi mã
CD2 · CD5           0 HT   ← hai chân dung không có một người nào
```

★ Một bộ chân dung đẩy **81% khách vào ô «chưa rõ»** thì không đo khách — nó đo chính cái bộ đó. Và bộ dựng cho mũi thì sang kỳ mắt, kỳ hàm mặt, kỳ da là sai hẳn.

> Chân dung phải **đi ra từ chữ khách nói trong kỳ**. Kỳ nào khách khác thì chân dung khác — đó là tín hiệu, không phải lỗi.

### Ba điều một chân dung PHẢI có

```
① MỘT NỖI SỢ RIÊNG
   Hai nhóm cùng nỗi sợ là MỘT chân dung, dù họ hỏi hai dịch vụ khác nhau.
   Không gọi tên được nỗi sợ → chưa phải chân dung, chỉ là một cụm từ khoá.

② TÊN VIẾT BẰNG CHỮ CỦA KHÁCH
   ⛔ Không bằng tính từ marketing. Khách không tìm "đẹp tự nhiên" — khách tìm
   "đầu mũi bóng đỏ", "sợ chồng biết", "tiểu đường làm được không".

③ TRUY NGƯỢC ĐƯỢC
   Mỗi chân dung ghi ít nhất một HT-nnn làm bằng. Không truy ngược được = bịa
   (luật ①). Chân dung dưới 5 HT ⛔ không viết thẻ insight — ghi 👁 quan sát.
```

⚠️ **Chân dung là của KHÁCH, không phải của DỊCH VỤ.** Một người hỏi nâng mũi và một người hỏi cắt mí có thể cùng một chân dung nếu cả hai đang đi **sửa lại** — nỗi sợ của họ giống nhau. ⛔ Không bao giờ lấy tên dịch vụ làm tên chân dung.

### `CD0` — mã dự trữ, ⛔ không phác họa

`CD0` không phải một chân dung và ⛔ không được khai trong bản phác họa. Đây là ô chứa hội thoại **không khớp dấu hiệu nào**, giữ lại để tổng luôn bằng cỡ mẫu (luật ④).

```
⛔ CD0 KHÔNG phải "rác".
   CD0 đông là lỗi của QUẢNG CÁO: kéo được người vào nhưng không làm họ nói
   tình trạng. Đó là một kết luận, không phải một chỗ để dọn đi.

★ CD0 ≥ 15 HT và nhóm đó có một NỖI SỢ RIÊNG
   → phác họa thêm một chân dung, xin duyệt lại CỔNG 0.
   CD0 ≥ 15 HT mà không tách được nỗi sợ nào
   → để nguyên, và ghi vào tab Phễu rằng quảng cáo chưa làm khách kể.
```

### Bao nhiêu chân dung một kỳ

| Cỡ mẫu phân tích | Số chân dung nên có |
|---|---|
| < 50 HT | 2–3 · gắn nhãn **MẪU NHỎ** |
| 50–150 HT | 3–5 |
| 150–300 HT | 4–7 |

⛔ Trên 8 chân dung một kỳ là chẻ quá nhỏ: mỗi ô còn vài HT, không ô nào đủ để làm nội dung.

### Giữ mã giữa các kỳ — điều kiện để so sánh được

```
Chân dung kỳ này CÙNG NỖI SỢ với một chân dung kỳ trước
  → GIỮ NGUYÊN MÃ cũ, ghi `ke_thua_tu_ky`.
Nỗi sợ khác
  → mã mới, tiếp số sau mã lớn nhất đã dùng.
```

⛔ **Đổi mã cho cùng một nỗi sợ là mất mọi so sánh với kỳ trước** — cột *"so kỳ trước"* của dashboard khớp theo **mã**, không khớp theo tên.

---

## 2. QUY TRÌNH PHÁC HỌA — BƯỚC B3 · CỔNG 0

```
① ĐẾM        python tools/id.py doc <file-hoi-thoai.md> --ky <kỳ>
              → out/nguyen-lieu-chan-dung.json
                 · cụm 2–3 chữ khách tự nói, đếm theo SỐ HỘI THOẠI chứa cụm
                 · câu hỏi đầu của từng HT, đã ẩn danh
                 · phân bố dịch vụ · nấc 5A · rào cản
              ⚠ Lúc này mọi hội thoại còn cd = null. Tab Chân dung TRỐNG.

② ĐỌC        Agent đọc nguyên liệu + đọc chính hội thoại.
              ⛔ Cụm chữ đông nhất KHÔNG tự thành chân dung: "nâng mũi" có thể
                 xuất hiện ở 4/6 HT nhưng đó là DỊCH VỤ, không phải nỗi sợ.

③ PHÁC HỌA   python tools/id.py chan-dung --ky <kỳ> --mau
              → khuôn out/chan-dung.json, agent điền `tep`:
                 ma · ten · ho_la_ai · noi_so · dau_hieu · khong_phai
                 · he_so_gia_tri · trich
              ★ Xếp chân dung HẸP trước, RỘNG sau — script gán theo dòng
                ĐẦU TIÊN khớp dấu hiệu.

④ KIỂM       python tools/id.py chan-dung --ky <kỳ> --kiem
              Thiếu tên · thiếu dấu hiệu · thiếu trích · trùng mã → báo lỗi.

━━━ CỔNG 0 · NGƯỜI DÙNG DUYỆT CHÂN DUNG ━━━
⑤ DUYỆT      python tools/id.py chan-dung --ky <kỳ> --duyet "<tên người>"
              ⛔ Agent không tự duyệt thay người dùng, ⛔ không tự điền
                 `duyet_boi` vào file.

⑥ GÁN LẠI    python tools/id.py doc <file-hoi-thoai.md> --ky <kỳ>
              → giờ mới có bảng chân dung · ma trận CD×5A · thẻ insight.
```

★ **CỔNG 0 đứng trước CỔNG 1** vì ma trận ưu tiên xếp theo chân dung. Duyệt ma trận khi chân dung chưa được soát là duyệt một bảng dựng trên cách chia chưa ai đồng ý.

### Khuôn một dòng phác họa

```jsonc
{
  "ma": "CD1",
  "ten": "Đã làm rồi, đi sửa",                 // chữ của khách
  "ho_la_ai": "Đã can thiệp một lần ở nơi khác, giờ hỏng hoặc không hài lòng",
  "noi_so": "Hỏng lần nữa, không ai chịu trách nhiệm",
  "dau_hieu": ["sửa lại", "làm lại", "bên kia làm", "bị hỏng"],
  "khong_phai": [],                             // cụm loại trừ khi hai CD chồng chữ
  "he_so_gia_tri": 3,                           // 1 · 2 · 3 — id-G §3
  "trich": ["HT-002", "HT-047"]                 // ⛔ không được rỗng
}
```

---

## 3. NĂM NẤC 5A

| Nấc | Khách đang ở đâu | Câu hỏi đầu tiên có dạng | Nhiệm vụ của nội dung | Loại hook mạnh |
|---|---|---|---|---|
| **A1 · AWARE** | Có vấn đề nhưng chưa gọi tên | tả tình trạng bằng chữ của mình · gửi ảnh | **Định danh vấn đề**, phá 1 niềm tin sai. ⛔ Không bán | PHỦ ĐỊNH · NGHỊCH LÝ |
| **A2 · APPEAL** | Đang so phương pháp, lập shortlist | *"công nghệ nào tốt"* · *"loại nào khác gì"* | Giáo dục giải pháp + cho thấy khác biệt | SO SÁNH A–B · CON SỐ |
| **A3 · ASK** ★ | Điểm quyết định — nỗi sợ đạt đỉnh | *"bao nhiêu tiền"* · *"đau không"* · *"bác sĩ nào"* | **Gỡ nỗi sợ** + minh bạch giá + bằng chứng | GỌI TÊN NỖI SỢ · TIẾT LỘ NỘI BỘ |
| **A4 · ACT** | Đã inbox/đặt lịch, còn có thể huỷ | *"T7 còn suất không"* | Giảm huỷ lịch: checklist, lộ trình theo ngày | CON SỐ · CÂU HỎI THẦM |
| **A5 · ADVOCATE** | Đã làm, lo hậu phẫu | *"kiêng gì"* · *"bao giờ tái khám"* | Cẩm nang theo mốc · cross-sell 1 hướng · xin review | TIẾT LỘ NỘI BỘ · CON SỐ |

### Luật gán nấc

> Đọc **câu hỏi đầu tiên của khách**, ⛔ không đọc cả hội thoại.

⚠️ **Khách nhảy nấc.** Hỏi giá ngay câu đầu không có nghĩa là ở `A3` thật. Dấu hiệu: hỏi giá rồi hỏi tiếp *"mà làm thế nào"* → thực ra `A1`, ghi `A3→A1`.

★ **Tỷ lệ nấc là một chỉ số.** Trên 60% hội thoại rơi `A3` nghĩa là phễu **thiếu nội dung A1–A2** — tệp mới không vào. Kết luận này ⛔ không nhìn ra được từ số liệu ads.

⚠️ Nấc 5A **không phụ thuộc chân dung** — gán được ngay ở B2, trước CỔNG 0. Nhờ vậy tab Phễu và phân bố 5A vẫn đọc được khi chân dung còn trống.

---

## 4. MA TRẬN CD × 5A — Ô TRỐNG LÀ LỖ HỔNG PHỄU

Mỗi kỳ dựng **hai ma trận `N×5`** cạnh nhau, với `N` = số chân dung đã duyệt **+ 1 dòng `CD0`**:

```
TRÁI : số NỘI DUNG ĐANG CÓ cho ô đó
PHẢI : số HỘI THOẠI rơi vào ô đó trong kỳ

ô PHẢI cao  × TRÁI = 0    →  ① LỖ HỔNG — ưu tiên 1
ô PHẢI cao  × TRÁI cao    →  ② nội dung đang trả lời SAI → kiểm trước khi làm thêm
ô PHẢI thấp × TRÁI cao    →  ③ ĐANG PHÍ — cắt bớt
ô PHẢI thấp × TRÁI thấp   →  ④ để yên
```

⚠️ **Ô ③ khó chấp nhận hơn ô ①** vì nó nói rằng kỳ trước khối đã làm nhiều nội dung không ai cần. Vẫn phải ghi ra — không ghi thì kỳ sau lại làm tiếp.

⚠️ Ma trận kỳ này so được với kỳ trước **chỉ ở những mã được giữ nguyên** (§1). Mã mới thì ghi `⚠ chưa có mốc so sánh`.

---

## 5. THÔNG ĐIỆP THẮNG — VIẾT TỪ KỲ NÀY, ⛔ KHÔNG LẤY TỪ KHO

Bản trước của sổ này chở một bảng *"thông điệp thắng"* viết sẵn cho từng chân dung mũi. ⛔ **Đã bỏ.** Thông điệp dán sẵn làm hai việc đều sai cùng lúc: nó nói hộ khách, và nó mang theo đúng những câu `id-K` đang chặn (*trọn đời* · *tỷ lệ thành công* · *đổi vận*).

Thay vào đó mỗi chân dung được duyệt viết **một câu dựng tại kỳ**, theo khuôn:

```
<điều khách sợ, bằng chữ của khách>  →  <điều mình làm khác>  →  <bằng chứng>
```

| Phải có | ⛔ Phải không có |
|---|---|
| Một `HT-nnn` truy ngược | Con số bảo hành (`id-K` §3) |
| Chữ khách dùng, không phải tính từ | Cam kết kết quả chắc chắn |
| Một điều mình làm khác được | Hứa đổi vận, tài lộc, tỷ lệ thành công |
| Qua **CỔNG 2** trước khi phát | Giá dịch vụ chưa có bảng hiện hành |

★ Viết bằng **chữ của khách**. Khách không tìm *"đẹp tự nhiên"* — khách tìm *"đầu mũi bóng đỏ"*.

---

## 6. ★ CƠ HỘI WIN — XẾP HẠNG CHÂN DUNG ĐỂ BIẾT DỒN SỨC VÀO ĐÂU

Bảng chân dung nói *có những ai*. Nó ⛔ không nói *làm ai trước*. Xếp theo số HT là xếp theo nhóm ĐÔNG nhất, không phải nhóm **đáng làm nhất**.

```
Điểm win = lead đang bỏ lỡ × hệ số giá trị đơn × tỷ lệ ĐANG CHỐT ĐƯỢC của chính nhóm
```

| Thành phần | Là gì | Lấy ở đâu |
|---|---|---|
| **lead đang bỏ lỡ** | HT của nhóm **chưa có SĐT** — phần còn lấy lại được | bảng chân dung |
| **hệ số giá trị đơn** | 1 · 2 · 3 | bản phác họa (`id-G` §3) |
| **tỷ lệ đang chốt được** | `% có SĐT` quan sát được của chính nhóm đó | bảng chân dung |

★ **Cả ba đều là số ĐÃ ĐO của kỳ.** ⛔ Không có hệ số nào tự đặt — đó là điều kiện để bảng này còn cãi được (luật ⑨).

★ **Vì sao nhân với tỷ lệ đang chốt được.** Một nhóm đã chốt tốt là nhóm mà công sức bỏ thêm sinh lời nhanh nhất. Nhóm đang chốt kém *vì câu trả lời của trực page* thì điểm thấp là ĐÚNG — việc của nó nằm ở ô `🔧 sửa vận hành` của ma trận, **sửa câu trả lời trước, làm nội dung sau**. Hai việc khác nhau, ⛔ không trộn vào một bảng xếp hạng.

```
⛔ CD0 KHÔNG được xếp hạng — nó là mã dự trữ, không phải một chân dung (§1).
   Vẫn để trong bảng để tổng còn khớp, nhưng luôn nằm cuối và không chiếm một bậc.

★ Thẻ insight xếp theo ĐÚNG thứ hạng này, mỗi thẻ mang theo hạng của mình.
   Người đọc lướt từ trên xuống là đang đọc theo thứ tự đáng làm.
```

⚠️ Điểm win là **đề xuất thứ tự**, ⛔ không thay CỔNG 1. Ma trận ưu tiên vẫn do người dùng duyệt.

---

## 7. ĐẦU RA CHUẨN CỦA BƯỚC B3

```
① BẢN PHÁC HỌA   : out/chan-dung.json — mã · tên · họ là ai · nỗi sợ · dấu hiệu
                    · hệ số · trích        → chờ CỔNG 0
② BẢNG CHÂN DUNG : CD · tên · số HT · HOT/WARM/COLD · có SĐT · % có SĐT
                    · chốt lịch · bỏ 1 lượt · rơi do trực page   (+ dòng CD0)
②' CƠ HỘI WIN    : hạng · lead bỏ lỡ · hệ số · đang chốt · điểm win  (§6)
③ THẺ INSIGHT    : mỗi CD ≥5 HT một thẻ — họ là ai · insight · câu hỏi ngầm
                    · tín hiệu nóng · hướng xử lý
④ MA TRẬN CD×5A  : hai bảng N×5, đánh dấu ô ① và ô ③
⑤ SO KỲ TRƯỚC    : % có SĐT từng CD thay đổi mấy ĐIỂM phần trăm
                    — chỉ với những mã được giữ nguyên
```

⛔ Chân dung dưới **5 HT** không viết thẻ insight — chỉ ghi vào danh sách `👁 quan sát`.

---

## 8. TỰ KIỂM SỔ NÀY

- [ ] Chân dung kỳ này có được **phác họa từ hội thoại của kỳ này** không, hay chép từ kỳ trước cho nhanh?
- [ ] Mỗi chân dung có gọi tên được **một nỗi sợ riêng** không?
- [ ] Có chân dung nào lấy **tên dịch vụ** làm tên không?
- [ ] Tên chân dung viết bằng **chữ của khách** hay bằng tính từ của người viết?
- [ ] Mỗi chân dung có ít nhất một `HT-nnn` làm bằng không?
- [ ] Tổng HT các chân dung **cộng cả `CD0`** có bằng đúng cỡ mẫu phân tích không?
- [ ] `CD0` có bị gọi là "rác" hay bị bỏ qua không? `CD0` ≥ 15 HT đã xét tách thêm chân dung chưa?
- [ ] Chân dung cùng nỗi sợ với kỳ trước có **giữ nguyên mã** không?
- [ ] Bản phác họa đã qua **CỔNG 0** chưa — `duyet_boi` có tên người thật chưa?
- [ ] Thẻ insight có viết bằng **chữ của khách** không, hay toàn tính từ của người viết?
- [ ] Thẻ insight có xếp theo **điểm cơ hội win** không, hay vẫn xếp theo số HT?
- [ ] Có hệ số nào trong công thức win là **tự đặt** không?

---

<!-- ===== id-D-dao-sau-insight.md ===== -->

# id-D · ★ ĐÀO SÂU INSIGHT — MÃ `O` · MỨC NÓNG · VÌ SAO RƠI

> Sổ sinh ra giá trị lớn nhất của agent. Số liệu ads cho biết **cái gì đã chạy**; hội thoại cho biết **cái gì còn thiếu**.
>
> ⛔ Luật tối thượng: **một insight không truy ngược được về `HT-nnn` hoặc một con số là một insight bịa.**

---

## 1. MƯỜI HAI MÃ PHẢN ĐỐI `O-01` … `O-12`

> **Danh sách đóng.** Không xếp được thì gán `O-00` và đếm riêng. `O-00` vượt 10% mẫu là tín hiệu danh sách cần bổ sung → **báo lại**, ⛔ đừng tự thêm mã.

| Mã | Tên | Khách hay nói | Nấc | Nội dung đóng được nó |
|---|---|---|---|---|
| `O-01` | **Giá & phát sinh** | *"bao nhiêu tiền"* · *"trọn gói gồm gì"* | `A3` | Bảng giá minh bạch + liệt kê quyền lợi |
| `O-02` | **Sợ kết quả xấu hơn** | *"làm xong có xấu hơn không"* | `A1`–`A2` | Before/After **cùng nhóm tình trạng** |
| `O-03` | **Sợ lộ sửa** | *"trông giả không"* | `A2` | Thiết kế dáng cá nhân hoá |
| `O-04` | **Đau · sưng · nghỉ việc** | *"mấy ngày đi làm được"* | `A3` | Mốc hồi phục 1–3–7–30 **do BS duyệt** |
| `O-05` | ★ **Nghi tay nghề bác sĩ** | *"ai mổ cho em"* | `A3` | Nhân hiệu bác sĩ → bàn giao `Agent-SeedingPlant` |
| `O-06` | **Nghi địa chỉ, uy tín** | *"bệnh viện hay spa"* | `A2` | Số giấy phép + tuyến bệnh viện |
| `O-07` | **Bảo hành & trách nhiệm** | *"bảo hành mấy năm"* | `A3` | 🔴 **ĐANG BỊ CHẶN** (`id-K` §3) |
| `O-08` | **Không biết mình cần gì** | *"em gửi ảnh bác xem"* | `A1` | CTA *"gửi ảnh để bác sĩ check"* |
| `O-09` | **Thời gian · khoảng cách** | *"em ở tỉnh"* · *"em về nước 10 ngày"* | `A4` | Lịch, đưa đón, tư vấn online trước |
| `O-10` | **So sánh đối thủ** | *"bên kia rẻ hơn"* | `A3` | Khác biệt cụ thể — ⛔ không dìm đối thủ |
| `O-11` | **Người nhà phản đối** | *"chồng em không cho"* | `A3` | Nội dung **nói với người nhà** |
| `O-12` | **Bệnh nền** | *"em bị tiểu đường"* · *"đang cho con bú"* | `A3` | 🔴 **BS duyệt từng câu** |

### Ba mã hay bị bỏ sót nhất

| Mã | Vì sao bị bỏ sót | Vì sao đáng làm |
|---|---|---|
| `O-11` · người nhà | Khách nói một lần rồi im nên đếm ra ít | **Người quyết không phải người hỏi.** Một clip *"gửi mẹ xem đi"* đóng được việc mà 10 clip nói với khách không đóng nổi |
| `O-09` · ở xa / về nước ngắn ngày | Bị gộp nhầm vào `O-01` | Đây là **quyền lợi dịch vụ, không phải claim y khoa** → sạch pháp chế, viết được ngay |
| `O-05` · nghi bác sĩ | Trực page trả lời xong khách im, tưởng đã xử xong | Là bằng chứng trực tiếp phải đẩy nhân hiệu bác sĩ |

### ⛔ Hai mã agent không được tự trả lời

```
O-07 bảo hành → hệ thống đang có BA mức cùng lưu hành (3 năm / 10 năm / trọn đời).
                ⛔ Không viết con số nào. Viết "chính sách bảo hành bằng văn bản".
O-12 bệnh nền → claim y khoa. Chỉ viết "trường hợp này cần bác sĩ khám trực tiếp đánh giá".
```

---

## 2. MỨC NÓNG — NĂM TÍN HIỆU

Một hội thoại được chấm **HOT / WARM / COLD** theo số tín hiệu đạt:

| # | Tín hiệu | Đạt khi |
|---|---|---|
| ① | **Nêu dịch vụ cụ thể** | Khách gọi tên dịch vụ hoặc tả vùng muốn làm |
| ② | **Mốc thời gian ≤ 14 ngày** | *"tuần này"*, *"trước Tết"*, *"có đám cưới 20/11"* |
| ③ | **Cho số điện thoại** | |
| ④ | **Hỏi điều kiện thực hiện** | giá cụ thể · lịch · bác sĩ · cơ sở nào |
| ⑤ | **Đồng ý khung giờ gọi** | Khách nói giờ nghe máy được |

| Mức | Số tín hiệu |
|---|---|
| 🔴 **HOT** | 4–5 |
| 🟠 **WARM** | 2–3 |
| ⚪ **COLD** | 0–1 |

⚠️ **Tín hiệu ② và ⑤ là hai tín hiệu hiếm nhất** và chính là lý do HOT luôn ít. Nếu HOT < 2% mẫu thì vấn đề **không phải tệp xấu** — là nội dung không tạo mốc thời gian và trực page không hỏi khung giờ gọi. Hai việc này sửa được ngay trong kỳ.

★ Nhãn nóng ở đây là nhãn **duy nhất** của một kỳ. `id-L` (KF-60) dùng nó để xếp hàng gọi nhưng ⛔ **không phát nhãn thứ hai** — xem `id-L` §7.2 để biết vì sao.

★ **Ô nguy hiểm nhất của cả dashboard:** `HOT` hoặc `WARM` **chưa có SĐT**. Đó là lead nóng chưa vào tay telesale — tô đỏ, đếm riêng, đưa lên thẻ số tổng.

---

## 3. VÌ SAO RƠI — MỖI HỘI THOẠI MỘT GIÁ TRỊ

> ⛔ Một hội thoại chỉ được gán **đúng một** nguyên nhân rơi. Gán hai là tổng không khớp cỡ mẫu.

| Nguyên nhân | Nhận ra khi | Ai sửa |
|---|---|---|
| **nội dung** | Khách vào rồi hỏi thứ quảng cáo đã hứa mà nội dung không có | Marketing |
| **trực page** | Khách hỏi, được trả lời, rồi im — hoặc bị bỏ sau 1 lượt | Trực page |
| **hệ thống** | Thiếu giá chính thức · page không có dịch vụ khách hỏi · ngoài giờ | Hệ thống / vận hành |
| **khách tự dừng** | Khách nói *"để em suy nghĩ"* rồi không quay lại dù đã được trả lời đủ | — |
| **không rơi** | Có SĐT hoặc chốt lịch trong chat | — |

⚠️ *"Khách rơi **sau khi** được trả lời"* là tín hiệu mạnh hơn *"khách không hỏi"*. **Rơi sau khi được trả lời là lỗi nội dung hoặc lỗi câu trả lời, không phải lỗi tệp.**

---

## 4. RÀO CẢN QUAN SÁT ĐƯỢC — ĐƯỢC PHÉP NHIỀU

Khác với "vì sao rơi", một hội thoại **có thể mang nhiều rào cản**. Đếm theo lượt xuất hiện:

`chưa nói tình trạng` · `hỏi giá ngay` · `sợ đau/nghỉ việc` · `ở xa` · `người nhà cản` ·
`đã làm nơi khác` · `so giá đối thủ` · `chờ ưu đãi` · `chưa tin cơ sở`

---

## 5. ★ BẢNG GIAO "YẾU GÌ" — ĐẦU RA THẬT CỦA BƯỚC B5

| `MÃ O` | `SỐ LẦN HỎI /100 HT` | `SỐ NỘI DUNG ĐÃ CÓ` | `KẾT LUẬN` |
|---|---|---|---|

### Luật đọc bảng — bốn ô

```
                      nội dung ĐÃ CÓ nhiều        nội dung ĐÃ CÓ ít
                  ┌──────────────────────────┬──────────────────────────┐
  khách hỏi NHIỀU │ ② ĐANG ĐÚNG HƯỚNG        │ ① LỖ HỔNG — ƯU TIÊN 1    │
                  │   nhưng có thể trả lời SAI│   nhu cầu có, nội dung   │
                  │   → kiểm trước khi làm thêm│   không. Viết ngay.      │
                  ├──────────────────────────┼──────────────────────────┤
  khách hỏi ÍT    │ ③ ĐANG PHÍ               │ ④ ĐỂ YÊN                 │
                  │   → cắt bớt               │                          │
                  └──────────────────────────┴──────────────────────────┘
```

### Ngưỡng ra việc

| Số lần / 100 hội thoại | Việc |
|---|---|
| **≥ 15** | Mở **tuyến riêng** trong kỳ — ≥ 2 nội dung, có format riêng |
| **8 – 14** | **Một hook** trong kỳ |
| **5 – 7** | Ghi nhận, gộp làm ý phụ trong nội dung khác |
| **< 5** | ⛔ Không lên kế hoạch. Ghi sổ theo dõi |

⚠️ Mẫu < 50 HT thì ⛔ không dùng ngưỡng tuyệt đối, chỉ xếp hạng tương đối và gắn nhãn `MẪU NHỎ`.

---

## 6. CÂU HỎI NGẦM — THỨ LÀM NÊN THẺ INSIGHT

> Câu khách gõ **không phải** điều khách muốn biết. Thẻ insight phải dịch được câu đó.

```
Khách gõ : "Giá bao nhiêu?"
Câu ngầm : "Giá trên quảng cáo có đúng với mình không,
            và cho số thì có bị gọi làm phiền không?"

Khách gõ : "Bác sĩ nào làm?"
Câu ngầm : "Người mổ cho tôi có đủ giỏi để tôi không thành ca hỏng không?"

Khách gõ : "Em ở tỉnh"
Câu ngầm : "Tôi phải nghỉ mấy ngày, ở đâu, ai đưa tôi về?"
```

★ Viết câu ngầm bằng **chữ của khách**, ⛔ không bằng tính từ marketing. Khách không tìm *"đẹp tự nhiên"* — khách tìm *"đầu mũi bóng đỏ"*.

---

## 7. ĐỌC NỬA TRỰC PAGE TRẢ LỜI — INSIGHT TẦNG HAI

| Dấu hiệu trong câu trả lời | Nghĩa là |
|---|---|
| Gõ đoạn dài giải thích **cùng một thứ** ở nhiều hội thoại | ★ **Thiếu hẳn một nội dung.** Việc này đáng lẽ clip làm |
| Gửi ảnh chụp màn hình bảng giá | Thiếu nội dung giá chính thức → làm ngay, lại sạch pháp chế |
| Xin số ngay câu đầu | Đang **né câu hỏi** → nội dung không giải quyết được mã `O` đó |
| Khách hỏi → được trả lời → im luôn | Câu trả lời **không đóng được nỗi sợ** |

★ Ở agent này, tầng hai có **hai đích đến** — khác với `Agent-SeedingPlant`, nơi nó chỉ là đầu vào nội dung:

1. **đầu vào làm nội dung** (ô ① của `id-C` §3), và
2. **bằng chứng chấm điểm** ở `id-F` — ⛔ chỉ khi gắn được vào đúng tiêu chí `N1…N6` và đúng `HT-nnn`.

⛔ Nhận xét chung chung kiểu *"bạn này tư vấn hời hợt"* mà không chỉ ra tiêu chí + hội thoại thì **không được ghi vào bất cứ đâu**.

---

## 8. ĐẦU RA CHUẨN CỦA BƯỚC B2–B5

```
① BẢNG ĐẾM MÃ O   : 12 mã × số lần × % mẫu (kể cả mã = 0)
② MỨC NÓNG        : HOT/WARM/COLD × trạng thái SĐT (ô HOT/WARM chưa có SĐT tô đỏ)
③ VÌ SAO RƠI      : 5 nguyên nhân, tổng = cỡ mẫu
④ RÀO CẢN         : xếp theo lượt xuất hiện
⑤ BẢNG GIAO §5    : 4 cột + kết luận theo 4 ô
⑥ TOP 10 CÂU CHÉP : câu hỏi đầu tiên hay nhất, nguyên văn, đã ẩn danh, kèm HT-nnn
⑦ CỠ MẪU          : đọc bao nhiêu · bỏ bao nhiêu · vì sao
```

---

## 9. TỰ KIỂM SỔ NÀY

- [ ] Đếm đủ 12 mã, kể cả mã bằng 0?
- [ ] `O-00` có vượt 10% không? Vượt thì đã báo lại chưa?
- [ ] Tổng "vì sao rơi" có **bằng đúng** cỡ mẫu không?
- [ ] Ô `HOT/WARM chưa có SĐT` có được đưa lên thẻ số tổng không?
- [ ] Mỗi insight có gắn `HT-nnn` truy ngược được không?
- [ ] Đã bỏ hết tên/SĐT/ảnh khách chưa?
- [ ] `O-07` và `O-12` có bị tự trả lời không?

---

<!-- ===== id-E-to-chuc-ads-chi-so.md ===== -->

# id-E · ★ TỔ CHỨC ADS & ĐỌC CHỈ SỐ — FACEBOOK + GOOGLE

> Sổ này trả lời hai câu: **quảng cáo Kangnam được tổ chức thế nào** (để cắt số đúng chiều), và **đọc số ra kết luận gì** (để không chữa nhầm bệnh).
> Nguồn: sheet `5. Tổ chức Ads`, sheet `Giao ban`, và dashboard *"Kangnam – Hiệu quả quảng cáo Meta"*.

---

## 1. CHUỖI CHỈ SỐ — GIỮ ĐÚNG THỨ TỰ

```
Chi phí tổng → CPM → CTR → CPI (Inbox) → CPL (Lead) → CPB (Booking) → Booking/Lead
```

Mỗi mắt xích hiện **ba thứ**: giá trị · so **mục tiêu** · so **kỳ trước**.

| Chỉ số | Công thức | Mục tiêu lấy từ đâu |
|---|---|---|
| ★ **Chi phí tổng** | Σ chi của kỳ | ngân sách kỳ · ⛔ không có «mốc tốt/xấu» |
| **CPM** | chi ÷ hiển thị × 1.000 | TB 30 ngày của dịch vụ |
| **CTR** | click ÷ hiển thị | TB 30 ngày của dịch vụ |
| **CPI** | chi ÷ inbox | TB 30 ngày của dịch vụ |
| **CPL** | chi ÷ lead SĐT hợp lệ | TB 30 ngày của dịch vụ |
| **CPB** | chi ÷ booking | TB 30 ngày của dịch vụ |
| **Booking/Lead** | booking ÷ lead | so kỳ trước, tính bằng **điểm %** |

★ **Mắt xích 0 là số tiền đã tiêu.** CPI, CPL, CPB đều là thương của cùng một tử số — không nhìn tử số thì đang đọc tỷ lệ trong chân không. ⚠ **CPL giảm mà chi cũng giảm theo thì chưa chắc đã tốt lên**: có thể chỉ là chạy ít đi. Ô này đi kèm số nội dung · hiển thị · inbox · lead · booking của kỳ để thấy ngay quy mô.

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

---

<!-- ===== id-F-cham-diem-nhan-vien.md ===== -->

# id-F · ★★ TIÊU CHÍ CHẤM ĐIỂM & PHÂN LOẠI NHÂN VIÊN TRỰC PAGE

> Sổ nhạy cảm nhất của repo. Nó tạo ra một con số gắn với **tên một con người**.
> ⛔ Chưa đọc hết §1 và §7 thì ⛔ không được chấm.

---

## 1. VÌ SAO AGENT NÀY CHẤM ĐIỂM SỐ CÒN `Agent-QC-Telesale` THÌ KHÔNG

`Agent-QC-Telesale` cố tình **không** cho điểm số, vì cuộc gọi có `K6 · giọng & ngữ điệu` — nhóm chỉ chấm được khi có audio, và bản ghi hay mất tiếng. Điểm số ở đó tạo cảm giác chính xác mà dữ liệu không có.

Chat thì khác ở ba điểm:

```
① Bằng chứng ĐẦY ĐỦ — mọi chữ đều được lưu, không có "mất tiếng".
② Mốc thời gian CHÍNH XÁC đến giây — SLA đo được, không phải cảm nhận.
③ Không có nhóm nào phụ thuộc âm thanh — mọi tiêu chí đều đọc được từ văn bản.
```

Nhưng điểm số vẫn chỉ hợp lệ khi đi kèm **bốn rào an toàn ở §7**. ⛔ Bỏ một rào là sổ này thành công cụ kỷ luật, không còn là công cụ kèm cặp.

---

## 2. CÁCH CHẤM — HAI TẦNG

```
TẦNG 1 · từng hội thoại : mỗi tiêu chí chấm ✓ / ✗ / —
TẦNG 2 · từng nhân viên : quy ra điểm 0–100 khi đủ mẫu, rồi phân loại A/B/C/D
```

| Ký hiệu | Khi nào | Tính điểm thế nào |
|---|---|---|
| `✓` **ĐẠT** | Có bằng chứng trong hội thoại | Cộng đủ điểm tiêu chí |
| `✗` **CHƯA ĐẠT** | Có bằng chứng là **không làm** hoặc **làm sai** | 0 điểm |
| `—` **KHÔNG ÁP DỤNG** | Tình huống không phát sinh (khách không hỏi giá thì không chấm tiêu chí giá) | ⛔ **Loại khỏi mẫu số**, ⛔ không tính là trượt |

### Công thức

```
Điểm một hội thoại = (tổng điểm ✓) ÷ (tổng điểm các tiêu chí KHÔNG phải "—") × 100

Điểm một nhân viên = trung bình điểm các hội thoại của người đó trong kỳ
```

⚠️ `—` **không phải** `✗`. Gộp hai cái này là cách làm cho một nhân viên trông tệ chỉ vì khách của bạn ấy không hỏi giá.

---

## 3. SÁU NHÓM TIÊU CHÍ — THANG 100

### `N1` · PHẢN HỒI & SLA — **20 điểm**

| Mã | Tiêu chí | Điểm | Đạt khi |
|---|---|---|---|
| `N1.1` | Trả lời tin đầu **≤ 2 phút** | 8 | Trong khung 8h30–22h. Ngoài khung → `—` |
| `N1.2` | Không để khách **bỏ sau 1 lượt** | 6 | Khách nhắn ≥2 lượt, hoặc NV có ít nhất 1 lượt đuổi theo |
| `N1.3` | Không bỏ sót tin khách trong ca | 3 | Mọi câu hỏi của khách đều được chạm tới |
| `N1.4` | **Theo đuổi lại** khi khách im | 3 | Có ≥1 tin chủ động sau khi khách im > 30 phút |

### `N2` · KHAI THÁC TÌNH TRẠNG — **20 điểm**

| Mã | Tiêu chí | Điểm | Đạt khi |
|---|---|---|---|
| `N2.1` ★ | Hỏi tình trạng **trước khi** báo giá hoặc xin số | 8 | Có ≥1 câu hỏi tình trạng trước lần nhắc giá / xin số đầu tiên |
| `N2.2` | Có ≥2 **câu hỏi mở** | 4 | Câu hỏi không trả lời được bằng có/không |
| `N2.3` | Mời **gửi ảnh / tả vùng** cụ thể | 4 | |
| `N2.4` | **Nhắc lại** đúng điều khách vừa nói | 4 | Có ít nhất 1 lần |

> ⚠️ **`N2.1` trượt là lỗi đắt nhất trong cả bộ.** Xin số trước khi biết khách cần gì biến cuộc tư vấn thành cuộc đòi số — và khách cho số xong thì không còn lý do gì để nghe tiếp. Trong dữ liệu thật, đây là tiêu chí trượt nhiều nhất.

### `N3` · TRẢ LỜI ĐÚNG & MINH BẠCH — **20 điểm**

| Mã | Tiêu chí | Điểm | Đạt khi |
|---|---|---|---|
| `N3.1` | **Nêu khung giá** khi khách hỏi giá | 6 | Có nêu khoảng giá hoặc nói rõ vì sao chưa nêu được. Né hẳn = `✗` |
| `N3.2` | Thông tin **khớp bảng hiện hành** | 5 | Giá · ưu đãi · thời gian khớp văn bản đang hiệu lực |
| `N3.3` | ⛔ Không **cam kết kết quả** | 5 | Không có câu hứa chắc chắn → vi phạm là **cờ đỏ `CĐ-1`** |
| `N3.4` | ⛔ Không **nói quá về bác sĩ / chứng chỉ** | 4 | Chỉ nói thông tin có trong hồ sơ → vi phạm là **cờ đỏ `CĐ-4`** |

⚠️ **`N3.1` phải tách được hai loại trượt** (xem `id-K` §3):
- *lỗi người* — đã có giá trong tay mà vẫn né;
- *lỗi hệ* — hệ thống **chưa cấp giá** cho dịch vụ đó.

⛔ Trừ điểm nhân viên cho **lỗi hệ** là sai. Loại đó chấm `—` và đẩy lên mục "việc hệ thống" của dashboard.

### `N4` · XỬ LÝ RÀO CẢN — **15 điểm**

| Mã | Tiêu chí | Điểm | Đạt khi |
|---|---|---|---|
| `N4.1` | **Nhận diện đúng** mã `O` khách nêu | 5 | Câu trả lời chạm đúng điều khách sợ |
| `N4.2` | **Xử đúng tầng** | 5 | Từ chối vì **giá** thì không trả lời bằng **chất lượng**, và ngược lại |
| `N4.3` | **Giữ cửa mở** | 5 | Có câu để lại đường quay lại, kể cả khi khách từ chối |

### `N5` · XIN SỐ & CHỐT — **20 điểm**

| Mã | Tiêu chí | Điểm | Đạt khi |
|---|---|---|---|
| `N5.1` | Xin số có **lý do cụ thể** | 6 | Nói rõ gọi để làm gì, mất bao lâu. *"Chị cho em xin số"* trống không = `✗` |
| `N5.2` | Xin lại **lần 2 khác cách** | 4 | Lần 2 không lặp nguyên văn lần 1 |
| `N5.3` | Hỏi **khung giờ nghe máy** | 4 | ★ Đây là tín hiệu ⑤ của mức nóng (`id-D` §2) |
| `N5.4` | Mời lịch **cụ thể ngày + giờ** | 6 | *"Khi nào rảnh chị qua"* = `✗`. *"Chiều mai 3h em giữ chỗ"* = `✓` |

> ⚠️ **`N5.4` nối thẳng với doanh số.** Hai câu trên là hai hội thoại khác nhau về bản chất dù phần tư vấn phía trước giống hệt.

### `N6` · NGÔN TỪ & THÁI ĐỘ — **5 điểm**

| Mã | Tiêu chí | Điểm | Đạt khi |
|---|---|---|---|
| `N6.1` | Không dán khối dài **lệch câu hỏi** | 2 | Đoạn copy-paste phải trả lời đúng điều khách vừa hỏi |
| `N6.2` | Xưng hô, chính tả, viết tắt đọc được | 2 | |
| `N6.3` | Không gắt, không ép khách | 1 | Vi phạm nặng → **cờ đỏ `CĐ-6`** |

**Tổng: 20 + 20 + 20 + 15 + 20 + 5 = 100**

---

## 4. PHÂN LOẠI A / B / C / D

| Loại | Điểm | Nghĩa vận hành | Sổ tay nhận được |
|---|---|---|---|
| 🟢 **A** | **≥ 85** | Làm chuẩn. Dùng hội thoại của người này làm mẫu cho khối | Sổ tay **mẫu lan toả** — 1 việc nâng cấp + 2 đoạn chat mẫu để chia sẻ |
| 🔵 **B** | **70 – 84** | Vững, hụt 1–2 nhóm | Sổ tay **sửa đúng một nhóm yếu nhất** |
| 🟡 **C** | **55 – 69** | Hụt nhiều nhóm, cần kèm | Sổ tay **2 việc + kịch bản mẫu + kèm cặp theo tuần** |
| 🔴 **D** | **< 55** | Đang làm mất lead đều đặn | Sổ tay **1 việc duy nhất** + ngồi cùng trưởng nhóm đọc lại 5 hội thoại |

⚠️ **Một cờ đỏ (`§5`) trong kỳ → trần điểm của hội thoại đó là 49**, và nhân viên ⛔ **không được xếp loại A** dù điểm trung bình cao.

---

## 5. SÁU CỜ ĐỎ `CĐ-1` … `CĐ-6`

> Cờ đỏ ⛔ **không phải lỗi trừ điểm thông thường**. Mỗi cờ đỏ được **báo riêng, kèm nguyên văn câu nói và `HT-nnn`**, và phải có người xử lý đích danh.

| Mã | Cờ đỏ | Vì sao nghiêm trọng |
|---|---|---|
| `CĐ-1` | **Cam kết kết quả chắc chắn** | Claim y khoa — rủi ro pháp lý, không chỉ rủi ro bán hàng |
| `CĐ-2` | **Nêu con số bảo hành** (*trọn đời* · *10 năm*) | Ba mức đang cùng lưu hành, chưa có văn bản (`id-K` §3) |
| `CĐ-3` | **Trả lời câu bệnh nền / chống chỉ định** thay bác sĩ | `O-12` — phải bác sĩ khám |
| `CĐ-4` | **Nói quá chức danh / bằng cấp bác sĩ** chưa đối chiếu | Hai bác sĩ đang chạy ads vẫn chưa xác minh chứng chỉ |
| `CĐ-5` | **Lộ thông tin khách khác** — nhắc tên, số, ca của người khác | Vi phạm riêng tư, mất niềm tin cả page |
| `CĐ-6` | **Dìm đối thủ / gắt với khách** | Rủi ro thương hiệu, có thể bị chụp màn hình |

---

## 6. ĐIỀU KIỆN ĐỦ MẪU

| Số HT của một nhân viên trong kỳ | Agent được làm gì |
|---|---|
| **< 5** | ⛔ Không chấm. Ghi `chưa đủ mẫu` |
| **5 – 9** | Chấm từng hội thoại, ⛔ **không cho điểm tổng, không phân loại** |
| **≥ 10** | ✅ Cho điểm tổng + phân loại A/B/C/D |
| **≥ 10 và liên tục 2 kỳ** | ✅ Được vẽ xu hướng, được so với kỳ trước |

⚠️ Nhân viên có **ca trực lệch giờ** (ca đêm, ca cuối tuần) thì tiêu chí `N1.1` phải tính theo **khung giờ của ca đó**, ⛔ không dùng khung chung 8h30–22h.

---

## 7. ★ BỐN RÀO AN TOÀN — ⛔ BỎ MỘT CÁI LÀ SỔ NÀY VÔ HIỆU

```
① ĐIỂM ĐỂ KÈM CẶP, KHÔNG ĐỂ KỶ LUẬT.
   Mọi bảng điểm phải mang đúng câu này ở chân bảng:
   "Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay xếp hạng công khai."

② MỖI ĐIỂM TRỪ PHẢI CÓ BẰNG CHỨNG.
   Một ô ✗ không gắn được HT-nnn + nguyên văn câu → đổi thành "—".
   ⛔ Không có bằng chứng thì không có điểm trừ.

③ LỖI HỆ KHÔNG TRỪ ĐIỂM NGƯỜI.
   Thiếu bảng giá · page không có dịch vụ · hệ thống ngoài giờ · công cụ lỗi
   → chấm "—" và đẩy lên mục "việc hệ thống", ⛔ không trừ nhân viên.

④ KHÔNG XẾP HẠNG CÔNG KHAI TOÀN KHỐI.
   Dashboard hiện phân bố A/B/C/D và chỉ số cả đội.
   Tên + điểm cá nhân CHỈ xuất hiện trong sổ tay RIÊNG của người đó
   và bản của trưởng nhóm. ⛔ Không có bảng xếp hạng dán lên màn hình chung.
```

⚠️ Rào ③ là rào hay bị quên nhất. Trong dữ liệu thật, một phần lớn ô *"né giá"* là **lỗi hệ** — hệ thống chưa cấp giá dịch vụ ngoài mắt. Trừ điểm nhân viên vì chuyện đó là chấm sai người.

---

## 8. ĐẦU RA CHUẨN CỦA BƯỚC B6

```
① PHÂN BỐ      : số người loại A/B/C/D + số người chưa đủ mẫu
② CHỈ SỐ ĐỘI   : % đạt từng nhóm N1…N6 — đây là thứ đưa lên dashboard
③ BẢNG CÁ NHÂN : tên · số HT · điểm · loại · nhóm yếu nhất · nhóm mạnh nhất
                 (⛔ chỉ vào sổ tay riêng + bản trưởng nhóm)
④ CỜ ĐỎ        : từng cờ · ai · HT-nnn · nguyên văn · người xử lý
⑤ VIỆC HỆ THỐNG: các ô "—" do lỗi hệ, gom theo nguyên nhân
⑥ TIÊU CHÍ YẾU NHẤT CỦA KHỐI : 3 tiêu chí trượt nhiều nhất → thành nội dung đào tạo kỳ sau
```

---

## 9. TỰ KIỂM SỔ NÀY

- [ ] Mọi `✗` đều có `HT-nnn` + nguyên văn câu chưa?
- [ ] Có ô nào là **lỗi hệ** mà bị chấm `✗` không?
- [ ] `—` có bị cộng vào mẫu số không?
- [ ] Người dưới 10 HT có bị phân loại không?
- [ ] Có bảng xếp hạng cá nhân nào lọt ra ngoài sổ tay riêng không?
- [ ] Câu *"Điểm dùng để kèm cặp…"* có ở chân mọi bảng điểm không?
- [ ] Cờ đỏ có được báo riêng kèm người xử lý đích danh không?

---

<!-- ===== id-G-ma-tran-uu-tien.md ===== -->

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
| ② | **GIẢM COLD** | Làm khách nói được tình trạng ngay từ quảng cáo | HT `COLD` của `CD0` (ô dự trữ — xem `id-C` §1) + HT tin đầu chỉ hỏi giá/địa chỉ |
| ③ | **TỐI ƯU WARM** | Gỡ rào cản làm WARM đứng lại | HT `WARM` đạt 2/5, có mã `O` rõ |

★ **Thứ tự này không đảo được.** Khối ① rẻ nhất (lead đã gần chín), khối ② đông nhất nhưng chậm, khối ③ là phần còn lại. Làm ② trước ① là bỏ tiền kéo người lạ trong khi người sắp mua đang đứng ngay đó.

---

## 3. CÔNG THỨC ĐIỂM

```
Điểm một ô = Σ ( lead bỏ lỡ trong ô × hệ số giá trị đơn )
```

### Hệ số giá trị đơn — theo dịch vụ chính khách hỏi

⚠️ Hệ số đi theo **dịch vụ**, ⛔ không đi theo chân dung. Một chân dung có thể khai sẵn `he_so_gia_tri` trong bản phác họa (`id-C` §2) — khi có, hệ số đó thắng, vì nó là kết luận của người đã đọc cả tệp.

| Bậc | Giá trị đơn ước tính | Hệ số |
|---|---|---|
| Thấp | < 5 triệu | **1** |
| Trung | 5 – 15 triệu | **2** |
| Cao | ≥ 15 triệu | **3** |
| ⚠ Chưa có giá hoặc khách không nêu dịch vụ | | **1** ⚠ |

⚠️ Giá trị đơn **ước từ bảng giá chuẩn**, không phải doanh thu thật. Mọi ô dùng hệ số đều gắn `⚠`. Khi hệ thống cấp bảng giá hiện hành (`id-K` §3), thay số thật vào và ghi lại ở `doc/CHANGELOG.md`.

### Ví dụ đọc một dòng

```
CD1 · "Đã làm rồi, đi sửa" · khối ① Tăng HOT
  (chân dung của kỳ này, đã duyệt ở CỔNG 0 — id-C §2)
  HT mới trong kỳ        : 42
  HT trong tập (WARM 3/5): 11
  Có SĐT                 : 6
  Hệ số giá trị đơn      : 3  (ca sửa lại ≥15tr)
  Điểm                   : 11 × 3 = 33
  Dừng ở                 : A3 (7 HT) · A2 (4 HT)
  → Ưu tiên 1 của khối ①, làm nội dung nấc A3
```

⚠️ Tên và số mã trong ví dụ là **của một kỳ cụ thể**. Kỳ khác chân dung khác — ⛔ không chép bảng này sang kỳ sau rồi chỉ đổi số.

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

👁 QUAN SÁT — dưới 5 HT mới: CD3 (3) · CD4 (2)

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

---

<!-- ===== id-H-ngan-hang-hook.md ===== -->

# id-H · NGÂN HÀNG HOOK — 7 LOẠI HOOK × 16 FORMAT

> Chạy **sau CỔNG 1**. Mỗi hook phải gắn: **1 chân dung · 1 nấc 5A · 1 mã `O` · 1 `HT-nnn` truy ngược · 3 format**.
> ⚠ Chân dung gắn vào hook là chân dung **đã duyệt ở CỔNG 0 của kỳ này** (`id-C` §1). ⛔ Không viết hook cho một chân dung của kỳ trước mà kỳ này không có.
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
- ⛔ Hook hứa **đổi vận, tài lộc, tướng số** hoặc **tỷ lệ thành công** — cấm với mọi chân dung, kể cả khi chính khách mở lời bằng chuyện đó
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

---

<!-- ===== id-I-so-tay-thuc-thi.md ===== -->

# id-I · ★ SỔ TAY THỰC THI CÁ NHÂN HOÁ

> Đầu ra cuối cùng và là thứ duy nhất **chạm tới từng con người**. Dashboard để lãnh đạo nhìn; sổ tay để nhân viên làm.
>
> ⚠️ **Khuôn trong sổ này là bản dựng tạm.** Người dùng sẽ gửi mẫu sổ tay chính thức; khi có, thay §3 và ghi lại ở `doc/CHANGELOG.md`. Mọi phần khác giữ nguyên.

---

## 1. BA LOẠI SỔ TAY

| Loại | Cho ai | Dài | Chứa tên ai |
|---|---|---|---|
| **ST-CN** | Một nhân viên trực page | **1 trang** | Chỉ người đó |
| **ST-TN** | Trưởng nhóm | 2–3 trang | Cả nhóm — ⛔ không phát ra ngoài nhóm |
| **ST-ND** | Người làm nội dung | 1–2 trang | ⛔ Không có tên nhân viên nào |

⛔ **ST-CN của người A ⛔ không bao giờ chứa tên, điểm hay hội thoại của người B.** Vi phạm là `CĐ-5` áp cho chính agent.

---

## 2. LUẬT MỘT VIỆC

```
Sổ tay loại D : ĐÚNG MỘT việc.
Sổ tay loại C : tối đa HAI việc.
Sổ tay loại B : ĐÚNG MỘT việc (nhóm yếu nhất).
Sổ tay loại A : MỘT việc nâng cấp + 2 đoạn chat mẫu để chia sẻ cho khối.
```

★ Sổ tay 7 việc là sổ tay 0 việc. Người đang làm sai 5 nhóm mà nhận danh sách 5 việc sẽ không sửa nhóm nào.
★ Việc được chọn là **nhóm `N` mất nhiều điểm nhất**, ⛔ không phải nhóm dễ sửa nhất.

---

## 3. KHUÔN `ST-CN` — SỔ TAY MỘT NHÂN VIÊN

```markdown
# SỔ TAY THỰC THI · <Tên nhân viên>
Kỳ <tu> → <den> · <n> hội thoại · <điểm>/100 · loại <A|B|C|D>

> Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay xếp hạng công khai.

## 1 · KỲ NÀY BẠN LÀM TỐT NHẤT ĐIỀU GÌ
<nhóm N mạnh nhất> — <% đạt> (khối: <% đạt của khối>)
Ví dụ từ chính bạn: HT-<nnn> — "<nguyên văn câu làm tốt>"

## 2 · ★ MỘT VIỆC CỦA KỲ TỚI
**<Tên việc — viết như một hành động, không phải một phẩm chất>**

Vì sao: <nhóm N yếu nhất> đạt <x>% trên <n> hội thoại áp dụng.
        Ước tính <m> lead rơi vì điều này.

Bằng chứng — 2 hội thoại của chính bạn:
  HT-<nnn> · khách hỏi "<...>" → bạn trả lời "<...>" → khách im luôn
  HT-<nnn> · <...>

Làm thế nào — câu mẫu dùng được ngay:
  ✅ "<câu đúng 1>"
  ✅ "<câu đúng 2>"
  ⛔ "<câu đang dùng, vì sao hỏng>"

Đo thế nào ở kỳ sau: <tiêu chí N>.<x> từ <a>% lên <b>%

## 3 · KHÁCH CỦA BẠN LÀ AI
Chân dung gặp nhiều nhất: <CD> · <tên> (<n>/<N> hội thoại)
Họ đang sợ: <mã O cao nhất> — <tên mã>
Câu hỏi ngầm: "<...>"
→ Ba câu trả lời sẵn cho tệp này:
  1. <...>
  2. <...>
  3. <...>

## 4 · ⛔ BA ĐIỀU TUYỆT ĐỐI KHÔNG
- ⛔ Không nêu con số bảo hành — nói "chính sách bảo hành bằng văn bản"
- ⛔ Không trả lời câu bệnh nền — chuyển "cần bác sĩ khám trực tiếp đánh giá"
- ⛔ Không cam kết kết quả chắc chắn
<thêm dòng nếu người này có cờ đỏ trong kỳ — ghi rõ HT-nnn>

## 5 · KIỂM TRƯỚC KHI ĐÓNG MỖI HỘI THOẠI
- [ ] Đã hỏi tình trạng trước khi xin số chưa?
- [ ] Đã nêu được khung giá hoặc nói rõ vì sao chưa nêu được chưa?
- [ ] Đã hỏi khung giờ nghe máy chưa?
- [ ] Đã mời lịch có ngày + giờ cụ thể chưa?
- [ ] <mục riêng theo việc ở phần 2>
```

---

## 4. KHUÔN `ST-TN` — SỔ TAY TRƯỞNG NHÓM

```markdown
# SỔ TAY TRƯỞNG NHÓM · <tên nhóm>
Kỳ <tu> → <den>

## 1 · PHÂN BỐ NHÓM
A: <n> · B: <n> · C: <n> · D: <n> · chưa đủ mẫu: <n>

## 2 · BA TIÊU CHÍ YẾU NHẤT CỦA NHÓM
<N>.<x> — <y>% đạt — đây là nội dung buổi đào tạo 15 phút kỳ tới

## 3 · AI KÈM AI
<người loại A> kèm <người loại D> — về đúng tiêu chí <N>.<x>
(người A đạt <a>%, người D đạt <b>% trên cùng tiêu chí)

## 4 · CỜ ĐỎ CẦN XỬ TRONG 48 GIỜ
<mã CĐ> · <người> · HT-<nnn> · nguyên văn: "<...>" · xử thế nào

## 5 · VIỆC KHÔNG PHẢI CỦA NHÓM BẠN
<các ô "—" do lỗi hệ> → đã đẩy lên mục hệ thống của dashboard
```

★ Mục 5 là mục giữ cho trưởng nhóm không bị đổ oan những việc mà hệ thống mới sửa được.

---

## 5. KHUÔN `ST-ND` — SỔ TAY NGƯỜI LÀM NỘI DUNG

```markdown
# SỔ TAY NỘI DUNG · kỳ <tu> → <den>

## 1 · <n> Ô ĐƯỢC CHỌN (ma trận đã duyệt <ngày>)
<bảng: # · khối · CD · nấc · điểm · hướng nội dung · format · deadline>

## 2 · NGÂN HÀNG HOOK KỲ NÀY — <n> hook
<bảng theo khuôn id-H §4>

## 3 · NỘI DUNG PHẢI DỪNG
<các nội dung 🔴 KÉM + mã O thấp → bỏ hẳn>

## 4 · Ô ĐANG PHÍ
<ô ③ của ma trận CD×5A — nhiều nội dung, ít người hỏi>

## 5 · ⛔ CỜ PHÁP CHẾ TRƯỚC KHI SẢN XUẤT
<danh sách 🔴 🟡 kèm câu thay thế>
```

---

## 6. VIẾT VIỆC THẾ NÀO CHO SỬA ĐƯỢC

| ⛔ Viết thế này | ✅ Viết thế này |
|---|---|
| *"Cần chủ động hơn"* | *"Sau khi khách im 30 phút, nhắn lại một câu hỏi về tình trạng — không nhắn lại lời chào"* |
| *"Kỹ năng khai thác yếu"* | *"Hỏi 1 câu về tình trạng **trước** khi gõ câu xin số"* |
| *"Chưa biết chốt"* | *"Thay 'khi nào rảnh chị qua' bằng 'chiều mai 15h em giữ chỗ cho chị nhé'"* |
| *"Thái độ chưa tốt"* | *"Bỏ câu 'chị đọc kỹ giúp em' — thay bằng nhắc lại đúng điều chị vừa hỏi"* |

★ Mỗi việc phải kiểm được bằng **ctrl-F trong hội thoại kỳ sau**. Việc không kiểm được là việc không tồn tại.

---

## 7. NHỊP PHÁT

| Khi nào | Ai nhận | Qua đâu |
|---|---|---|
| Ngay sau CỔNG 2 | Trưởng nhóm — `ST-TN` | Bản riêng |
| Sau khi trưởng nhóm đọc xong | Từng nhân viên — `ST-CN` | **Bản riêng của từng người** |
| Cùng lúc | Người làm nội dung — `ST-ND` | Chung |

⛔ Không phát `ST-CN` vào nhóm chat chung. ⛔ Không đính kèm nhiều `ST-CN` trong một file.

---

## 8. TỰ KIỂM SỔ NÀY

- [ ] Mỗi `ST-CN` có **đúng số việc** theo loại A/B/C/D không?
- [ ] Việc được chọn có phải nhóm `N` **mất nhiều điểm nhất** không?
- [ ] Mỗi việc có **câu mẫu dùng được ngay** không, hay chỉ có lời khuyên?
- [ ] Mỗi việc có **cách đo ở kỳ sau** không?
- [ ] Có `ST-CN` nào chứa tên người khác không?
- [ ] Câu *"Điểm dùng để phân việc kèm cặp…"* có ở đầu mọi `ST-CN` không?
- [ ] Lỗi hệ có bị viết thành việc của nhân viên không?

---

<!-- ===== id-J-dashboard-schema.md ===== -->

# id-J · DASHBOARD & SCHEMA BÁO CÁO

> Dashboard là **một trang HTML cố định** đọc dữ liệu từ `data/*.json`. Mỗi kỳ chỉ sinh thêm một file JSON, ⛔ không sửa trang.
> Nhờ vậy link gửi cho sếp **không bao giờ đổi**, và xem lại được mọi kỳ cũ.

---

## 1. MƯỜI TAB

| # | Tab | Trả lời câu |
|---|---|---|
| ① | **Phễu inbox** | Khách vào bao nhiêu, nóng tới đâu, rơi ở đâu và vì sao |
| ② | **Chân dung & Insight** | Khách là ai, họ sợ gì, câu hỏi ngầm là gì. ⏳ Khoá lại khi chân dung chưa qua CỔNG 0 |
| ③ | ★ **Chấm điểm nhân viên** | Khối trực page đang yếu tiêu chí nào, ai cần kèm |
| ④ | **Marketing — Facebook** | Chuỗi chi → CPM→CTR→CPI→CPL→CPB, nội dung nào tốt/kém |
| ⑤ | **Marketing — Google Ads** | ⚠ chờ dữ liệu |
| ⑥ | **Ma trận ưu tiên** | Kỳ tới làm 5 việc nào |
| ⑦ | **Ngân hàng hook** | Viết gì, cho ai, format nào |
| ⑧ | **Sổ tay & việc cần xử lý** | Ai làm gì, hạn bao giờ, đo thế nào |
| ⑨ | **Ghi chú dữ liệu** | Mọi con số đến từ đâu, loại gì ra, vì sao |
| ⑩ | ★ **Hàng chờ gọi** | Sale gọi ai trước · ai phải xin số ngay · thang điểm hụt ở đâu |

### Bốn bố cục — ⛔ vẫn chỉ MỘT bản trang

Mười tab ở trên là bản **đầy đủ**. Cùng một trang và cùng một file kỳ còn dựng được hai báo cáo hẹp hơn cho hai người đọc khác nhau — chọn bằng trường `bo_cuc` trong `data/index.json`:

| `bo_cuc` | Tên báo cáo | Tab | Thẻ số tổng |
|---|---|---|---|
| *(không khai)* · `day-du` | Chân dung khách & chất lượng trực page | cả 10 | cả 7 |
| `insight` | **Insight khách** — khách là ai · họ sợ gì · kỳ tới làm nội dung gì | ② ⑥ ⑦ · ẩn khối `nac-5a` | HT · bỏ 1 lượt · có SĐT · HOT/WARM chưa SĐT |
| `truc-page` | **Chất lượng trực page** — khối yếu gì · ai cần kèm · sửa câu nào | ③ ⑩ ① ② ⑧ ⑨ | HT · trả lời lượt đầu · rơi do trực page · bỏ 1 lượt · HOT/WARM chưa SĐT |
| ★ `sale` | **Hàng chờ gọi** — gọi ai trước · ai phải xin số ngay | ⑩ ① ② ⑨ | HT · có SĐT · HOT/WARM chưa SĐT · hàng chờ Sale |

```
⛔ Tách báo cáo KHÔNG được đẻ thêm một bản trang.
   Hai bản trang là hai chỗ phải sửa mỗi lần đổi, và sẽ lệch nhau sau hai kỳ.
   Trang đọc `bo_cuc`, tự lọc tab và thẻ số, tự đổi tiêu đề.

★ Thứ tự tab đi theo ĐÚNG thứ tự khai trong bố cục, không theo thứ tự 10 tab gốc:
   bản `truc-page` mở bằng tab Chấm điểm, bản `sale` mở bằng tab Hàng chờ gọi —
   vì đó là việc của người đọc từng bản.

⛔ Bố cục `sale` KHÔNG có tab ③ Chấm điểm nhân viên. Sale ⛔ không phải người
   xử lý con số đó, và id-F §7 rào ④ giới hạn chỗ con số gắn tên người được xuất hiện.

⚠ Hai bố cục hẹp dùng CHUNG một file kỳ. Số liệu chỉ có một bản —
   ⛔ không bao giờ có chuyện hai báo cáo nói hai con số khác nhau.

★ Bố cục còn giấu được từng **KHỐI bên trong một tab**, qua `an:['<tên khối>']` — nhỏ hơn một tab. Hiện có `nac-5a` (phân bố nấc 5A trong tab ②). Luật áp dụng y như với tab: khối ẩn ở bố cục này phải còn đọc được ở bố cục khác.

⚠️ Bố cục hẹp **giấu tab chứ không xoá dữ liệu**: file kỳ vẫn đủ mọi khối. Khối nào bị ẩn ở bố cục này thì phải còn đọc được ở một bố cục khác — `insight` bỏ tab ① thì tab ① vẫn nằm ở `truc-page` (tên «Khách rơi ở đâu») và ở bản đầy đủ. ⛔ Không để một khối biến mất khỏi CẢ BA bố cục.

★ Bố cục bỏ tab ⑨ thì ghi chú dữ liệu **chuyển lên ô gập đầu trang**, ⛔ không biến mất. Tab ⑨ là tab bắt buộc của bản đầy đủ; bỏ nó khỏi thanh tab là để trang gọn, ⛔ không phải để thôi nói số đến từ đâu.

★ `insight` ⛔ KHÔNG có hai tab quảng cáo. Đầu vào của nó là HỘI THOẠI; số chi
   phí tới từ một nguồn khác (`id.py ads`) và chỉ nằm ở bản `day-du`. Bỏ tab
   không phải để giấu — thiếu nguồn nào vẫn phải ghi ở tab ⑨ và ở ô lưu ý
   đầu trang, đúng luật ① bên dưới.
```

### Đầu trang — luôn hiện, không nằm trong tab nào

```
ĐẦU TRANG   Tiêu đề + chọn kỳ
            Thẻ số tổng   (giá trị · so kỳ trước · so mốc gốc)
            Thanh tab

CHÂN TRANG  ▶ n lưu ý dữ liệu              (gập lại, mở ra xem)
            ▶ n ghi chú dữ liệu            (bố cục không có tab ⑨)
```

★ Hai ô gập nằm ở **chân trang**, sau mọi tab, và hiện ở mọi tab. Đầu trang để dành cho con số và thanh tab — thứ người đọc cần thấy trong hai giây đầu. ⚠ Chúng gập lại nên ⛔ không thay được cho cảnh báo thật sự chặn: lỗi phải dừng bản phát hành thì gắn cờ 🔴 vào đúng dòng chạm tới, không để riêng dưới chân trang.

### Bảy thẻ số tổng

| Thẻ | Kiểu | Tốt là |
|---|---|---|
| `Hội thoại mới` | số | — |
| `Bỏ sau 1 lượt` | % | thấp |
| `Có SĐT` | % | cao |
| `Trả lời tin đầu ≤2′` | % | cao · chuẩn ≥90% |
| `Rơi do trực page` | % | thấp — câu trả lời làm khách dừng |
| ★ `HOT/WARM chưa có SĐT` | số | **thấp** — lead nóng chưa vào tay telesale |
| ★ `Hàng chờ Sale gọi ≤15′` | số | — · số lead nhóm `GOI_NGAY` của bộ KF-60 (§2b) |

⚠️ Tab ⑨ **không phải tab phụ**. Báo cáo không nói được số đến từ đâu thì không ai dám dùng để ra quyết định.

---

## 2. SCHEMA DỮ LIỆU — `insight-dashboard-kangnam/2`

> **Đổi gì ở `/2`:** thêm khối `lead` (§2b) và `pheu.chot_lich` ·
> `nhan_vien.du_mau` · `nhan_vien.ht_khong_xep`.
> File `/1` vẫn đọc được: thiếu khối `lead` thì tab ⑩ hiện **ô khoá**,
> ⛔ không hiện 0 — luật ① của §3.

```jsonc
{
  "schema": "insight-dashboard-kangnam/2",
  "ky":   { "id","tu","den","tu_hien","den_hien","nhan","tao","nguon","crawl" },
  "chan": { "van_ban","het_han","con_hieu_luc" },   // văn bản ưu đãi đang đối chiếu
  "chi_phi": { "co_file": true, "nguon": "..." },
  "canh_bao": [ { "muc":"bad|warn", "text":"..." } ],
  "the_tong": [ { "id","nhan","gia_tri","kieu":"n|pct|s","tot":"cao|thap","phu" } ],

  "ket_luan": {                                      // 3 việc trọng tâm mỗi bộ phận
    "marketing":  [ { "viec","ly_do","so_huu","do_ky_sau","nhan":"da_do|gia_thuyet" } ],
    "truc_page":  [ ... ],
    "he_thong":   [ ... ],
    "bu_quyet":   [ { "viec","chi_tiet" } ]
  },
  "theo_doi": [ { "bo_phan","viec","muc_tieu","ket_qua","dat":true|false|null,"lan" } ],

  "pheu": {
    "so_ht_phan_tich": 0,
    "nhiet": { "HOT":0,"WARM":0,"COLD":0 },
    "nhiet_x_sdt": [ { "muc","chua","moi","cu" } ],
    "tin_hieu":   [ { "nhan","so" } ],               // 5 tín hiệu id-D §2
    "nguyen_nhan_roi": { "nội dung":0,"trực page":0,"hệ thống":0,"khách tự dừng":0,"không rơi":0 },
    "rao_can":    [ { "nhan","so" } ],
    "ma_o":       [ { "ma","ten","so","pct","noi_dung_da_co","ket_luan" } ],
    "chot_lich":  0,                                 // /2 — máy sinh
    "van_de":     [ { "muc","tieu_de","nhan_do","so_lieu","de_xuat","so_huu","anh_huong" } ]
  },

  // ★ /2 · KHỐI LEAD — tab ⑩. Chi tiết ở §2b.
  "lead": {
    "bo_cham": "KF-60/1.1",
    "nguong_nuoi": 17,
    "so_cham": 0,
    "phan_luong":  [ { "ma":"LEAD|N1a|N1b|N2|N3|N4|N5", "ten", "so" } ],
    "nhom_goi":    [ { "ma":"GOI_NGAY|XIN_SO|NUOI|KHONG", "ten", "so", "pct" } ],
    "chua_so": 0,
    "ghi_de":      [ { "ma","ten","so" } ],
    "nhom_diem":   [ { "nhan":"A…E", "trung_binh", "toi_da", "cao_nhat" } ],
    "diem": { "trung_vi":0, "cao_nhat":0, "goc_cao_nhat":0 },
    "doi_chieu":   [ { "id_d":"HOT|WARM|COLD", "nhom":{ "GOI_NGAY":0,… } } ],
    "bat_bien": { "goi_ngay_thieu_sdt":0, "id_d_hot_roi_khong":0, "dat":true,
                  "ht_v1":[], "ht_v2":[] },
    "hang_cho":    [ { "ht","cd","the","dich_vu","he_so","nhom_goi","id_d","diem",
                       "uu_tien","co_sdt","ma_o","ghi_de","gio_im","viec",
                       "viec_chi_tiet","viec_mac_dinh" } ],
    "viec_mac_dinh": 0,   // số dòng phải dùng lời mặc định vì chưa xếp được chân dung
    "ghi_chu": [ "…" ]
  },

  "chan_dung": {
    // ⛔ KHÔNG có bộ chân dung mặc định. `tep` rỗng = chưa qua CỔNG 0 (id-C §1).
    "phac_hoa": { "trang_thai":"chua_phac_hoa|da_duyet", "vi_sao", "file",
                  "nguyen_lieu", "so_chan_dung", "duyet_boi", "duyet_luc" },
    // `cd` nay là mã THƯ VIỆN KF-62 (`SACTO-NAM_TAI_PHAT`), ⛔ không còn CD1…CDn.
    // Chỉ liệt kê chân dung CÓ hội thoại; dòng `<DV>-CHUA_XAC_DINH` rồi
    // `KHONG_XAC_DINH_DV` xuống cuối. ⚠ Tổng cột `ht` phải bằng `so_ht_phan_tich`.
    "tep":     [ { "cd","ten","ht","quan_sat","hot","warm","cold","co_sdt",
                   "chot_lich","bo_1_luot","roi_truc","he_so" } ],
    "insight": [ { "cd","ten","nhom","ho_la_ai","insight","cau_hoi_ngam","tin_hieu_nong","huong_xu_ly","trich" } ],
    // xếp theo điểm win; mỗi ô là gạch đầu dòng — dòng mở đầu "- " thành <li> (id-C §6)
    "co_hoi_win":    [ { "cd","ten","ht","lead_bo_lo","he_so","pct_sdt","diem","hang",
                         "uu_tien","roi_truc","ghi_chu","ly_do_chon" } ],  // CD0 cuối, hang=null
    // ⚠ Bảng Cơ hội win hiện HOT/WARM/COLD lấy từ `tep` cùng mã CD — ⛔ không
    //    lặp ba số đó vào `co_hoi_win`. Một con số hai chỗ là hai chỗ lệch nhau.
    "cach_tinh_win": "công thức, viết ra để người đọc cãi được",
    "ma_tran_cd_5a": { "noi_dung": {...}, "hoi_thoai": {...} }   // hai bảng N×5
  },

  "nhan_vien": {                                      // ★ tab ③
    "du_mau": true,
    // ⛔ Luôn đủ 5 khoá. `0` = ĐÃ ĐO và bằng không, khác hẳn "chưa đo".
    "phan_bo": { "A":0,"B":0,"C":0,"D":0,"chưa đủ mẫu":0 },
    // ★ /2 — hội thoại ⛔ KHÔNG gán được cho một người, nên bị loại khỏi phần
    //   xếp loại cá nhân (vẫn tính vào `nhom` của cả đội). Một hội thoại có từ
    //   hai nhân viên trực thì điểm của nó ⛔ không phải việc của riêng ai.
    "ht_khong_xep": { "(nhiều người)":0, "(không rõ)":0 },
    "nhom":    [ { "ma":"N1","ten","diem_toi_da":20,"pct_dat":0,
                   "tieu_chi":[ { "ma":"N1.1","ten","diem":8,"dat":0,"chua":0,"khong_ap_dung":0 } ] } ],
    "ca_nhan": [ { "ten","ht","diem","loai","yeu_nhat","manh_nhat","co_do":[] } ],   // ⛔ chỉ vào sổ tay riêng
    "co_do":   [ { "ma":"CĐ-2","nguoi","ht","nguyen_van","nguoi_xu_ly" } ],
    "viec_he_thong": [ { "nguyen_nhan","so_ht","so_huu" } ],
    "ghi_chu": "Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay xếp hạng công khai."
  },

  "facebook": {
    "nguon","ky","ky_truoc","don_vi":"nghìn đ",
    "chuoi": [ { "ma":"CHI|CPM|CTR|CPI|CPL|CPB|BK_LEAD","nhan","gia_tri","muc_tieu","ky_truoc",
                 "kieu","tot","phu" } ],   // CHI = chi phí tổng, mở đầu chuỗi; `phu` thay
                                           // dòng "mục tiêu" khi ô không có mốc tốt/xấu
    "theo_ngay": [ { "ngay","booking","cpb","du_ket_qua":true } ],
    "dong":      [ { "ten","cap","chi","inbox","inbox_moi","deal","bk","cpi","cpl","cpb","ty_trong" } ],
    "noi_dung":  [ { "noi_dung","cum","danh_gia":"tot|giu|kem","tong":{...},"nhan_xet" } ],
    "nhieu_mau": { "chien_dich":[ { "ten","chi" } ], "ghi_chu" },
    "van_de":    [ ... ]
  },

  "google": { "co_du_lieu": false, "ghi_chu": "⚠ chưa có dữ liệu Google Ads" },

  "ma_tran": {
    "trang_thai":"cho_duyet|da_duyet","duyet_boi","duyet_luc","cach_xep",
    "khoi": [ { "ma":"tang_hot","ten","muc_tieu","tap_lead",
                "dong":[ { "cd","ten","ht","lead","co_sdt","he_so","diem","nac","huong","chon","uu_tien" } ] } ],
    "sua_van_hanh": [ { "cd","ten","ht","truc","ly_do" } ],
    "quan_sat":     [ { "cd","ten","ht" } ]
  },

  "hook":   { "ghi_chu","dong": [ { "ma","khoi","cd","ten","nac","ma_o","insight","hook",
                                    "loai_hook","fm":["L01","L08","L02"],"cta","truy_nguoc",
                                    "o_camp","co_phap_che","duyet" } ] },

  "so_tay": { "da_sinh": false, "so_ban": 0, "duong_dan": "out/so-tay/" },
  "viec":   [ { "so","viec","bo_phan","so_huu","han","do_the_nao","trang_thai" } ],
  "ghi_chu": [ "..." ],
  "truoc":   { "ky","the_tong","tep","noi_dung","chuoi","nhan_vien" },
  "moc_goc": { "ky","nguon","dong":[...] }
}
```

### 2b. KHỐI `lead` — ⛔ MỘT BÁO CÁO CHỈ CÓ MỘT NHÃN NÓNG

★ **Ba thứ gặp nhau ở một dòng hàng chờ** — thiếu cái nào thì dòng đó ⛔ không dùng được:

```
id-D §2   → nhãn nóng          → hội thoại này nóng tới đâu
KF-60     → nhom_goi           → GỌI AI TRƯỚC, và AI gọi (Sale hay trực page)
KF-62     → cd  → viec_chi_tiet→ NÓI GÌ với đúng chân dung đó
```

⚠ `viec_mac_dinh = true` nghĩa là chưa xếp được chân dung nên phải dùng **lời
mặc định** của `lien_ket_kf60.mac_dinh`. Đủ để chạy, ⛔ nhưng không phải kịch bản
riêng — đó là nợ của cổng ① KF-62, phải đếm và nói ra ở đầu bảng.


```
Nhãn HOT / WARM / COLD của kỳ  →  pheu.nhiet   (5 tín hiệu · id-D §2)
Việc phải làm với từng lead     →  lead.nhom_goi (bốn nhóm · KF-60)
```

⛔ **Khối `lead` KHÔNG phát nhãn HOT/WARM/COLD thứ hai.** Bản nháp KF-60 từng
định làm thế; chấm thật 493 hội thoại cho thấy ⛔ không cặp ngưỡng nào làm hai
nhãn khớp nhau — lệch thấp nhất 12,8%, và cấu hình đó chỉ cho 5 lead vào hàng
chờ. Hai bộ đo hai thứ khác nhau **có chủ ý**: `id-D` đếm 5 tín hiệu nhị phân,
KF-60 cân 19 tiêu chí. ⚠ Hai nơi cùng gọi một hội thoại là HOT theo hai cách
khác nhau thì không ai còn tin con số nào.

| Nhóm | Ai làm · SLA |
|---|---|
| `GOI_NGAY` | **Sale gọi ≤15′** — có SĐT và khớp luật ghi đè |
| `XIN_SO` | **Trực page xin số ≤15′** — nóng mà chưa có SĐT |
| `NUOI` | Sale/CSKH · 24–72h theo mã `O` |
| `KHONG` | Marketing · remarketing tự động |

★ **`bat_bien` là cổng chặn phát hành**, thay cho luật «lệch nhãn ≤5%» đã bỏ:

```
① ⛔ Mọi HT nhóm GOI_NGAY phải CÓ SĐT — không có số thì không gọi được.
② ⛔ HT mà id-D xếp HOT phải KHÔNG nằm trong nhóm KHONG.

Khác 0 là LỖI CODE, ⛔ không phải chuyện ngưỡng → báo cáo tự gắn cờ 🔴 ở
đầu trang và ⛔ KHÔNG được phát hàng chờ.
```

⚠️ `hang_cho` ⛔ **không chứa chữ của khách**: chỉ mã `HT`, chân dung, dịch vụ,
mã `O` và việc. Nội dung hội thoại ở lại `out/ban-ghi.json` — ⛔ không lên trang.
⚠️ `nhom_diem` phải được đọc cùng `diem`: nhóm nào trung bình dưới 10% trần là
nhóm **gần như không ghi điểm**, nghĩa là thang điểm chưa phân biệt được lead
trên tệp đó. Kỳ 24–29/10: nhóm B đạt **1,4/35**.

---

## 2c. HAI FILE MỘT KỲ — ⛔ CHẠY LẠI KHÔNG ĐƯỢC XOÁ CHỮ NGƯỜI

| File | Ai viết | Chạy lại `bao-cao` |
|---|---|---|
| `data/<ky>.json` | **máy sinh** từ `out/doc-hoi-thoai.json` | ghi lại toàn bộ |
| `data/<ky>.nguoi.json` | ★ **người và agent** — phần đọc hiểu | ⛔ không chạm, chỉ **phủ lên** |

Lớp phủ giữ: `ket_luan` · `theo_doi` · `canh_bao` · `pheu.van_de` ·
`chan_dung.insight` · `co_hoi_win` · `cach_tinh_win` · `ma_tran_cd_5a` ·
`ma_tran` · `hook` · `so_tay` · `viec` · `ghi_chu` · `facebook` ·
`nhan_vien.viec_he_thong` · `ky.tu/den/crawl/nguon` · `the_phu` (chữ dưới mỗi thẻ số).

★ Kỳ đã có file mà **chưa** có lớp phủ: lần chạy đầu `id.py bao-cao` **tự rút**
chữ người ra `.nguoi.json` rồi mới ghi — ⛔ không mất gì.
⚠️ Con số nằm trong câu của lớp phủ ⛔ **không tự cập nhật**. Mẫu đổi thì phải
sửa cả câu, ⛔ đừng để câu cũ nói một số mà bảng bên dưới nói số khác.

---

## 3. BỐN LUẬT HIỂN THỊ

```
① KHÔNG CÓ SỐ thì hiện "—", ⛔ không hiện 0.
   0 nghĩa là đã đo và bằng không. "—" nghĩa là chưa đo. Hai thứ khác nhau.

   Cùng luật đó cho CHÂN DUNG: `tep` rỗng thì tab ② hiện một ô khoá
   "⏳ chân dung chưa được phác họa" kèm lý do, ⛔ không hiện bảng trống và
   ⛔ không điền tạm một bộ chân dung nào vào cho đủ bảng.

② MỌI SO SÁNH ghi rõ so với cái gì:
   "▲ 2,1 điểm so kỳ trước"  ·  "mốc gốc 42,7% · ▼ 3,2 điểm"
   Chưa có mốc → "⚠ chưa có mốc so sánh".

③ TIỀN quy về NGHÌN ĐỒNG, ghi đơn vị ở đầu bảng.

④ TÊN NHÂN VIÊN ⛔ không xuất hiện trong tab ③ ở dạng bảng xếp hạng.
   Tab ③ hiện: phân bố A/B/C/D · % đạt từng tiêu chí · cờ đỏ (có tên, vì cần người xử).
   Bảng điểm có tên chỉ nằm trong sổ tay riêng (id-I).
```

---

## 4. KHỐI "VIỆC CẦN XỬ LÝ" — CUỐI TRANG

Giống dòng *"31 việc cần xử lý ở cuối trang"* của dashboard Meta hiện hành.

| Cột | Ghi chú |
|---|---|
| `#` | Số thứ tự |
| `Việc` | Viết như hành động |
| `Bộ phận` | Marketing · Trực page · Hệ thống · BU |
| `Sở hữu` | ★ **Tên người thật.** Việc không có tên là việc không ai làm |
| `Hạn` | |
| `Đo thế nào` | Chỉ số cụ thể của kỳ sau |
| `Trạng thái` | mới · đang làm · đạt · chưa đạt |

★ Việc **chưa đạt 2 kỳ liên tiếp** → tự động gắn cờ `2 kỳ — đẩy BU`.

---

## 5. THEO DÕI VIỆC KỲ TRƯỚC

Mỗi kỳ mở đầu bằng việc **chấm lại việc kỳ trước**: đạt / chưa đạt / chưa đo.

⛔ Báo cáo không theo dõi việc kỳ trước là báo cáo bắt đầu lại từ đầu mỗi kỳ — và khối sẽ học được đúng con số 0 sau một năm.

---

## 6. TỰ KIỂM SỔ NÀY

- [ ] File JSON có `schema` đúng phiên bản không?
- [ ] Tổng các cột có khớp `so_ht_phan_tich` không? Bảng chân dung đã **cộng cả dòng `CD0`** chưa?
- [ ] `chan_dung.phac_hoa.duyet_boi` có tên người thật chưa, hay tab ② đang hiện số của một cách chia chưa ai duyệt?
- [ ] Ô chưa đo có hiện `—` thay vì `0` không?
- [ ] Mọi so sánh có ghi rõ so với cái gì không?
- [ ] Tab ③ có bảng xếp hạng có tên lọt ra không?
- [ ] Mỗi việc ở khối cuối trang có **tên người thật** không?
- [ ] Tab ⑨ có đủ: nguồn · đã loại gì · vì sao loại không?
- [ ] Báo cáo có đúng **một** nhãn HOT/WARM/COLD không, hay khối `lead` đang phát nhãn thứ hai?
- [ ] `lead.bat_bien.dat` có bằng `true` không? Bằng `false` thì đã **dừng phát hàng chờ** chưa?
- [ ] `hang_cho` có lọt chữ của khách, tên hay SĐT vào không?
- [ ] Chạy lại `bao-cao` xong, phần chữ người còn đủ không — `ket_luan`, `van_de`, `hook`, `viec`?
- [ ] Câu trong `.nguoi.json` có nói con số nào đã lệch so với bảng máy sinh không?
- [ ] `nhan_vien.ht_khong_xep` có được nói ra không, hay bảng xếp loại đang im lặng gán điểm hội thoại nhiều người cho một người?

---

<!-- ===== id-K-module-kangnam-phap-che.md ===== -->

# id-K · MODULE ĐƠN VỊ KANGNAM & PHÁP CHẾ

> ★ **Đây là module thương hiệu.** Đổi đơn vị (Paris, THV…) → **thay đúng sổ này**, ⛔ không sửa `id-A` … `id-J`.
> Dữ kiện ở đây đồng bộ với `Agent-SeedingPlant-Kangnam/knowledge/sp-I` + `sp-J`. Lệch nhau thì **sp-I/sp-J là bản gốc**.

---

## 1. HỆ THỐNG

| Dữ kiện | Giá trị | Nguồn |
|---|---|---|
| Tên dùng trên truyền thông | **Bệnh viện Thẩm mỹ Kangnam** | website chính thức |
| Quy mô | **2 bệnh viện + 5 viện thẩm mỹ, 7 tỉnh thành** | website |
| Số bác sĩ công bố | **15** ⚠ *(hồ sơ nội bộ chỉ có 8)* | website |
| Số ca công bố toàn hệ thống | **3.000.000+** ⛔ không chia cho từng bác sĩ | website |
| Mô hình | 5 chuyên khoa: hàm mặt · mũi · vòng 1 · hút mỡ · trẻ hoá da | website |

### Chi nhánh & giấy phép

| Cơ sở | Địa chỉ | Giấy phép |
|---|---|---|
| **BVTM Kangnam Sài Gòn** | 666 Cách Mạng Tháng 8, TP.HCM | **287/BYT-GPHĐ** |
| **BVTM Kangnam Hà Nội** | 190 Trường Chinh, Hà Nội ⚠ *(từ kế hoạch Ads nội bộ)* | **194/BYT-GPHĐ** |
| 5 viện thẩm mỹ còn lại | 🔴 `[CHỜ CẤP]` — tên, địa chỉ, số giấy phép riêng | |

★ **Số giấy phép là bắt buộc trong mọi nội dung quảng cáo**, lấy đúng giấy phép của cơ sở xuất hiện trong bài.
⛔ Nội dung local gắn cơ sở **ngoài hai bệnh viện trên** → 🔴 CHẶN.
⚠️ **Luật tuyến:** có kỹ thuật chỉ làm ở tuyến bệnh viện (dữ liệu nội bộ ghi rõ: *nâng mũi cấu trúc chỉ làm tại tuyến bệnh viện*). Nội dung nói kỹ thuật tuyến bệnh viện mà gắn địa chỉ clinic → 🔴.

---

## 2. MENU DỊCH VỤ — 10 CHUYÊN KHOA

| Chuyên khoa | Dịch vụ |
|---|---|
| **Mắt** | Tạo mắt 2 mí · mở khoé · trẻ hoá mắt · khắc phục sụp mí |
| **Mũi** | Nâng mũi · thu nhỏ cánh mũi · mài gồ chỉnh xương · khắc phục mũi hỏng |
| **Hàm mặt** | Chỉnh hàm hô/móm · V-line · hạ gò má · má lúm · tạo hình môi |
| **Vòng 1** | Nâng ngực · treo sa trễ |
| **Lipo 360 — mỡ — mông** | Giảm mỡ · tạo hình thành bụng · cấy mỡ |
| **Trẻ hoá da** | Tiêm trẻ hoá · căng da · căng chỉ |
| **Da liễu** | Trị mụn · trị sẹo |
| **Trị sắc tố** | Trị nám tàn nhang · trị bớt · xoá xăm |
| **Kangnam Clinic** | Triệt lông · tắm trắng · phun xăm · điêu khắc |
| **Nha khoa** | Niềng răng · bọc sứ · implant · dán mặt sứ |

### Cross-sell — ⛔ chỉ MỘT hướng mỗi lần

| Đã làm | Cross-sell hợp lý |
|---|---|
| Mũi | mí → cằm → hàm *(cùng cụm gương mặt)* |
| Mắt | mũi → hàm |
| Hàm mặt | mũi → mí |

⛔ Không cross-sell cho khách **đang điều trị**. ⛔ Không cross-sell sang tuyến khác hẳn ở nấc `A5`.

---

## 3. 🔴 BA THỨ ĐANG CHẶN — GỐC CỦA PHẦN LỚN CỜ ĐỎ

### ① BẢO HÀNH — ba mức xung đột

```
"bảo hành nếp mí lên đến 3 NĂM"   ← kịch bản mắt (cụ thể nhất)
"bảo hành 10 NĂM"                 ← kịch bản tệp khách đi sửa lại (mũi)
"bảo hành TRỌN ĐỜI"               ← nhiều hook mũi đang chạy

→ BA CÁI NÀY KHÔNG THỂ CÙNG ĐÚNG CHO CÙNG MỘT DỊCH VỤ.
```

| Dịch vụ | Xử thế nào |
|---|---|
| **Mắt** | Dùng `3 năm`, vẫn ghi ⚠ *đối chiếu văn bản* |
| **Mũi** | ⛔ Không dùng số nào. Viết *"chính sách bảo hành bằng văn bản"* |
| Mọi dịch vụ | ⛔ **Không bao giờ dùng *"trọn đời"*** cho tới khi có văn bản đúng chữ đó |

★ Đây là mã `O-07` ở `id-D` và cờ đỏ `CĐ-2` ở `id-F`. Khách hỏi rất nhiều mà agent ⛔ **không được trả lời**.

### ② BẢNG GIÁ dịch vụ ngoài mắt — chưa có bản hiện hành

🔴 **CHẶN:** mọi hook `A4` có giá và mọi format `L11` của dịch vụ **ngoài mắt**.

Giá mắt có số nháp *(⚠ nguồn kịch bản, không phải bảng giá chính thức)*: cắt mí Plasma 8tr · cắt mí 6D 12,8tr · cắt mí + tạo khoé 13,6tr · cắt mí + cấy mỡ 17,9tr · nâng cung mày 8,8tr.

⚠️ Con số *"chỉ 31TR"* xuất hiện trong nhiều ad mũi cũ — **chưa đối chiếu bảng giá hiện hành**.
⛔ **Lấy số từ hook cũ là cách sai phổ biến nhất. Hook cũ không phải nguồn giá.**

★ Hệ quả cho `id-F`: khi trực page né giá dịch vụ ngoài mắt, phần lớn là **lỗi hệ**, chấm `—`, ⛔ không trừ điểm người.

### ③ CHỨNG CHỈ BÁC SĨ — chưa đối chiếu

🔴 **CHẶN:** mọi nội dung và mọi câu trả lời gắn **chức danh / số năm / số ca** của bác sĩ chưa đối chiếu được chứng chỉ hành nghề.
⚠️ Có bác sĩ **đã nghỉ việc** mà ad cũ còn tên — rà soát và gỡ.

---

## 4. MƯỜI HAI ĐIỂM PHÁP CHẾ `L`

| Mã | Điểm | Cờ |
|---|---|---|
| `L01` | Thiếu số giấy phép của đúng cơ sở | 🔴 |
| `L02` | Kỹ thuật tuyến bệnh viện gắn địa chỉ clinic | 🔴 |
| `L03` | Cam kết kết quả chắc chắn | 🔴 |
| `L04` | Con số bảo hành chưa có văn bản | 🔴 |
| `L05` | Ảnh/video khách chưa có consent đúng mục đích quảng cáo | 🔴 |
| `L06` | Seeding giả review bằng nick ảo | 🔴 |
| `L07` | Nói quá chức danh/bằng cấp bác sĩ | 🔴 |
| `L08` | Trả lời câu bệnh nền / chống chỉ định | 🔴 |
| `L09` | Giá không khớp bảng hiện hành | 🟡 |
| `L10` | Mốc hồi phục / thời gian mổ chưa BS duyệt | 🟡 |
| `L11` | Số suất ưu đãi không thật | 🟡 |
| `L12` | Dìm đối thủ | 🟡 |

★ **Consent:** trang case thực tế là nguồn **tham khảo tình trạng**, ⛔ **không phải nguồn lấy ảnh dùng lại**.

---

## 5. KHU VỰC PHÁT

| Khu vực | Đặc điểm đã đo |
|---|---|
| **NAM** | Kho nội dung dày nhất. Hook *"gọi tình trạng"* thắng rõ |
| **BẮC** | ⚠ Yếu hơn Nam. Nhiều nội dung TỐT ở Nam bị chấm KÉM khi port ra Bắc |
| **MIỀN TÂY** | ★ Công thức riêng rất mạnh: *"lên thành phố làm"* |
| **VIỆT KIỀU** | Nỗi sợ riêng: về nước ngắn ngày, sợ không kịp hồi phục và cắt chỉ → mã `O-09` |

### ★ Bốn quyền lợi riêng cho tệp Việt kiều

```
① Cấp GIẤY XÁC NHẬN PHẪU THUẬT của bệnh viện
② Hỗ trợ làm THỦ TỤC HẢI QUAN
③ Hỗ trợ ĐƯA ĐÓN SÂN BAY
④ Tư vấn ONLINE + hướng dẫn đặt lịch trước khi bay
```

★ Bốn mục này là **quyền lợi dịch vụ, không phải claim y khoa → sạch pháp chế**, viết được ngay và trực page trả lời được ngay. ⚠ Vẫn phải xác nhận còn áp dụng.

---

## 6. BẢNG CHẶN TỔNG

| Dòng loại này | Bị chặn bởi | Trạng thái |
|---|---|---|
| Nói *"bảo hành trọn đời / 10 năm"* | §3① | 🔴 **CHẶN** |
| Hook `A4` có giá / `L11`, dịch vụ ngoài mắt | §3② | 🔴 **CHẶN** |
| Gắn chức danh bác sĩ chưa đối chiếu | §3③ | 🔴 **CHẶN** |
| Nội dung local cơ sở ngoài 2 bệnh viện | §1 | 🔴 **CHẶN** |
| Kỹ thuật tuyến bệnh viện gắn địa chỉ clinic | §1 | 🔴 **CHẶN** |
| Ảnh/video khách chưa có consent | §4 `L05` | 🔴 **CHẶN** |
| Giá mắt / cắt mí | §3② | 🟢 **CÓ SỐ NHÁP** — đối chiếu trước khi đăng |
| Mốc hồi phục, thời gian mổ | §4 `L10` | 🟡 **HỎI LẠI** — cần BS duyệt |

★ **Ba thứ cần xin để mở phần lớn các chặn trên:**
`① chính sách bảo hành bằng văn bản — CẤP BÁCH NHẤT` · `② bảng giá hiện hành dịch vụ ngoài mắt` · `③ đối chiếu chứng chỉ bác sĩ đang chạy`.

---

## 7. CỔNG 2 — SOÁT TRƯỚC KHI PHÁT

Trước khi phát sổ tay / đăng hook, agent chạy soát và in ra:

```
🔴 <n> dòng CHẶN   — không phát được, kèm câu thay thế
🟡 <n> dòng HỎI LẠI — ai duyệt, chờ gì
🟢 <n> dòng SẠCH
```

⛔ Còn một dòng 🔴 thì ⛔ không phát bản đó. Gỡ dòng đó ra hoặc thay câu, rồi soát lại.

---

## 8. TỰ KIỂM SỔ NÀY

- [ ] Mỗi dòng có gắn **đúng giấy phép của cơ sở** trong bài không?
- [ ] Có con số bảo hành nào lọt ra không?
- [ ] Có giá dịch vụ ngoài mắt nào lọt ra không?
- [ ] Có lấy số từ **hook cũ** làm nguồn giá không?
- [ ] Có chức danh bác sĩ chưa đối chiếu nào lọt ra không?
- [ ] Trực page né giá do **lỗi hệ** có bị trừ điểm không?
- [ ] Đã chạy CỔNG 2 trước khi phát chưa?

---

<!-- ===== id-L-lead-scoring-kf60.md ===== -->

# id-L · ★ LEAD SCORING HỘI THOẠI — BỘ KF-60

> Sổ **nhập từ ngoài**: đây là văn bản KF-60 của khối Sale, ⛔ không phải sổ do
> repo này viết ra. Giữ nguyên văn để còn đối chiếu với bản Sale đang dùng.
> Sửa tiêu chí thì sửa **ở đây và ở `tools/id.py` cùng lúc** — thang điểm nằm
> hai chỗ mà lệch nhau thì không ai biết báo cáo đang chấm theo bản nào.

**Sổ này trả lời:** hội thoại nào Sale gọi trước, ai gọi, và nói gì.

### Ranh giới với bốn sổ đang chạy — ⛔ đừng để hai nơi cùng chấm một thứ

```
id-D §2  → PHÂN LOẠI nóng  (5 tín hiệu)    → nhãn báo ra ngoài, so được giữa các kỳ
id-L     → XẾP HÀNG GỌI    (4 nhóm việc)   → gọi ai trước · AI gọi
id-M     → CHÂN DUNG       (thư viện KF-62)→ NÓI GÌ với người đó
id-F     → CHẤM NHÂN VIÊN  (22 tiêu chí)   → sổ tay kèm cặp
id-G §3  → HỆ SỐ GIÁ TRỊ ĐƠN 1/2/3         → dùng chung, ⛔ không đẻ thang thứ hai
```

★ **Sổ này ⛔ KHÔNG phát nhãn HOT/WARM/COLD.** Nhãn nóng của một kỳ chỉ có một
bản, là nhãn 5 tín hiệu của `id-D` §2. Lý do đo được nằm ở §7.2.

### Chạy ở đâu

| Thứ | Chỗ |
|---|---|
| Bộ chấm | `tools/id.py` → `cham_lead()` · `gom_lead()` · `viec_cua()` |
| Từ khoá | `tools/tu_dien.json` → khối `lead_kf60` |
| Nối với chân dung | `tools/chan_dung_kf62.json` → `lien_ket_kf60` |
| Đầu ra | khối `lead` của file kỳ · tab **Hàng chờ gọi** · bố cục `?bo_cuc=sale` |

---

## KF-60 · Lead Scoring hội thoại Inbox Facebook (Kangnam / HCI) — **v1.1**

**Trạng thái: ĐANG ÁP DỤNG từ 02/11/2026 — anh UY đã duyệt v1.1.** v1.1 **đổi 9 điểm** so với v1.0 sau khi **chấm thật 493 hội thoại bằng chính thang điểm này**; hai điểm lệch khỏi bản v1.0 đã duyệt (**bỏ nhãn HOT/WARM/COLD của KF-60** và **đổi thang hệ số sang 1/2/3**) đã được anh UY duyệt riêng — xem §16.

⚠ **«Đã duyệt» ⛔ không phải «đã được booking kiểm».** `NGUONG_NUOI = 17`, trọng số 19 tiêu chí và thang hệ số vẫn **chưa có dòng CRM nào đối chiếu**. Chúng được duyệt để **chạy**, ⛔ không phải được duyệt là **đúng** — mốc kiểm là tuần 5–6 (§11).

★ **Bản này đã chạy, không còn là đề xuất trên giấy.** Bộ chấm nằm ở `tools/id.py`
(`cham_lead`), đầu ra ở khối `lead` của file báo cáo, hiện trên tab **Hàng chờ gọi**
của dashboard. Mọi con số trong §2, §7 và §8 là số đo, ⛔ không phải số ước.
**Thay thế** `KF-60 … v1.0`. Mọi thay đổi tiếp theo ghi vào tab `9. Nhật ký điều chỉnh` của file Driver.
**File Driver đi kèm:** `KF-60_Driver_Lead_Scoring_Inbox_v1.0.xlsx` — ⚠ các ô nền vàng phải cập nhật theo §7 và §8 bản này.

**Bằng chứng dùng để sửa:** kỳ **24–29/10/2026**, **494 hội thoại** đã phân tích và truy ngược được từng `HT-nnn`
(`dashboard/data/24-29-10.json` · nguồn `KNB_1_toan_bo_24-10_den_29-10.txt` · **line Da**, Caresoft/Messenger).
⚠ Kỳ này **chỉ có line Da** — mọi kết luận về hệ số theo BL vẫn chưa có dữ liệu PTTM để kiểm (§8, §12).

---

## 0. ĐỔI GÌ Ở v1.1 — VÀ BẰNG CHỨNG NÀO BUỘC ĐỔI

| # | v1.0 | v1.1 | Vì sao đổi |
|---|---|---|---|
| ① | Ngưỡng **HOT ≥65 · WARM 35–64** phát nhãn HOT/WARM/COLD | ★ **Bỏ hẳn nhãn của KF-60.** Thay bằng **bốn NHÓM GỌI** + một ngưỡng nuôi ≥17 · ✅ **anh UY duyệt 02/11/2026** | Chấm thật 493 HT: điểm **trung vị 12 · p75 20 · p90 35 · cao nhất 65/100**. ⛔ Chỉ 5 hội thoại vượt 50. Và ⛔ **không cặp ngưỡng nào** làm nhãn KF-60 khớp nhãn `id-D` — lệch thấp nhất đo được là 12.8%, mà cấu hình đó chỉ cho **5 lead** vào hàng chờ. Hai bộ đo hai thứ khác nhau có chủ ý; bắt chúng khớp là **sai đề** (§7) |
| ② | Rào cản ghi chữ tự do (`gia`, `so_bien_chung`) | **Bắt buộc `O-01…O-12` + `O-00`** | Danh sách đóng của `id-D` §1, dùng chéo ở 30+ chỗ và ở 2 agent khác. v1.0 thiếu hẳn **O-08** (13.2% mẫu) và **O-06** (3.8%) |
| ③ | `compliance_issue` ghi chữ tự do | **`CĐ-1…CĐ-6`** của `id-F` §5 | Để cờ pháp chế đi đúng đường xử lý đã có, không sinh danh mục thứ hai |
| ④ | `agent_flags` tự định nghĩa | **Trỏ về `N1…N6`** của `id-F`, ⛔ không chấm lại nhân viên | v1.0 đang dựng bộ chấm nhân viên thứ hai song song với bộ 22 tiêu chí đang chạy |
| ⑤ | Hệ số BL **1,0 / 0,8 / 0,7 / 0,5** | **Hệ số giá trị đơn 1 / 2 / 3** của `id-G` §3 · ✅ **anh UY duyệt 02/11/2026** | Hai thang hệ số khác nhau cho cùng một lead = hàng chờ Sale và ma trận ưu tiên xếp khác nhau. Và: kỳ 24–29/10 **toàn bộ là line Da** → mọi lead bị nhân 0,5–0,7, trong hàng chờ trộn thì **không bao giờ được gọi trước** |
| ⑥ | `N1 Chưa tương tác` = «KH ≤1 tin tự viết» | **Tách N1a / N1b** | 45.3% hội thoại (224/494) bỏ sau 1 lượt, nhưng **43.9% rơi là do câu trả lời của trực page** — khách *đã được trả lời rồi mới im*. Nhóm đó ⛔ không phải N1, là **LEAD có lỗi nội dung/câu trả lời** |
| ⑦ | Không nói gì về bộ 5 tín hiệu đang chạy | **§7.3 bốn nhóm gọi + hai bất biến** | `id-D` §2 đang phân loại HOT/WARM/COLD bằng 5 tín hiệu và số đó đã lên dashboard. Hai định nghĩa HOT cùng tên khác ruột là lỗi nặng nhất của v1.0 — v1.1 xử bằng cách **bỏ nhãn của KF-60**, ⛔ không bằng cách hiệu chỉnh cho khớp |
| ⑧ | Tuần 1: xuất 300 HT mới, 2 trưởng nhóm gắn nhãn | **Dùng 494 HT đã có làm tập vàng đầu tiên**, chỉ gắn nhãn tay **120 HT phân tầng** | 494 HT đã phân loại, đã truy ngược `HT-nnn`, đã có nhãn rào cản và nguyên nhân rơi. Gắn nhãn lại từ đầu là làm lại việc đã làm |
| ⑨ | §6 theo dõi «% `HOT_CHUA_SO` theo từng nhân viên» | **Chỉ vào sổ tay riêng của người đó** (§13) | Vi phạm rào ④ của `id-F` §7: ⛔ không bảng xếp hạng cá nhân ngoài sổ tay riêng |

---

## 1. CHỖ ĐỨNG CỦA BỘ NÀY — RANH GIỚI VỚI BA SỔ ĐANG CHẠY

```
id-D §2  → PHÂN LOẠI hội thoại  (5 tín hiệu)   → số lên dashboard, so được giữa các kỳ
KF-60    → XẾP HÀNG GỌI trong từng loại        → Sale gọi ai trước
id-F     → CHẤM NHÂN VIÊN       (22 tiêu chí)  → sổ tay kèm cặp
id-G §3  → XẾP ƯU TIÊN NỘI DUNG (hệ số 1/2/3)  → Marketing làm gì kỳ sau
```

★ **KF-60 ⛔ không thay `id-D`.** Nhãn HOT/WARM/COLD báo ra ngoài **vẫn là nhãn 5 tín hiệu**. Điểm 0–100 của bộ này là **thứ tự gọi bên trong một nhãn**, cộng một số luật ghi đè được phép đổi nhãn (§6).
⛔ Hai nơi cùng gọi một hội thoại là HOT theo hai cách khác nhau thì không ai còn tin con số nào.

---

## 2. ★ BA PHÁT HIỆN PHẢI ĐỌC TRƯỚC KHI CHẤM

### ① Hai tín hiệu mà cả bảng điểm dựa vào thì gần như **không bao giờ xuất hiện**

| Tín hiệu (`id-D` §2) | Số HT / 494 | % |
|---|---|---|
| ① Nêu dịch vụ cụ thể | 261 | 52.8% |
| ④ Hỏi điều kiện thực hiện | 100 | 20.2% |
| ③ Cho SĐT | 96 | 19.4% |
| ② **Mốc thời gian ≤14 ngày** | **9** | **1.8%** |
| ⑤ **Đồng ý khung giờ gọi** | **1** | **0.2%** |

⛔ **`B1` (thời điểm, 12 điểm) · `C2` (lịch hẹn, 8 điểm) · `C3` (chuẩn bị đến, 10 điểm) — 30 trên 100 điểm — treo vào hai tín hiệu chỉ xuất hiện 1,8% và 0,2%.** Kết quả: HOT = **3/494 = 0.6%**, chốt lịch 23/494 = 4.7%.

★ Nghĩa vận hành: **bộ chấm chưa thể sinh ra khách Hot cho tới khi trực page bắt đầu hỏi hai câu** — *"chị dự định làm khoảng khi nào"* và *"giờ nào chị nghe máy được"*. Đây là việc của `N5.3` (`id-F`), ⛔ không phải việc của bộ chấm. Đặt SLA 15 phút cho một hàng chờ 3 người là đặt sai chỗ.

### ② Rào cản lớn thứ ba của khách **không có trong bảng của v1.0**

| Mã `O` | Tên | Số HT | % mẫu | v1.0 có? |
|---|---|---|---|---|
| `O-00` | **Không xếp được** | 140 | **28.3%** | — |
| `O-01` | Giá & phát sinh | 134 | 27.1% | ✓ `gia` |
| `O-09` | Thời gian · khoảng cách | 70 | 14.2% | ✓ `khoang_cach` |
| `O-08` | **Không biết mình cần gì** | **65** | **13.2%** | ⛔ **thiếu** |
| `O-06` | **Nghi địa chỉ, uy tín** | **19** | **3.8%** | ⛔ **thiếu** |
| `O-03` | Sợ lộ sửa | 13 | 2.6% | ✓ |
| `O-12` | Bệnh nền | 12 | 2.4% | ⛔ thiếu |
| `O-04` · `O-07` | Đau/nghỉ · Bảo hành | 2 · 2 | 0.4% · 0.4% | ✓ · ⛔ |
| `O-02` · `O-10` | Kết quả xấu · So đối thủ | 1 · 1 | 0.2% · 0.2% | ✓ · ⛔ |
| `O-05` · `O-11` | Nghi bác sĩ · Người nhà | 0 · 0 | 0% | ✓ · ✓ |
| *(chưa nêu)* | Khách chưa nêu phản đối nào | 110 | 22.3% | — |

⚠️ **`O-00` = 28.3%, vượt xa ngưỡng 10% của `id-D` §1.** Theo luật sổ đó: **báo lại để bổ sung danh sách**, ⛔ agent không tự thêm mã. Cho tới khi có mã mới, `O-00` phải được đếm riêng và ⛔ không gộp vào `O-01`.
⚠️ `O-08` = *"em gửi ảnh bác xem"* — khách **không biết mình cần gì**. Đây là nhóm Warm dễ nuôi nhất và v1.0 không có chỗ để ghi.

### ③ Khách rơi **sau khi đã được trả lời**, không phải vì không ai trả lời

| | Số HT | % |
|---|---|---|
| Rơi do **trực page** | 217 | 43.9% |
| Khách tự dừng | 174 | 35.2% |
| **Không rơi** (có SĐT hoặc chốt lịch) | 100 | 20.2% |
| Hệ thống | 3 | 0.6% |

Kèm theo: **bỏ sau 1 lượt 45.3%** (224/494) · trả lời lượt đầu ≤2′ chỉ **35.4%** · **67% hội thoại dừng ở nấc A1** (329/494, chỉ 1 HT lên A2).
→ Luồng `N1` của v1.0 phải tách (§3). Và SLA gọi Hot 15 phút chỉ có nghĩa **sau khi** sửa được hai số trên.

---

## 3. Bước 0 — PHÂN LUỒNG (⛔ không chấm nhiệt độ)

| Mã | Nhãn | Dấu hiệu | Chuyển cho | SLA |
|---|---|---|---|---|
| `N1a` | **Chưa tương tác thật** | Chỉ có tin tự động từ quảng cáo, hoặc ≤1 tin tự viết **và chưa được trả lời** | Nhân viên page / bot mở lời lại | 2–4h |
| `N1b` | ★ **Đã trả lời rồi khách im** | KH ≤1–2 tin tự viết nhưng **đã nhận câu trả lời** rồi dừng | ⛔ **Vẫn chấm như LEAD.** Gắn `nguyen_nhan_roi="trực page"` → `id-D` §3 + `id-F` | theo nhãn nhiệt |
| `N2` | Không phải lead | Spam, chào hàng, đối tác, tuyển dụng, báo chí | Admin page | 24h |
| `N3` | KH cũ – CSKH | Tái khám, hậu phẫu, bảo hành, lịch hẹn đã có | CSKH chi nhánh | 4h |
| `N4` | **Cảnh báo đỏ** | Khiếu nại, nghi biến chứng, đòi hoàn tiền, dọa đánh giá xấu/báo chí/kiện | Quản lý chi nhánh + quy trình khủng hoảng **+ đầu mối pháp chế** (`id-K`) | **≤30 phút** |
| `N5` | Chưa đủ điều kiện | Chưa đủ tuổi với dịch vụ PTTM, hoặc KH tự nói tình trạng không phù hợp (mang thai…) | Tư vấn an toàn, ⛔ không bán | 24h |

★ **`N1b` là luồng mới và là luồng đông nhất.** Gộp nó vào `N1a` làm hai việc sai cùng lúc: bỏ qua một lead thật, và che mất lỗi câu trả lời của trực page.
> KH cũ hỏi **dịch vụ mới** vẫn chấm như lead, kèm cờ `KH_cu_cross_sell` — nhóm LTV cao nhất.

---

## 4. Bước 1 — BẢNG ĐIỂM CỘNG (tổng tối đa 100)

Thang điểm giữ nguyên v1.0 ở ba nhóm A, B, D. **Nhóm C sửa một ô** (`C3`).

**A. Nhu cầu & mức phù hợp — tối đa 25**

| Mã | Tiêu chí | Mức → Điểm |
|---|---|---|
| `A1` | Xác định dịch vụ ★ = tín hiệu ① | Chung chung 0 · Nhóm dịch vụ 4 · Dịch vụ cụ thể 8 |
| `A2` | Mô tả tình trạng của chính mình | Không 0 · Có mô tả 4 · **Gửi ảnh/video** 8 |
| `A3` | Khả năng đến cơ sở | Không rõ 0 · Ở gần CN / Việt kiều có ngày về 3 · Nói rõ sẽ đến, đã biết CN 5 |
| `A4` | Hỏi cho ai | Không rõ 0 · Cho chính mình / người thân cụ thể 4 |

**B. Ý định mua — tối đa 35**

| Mã | Tiêu chí | Mức → Điểm |
|---|---|---|
| `B1` | Thời điểm dự kiến ★ = tín hiệu ② — **1.8% mẫu** | Chưa rõ 0 · 1–3 tháng 5 · ≤1 tháng 9 · ≤2 tuần hoặc gắn sự kiện 12 |
| `B2` | Hỏi giá có ngữ cảnh | Không hỏi 0 · Chỉ *"giá bao nhiêu"* 2 · Hỏi giá cho tình trạng của mình 5 · Hỏi trả góp/cọc/ưu đãi còn hạn 8 |
| `B3` | Hỏi thông tin để ra quyết định ★ = tín hiệu ④ | Không 0 · 1 chủ đề 4 · ≥2 chủ đề 8 |
| `B4` | Đang so sánh / đã tư vấn nơi khác (= `O-10`) | Không 0 · Có 7 |

**C. Cam kết hành động — tối đa 25**

| Mã | Tiêu chí | Mức → Điểm |
|---|---|---|
| `C1` | SĐT/Zalo ★ = tín hiệu ③ | Chưa có 0 · Để lại SĐT/Zalo hợp lệ 12 |
| `C2` | Lịch hẹn | Không 0 · Hỏi lịch trống 4 · Đồng ý ngày/giờ cụ thể 8 |
| `C3` | **Chuẩn bị đến** — ⚠ **sửa ở v1.1** | Không 0 · **Hỏi địa chỉ/đường đi/gửi xe 2** · Hỏi cách chuyển cọc 5 |

⚠️ **Vì sao hạ `C3` hỏi-địa-chỉ từ 5 xuống 2:** trong kỳ này **70 HT mang `O-09`** và hỏi địa chỉ là câu mở đầu rất thường gặp của khách ở tỉnh — nhưng nhóm CD6 *(khách tỉnh)* chỉ **9.4% cho SĐT** và **4/64 đạt WARM**. Hỏi địa chỉ ⛔ không phải tín hiệu cam kết; hỏi **cách chuyển cọc** thì đúng là. Để cùng 5 điểm làm cả nhóm CD6 nhảy hạng sai.

**D. Mức tương tác — tối đa 15** *(giữ nguyên v1.0)*

| Mã | Tiêu chí | Mức → Điểm |
|---|---|---|
| `D1` | Số tin KH tự viết | 1–2 tin 0 · 3–5 tin 3 · 6–10 tin 5 · >10 tin 6 |
| `D2` | Vẫn hỏi/trả lời tiếp **sau khi đã biết giá** | Không 0 · Có 5 |
| `D3` | Tốc độ KH trả lời (trung vị) | >1 giờ 0 · <1 giờ 2 · <10 phút 4 |

---

## 5. Bước 2 — TÍN HIỆU ÂM (tối đa −30) · giữ nguyên v1.0

| Mã | Tín hiệu | Điểm | Ghi chú v1.1 |
|---|---|---|---|
| `E1` | Biết giá rồi im lặng ≥48h | −10 | ⚠ phải ghi kèm `nguyen_nhan_roi` — xem cảnh báo dưới |
| `E2` | Phản đối giá / *"để em tính"* rồi **không** tương tác tiếp | −5 | = `O-01` |
| `E3` | Từ chối cho số sau ≥2 lần được xin | −5 | ⚠ chỉ trừ khi `N5.1` của `id-F` đạt |
| `E4` | *"Hỏi cho biết"*, hỏi hộ không rõ ai | −5 | |
| `E5` | Ở xa, không có kế hoạch đến | −5 | = `O-09`, ⛔ không trùng `C3` |

⚠️ **`E1` và `E3` là hai ô dễ chấm sai người nhất.** 43.9% hội thoại rơi vì **câu trả lời của trực page**, và `N5.1` *(xin số có lý do cụ thể)* là tiêu chí trượt nhiều. Khách im sau một câu trả lời không đóng được nỗi sợ ⛔ **không phải khách nguội** — đó là lead còn nóng bị trả lời sai.
→ Luật: **trừ `E1`/`E3` chỉ khi hội thoại có `nguyen_nhan_roi = "khách tự dừng"`.** Nếu là `"trực page"` thì ⛔ không trừ, và đẩy sang `id-F`.

---

## 6. Bước 3 — LUẬT GHI ĐÈ

| # | Luật | Thành |
|---|---|---|
| ① | Có SĐT **và** (thời điểm ≤1 tháng **hoặc** đồng ý lịch cụ thể) | **HOT** |
| ② | Hỏi **cách chuyển cọc** | **HOT** |
| ③ | ★ **mới v1.1** — Có SĐT **và** (dịch vụ cụ thể **hoặc** ≥2 chủ đề quyết định) | **HOT** |
| ④ | Khớp luật Hot nhưng **chưa có SĐT/Zalo** | nhãn **`HOT_CHUA_SO`** |
| ⑤ | **sửa v1.1** — WARM trở lên mà **chưa có SĐT** | cũng vào hàng **`HOT_CHUA_SO`** |
| ⑥ | Có SĐT nhưng **tổng nhóm B = 0** (để số vì form/khuyến mãi) | trần **WARM** |

★ **Luật ③ là cái làm hàng chờ Sale tồn tại** — ⛔ và đo rồi thì thấy nó là thứ *duy nhất* làm được việc đó: điểm thuần hầu như không ai vượt ngưỡng. Số lần mỗi luật chạy trên kỳ 24–29/10: ① **20** · ② **0** · ③ **70** · ⑥ chặn lại **36**.
★ **Luật ⑤ nối thẳng với ô đỏ của dashboard.** `id-D` §2: ô nguy hiểm nhất là **HOT/WARM chưa có SĐT** — kỳ này **43 HT**, trong đó HOT 0 và **WARM 43**. Nhãn `HOT_CHUA_SO` của v1.0 chỉ phủ HOT nên bỏ sót đúng 43 lead đang rơi.

---

## 7. Bước 4 — HỆ SỐ THỜI GIAN · PHÂN BỐ ĐIỂM THẬT · BỐN NHÓM GỌI

### 7.1 Hệ số thời gian *(giữ nguyên v1.0)*

**Nhiệt độ hiện tại** = Điểm gốc × hệ số, tính từ **tin cuối của KH**:

| Từ tin cuối KH | ≤24h | 1–3 ngày | 4–7 ngày | >7 ngày |
|---|---|---|---|---|
| Hệ số | 1,0 | 0,85 | 0,7 | 0,5 |

⛔ Không áp hệ số nếu KH đã có lịch hẹn trong tương lai. KH nhắn tin mới thì chấm lại.

### 7.2 ★ PHÂN BỐ ĐIỂM THẬT — và vì sao KF-60 ⛔ không phát nhãn nữa

Chấm **493 hội thoại** của kỳ 24–29/10 bằng đúng thang §4–§6:

| | Điểm gốc /100 | Sau hệ số thời gian |
|---|---|---|
| Trung vị | **12** | 9,8 |
| p75 | 20 | 16,9 |
| p90 | 35 | 28,9 |
| **Cao nhất** | **65** | 65,0 |
| Số HT vượt 50 | **5** | 5 |

**Trung bình từng nhóm so với trần:**

| Nhóm | Trần | Trung bình | Cao nhất thực | |
|---|---|---|---|---|
| A · nhu cầu | 25 | **8,5** | 25 | |
| B · ý định mua | 35 | **1,4** | 21 | ⛔ **nhóm gần như không ghi điểm** |
| C · cam kết | 25 | 3,1 | 22 | |
| D · tương tác | 15 | 2,9 | 15 | |
| E · tín hiệu âm | −30 | −1,4 | 0 | |

★ **Nhóm B — 35 trên 100 điểm — trung bình 1,4.** Đó là hệ quả trực tiếp của §2 ①: `B1` cần mốc thời gian (1,8% mẫu), `B4` cần khách so đối thủ (0,2%), `B3` cần chủ đề ra quyết định. Thang điểm này **chưa thể phân biệt lead trên tệp hiện tại** vì hai phần ba trọng số nằm ở những điều khách chưa bao giờ nói.

### Thử mọi cặp ngưỡng — ⛔ không cặp nào cứu được

| Ngưỡng (có luật ghi đè) | HOT / WARM / COLD | Lệch so với nhãn `id-D` |
|---|---|---|
| ≥50 / ≥25 | 72 · 12 · 409 | 116 HT (**23,5%**) |
| ≥40 / ≥20 | 74 · 32 · 387 | 126 HT (25,6%) |
| ≥35 / ≥15 | 74 · 68 · 351 | 150 HT (30,4%) |
| ≥30 / ≥12 | 77 · 109 · 307 | 188 HT (38,1%) |
| ≥50 / ≥25 · **bỏ luật ghi đè** | **5** · 68 · 420 | 63 HT (12,8%) |

⛔ **Kết luận buộc phải nhận:** mức lệch thấp nhất là 12,8% — hơn gấp đôi ngưỡng 5% mà bản nháp của §7.3 đặt ra — và đạt được nó phải trả giá bằng một hàng chờ 5 người. **Luật 5% đó là một luật sai**, vì nó bắt hai dụng cụ đo khác nhau phải cho cùng một số: `id-D` đếm **5 tín hiệu nhị phân**, KF-60 **cân 19 tiêu chí**. Chúng khác nhau có chủ ý.

### 7.3 ★ BỐN NHÓM GỌI — ĐẦU RA THẬT CỦA BỘ NÀY

KF-60 phát **việc**, ⛔ không phát nhãn. Nhãn HOT/WARM/COLD của kỳ **chỉ có một bản**, là nhãn 5 tín hiệu của `id-D` §2.

| Nhóm | Ai làm · SLA | Vào nhóm khi | Kỳ 24–29/10 |
|---|---|---|---|
| **`GOI_NGAY`** | **Sale gọi ≤15′** | Có SĐT **và** khớp luật ghi đè ①②③, ⛔ trừ khi luật ⑥ chặn | **36** · 7,3% |
| **`XIN_SO`** | **Trực page xin số ≤15′** | Chưa có SĐT **và** (`id-D` xếp HOT/WARM **hoặc** điểm ≥17) | **70** · 14,2% |
| **`NUOI`** | Sale/CSKH online · 24–72h | Có SĐT, hoặc `id-D` WARM, hoặc điểm ≥17 | **60** · 12,2% |
| **`KHONG`** | Marketing · remarketing tự động | Còn lại | **327** · 66,3% |

**Ngưỡng duy nhất còn lại: `NGUONG_NUOI = 17`** — p75 của phân bố nhiệt đo được. Nó chỉ quyết định `NUOI` so với `KHONG`, ⛔ không quyết định ai được gọi. ⚠ Vẫn là **ngưỡng tạm**: chưa có dòng CRM để đối chiếu booking.

### Hai bất biến — thay cho luật 5% đã bỏ

```
① ⛔ Mọi HT trong nhóm GOI_NGAY phải CÓ SĐT.
   Không có số thì không gọi được — nó thuộc XIN_SO, và người làm là trực page.

② ⛔ Mọi HT mà id-D xếp HOT phải KHÔNG nằm trong nhóm KHONG.
   Lead nóng nhất của kỳ rơi vào remarketing tự động là lỗi nghiêm trọng.

Hai số này phải bằng 0. Khác 0 là LỖI CODE, ⛔ không phải chuyện hiệu chỉnh ngưỡng
— và báo cáo tự gắn cờ 🔴 vào đầu trang, ⛔ không phát hàng chờ.
Kỳ 24–29/10: ① 0 · ② 0 — đạt.
```

### Bảng đối chiếu — để ĐỌC, ⛔ không để bắt khớp

| Nhãn `id-D` | Gọi ngay | Xin số | Nuôi | Remarketing | Tổng |
|---|---|---|---|---|---|
| 🔴 HOT | **3** | 0 | 0 | 0 | 3 |
| 🟠 WARM | 32 | **43** | 42 | 0 | 117 |
| ⚪ COLD | 1 | 27 | 18 | 327 | 373 |

★ **Ô `WARM × XIN_SO` ra đúng 43** — bằng chính con số *«HOT/WARM chưa có SĐT = 43»* mà `id-D` §2 đã đếm độc lập bằng cách khác. Hai đường tính khác nhau gặp nhau ở một số là bằng chứng mạnh nhất có được ở bước này.
⚠ Một HT `COLD` lọt vào `GOI_NGAY`: khách cho số và hỏi ≥2 chủ đề ra quyết định nhưng **chưa gọi tên dịch vụ** nào — nên chỉ đạt 1 tín hiệu của `id-D`. Đây là chỗ KF-60 **thấy được điều `id-D` bỏ sót**, ⛔ không phải lỗi.

---

## 8. Bước 5 — ĐIỂM ƯU TIÊN GỌI

```
Ưu tiên = Điểm sau hệ số thời gian × hệ số giá trị đơn
```
Điểm này chỉ xếp **thứ tự trong một nhóm gọi**, ⛔ không đổi nhóm. Nhóm đã mang mức cấp bách rồi, nên v1.1 ⛔ **bỏ cái sàn «tối thiểu bằng ngưỡng Hot»** của bản nháp — sàn đó chỉ có nghĩa khi còn nhãn.

**Hệ số giá trị đơn — ✅ anh UY duyệt 02/11/2026 · lấy đúng thang `id-G` §3:**

| Bậc | Giá trị đơn ước tính | Hệ số |
|---|---|---|
| Thấp | < 5 triệu | **1** |
| Trung | 5 – 15 triệu | **2** |
| Cao | ≥ 15 triệu | **3** |
| ⚠ Chưa có giá, hoặc khách chưa nêu dịch vụ | | **1** ⚠ |

⚠️ Hệ số đi theo **dịch vụ khách hỏi**, ⛔ không theo BL và ⛔ không theo chân dung — **trừ** khi bản phác họa chân dung của kỳ đã khai `he_so_gia_tri` (`id-C` §2); khi có, số đó thắng, vì là kết luận của người đã đọc cả tệp. Kỳ 24–29/10 đã khai: CD1 `2` · CD3 `2` · CD4 `2` · CD2/CD5/CD6/CD7/CD0 `1`.

**Vì sao bỏ thang BL 1,0–0,5 của v1.0:**
```
① Kỳ 24–29/10 toàn bộ là line Da → mọi lead bị nhân 0,5–0,7.
   Trong một hàng chờ trộn với PTTM, không lead nào của line này được gọi trước.
② Giá trị đơn đi theo DỊCH VỤ, không theo BL: một ca implant toàn hàm
   và một ca tẩy trắng cùng nằm trong "Nha khoa 0,8".
③ Repo đã có một thang hệ số đang chạy. Hai thang = hai thứ tự ưu tiên.
```
⚠️ Hệ số **ước từ bảng giá chuẩn, không phải doanh thu thật** → mọi ô dùng hệ số gắn `⚠`. Khi hệ thống cấp bảng giá hiện hành (`id-K` §3) thì thay số thật và ghi vào `doc/CHANGELOG.md`.
★ Beauty & Spa là cửa vào hệ sinh thái: **khách nhóm `GOI_NGAY` của B&S vẫn gọi trong SLA**, chỉ xếp sau khi trùng giờ.

### ⚠ Hệ quả đo được của chính thay đổi này

Trên hàng chờ kỳ 24–29/10 (106 dòng), thang mới cho ra: **hệ số 1 → 103 dòng · hệ số 3 → 3 dòng · hệ số 2 → 0 dòng.**

Thang `1/2/3` **sửa được** cái sai của thang BL cũ — line Da không còn bị nhân xuống 0,5–0,7 nên lead của nó vào được hàng chờ trộn. Nhưng ⛔ **trên riêng line Da nó gần như phẳng**: `gia_tri_don` bậc 1 chứa đúng toàn bộ dịch vụ da (trị nám · tàn nhang · filler · botox · chăm sóc da), bậc 2 là mũi/mí, bậc 3 là implant/hút mỡ. Nghĩa là **97% hàng chờ cùng nhân 1**, và thứ tự gọi thực tế do **điểm** quyết định, ⛔ không do hệ số.

→ Hệ số chỉ bắt đầu có việc khi hàng chờ **trộn nhiều line**. Đó chính là lý do việc ③ ở §16 — xin một kỳ PTTM — là việc chặn, ⛔ không phải việc tốt-thì-có.
⚠ Và ⛔ đừng đọc «hệ số 1» là «khách giá trị thấp»: nó chỉ nói **bậc giá vé ước từ bảng giá chuẩn**, mà bảng giá hiện hành của line Da thì hệ thống **chưa cấp** (`id-K` §3).

---

## 9. ĐẦU RA AI CHO MỖI HỘI THOẠI

- **`ht_id`** — ⛔ bắt buộc, dạng `HT-nnn`. Không có thì bỏ hội thoại khỏi mẫu.
- **Dịch vụ quan tâm** + cờ `KH_cu_cross_sell`.
- **Rào cản**: `O-01…O-12`, không xếp được thì `O-00` **và đếm riêng** — ⛔ đừng tự thêm mã.
- **Nguyên nhân rơi**: ⛔ **đúng một** trong `nội dung · trực page · hệ thống · khách tự dừng · không rơi` (`id-D` §3).
- **Bằng chứng**: 1–3 câu chat ngắn, **đã ẩn danh**, cho mỗi tiêu chí có điểm.
- **Câu tiếp theo đề xuất** (1–2 câu).
- **Cờ chất lượng tư vấn**: ⛔ **không chấm lại nhân viên** — chỉ ghi dữ kiện thô và trỏ về mã `N` của `id-F`.
- **Cờ pháp chế**: `CĐ-1…CĐ-6`. ⛔ `O-07` (bảo hành) và `O-12` (bệnh nền) — agent ⛔ không tự trả lời.

### Mẫu JSON v1.1

```json
{
  "ht_id": "HT-001",
  "conversation_id": "",
  "page_id": "",
  "ad_id": "",
  "route": "LEAD | N1a | N1b | N2 | N3 | N4 | N5",
  "service": {"bl": "Da", "service": "Trị nám", "he_so_gia_tri": 2},
  "cd": "CD3",
  "nac": "A1",
  "cross_sell_existing_customer": false,
  "scores": {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0},
  "criteria_hits": [
    {"code": "B1", "level": "≤2 tuần / gắn sự kiện", "points": 12,
     "evidence": "tháng 12 em cưới", "ht_id": "HT-001"}
  ],
  "goc": 0,
  "ghi_de": ["HOT_SDT_MOC", "HOT_COC", "HOT_SDT_DV", "TRAN_WARM", "HOT_CHUA_SO"],
  "gio_im": 0,
  "he_so_tg": 1.0,
  "chot_lich": false,
  "diem": 0,
  "nhom_goi": "GOI_NGAY | XIN_SO | NUOI | KHONG",
  "tin_hieu": {"1_dich_vu": false, "2_thoi_gian": false, "3_sdt": false,
               "4_dieu_kien": false, "5_khung_gio": false},
  "nhiet": "HOT | WARM | COLD",
  "co_sdt": false,
  "uu_tien": 0,
  "ma_o": ["O-01", "O-09"],
  "ma_o_00": false,
  "nguyen_nhan_roi": "trực page",
  "next_best_message": "",
  "du_kien_truc_page": {"da_xin_so": true, "phan_hoi_dau_phut": 3,
                        "tra_loi_cau_hoi_gia": true, "tro_ve": ["N5.1", "N3.1"]},
  "co_phap_che": [],
  "confidence": 0.0
}
```

⚠️ `nhiet` (nhãn 5 tín hiệu) và `nhom_goi` (việc) **phải cùng có mặt**: cái đầu là nhãn báo ra ngoài, cái sau là việc. ⛔ Không có trường nào phát nhãn HOT/WARM/COLD thứ hai.
⚠️ Khối tổng hợp cho báo cáo còn mang `o` — **điểm từng ô tiêu chí A1…E5** — để người soát cãi lại được từng ô. Xem cột `A1`…`E5` trong `out/cham-hoi-thoai.csv`.

### Prompt lõi cho AI

> Bạn là chuyên viên chấm điểm lead của hệ thống y tế – thẩm mỹ Kangnam/HCI. Đọc toàn bộ hội thoại Messenger giữa KHÁCH và NHÂN VIÊN.
>
> Chỉ chấm dựa trên lời hoặc hành động của KHÁCH; lời nhân viên chỉ dùng làm ngữ cảnh và để ghi `du_kien_truc_page`.
>
> Làm đúng thứ tự:
> 0. Phân luồng `N1a` · `N1b` · `N2`–`N5` hoặc `LEAD`. **Khách đã nhận câu trả lời rồi mới im là `N1b`, vẫn chấm như LEAD.**
> 1. Chấm A, B, C, D theo bảng tiêu chí; mỗi tiêu chí chọn **đúng một** mức.
> 2. Trừ điểm nhóm E — ⛔ chỉ trừ `E1`/`E3` khi `nguyen_nhan_roi = "khách tự dừng"`.
> 3. Áp 6 luật ghi đè.
> 4. Nhân hệ số thời gian → `diem`. Chấm 5 tín hiệu `id-D` → `nhiet`. ⛔ Không phát nhãn HOT/WARM/COLD nào khác.
> 5. Xếp vào **một** trong bốn `nhom_goi` theo §7.3, rồi tính điểm ưu tiên bằng hệ số giá trị đơn 1/2/3.
>
> Gán rào cản bằng `O-01…O-12`; không xếp được thì `O-00`, ⛔ **tuyệt đối không tự đặt mã mới**.
> Gán **đúng một** nguyên nhân rơi.
> Với mỗi tiêu chí có điểm, trích câu chat làm bằng chứng kèm `HT-nnn`; **không có bằng chứng thì cho 0**.
> ⛔ Không suy diễn SĐT: chỉ tính khi thấy dãy số hợp lệ hoặc số/tên Zalo.
> ⛔ Không ghi lại thông tin sức khỏe chi tiết ngoài dịch vụ quan tâm; ⛔ bỏ hết tên, SĐT, ảnh của khách trong phần bằng chứng.
> ⛔ Không tự trả lời `O-07` (bảo hành) và `O-12` (bệnh nền).
> Trả về đúng JSON mẫu, không thêm chữ.

(Đính kèm vào prompt bảng tiêu chí mới nhất xuất từ tab `2. Tiêu chí` của file Driver, **và** bảng 12 mã `O` của `id-D` §1.)

---

## 10. ACTION PLAN THEO PHÂN LOẠI (SLA)

| Nhãn | Ai xử lý | SLA | Việc cần làm |
|---|---|---|---|
| `N4` Cảnh báo đỏ | Quản lý CN + CSKH + pháp chế | **≤30 phút** | Quy trình khủng hoảng, ⛔ không tranh luận trên inbox |
| **`GOI_NGAY`** | Sale senior theo BL | Gọi ≤15 phút (giờ làm việc); ngoài giờ thì trước 9h sáng hôm sau | Chốt lịch tư vấn bác sĩ / đặt cọc, gửi case thật **cùng nhóm tình trạng** |
| **`XIN_SO`** ★ | Nhân viên trực page | ≤15 phút | Xin số theo kịch bản `N5.1`, gắn với giá trị cho khách (*"bác sĩ xem ảnh và gọi tư vấn riêng"*) |
| **`NUOI`** | Sale/CSKH online | 24–72h | Chuỗi chăm sóc Zalo **theo mã `O`**, mời tư vấn bác sĩ online |
| **`KHONG`** | Marketing (CDP) | Tự động | Remarketing, chuỗi nội dung TOF/MOF 7–14 ngày |
| `N1a` | Bot/nhân viên page | 2–4h | Mở lời lại 1 lần; không phản hồi thì coi như Cold |
| `N1b` ★ | Trực page + Marketing | theo nhãn nhiệt | Chấm như lead **và** ghi lỗi câu trả lời về `id-F` / `id-D` §7 |

### ★ THỨ TỰ SỬA — ⛔ ĐỪNG ĐẢO

```
① Trực page hỏi MỐC THỜI GIAN và KHUNG GIỜ GỌI   (tín hiệu ② 1.8% · ⑤ 0.2%)
   → không có bước này thì hàng chờ HOT vẫn chỉ vài người, SLA 15 phút vô nghĩa.
② Trả lời lượt đầu ≤2 phút                        (đang 35.4%)
③ Không bỏ khách sau 1 lượt                       (đang 45.3% bị bỏ)
④ Rồi mới siết SLA gọi Hot.
```

**Gắn với bộ chấm chiến dịch (KF-49/50):**
- Lấy `ad_id` từ tham chiếu hội thoại click-to-Messenger, nối về chiến dịch.
- Theo dõi **% Hot+Warm/tổng inbox** và **% Hot** theo chiến dịch.
- ⚠ Đề xuất **chờ duyệt**: thay một phần trọng số Lead→Booking bằng **% `GOI_NGAY` + % `XIN_SO`** — ⛔ chỉ sau khi nhóm B được cân lại (§13), vì hàng chờ hiện do luật ghi đè quyết định chứ không do điểm.

---

## 11. LỘ TRÌNH TRIỂN KHAI 6 TUẦN

| Tuần | Việc | Đầu ra |
|---|---|---|
| 1 | ★ **Dùng 494 HT của 24–29/10 làm tập vàng đầu tiên** — đã phân loại, đã truy ngược `HT-nnn`. 2 trưởng nhóm Sale gắn nhãn tay **độc lập** trên **120 HT phân tầng** (theo CD và theo nhãn nhiệt). ⚠ Tập này **chỉ có line Da** → xin thêm **1 kỳ PTTM** trước khi kết luận gì về hệ số | Tập vàng 120 HT + 1 kỳ PTTM đang chờ |
| 2 | AI chấm cùng 120 HT, so với nhãn người. ★ **So nhãn người với `nhom_goi`, ⛔ không so với một nhãn HOT/WARM/COLD của KF-60 — nhãn đó đã bỏ** | Mục tiêu: nhóm `GOI_NGAY` **đúng ≥85%** (người chấm cũng nói «gọi ngay»). Hai bất biến §7.3 phải bằng 0. ★ **Việc nặng nhất của tuần này là cân lại nhóm B** (trung bình 1,4/35) |
| 3–4 | Chạy song song tại 1–2 page thí điểm **đã nối CRM** | Tỷ lệ booking theo CRM của nhóm Hot và nhóm Warm |
| 5–6 | ★ **Thay `NGUONG_NUOI` và trọng số nhóm B bằng số đo từ booking thật** | Bộ v1.2 + SOP nhân rộng |

**Chỉ số theo dõi**

| Chỉ số | Mốc kỳ 24–29/10 |
|---|---|
| Booking theo `GOI_NGAY` / `XIN_SO` / `NUOI` / `KHONG` — phải **giảm dần rõ rệt** | chưa có dòng CRM |
| Hàng chờ `GOI_NGAY` · `XIN_SO` | **36** · **70** |
| Hai bất biến §7.3 | **0 · 0** — đạt |
| Trung bình nhóm B / 35 | **1,4** — ⛔ thang điểm chưa phân biệt được lead |
| Tín hiệu ② mốc thời gian | 1.8% → mục tiêu kỳ sau |
| Tín hiệu ⑤ khung giờ gọi | **0.2%** → mục tiêu kỳ sau |
| HOT/WARM chưa có SĐT | **43 HT** |
| Có SĐT | 19.4% |
| Bỏ sau 1 lượt | 45.3% |
| `O-00` | **28.3%** — ⛔ vượt ngưỡng 10%, đang chờ bổ sung mã |
| % Hot theo chiến dịch | chưa nối `ad_id` |

⚠ **Ba nhóm booking không tách biệt nhau thì tiêu chí chưa đúng** — ⛔ đừng siết SLA, sửa tiêu chí.

**Điều kiện kỹ thuật:** lấy được nội dung hội thoại từ Caresoft hoặc API hộp thư Page · gộp trùng khách nhắn nhiều page (theo SĐT hoặc PSID) · thí điểm trước ở page đã nối CRM.

---

## 12. ★ RÀO AN TOÀN — KẾ THỪA `id-F` §7

```
① ĐIỂM NÀY CHẤM KHÁCH, KHÔNG CHẤM NGƯỜI.
   Mọi dữ kiện về nhân viên trong JSON là ĐẦU VÀO cho id-F, ⛔ không phải điểm.

② MỖI ĐIỂM PHẢI CÓ BẰNG CHỨNG GẮN HT-nnn.
   Không trích được câu chat → tiêu chí đó cho 0, ⛔ không đoán.

③ LỖI HỆ KHÔNG TRỪ ĐIỂM AI.
   Thiếu bảng giá · page không có dịch vụ · ngoài giờ → nguyen_nhan_roi="hệ thống",
   ⛔ không trừ khách E-gì, ⛔ không trừ nhân viên.

④ ⛔ KHÔNG XẾP HẠNG CÁ NHÂN CÔNG KHAI.
   «% HOT_CHUA_SO theo từng nhân viên» CHỈ xuất hiện trong sổ tay riêng của
   người đó và bản của trưởng nhóm. ⛔ Không dán lên màn hình chung.

⑤ ĐIỂM LÀ THỨ TỰ GỌI, ⛔ KHÔNG PHẢI QUYỀN ĐƯỢC TƯ VẤN.
   ⛔ Không dùng điểm để bỏ khách hay từ chối tư vấn y khoa.
   Khách Cold vẫn được chăm sóc tự động.
```

---

## 13. RISK / WARNING

- **Dữ liệu sức khỏe là dữ liệu nhạy cảm**: giới hạn quyền xem · che SĐT khi gửi sang công cụ AI bên ngoài nếu không cần · ⛔ không lưu ảnh ngoài hệ thống · tin chào tự động có câu xin đồng ý xử lý dữ liệu. **Cần pháp chế xác nhận trước khi chạy toàn hệ thống.**
- **`NGUONG_NUOI` và hệ số ở §8 chưa được booking kiểm.** Suy từ một kỳ, một line. ⛔ Đừng dùng để đánh giá chiến dịch hay con người cho tới tuần 5–6.
- ★ **Thang 100 điểm hiện chưa phân biệt được lead trên tệp này** — nhóm B đạt 1,4/35, cao nhất toàn tệp 65/100. Hàng chờ đang do **luật ghi đè** quyết định, ⛔ không do điểm. Nghĩa là: cải thiện bộ chấm bằng cách **thêm trọng số cho những gì khách THỰC SỰ nói** (`O-08` không biết mình cần gì, `O-09` ở xa, gửi ảnh tình trạng), ⛔ không bằng cách hạ ngưỡng.
- **Tập vàng hiện có lệch line.** 494 HT đều là line Da; CD1–CD7 là ca da/tiêm. ⛔ Không kết luận gì về PTTM từ tập này.
- **`O-00` = 28.3%** — hơn một phần tư rào cản chưa có mã. Mọi bảng đếm mã `O` kỳ này phải hiện `O-00` riêng, ⛔ không gộp.
- **AI bịa bằng chứng / đọc sai SĐT**: bắt buộc trường bằng chứng; kiểm ngẫu nhiên 5% mỗi tuần.
- ⚠ **Hai lỗ hổng đã biết của bộ chấm, đo được, chưa vá:**
  - `chot_lich` nhận ra lúc **đặt** lịch nhưng ⛔ không nhận ra lúc khách **huỷ**. Kỳ 24–29/10: **2 trong 23** ca chốt lịch sau đó có lời giống huỷ/hoãn, và cả hai đang nằm trong `GOI_NGAY`. Chốt lịch còn **miễn hệ số thời gian**, nên hai ca đó không bị nguội. ⚠ Để nguyên là chấp nhận được (khách huỷ vì bác sĩ không có mặt vẫn là khách nóng), nhưng ⛔ đừng đọc `chot_lich` như «đã đến khám».
  - `dich_vu` lấy theo **thẻ quảng cáo** của bản xuất, còn `he_so` lấy theo **chữ của khách** — hai cột có thể nói hai dịch vụ khác nhau trên cùng một dòng hàng chờ. ⛔ Đừng cộng doanh thu dự kiến từ cặp này.
- **Nhân viên "làm đẹp" điểm**: điểm chỉ tính lời khách; kết quả cuối đo bằng booking.
- **Lệch theo BL**: theo dõi Hot→Booking theo từng BL; lệch thì tách ngưỡng ở v1.2.
- **Hội thoại đa ngôn ngữ**: CD1 *(khách nói tiếng nước ngoài)* có **29 HT** trong kỳ. Tiêu chí giữ nguyên; prompt phải nêu rõ AI đọc được tiếng Anh và ngôn ngữ khác.

---

## 14. TỰ KIỂM BẢN NÀY

- [ ] Mọi hội thoại có `ht_id` truy ngược được chưa?
- [ ] Báo cáo có đúng **một** nhãn HOT/WARM/COLD (của `id-D`) không, hay có chỗ nào phát nhãn thứ hai?
- [ ] Hai bất biến §7.3 có bằng **0** không? Khác 0 thì đã **dừng phát hàng chờ** chưa?
- [ ] `nhom_goi` của mọi HT có nằm trong đúng bốn giá trị không?
- [ ] Rào cản có dùng đúng `O-01…O-12`/`O-00`, ⛔ không mã tự đặt?
- [ ] `O-00` vượt 10% đã **báo lại** chưa?
- [ ] `nguyen_nhan_roi` có **đúng một** giá trị, và tổng có bằng cỡ mẫu?
- [ ] `E1`/`E3` có bị trừ cho hội thoại rơi do **trực page** không?
- [ ] Ô `HOT/WARM chưa có SĐT` có lên thẻ số tổng chưa?
- [ ] Có số liệu cá nhân nào của nhân viên lọt ra ngoài sổ tay riêng không?
- [ ] `NGUONG_NUOI` có bị trích dẫn như con số đã kiểm bằng booking không?
- [ ] Phân bố điểm §7.2 có được đọc kèm cảnh báo «nhóm B 1,4/35» không?
- [ ] Đã bỏ hết tên · SĐT · ảnh khách trong phần bằng chứng chưa?
- [ ] `O-07` và `O-12` có bị tự trả lời không?

---

---

## 15. CHẠY Ở ĐÂU

> ⚠ Bảng đường dẫn đã có ở **đầu sổ**; mục này giữ phần lệnh chạy và luật sửa hai nơi.

| Thứ | Chỗ |
|---|---|
| Bộ chấm | `tools/id.py` → `cham_lead()` · `gom_lead()` · hằng `NGUONG_NUOI`, `NHOM_GOI` |
| Từ khoá | `tools/tu_dien.json` → khối `lead_kf60` (23 nhóm · 219 từ khoá) |
| Đọc bản xuất KNB | `tools/knb.py` |
| Khối trong file báo cáo | `dashboard/data/<ky>.json` → `lead` · schema `insight-dashboard-kangnam/2` |
| Từng ô tiêu chí mỗi HT | `out/cham-hoi-thoai.csv` → cột `A1`…`E5`, `lead_*` |
| Trang hiển thị | tab **Hàng chờ gọi** · bố cục `?bo_cuc=sale` |

```bash
python tools/knb.py data/<file KNB>.txt --ky "24-29/10"   # hoặc id.py doc cho khuôn Caresoft
python tools/id.py bao-cao --ky "24-29/10"
```

⛔ Sửa tiêu chí thì sửa ở `tools/id.py` và ở bản này **cùng lúc**. Thang điểm nằm hai chỗ mà lệch nhau thì không ai biết báo cáo đang chấm theo bản nào.

---

## 16. NHẬT KÝ DUYỆT

| Ngày | Người duyệt | Duyệt cái gì | Lệch khỏi bản nào |
|---|---|---|---|
| 02/11/2026 | anh UY | **v1.0** — toàn bộ bộ chấm, áp dụng tạm thời | — |
| **02/11/2026** | **anh UY** | ① **Bỏ nhãn HOT/WARM/COLD của KF-60**, thay bằng bốn nhóm gọi `GOI_NGAY` · `XIN_SO` · `NUOI` · `KHONG` và hai bất biến (§7.3). Bỏ luôn luật *«lệch nhãn >5% thì dừng»* | v1.0 Bước 4 · bản nháp v1.1 §7.3 |
| **02/11/2026** | **anh UY** | ② **Hệ số BL `1,0 / 0,8 / 0,8 / 0,7 / 0,5` → thang giá trị đơn `1 / 2 / 3`** của `id-G` §3, đi theo **dịch vụ** chứ ⛔ không theo BL (§8) | v1.0 Bước 5 |

**Căn cứ của hai quyết định trên** — ⛔ không phải ý kiến, là số đo trên 493 hội thoại kỳ 24–29/10:
- ① Điểm trung vị **12/100**, cao nhất **65**, chỉ **5 HT** vượt 50; và ⛔ không cặp ngưỡng nào làm nhãn KF-60 khớp nhãn 5 tín hiệu `id-D` — lệch thấp nhất **12,8%**, mà cấu hình đó chỉ cho **5 lead** vào hàng chờ. Chi tiết §7.2.
- ② Kỳ này **toàn bộ là line Da** → thang BL cũ nhân mọi lead xuống **0,5–0,7**, nên trong một hàng chờ trộn với PTTM ⛔ không lead nào của line này được gọi trước. Chi tiết §8.

### ⚠ Việc còn phải làm sau khi duyệt

| # | Việc | Ai |
|---|---|---|
| ① | Ghi hai dòng duyệt trên vào tab **`9. Nhật ký điều chỉnh`** của `KF-60_Driver_Lead_Scoring_Inbox_v1.0.xlsx` | QL Sale |
| ② | Sửa ô nền vàng của Driver: **bỏ bảng hệ số BL** → thang `1/2/3`; **bỏ hai ô ngưỡng HOT/WARM** → một ô `NGUONG_NUOI` | QL Sale |
| ③ | Xin **một kỳ PTTM**: tập vàng hiện có ⛔ chỉ có line Da, nên thang hệ số mới chưa kiểm được (§11, §13) | QL Sale |
| ④ | ⛔ **CHƯA duyệt** — đề xuất thay một phần trọng số Lead→Booking của KF-49/50 bằng % `GOI_NGAY` + % `XIN_SO` (§10). ⛔ Chỉ đưa ra sau khi nhóm B được cân lại | — |

---

### Liên quan
`id-D` §1–§3 (mã `O` · 5 tín hiệu · vì sao rơi) · `id-F` §5, §7 (cờ đỏ · rào an toàn) · `id-G` §3 (hệ số giá trị đơn) · `id-C` §2 (chân dung · `he_so_gia_tri`) · `id-K` §3 (giá · bảo hành đang chặn) · KF-49/KF-50 (chấm chiến dịch Lead v2) · KF-21/22/34 (CDP automation) · KF-11 (pháp lý truyền thông)

---

<!-- ===== id-M-thu-vien-chan-dung-kf62.md ===== -->

# id-M · ★★ THƯ VIỆN CHÂN DUNG KHÁCH HÀNG — BỘ KF-62 v2.2

> Sổ **nhập từ ngoài**, như `id-L`: đây là thư viện KF-62 của khối Sale.
> ⛔ Repo không tự đặt thêm chân dung nào. Thiếu thì **báo lại để bổ sung ở bản sau**.
>
> ★ Sổ này **thay §1–§2 của `id-C`**. Phần còn lại của `id-C` (nấc 5A, cách đọc
> insight) vẫn đúng.

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

⛔ **Đừng chép danh mục chân dung sang chỗ thứ hai.** Bảng ở §7 sinh thẳng từ
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

## 7. DANH MỤC — sinh tự động từ `tools/chan_dung_kf62.json`

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

## 8. TRIỂN KHAI — KF-62 §5

| Tuần | Việc |
|---|---|
| 1 | ★ **Áp 2 câu hỏi vàng cho mọi page dịch vụ.** Lấy ~100 hội thoại mỗi dịch vụ; 2 trưởng nhóm Sale gắn nhãn độc lập |
| 2 | AI phân loại cùng bộ hội thoại, so khớp; sửa câu hỏi và dấu hiệu ở chỗ hay nhầm |
| 3–4 | Chạy thực tế cùng `id-L`, đối chiếu booking trên CRM; lần đầu tính chỉ số ưu tiên |
| Mỗi 2 tuần | Cập nhật chỉ số ưu tiên → điều chỉnh ngân sách ads, nội dung, đào tạo kịch bản |

**A/B test:** kịch bản theo chân dung so với kịch bản chung (tỷ lệ xin số, booking) ·
hỏi 2 câu vàng ở tin **thứ 1** so với tin **thứ 3**.

---

## 9. TỰ KIỂM SỔ NÀY

- [ ] Mỗi hội thoại có **đúng một** chân dung, **tối đa ba** thẻ không?
- [ ] Có thẻ nào bị xếp nhầm thành chân dung không (`AR02` ở tỉnh, `AR06` so giá)?
- [ ] *"Chỉ hỏi giá, chưa nói tình trạng"* có bị gán chân dung không? ⛔ Phải là trạng thái lead.
- [ ] Tỷ lệ *"Chưa xác định"* của từng dịch vụ có vượt 15% không? Vượt thì đã **báo cờ đỏ** chưa?
- [ ] Tổng cột `ht` của bảng chân dung có **bằng đúng** cỡ mẫu không?
- [ ] Chân dung nào chưa khai `hanh_dong` mà đã lên hàng chờ? Dòng đó có gắn nhãn **«lời mặc định»** chưa?
- [ ] Có ai tự thêm chân dung ngoài KF-62 không? ⛔ Phải báo lại, ⛔ không tự đặt.
- [ ] Bảng §7 có khớp `tools/chan_dung_kf62.json` không — đã chạy lại `so-chan-dung.py` chưa?
- [ ] Thẻ `AR08` có lọt ra nội dung quảng cáo hay tin Zalo không?

---

### Liên quan

`id-C` (nấc 5A · cách đọc insight — §1–§2 đã thay bằng sổ này) · `id-D` §2 (nhãn nóng) ·
`id-L` (lead scoring · nhóm gọi · `lien_ket_kf60`) · `id-G` §3 (hệ số giá trị đơn) ·
`id-J` §2b (khối `lead` · cột `viec_chi_tiet`) · `id-K` (pháp chế) ·
KF-61 (khung thí điểm Mũi) · KF-24 (mã pháp lý `L0–L9`)

---
