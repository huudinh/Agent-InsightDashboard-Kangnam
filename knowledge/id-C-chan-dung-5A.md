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
