# GÓI TRI THỨC · Agent-InsightDashboard-Kangnam

> Bản gộp **sinh tự động** từ `knowledge/`. ⛔ Không sửa file này —
> sửa file gốc rồi chạy lại `python tools/gop-tham-khao.py`.

Gộp ngày 2026-10-30 · 11 sổ

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
B4  ĐỌC SỐ ADS               → FB + Google: CPM→CTR→CPI→CPL→CPB, so mục tiêu & kỳ trước
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
CPM → CTR → CPI (Inbox) → CPL (Lead) → CPB (Booking) → Booking/Lead
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

---

<!-- ===== id-C-chan-dung-5A.md ===== -->

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

## 6. ĐẦU RA CHUẨN CỦA BƯỚC B3

```
① BẢN PHÁC HỌA   : out/chan-dung.json — mã · tên · họ là ai · nỗi sợ · dấu hiệu
                    · hệ số · trích        → chờ CỔNG 0
② BẢNG CHÂN DUNG : CD · tên · số HT · HOT/WARM/COLD · có SĐT · % có SĐT
                    · chốt lịch · bỏ 1 lượt · rơi do trực page   (+ dòng CD0)
③ THẺ INSIGHT    : mỗi CD ≥5 HT một thẻ — họ là ai · insight · câu hỏi ngầm
                    · tín hiệu nóng · hướng xử lý
④ MA TRẬN CD×5A  : hai bảng N×5, đánh dấu ô ① và ô ③
⑤ SO KỲ TRƯỚC    : % có SĐT từng CD thay đổi mấy ĐIỂM phần trăm
                    — chỉ với những mã được giữ nguyên
```

⛔ Chân dung dưới **5 HT** không viết thẻ insight — chỉ ghi vào danh sách `👁 quan sát`.

---

## 7. TỰ KIỂM SỔ NÀY

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

## 1. CHÍN TAB

| # | Tab | Trả lời câu |
|---|---|---|
| ① | **Phễu inbox** | Khách vào bao nhiêu, nóng tới đâu, rơi ở đâu và vì sao |
| ② | **Chân dung & Insight** | Khách là ai, họ sợ gì, câu hỏi ngầm là gì. ⏳ Khoá lại khi chân dung chưa qua CỔNG 0 |
| ③ | ★ **Chấm điểm nhân viên** | Khối trực page đang yếu tiêu chí nào, ai cần kèm |
| ④ | **Marketing — Facebook** | Chuỗi CPM→CTR→CPI→CPL→CPB, nội dung nào tốt/kém |
| ⑤ | **Marketing — Google Ads** | ⚠ chờ dữ liệu |
| ⑥ | **Ma trận ưu tiên** | Kỳ tới làm 5 việc nào |
| ⑦ | **Ngân hàng hook** | Viết gì, cho ai, format nào |
| ⑧ | **Sổ tay & việc cần xử lý** | Ai làm gì, hạn bao giờ, đo thế nào |
| ⑨ | **Ghi chú dữ liệu** | Mọi con số đến từ đâu, loại gì ra, vì sao |

### Đầu trang — luôn hiện, không nằm trong tab nào

```
Tiêu đề + chọn kỳ
▶ n lưu ý dữ liệu        (gập lại, mở ra xem)
5 thẻ số tổng            (giá trị · so kỳ trước · so mốc gốc)
```

### Năm thẻ số tổng

| Thẻ | Kiểu | Tốt là |
|---|---|---|
| `Hội thoại mới` | số | — |
| `Bỏ sau 1 lượt` | % | thấp |
| `Có SĐT` | % | cao |
| `Trả lời tin đầu ≤2′` | % | cao · chuẩn ≥90% |
| ★ `HOT/WARM chưa có SĐT` | số | **thấp** — lead nóng chưa vào tay telesale |

⚠️ Tab ⑨ **không phải tab phụ**. Báo cáo không nói được số đến từ đâu thì không ai dám dùng để ra quyết định.

---

## 2. SCHEMA DỮ LIỆU — `insight-dashboard-kangnam/1`

```jsonc
{
  "schema": "insight-dashboard-kangnam/1",
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
    "chot_lich":  0,
    "van_de":     [ { "muc","tieu_de","nhan_do","so_lieu","de_xuat","so_huu","anh_huong" } ]
  },

  "chan_dung": {
    // ⛔ KHÔNG có bộ chân dung mặc định. `tep` rỗng = chưa qua CỔNG 0 (id-C §1).
    "phac_hoa": { "trang_thai":"chua_phac_hoa|da_duyet", "vi_sao", "file",
                  "nguyen_lieu", "so_chan_dung", "duyet_boi", "duyet_luc" },
    "tep":     [ { "cd","ten","ht","quan_sat","hot","warm","cold","co_sdt",
                   "chot_lich","bo_1_luot","roi_truc","he_so" } ],   // + 1 dòng CD0
    "insight": [ { "cd","ten","nhom","ho_la_ai","insight","cau_hoi_ngam","tin_hieu_nong","huong_xu_ly","trich" } ],
    "ma_tran_cd_5a": { "noi_dung": {...}, "hoi_thoai": {...} }   // hai bảng N×5
  },

  "nhan_vien": {                                      // ★ tab ③
    "du_mau": true,
    "phan_bo": { "A":0,"B":0,"C":0,"D":0,"chua_du_mau":0 },
    "nhom":    [ { "ma":"N1","ten","diem_toi_da":20,"pct_dat":0,
                   "tieu_chi":[ { "ma":"N1.1","ten","diem":8,"dat":0,"chua":0,"khong_ap_dung":0 } ] } ],
    "ca_nhan": [ { "ten","ht","diem","loai","yeu_nhat","manh_nhat","co_do":[] } ],   // ⛔ chỉ vào sổ tay riêng
    "co_do":   [ { "ma":"CĐ-2","nguoi","ht","nguyen_van","nguoi_xu_ly" } ],
    "viec_he_thong": [ { "nguyen_nhan","so_ht","so_huu" } ],
    "ghi_chu": "Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay xếp hạng công khai."
  },

  "facebook": {
    "nguon","ky","ky_truoc","don_vi":"nghìn đ",
    "chuoi": [ { "ma":"CPM|CTR|CPI|CPL|CPB|BK_LEAD","nhan","gia_tri","muc_tieu","ky_truoc","kieu","tot" } ],
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
