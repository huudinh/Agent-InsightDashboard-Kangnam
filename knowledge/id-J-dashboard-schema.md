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
| ④ | **Marketing — Facebook** | Chuỗi chi → CPM→CTR→CPI→CPL→CPB, nội dung nào tốt/kém |
| ⑤ | **Marketing — Google Ads** | ⚠ chờ dữ liệu |
| ⑥ | **Ma trận ưu tiên** | Kỳ tới làm 5 việc nào |
| ⑦ | **Ngân hàng hook** | Viết gì, cho ai, format nào |
| ⑧ | **Sổ tay & việc cần xử lý** | Ai làm gì, hạn bao giờ, đo thế nào |
| ⑨ | **Ghi chú dữ liệu** | Mọi con số đến từ đâu, loại gì ra, vì sao |

### Ba bố cục — ⛔ vẫn chỉ MỘT bản trang

Chín tab ở trên là bản **đầy đủ**. Cùng một trang và cùng một file kỳ còn dựng được hai báo cáo hẹp hơn cho hai người đọc khác nhau — chọn bằng trường `bo_cuc` trong `data/index.json`:

| `bo_cuc` | Tên báo cáo | Tab | Thẻ số tổng |
|---|---|---|---|
| *(không khai)* · `day-du` | Chân dung khách & chất lượng trực page | cả 9 | cả 6 |
| `insight` | **Insight khách** — khách là ai · họ sợ gì · kỳ tới làm nội dung gì | ① ② ⑥ ⑦ | HT · bỏ 1 lượt · có SĐT · HOT/WARM chưa SĐT |
| `truc-page` | **Chất lượng trực page** — khối yếu gì · ai cần kèm · sửa câu nào | ③ ① ② ⑧ ⑨ | HT · trả lời lượt đầu · rơi do trực page · bỏ 1 lượt · HOT/WARM chưa SĐT |

```
⛔ Tách báo cáo KHÔNG được đẻ thêm một bản trang.
   Hai bản trang là hai chỗ phải sửa mỗi lần đổi, và sẽ lệch nhau sau hai kỳ.
   Trang đọc `bo_cuc`, tự lọc tab và thẻ số, tự đổi tiêu đề.

★ Thứ tự tab đi theo ĐÚNG thứ tự khai trong bố cục, không theo thứ tự 9 tab gốc:
   bản `truc-page` mở bằng tab Chấm điểm vì đó là việc của người đọc nó.

⚠ Hai bố cục hẹp dùng CHUNG một file kỳ. Số liệu chỉ có một bản —
   ⛔ không bao giờ có chuyện hai báo cáo nói hai con số khác nhau.

★ Bố cục bỏ tab ⑨ thì ghi chú dữ liệu **chuyển lên ô gập đầu trang**, ⛔ không biến mất. Tab ⑨ là tab bắt buộc của bản đầy đủ; bỏ nó khỏi thanh tab là để trang gọn, ⛔ không phải để thôi nói số đến từ đâu.

★ `insight` ⛔ KHÔNG có hai tab quảng cáo. Đầu vào của nó là HỘI THOẠI; số chi
   phí tới từ một nguồn khác (`id.py ads`) và chỉ nằm ở bản `day-du`. Bỏ tab
   không phải để giấu — thiếu nguồn nào vẫn phải ghi ở tab ⑨ và ở ô lưu ý
   đầu trang, đúng luật ① bên dưới.
```

### Đầu trang — luôn hiện, không nằm trong tab nào

```
Tiêu đề + chọn kỳ
▶ n lưu ý dữ liệu        (gập lại, mở ra xem)
5 thẻ số tổng            (giá trị · so kỳ trước · so mốc gốc)
```

### Sáu thẻ số tổng

| Thẻ | Kiểu | Tốt là |
|---|---|---|
| `Hội thoại mới` | số | — |
| `Bỏ sau 1 lượt` | % | thấp |
| `Có SĐT` | % | cao |
| `Trả lời tin đầu ≤2′` | % | cao · chuẩn ≥90% |
| `Rơi do trực page` | % | thấp — câu trả lời làm khách dừng |
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
    // xếp theo điểm win; mỗi ô là gạch đầu dòng — dòng mở đầu "- " thành <li> (id-C §6)
    "co_hoi_win":    [ { "cd","ten","ht","lead_bo_lo","he_so","pct_sdt","diem","hang",
                         "uu_tien","roi_truc","ghi_chu" } ],   // CD0 luôn cuối, hang = null
    "cach_tinh_win": "công thức, viết ra để người đọc cãi được",
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
