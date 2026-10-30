#!/usr/bin/env python3
"""trang-huong-dan.py — sinh trang hướng dẫn HTML từ chính nội dung repo.

Generator DÙNG CHUNG cho bộ agent trong Project/Agent. Phần riêng của mỗi gói
nằm ở tools/huong-dan.json, không nằm trong file này — sửa nội dung thì sửa JSON.

    python tools/gop-tham-khao.py     # gộp lại tri thức trước (nếu có)
    python tools/trang-huong-dan.py   # rồi sinh lại trang

Mặc định ghi ra tools/huong-dan.html (artifact, không phải nguồn).
"""

from __future__ import annotations

import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAU_HINH = Path(__file__).resolve().parent / "huong-dan.json"
RA = ROOT / "tools" / "huong-dan.html"

CSS = r"""<style>
/* Bảng màu dùng chung của bộ tài liệu hướng dẫn agent Kangnam — nâu đỏ #8A1F33 +
   vàng #86560D + nền kem, Be Vietnam Pro + Lora. Giữ nguyên để cả bộ đọc như một hệ.

   Chiều dữ liệu cần mã hoá của gói này là KHOẢNG CÁCH ĐI LẠI — V1 gần nhất tới V4
   xa nhất. Thang đi theo hướng NÓNG DẦN = XA DẦN = RỦI RO DẦN:

       V1 #4F5E22  →  V2 #86560D  →  V3 #A85205  →  V4 #A8162B

   V4 dùng cùng màu với mã lỗi nặng vì nó đúng là như vậy: chạy V4 là đốt tiền vào
   người không bao giờ tới phòng khám. Màu không bao giờ là phần duy nhất mang
   thông tin — mỗi vành đai có nhãn chữ (V1…V4) và có số phút đi lại. */
:root{
  --ground:#EADDD8; --surface:#FFFFFF; --surface-2:#F7EBE6; --surface-3:#F7EBE6;
  --ink:#1F0E17; --ink-2:#4D2E39; --ink-3:#7A5560;
  --line:#D6BDB8; --line-2:#E6D2CD;
  --primary:#8A1F33; --primary-ink:#6B1526; --primary-wash:#F7E4E4; --on-primary:#FFFFFF;
  --accent:#86560D; --accent-soft:#A9761A; --accent-wash:#F9ECD2;
  --band:#3A1425; --band-ink:#FBEEF1; --band-accent:#EDBD6B; --on-band-accent:#20101A;
  --do:#A8162B;   --do-bg:#FBE3E6;
  --cam:#A85205;  --cam-bg:#FCEBDA;
  --vang:#86560D; --vang-bg:#F9ECD2;
  --theo:#7A5560; --theo-bg:#F7EBE6;
  --ok:#4F5E22;   --ok-bg:#EFF3E0;
  --f:'Be Vietnam Pro',system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif;
  --f2:'Lora',Georgia,'Times New Roman',serif;
  --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  --r:10px; --r-lg:14px;
  --sh:0 1px 2px rgba(58,20,37,.10),0 2px 6px rgba(58,20,37,.05);
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --ground:#0E0609; --surface:#352228; --surface-2:#412A32; --surface-3:#412A32;
    --ink:#FBEFEC; --ink-2:#E8D2CF; --ink-3:#BDA2A7;
    --line:#603D46; --line-2:#4B3038;
    --primary:#F09AA1; --primary-ink:#F7B9BD; --primary-wash:#43242B; --on-primary:#20101A;
    --accent:#EEC074; --accent-soft:#D09A46; --accent-wash:#3B2A17;
    --band:#2B1020; --band-ink:#FBEEF1; --band-accent:#EDBD6B; --on-band-accent:#20101A;
    --do:#F2969F;   --do-bg:#45202A;
    --cam:#EFB478;  --cam-bg:#3E2612;
    --vang:#EEC074; --vang-bg:#3B2A17;
    --theo:#BDA2A7; --theo-bg:#412A32;
    --ok:#B3C975;   --ok-bg:#1F2A12;
    --sh:0 1px 2px rgba(0,0,0,.45),0 3px 10px rgba(0,0,0,.30);
  }
}
:root[data-theme="dark"]{
  --ground:#0E0609; --surface:#352228; --surface-2:#412A32; --surface-3:#412A32;
  --ink:#FBEFEC; --ink-2:#E8D2CF; --ink-3:#BDA2A7;
  --line:#603D46; --line-2:#4B3038;
  --primary:#F09AA1; --primary-ink:#F7B9BD; --primary-wash:#43242B; --on-primary:#20101A;
  --accent:#EEC074; --accent-soft:#D09A46; --accent-wash:#3B2A17;
  --band:#2B1020; --band-ink:#FBEEF1; --band-accent:#EDBD6B; --on-band-accent:#20101A;
  --do:#F2969F;   --do-bg:#45202A;
  --cam:#EFB478;  --cam-bg:#3E2612;
  --vang:#EEC074; --vang-bg:#3B2A17;
  --theo:#BDA2A7; --theo-bg:#412A32;
  --ok:#B3C975;   --ok-bg:#1F2A12;
  --sh:0 1px 2px rgba(0,0,0,.45),0 3px 10px rgba(0,0,0,.30);
}

*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);
  font:400 15.5px/1.62 var(--f);-webkit-font-smoothing:antialiased}
.wrap{max-width:940px;margin:0 auto;padding-inline:20px}
@media(max-width:480px){.wrap{padding-inline:16px}}
h1,h2,h3{line-height:1.18;text-wrap:balance;margin:0}
p{margin:0 0 .8em}
a{color:var(--primary);text-decoration-thickness:1px;text-underline-offset:2px}
code{font-family:var(--mono);font-size:.88em;background:var(--surface-2);
  border:1px solid var(--line-2);border-radius:5px;padding:.08em .35em;overflow-wrap:anywhere}
:focus-visible{outline:2.5px solid var(--accent);outline-offset:2px;border-radius:6px}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}

header.top{background:var(--band);color:var(--band-ink);border-bottom:4px solid var(--band-accent)}
.eyebrow{font:italic 600 17px/1.3 var(--f2);color:var(--band-accent);margin:0 0 6px}
.top h1{font-size:clamp(27px,5.2vw,39px);font-weight:800;letter-spacing:-.02em;color:#fff}
.lede{margin:12px 0 0;font-size:17px;color:rgba(255,255,255,.86);max-width:62ch}
.lede b{color:#fff}
.quick{margin:14px 0 0;font-size:14.5px;color:rgba(255,255,255,.80);max-width:68ch;
  padding-left:13px;border-left:3px solid var(--band-accent)}
.quick b{color:#fff}
.quick span.ar{color:var(--band-accent);font-weight:700;padding:0 2px}
.quick .quick-x{display:inline-block;margin-top:4px;font-size:13.5px;color:rgba(255,255,255,.55)}
.top .dim{color:rgba(255,255,255,.62);font-size:14px}
.top .dim a{color:var(--band-accent)}
.chips{display:flex;flex-wrap:wrap;gap:7px;margin-top:18px}
.chip{font-size:12.5px;font-weight:600;color:rgba(255,255,255,.80);
  background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.22);
  border-radius:999px;padding:5px 11px}
.chip.on{color:var(--on-band-accent);background:var(--band-accent);border-color:var(--band-accent)}

nav.bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:40;
  background:var(--band);border-bottom:1px solid rgba(255,255,255,.16)}
nav.bar .wrap{display:flex;gap:2px;align-items:center;overflow-x:auto;
  padding-block:9px;scrollbar-width:none}
nav.bar .wrap::-webkit-scrollbar{display:none}
nav.bar a{flex:0 0 auto;font-size:13px;font-weight:600;color:rgba(255,255,255,.74);
  text-decoration:none;padding:6px 11px;border-radius:7px}
nav.bar a:hover{background:rgba(255,255,255,.14);color:#fff}
.themebtn{flex:0 0 auto;margin-left:auto;font:600 12.5px var(--f);
  color:rgba(255,255,255,.74);background:transparent;cursor:pointer;
  border:1px solid rgba(255,255,255,.22);border-radius:999px;padding:5px 12px}
.themebtn:hover{background:rgba(255,255,255,.14);color:#fff}

section.sec{padding-block:46px;border-top:1px solid var(--line);scroll-margin-top:62px}
section.sec:first-of-type{border-top:0}
.sec-h{margin-bottom:22px}
.sec-h .pre{font:italic 600 15px/1.3 var(--f2);color:var(--accent);display:block}
.sec-h h2{font-size:clamp(21px,3.4vw,27px);font-weight:800;color:var(--primary-ink);margin-top:3px}
.sec-h .bar{display:block;width:42px;height:3px;border-radius:3px;background:var(--accent-soft);margin-top:11px}
.sec-h p{margin:12px 0 0;color:var(--ink-2);max-width:66ch}
h3.sub{font-size:16px;font-weight:800;color:var(--primary-ink)}
.dim{color:var(--ink-3);font-size:13px}

.grid{display:grid;gap:14px}
.g3{grid-template-columns:repeat(3,1fr)}
.g2{grid-template-columns:repeat(2,1fr)}
@media(max-width:760px){.g3,.g2{grid-template-columns:1fr}}

.steps{display:grid;gap:1px;background:var(--line);border:1px solid var(--line);
  border-radius:var(--r-lg);overflow:hidden;margin:0 0 18px;grid-template-columns:repeat(3,1fr)}
@media(max-width:700px){.steps{grid-template-columns:1fr}}
.steps div{background:var(--surface);padding:15px 16px}
.steps b{display:block;font-size:13px;font-weight:800;color:var(--primary-ink);margin-bottom:3px}
.steps span{font-size:13.5px;color:var(--ink-2)}
.steps .n{display:inline-grid;place-content:center;width:21px;height:21px;border-radius:50%;
  background:var(--band);color:#fff;font:800 11.5px var(--f);margin-right:7px;vertical-align:1px}

.dl{background:var(--surface);border:1px solid var(--line);border-top:4px solid var(--accent-soft);
  border-radius:var(--r-lg);padding:22px 20px;text-align:center;box-shadow:var(--sh);margin:0 0 16px}
.dl h3{font-size:17px;font-weight:800;color:var(--primary-ink);margin:0 0 4px}
.dl p{margin:0;font-size:14px;color:var(--ink-2)}
a.dl-btn{display:inline-flex;align-items:center;gap:9px;margin:14px 0 0;background:var(--primary);
  color:var(--on-primary);font:800 16.5px var(--f);text-decoration:none;padding:14px 26px;
  border-radius:9px;box-shadow:0 2px 0 var(--accent-soft)}
a.dl-btn:hover{background:var(--primary-ink)}
.dl .alt{margin-top:13px;font-size:13px;color:var(--ink-3)}

.tabs{display:flex;gap:6px;flex-wrap:wrap;margin:0 0 -1px;position:relative;z-index:1}
.tab{border:1px solid var(--line);border-bottom-color:transparent;background:var(--surface-2);
  color:var(--ink-3);font:700 13.5px var(--f);padding:9px 16px;
  border-radius:var(--r) var(--r) 0 0;cursor:pointer}
.tab:hover{color:var(--primary-ink)}
.tab[aria-selected="true"]{background:var(--surface);color:var(--primary-ink);
  border-top:3px solid var(--primary);border-bottom-color:var(--surface);padding-top:7px}
.tabpanel{background:var(--surface);border:1px solid var(--line);
  border-radius:0 var(--r-lg) var(--r-lg) var(--r-lg);padding:18px;box-shadow:var(--sh)}
ol.list{margin:0;padding-left:1.25em}
ol.list li{margin-bottom:9px}
ol.list li::marker{font-weight:800;color:var(--primary)}

.mbox{background:var(--surface);border:1px solid var(--line);border-top:4px solid var(--primary);
  border-radius:var(--r-lg);overflow:hidden;box-shadow:var(--sh);margin:0 0 16px}
.mrow{display:flex;gap:11px;align-items:flex-start;padding:13px 15px;
  border-bottom:1px solid var(--line-2);flex-wrap:wrap}
.mrow:last-child{border-bottom:0}
.mrow .lb{flex:none;width:112px;font-size:11.5px;font-weight:800;letter-spacing:.07em;
  text-transform:uppercase;color:var(--ink-3);padding-top:4px}
.mrow .vl{flex:1;min-width:210px;font-size:14.2px;color:var(--ink);line-height:1.55}
.mrow .vl.mono{font:700 13.6px/1.5 var(--mono)}
.mrow .copy{flex:none}
@media(max-width:600px){.mrow .lb{width:auto;padding-top:0}}
.st{display:flex;flex-direction:column;gap:8px;width:100%}
.st-i{display:flex;gap:9px;align-items:center;flex-wrap:wrap}
.st-i span{flex:1;min-width:170px;font:400 13.4px/1.5 var(--mono);color:var(--ink-2)}
.st-i .copy{padding:5px 11px;font-size:12px}

.cc{display:flex;flex-direction:column;gap:11px;background:var(--surface);
  border:1px solid var(--line);border-top:4px solid var(--accent-soft);
  border-radius:var(--r-lg);padding:17px;box-shadow:var(--sh)}
.cc .tag{font-size:11.5px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;color:var(--ink-3)}
.cc h3{font-size:17px;font-weight:800;color:var(--primary-ink);margin:0}
.cc .meta{font-size:13px;color:var(--ink-2);margin:0;flex:1}
.cc .count{font-variant-numeric:tabular-nums;font-weight:700;color:var(--ink)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:7px;width:100%;
  min-height:44px;border:0;border-radius:9px;background:var(--primary);color:var(--on-primary);
  font:800 14.5px var(--f);letter-spacing:.2px;cursor:pointer;
  box-shadow:0 2px 0 var(--accent-soft);transition:background-color .15s,transform .1s}
.btn:hover{background:var(--primary-ink)}
.btn:active{transform:translateY(1px);box-shadow:0 1px 0 var(--accent-soft)}
details.peek,details.fview{border-top:1px solid var(--line-2);padding-top:10px}
details.peek summary,details.fview summary{cursor:pointer;font-size:13px;font-weight:600;
  color:var(--primary);list-style:none}
details summary::-webkit-details-marker{display:none}
details.peek summary::before,details.fview summary::before{content:"\\25b8 ";color:var(--ink-3)}
details[open].peek summary::before,details[open].fview summary::before{content:"\\25be "}
.filebody,pre.code{margin:10px 0 0;max-height:260px;overflow:auto;background:var(--surface-2);
  border:1px solid var(--line-2);border-radius:var(--r);padding:12px;
  font:400 12px/1.5 var(--mono);white-space:pre-wrap;word-break:break-word;color:var(--ink-2)}
pre.code{margin-top:0}

.files{margin-top:8px}
.fcard{border:1px solid var(--line);border-radius:var(--r);overflow:hidden;background:var(--surface);
  margin:0 0 9px;box-shadow:var(--sh)}
.fcard.hi{border:2px solid var(--accent-soft)}
.fcard-h{display:flex;gap:10px;align-items:center;padding:11px 13px;flex-wrap:wrap}
.fname{font:700 13.4px var(--mono);color:var(--ink);overflow-wrap:anywhere}
.fbadge{font-size:10.5px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;
  padding:3px 8px;border-radius:999px;background:var(--accent-wash);color:var(--accent);
  border:1px solid var(--accent-soft)}
.fsize{font-size:12.5px;color:var(--ink-3);font-variant-numeric:tabular-nums;margin-left:auto}
.fhow{margin:0;padding:0 13px 11px;font-size:13.8px;color:var(--ink-2)}
.fhow b{color:var(--ink)}
.fcard details.fview{margin:0 13px 11px}
@media(max-width:520px){.fsize{margin-left:0}}

.copy{font:700 13px var(--f);padding:7px 14px;border-radius:7px;cursor:pointer;
  border:1px solid var(--primary);background:transparent;color:var(--primary);white-space:nowrap}
.copy:hover{background:var(--primary-wash)}
.copy.done{border-color:var(--ok);color:var(--ok);background:var(--ok-bg)}

.tw{overflow-x:auto;border:1px solid var(--line);border-radius:var(--r-lg);background:var(--surface)}
table{border-collapse:collapse;width:100%;min-width:620px;font-size:14px}
th,td{text-align:left;padding:11px 13px;border-bottom:1px solid var(--line-2);vertical-align:top}
thead th{font-size:11.5px;font-weight:800;letter-spacing:.07em;text-transform:uppercase;
  color:rgba(255,255,255,.94);background:var(--band);border-bottom:0;white-space:nowrap}
tbody tr:last-child td{border-bottom:0}
td.num,th.num{font-variant-numeric:tabular-nums;text-align:right;white-space:nowrap;color:var(--ink-2)}
td.mono{font:600 13px var(--mono);white-space:nowrap}
tr.sao td{background:var(--accent-wash)}
tr.sao .st{color:var(--accent);font-size:11px}
tr.loai td{background:var(--do-bg)}

.sev{display:inline-flex;align-items:center;gap:6px;font-size:11px;font-weight:800;
  letter-spacing:.04em;padding:2px 8px;border-radius:999px;white-space:nowrap;
  border:1px solid currentColor;color:var(--do);background:var(--do-bg)}
.sev .dot{width:7px;height:7px;border-radius:50%;background:currentColor;flex:none}
tr.s-do  td:first-child{box-shadow:inset 4px 0 0 var(--do)}
tr.s-cam td:first-child{box-shadow:inset 4px 0 0 var(--cam)}
tr.s-vang td:first-child{box-shadow:inset 4px 0 0 var(--vang)}
tr.s-theo td:first-child{box-shadow:inset 4px 0 0 var(--theo)}

/* ---------- năm thứ khác gói KN-QT ---------- */
.kcard{display:flex;gap:14px;align-items:flex-start;background:var(--surface);
  border:1px solid var(--line);border-radius:var(--r-lg);padding:16px 18px;
  box-shadow:var(--sh);margin:0 0 11px}
.kcard .kn{flex:none;display:grid;place-content:center;width:34px;height:34px;
  border-radius:50%;background:var(--band);color:var(--band-accent);font:800 15px var(--f)}
.kcard h3{font-size:15.5px;font-weight:800;color:var(--primary-ink);margin:0 0 5px}
.kcard p{margin:0;font-size:14px;color:var(--ink-2)}

/* ---------- bốn vành đai: thang GẦN → XA = NÓNG DẦN ---------- */
.vwrap{display:grid;gap:1px;background:var(--line);border:1px solid var(--line);
  border-radius:var(--r-lg);overflow:hidden;margin:0 0 14px;grid-template-columns:repeat(4,1fr)}
@media(max-width:860px){.vwrap{grid-template-columns:repeat(2,1fr)}}
@media(max-width:520px){.vwrap{grid-template-columns:1fr}}
.vtier{background:var(--surface);padding:14px 15px;border-top:4px solid var(--line);
  display:flex;flex-direction:column;gap:4px}
.vtier.t-v1{border-top-color:var(--ok)}
.vtier.t-v2{border-top-color:var(--vang)}
.vtier.t-v3{border-top-color:var(--cam)}
.vtier.t-v4{border-top-color:var(--do)}
.vtier .vt{font:800 14.5px var(--f)}
.vtier.t-v1 .vt{color:var(--ok)}
.vtier.t-v2 .vt{color:var(--vang)}
.vtier.t-v3 .vt{color:var(--cam)}
.vtier.t-v4 .vt{color:var(--do)}
.vtier .vkhu{font-size:12.5px;color:var(--ink-2);line-height:1.45}
.vtier .vtg{font:700 12px var(--mono);color:var(--ink);font-variant-numeric:tabular-nums}
.vtier .vy{margin:3px 0 0;font-size:12.5px;color:var(--ink-3);line-height:1.45}

/* ---------- khối so sánh hai cột (.vs) — thành phần riêng của khuôn KN-QT ---------- */
.vs{display:grid;gap:1px;background:var(--line);border:1px solid var(--line);
  border-radius:var(--r-lg);overflow:hidden;grid-template-columns:1fr 1fr;margin:0 0 14px}
@media(max-width:620px){.vs{grid-template-columns:1fr}}
.vs > div{background:var(--surface);padding:16px 18px}
.vs .h{font:800 11.5px var(--f);letter-spacing:.09em;text-transform:uppercase;
  color:var(--ink-3);margin-bottom:7px}
.vs .w{font-size:17px;font-weight:800;color:var(--primary-ink);margin-bottom:7px}
.vs p{font-size:13.8px;color:var(--ink-2);margin:0 0 .5em}
.vs p:last-child{margin-bottom:0}
.vs .me{font-size:12.8px;color:var(--ink-3);margin-top:9px;padding-top:9px;
  border-top:1px solid var(--line-2)}
.vs .bad .w{color:var(--do)}
.vs .good .w{color:var(--ok)}

/* eyebrow lồng trong h3 — "Bước 1" / "Điều 2" */
h3.sub .pre2{font:italic 600 14px/1.3 var(--f2);color:var(--accent);display:block;font-weight:600}
tr.hl td{background:var(--accent-wash)}
.steps4{grid-template-columns:repeat(4,1fr)}
@media(max-width:860px){.steps4{grid-template-columns:repeat(2,1fr)}}
@media(max-width:520px){.steps4{grid-template-columns:1fr}}

.note{border-radius:0 var(--r) var(--r) 0;padding:13px 16px;font-size:14.5px;
  background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--accent-soft);
  box-shadow:var(--sh);color:var(--ink-2);margin:14px 0}
.note b{font-weight:800;color:var(--ink)}
.note.warn{border-left-color:var(--cam);background:var(--cam-bg)}
.note.ok{border-left-color:var(--ok);background:var(--ok-bg)}
.note.stop{background:var(--band);color:var(--band-ink);border:1px solid var(--band-accent);
  border-left:5px solid var(--band-accent);border-radius:var(--r)}
.note.stop b{color:#fff}
.note.stop code,header.top code,nav.bar code,thead th code{
  background:rgba(255,255,255,.10);border-color:rgba(255,255,255,.22);color:var(--band-ink)}
.note.stop i{color:var(--band-accent);font-style:normal}
.note.stop a{color:var(--band-accent)}
.note + .note{margin-top:10px}
.note p:last-child{margin-bottom:0}

.qa-bar{display:flex;gap:7px;flex-wrap:wrap;align-items:center;margin:0 0 16px}
.qa-bar button{font:600 13px var(--f);padding:6px 13px;border:1px solid var(--line);
  background:var(--surface);color:var(--ink-3);border-radius:999px;cursor:pointer;white-space:nowrap}
.qa-bar button:hover{color:var(--primary-ink);border-color:var(--primary)}
.qa-bar button[aria-pressed="true"]{background:var(--primary);color:var(--on-primary);border-color:var(--primary)}
.prompt{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-lg);
  margin:0 0 12px;overflow:hidden;box-shadow:var(--sh)}
.prompt-h{display:flex;gap:11px;align-items:center;padding:12px 15px;flex-wrap:wrap;
  background:var(--surface-2);border-bottom:1px solid var(--line-2)}
.prompt-h .n{flex:none;font:700 12.5px var(--mono);color:var(--primary-ink);font-variant-numeric:tabular-nums}
.prompt-h .t{font-size:14.8px;font-weight:700;flex:1;min-width:0;color:var(--ink)}
.prompt-h .k{flex:none;font-size:10.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;
  color:var(--ink-3);border:1px solid var(--line);border-radius:999px;padding:3px 9px;white-space:nowrap}
.prompt-b{margin:0;padding:14px 15px;max-height:280px;overflow:auto;
  font:400 12.6px/1.66 var(--mono);color:var(--ink-2);white-space:pre-wrap;
  overflow-wrap:anywhere;background:var(--surface)}
.prompt-f{display:flex;gap:10px;align-items:center;justify-content:space-between;
  padding:11px 15px;flex-wrap:wrap;border-top:1px solid var(--line-2);background:var(--surface-2)}
.prompt-f .get{font-size:12.8px;color:var(--ink-3);flex:1;min-width:150px}
@media (max-width:420px){.prompt-h .k{display:none}}

footer{border-top:1px solid var(--line);background:var(--surface);
  padding-block:30px;font-size:13px;color:var(--ink-3)}
footer b{color:var(--ink-2)}
.toast{position:fixed;left:50%;transform:translateX(-50%);
  bottom:calc(20px + env(safe-area-inset-bottom,0px));
  background:var(--band);color:var(--band-ink);font:700 13.5px var(--f);padding:10px 18px;
  border-radius:999px;z-index:90;box-shadow:0 8px 24px rgba(0,0,0,.3);
  opacity:0;pointer-events:none;transition:opacity .18s ease}
.toast.on{opacity:1}
</style>"""


def doc(duong_dan: str) -> str:
    return (ROOT / duong_dan).read_text(encoding="utf-8")


def khoi_copy(duong_dan: str) -> str:
    """Lấy khối giữa hai vạch ▼▲ nếu có; không có thì lấy cả file."""
    t = doc(duong_dan)
    if "▼▼▼ COPY TỪ ĐÂY ▼▼▼" not in t:
        return t.strip()
    dau = t.index("▼▼▼ COPY TỪ ĐÂY ▼▼▼")
    rao = t.index("```", dau)
    dau = t.index("\n", rao) + 1
    cuoi = t.rindex("```", dau, t.index("▲▲▲ COPY ĐẾN ĐÂY ▲▲▲"))
    return t[dau:cuoi].strip()


def n(so: int) -> str:
    return f"{so:,}".replace(",", ".")


def e(s: str) -> str:
    return html.escape(s, quote=False)


# ------------------------------------------------------------------ dựng khối

def khoi_the(cf, payload) -> str:
    """Các thẻ dán sẵn: bộ não đầy đủ · bản ngắn (nếu có) · các file gộp."""
    ra = []
    for i, the in enumerate(cf["the"]):
        ma = the["ma"]
        so = len(payload[ma])
        tran = the.get("tran")
        dong = f'<span class="count">{n(so)}</span>'
        dong += f" / {n(tran)} ký tự" if tran else " ký tự"
        if the.get("nen_tang"):
            dong += " · " + the["nen_tang"]
        du = f" Dư {n(tran - so)} ký tự." if tran else ""
        ra.append(
            f'<div class="cc"><span class="tag">{e(the["nhan"])}</span>'
            f'<h3>{e(the["ten"])}</h3>'
            f'<p class="meta">{dong}<br>'
            f'<span class="dim">{the["mo_ta"]}{du}</span></p>'
            f'<button class="btn" data-copy="{ma}" type="button">Copy {e(the["nhan"])}</button>'
            f'<details class="peek"><summary>Xem nội dung</summary>'
            f'<pre class="filebody" data-peek="{ma}"></pre></details></div>')
    cot = "g2" if len(ra) <= 2 or len(ra) == 4 else "g3"
    return f'<div class="grid {cot}">' + "".join(ra) + "</div>"


def khoi_file(cf, payload) -> str:
    ra = []
    for i, f in enumerate(cf["files"], 1):
        so = len(payload[f"f{i}"])
        badge = f.get("badge", "")
        hi = " hi" if badge.startswith("★") else ""
        bd = f'<span class="fbadge">{e(badge)}</span>' if badge else ""
        ra.append(
            f'<article class="fcard{hi}"><div class="fcard-h">'
            f'<span class="fname">{e(f["duong_dan"])}</span>{bd}'
            f'<span class="fsize">{n(so)} ký tự</span>'
            f'<button class="copy" data-copy="f{i}" type="button">Copy</button></div>'
            f'<p class="fhow">{f["mo_ta"]}</p>'
            f'<details class="fview"><summary>Xem nội dung</summary>'
            f'<pre class="filebody" data-peek="f{i}"></pre></details></article>')
    return "\n".join(ra)


def khoi_tab(cf) -> str:
    nut, panel = [], []
    for i, tb in enumerate(cf["tabs"]):
        chon = "true" if i == 0 else "false"
        an = "" if i == 0 else " hidden"
        nut.append(f'<button class="tab" role="tab" aria-selected="{chon}" '
                   f'data-tab="t{i}" type="button">{e(tb["ten"])}</button>')
        buoc = "".join(f"<li>{b}</li>" for b in tb["buoc"])
        ghi = f'<div class="note {tb.get("ghi_kieu", "warn")}" style="margin-top:14px;margin-bottom:0">{tb["ghi_chu"]}</div>' if tb.get("ghi_chu") else ""
        mo = f'<p class="dim" style="margin-bottom:13px">{tb["mo_ta"]}</p>' if tb.get("mo_ta") else ""
        panel.append(
            f'<div class="tabpanel" data-panel="t{i}"{an}>'
            f'<h3 class="sub" style="margin-bottom:10px">{e(tb["tieu_de"])}</h3>'
            f'{mo}<ol class="list">{buoc}</ol>{ghi}</div>')
    return ('<div class="tabs" role="tablist">' + "".join(nut) + "</div>"
            + "".join(panel))


def khoi_smoke(cf) -> str:
    if not cf.get("smoke"):
        return ""
    hang = "\n".join(
        f'<tr{" class=\"hl\"" if s.get("hl") else ""}>'
        f'<td class="num">{i}</td><td>{s["go"]}</td><td>{s["thay"]}</td></tr>'
        for i, s in enumerate(cf["smoke"], 1))
    ghi = f'<div class="note warn" style="margin-top:14px">{cf["smoke_ghi"]}</div>' if cf.get("smoke_ghi") else ""
    return (f'<h3 class="sub" style="margin:28px 0 6px">Smoke test — {len(cf["smoke"])} câu</h3>'
            '<p class="dim" style="margin:0 0 13px">Chạy đúng mấy câu này sau khi cài. '
            'Sai một câu là cài chưa xong.</p>'
            '<div class="tw"><table><thead><tr><th class="num">#</th><th>Gõ vào</th>'
            f'<th>Phải thấy</th></tr></thead><tbody>{hang}</tbody></table></div>{ghi}')


def khoi_prompt(cf, payload) -> str:
    nhom = []
    for g in cf.get("nhom_prompt", []):
        nhom.append(f'<button data-f="{g["ma"]}" aria-pressed="false" type="button">{e(g["ten"])}</button>')
    bar = ""
    if nhom:
        bar = ('<div class="qa-bar"><button data-f="all" aria-pressed="true" type="button">'
               f'Tất cả ({len(cf["prompts"])})</button>' + "".join(nhom) + "</div>")
    ra = []
    for i, p in enumerate(cf["prompts"], 1):
        ra.append(
            f'<article class="prompt" data-g="{p.get("nhom", "all")}">'
            f'<div class="prompt-h"><span class="n">{i:02d}</span>'
            f'<span class="t">{e(p["ten"])}</span>'
            f'<span class="k">{e(p.get("kieu", ""))}</span></div>'
            f'<pre class="prompt-b">{e(payload[f"p{i}"])}</pre>'
            f'<div class="prompt-f"><span class="get">{n(len(payload[f"p{i}"]))} ký tự</span>'
            f'<button class="copy" data-copy="p{i}" type="button">Copy prompt</button>'
            "</div></article>")
    return bar + "".join(ra)


def khoi_dieu(cf) -> str:
    ra = []
    for d in cf.get("dieu", []):
        pre = f'<span class="pre2">{e(d["pre"])}</span>' if d.get("pre") else ""
        ra.append(f'<h3 class="sub" style="margin:26px 0 10px">{pre}{d["h3"]}</h3>{d["html"]}')
    return "\n".join(ra)


def khoi_chan(cf) -> str:
    if not cf.get("chan"):
        return ""
    hang = "\n".join(
        f'<tr{" class=\"hl\"" if c.get("hl") else ""}>'
        f'<td>{c["muc"]}</td><td>{c["viec"]}</td><td>{c["ai"]}</td><td>{c["chan"]}</td></tr>'
        for c in cf["chan"])
    ghi = "".join(f'<div class="note {g.get("kieu", "ok")}" style="margin-top:14px">{g["html"]}</div>'
                  for g in cf.get("chan_ghi", []))
    return ('<div class="tw"><table><thead><tr><th>Mức</th><th>Việc</th><th>Ai cấp</th>'
            f'<th>Chặn gì</th></tr></thead><tbody>{hang}</tbody></table></div>{ghi}')


# ------------------------------------------------------------------ dựng trang

def dung(cf) -> str:
    payload = {}
    payload["brain"] = khoi_copy(cf["brain"])
    if cf.get("brain_ngan"):
        payload["ngan"] = khoi_copy(cf["brain_ngan"])
    for the in cf["the"]:
        if the.get("file"):
            payload[the["ma"]] = doc(the["file"])
    for i, f in enumerate(cf["files"], 1):
        payload[f"f{i}"] = doc(f["duong_dan"])
    for i, p in enumerate(cf["prompts"], 1):
        payload[f"p{i}"] = p["noi_dung"]
    payload["clone"] = f'git clone {cf["repo"]}.git'
    payload["m_ten"] = cf["ten_agent"]
    payload["m_mota"] = cf["mo_ta_agent"]
    for i, s in enumerate(cf.get("cau_mo_dau", []), 1):
        payload[f"m_st{i}"] = s

    chips = "".join(
        f'<span class="chip{" on" if i == 0 else ""}">{e(c)}</span>'
        for i, c in enumerate(cf["chips"]))
    stt = "".join(
        f'<div class="st-i"><span>{e(s)}</span>'
        f'<button class="copy" data-copy="m_st{i}" type="button">Copy</button></div>'
        for i, s in enumerate(cf.get("cau_mo_dau", []), 1))
    muc = cf.get("muc", ["Cài đặt", "Prompt mẫu", "Điều phải biết", "Việc đang chặn"])
    nav = "".join(
        f'<a href="#m{i}">{i} &middot; {e(t)}</a>' for i, t in enumerate(muc, 1))

    sec4 = ""
    if cf.get("chan"):
        sec4 = f"""
<section class="sec" id="m4">
  <div class="sec-h"><span class="pre">Mục 4</span><h2>{e(muc[3])}</h2>
    <span class="bar"></span><p>{cf.get("chan_intro", "")}</p></div>
  {khoi_chan(cf)}
</section>"""

    quick = f'<p class="quick">{cf["quick"]}</p>' if cf.get("quick") else ""
    so_file = len(cf["files"])

    return f"""<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(cf["title"])}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&family=Lora:ital,wght@1,600&display=swap" rel="stylesheet">
{CSS}

<header class="top">
  <div class="wrap" style="padding-block:42px 36px">
    <p class="eyebrow">{e(cf.get("eyebrow", "Hướng dẫn cài đặt & vận hành"))}</p>
    <h1>{e(cf["h1"])}</h1>
    <p class="lede">{cf["lede"]}</p>
    {quick}
    <div class="chips">{chips}</div>
    <p class="dim" style="margin-top:18px">{cf["dim"]} ·
      <a href="{cf["repo"]}" target="_blank" rel="noopener">repo trên GitHub</a></p>
  </div>
</header>

<nav class="bar">
  <div class="wrap">{nav}
    <button class="themebtn" id="theme" type="button">Đổi nền</button>
  </div>
</nav>

<main class="wrap">

<section class="sec" id="m1">
  <div class="sec-h"><span class="pre">Mục 1</span><h2>{e(muc[0])}</h2>
    <span class="bar"></span><p>{cf["cai_dat_intro"]}</p></div>

  <div class="steps">
    <div><b><span class="n">1</span>Lấy bộ file</b><span>Tải ZIP rồi giải nén bằng <b>Extract&nbsp;All</b></span></div>
    <div><b><span class="n">2</span>Tạo project + dán bộ não</b><span>{cf.get("buoc2", "<b>Thẻ A</b> vào ô chỉ dẫn")}</span></div>
    <div><b><span class="n">3</span>Upload {so_file} file tri thức</b><span>Thiếu file nào thì agent đoán chỗ đó — và <b>không báo lỗi</b></span></div>
  </div>

  <div class="dl">
    <h3>Tải bộ file</h3>
    <p>{cf["dl_mo_ta"]}</p>
    <a class="dl-btn" href="{cf["repo"]}/archive/refs/heads/main.zip">&#11015; Tải ZIP</a>
    <p class="alt">Thư mục cần dùng nằm ở <code>{e(cf["ten_agent"])}-main/knowledge/</code><br>
      Hoặc clone: <button class="copy" data-copy="clone" type="button">Copy lệnh git clone</button></p>
  </div>

  <h3 class="sub" style="margin:28px 0 6px">Tên &amp; mô tả — dán vào form</h3>
  <p class="dim" style="margin:0 0 13px">Nền tảng nào cũng hỏi ba ô này khi tạo mới.
    <b>Câu mở đầu</b> là ô <i>Conversation starters</i> của ChatGPT; Claude và Gemini không có ô này,
    cứ dán vào chat lần đầu.</p>
  <div class="mbox">
    <div class="mrow"><span class="lb">Tên</span>
      <span class="vl mono">{e(cf["ten_agent"])}</span>
      <button class="copy" data-copy="m_ten" type="button">Copy</button></div>
    <div class="mrow"><span class="lb">Mô tả</span>
      <span class="vl">{e(cf["mo_ta_agent"])}</span>
      <button class="copy" data-copy="m_mota" type="button">Copy</button></div>
    <div class="mrow"><span class="lb">Câu mở đầu</span><div class="st">{stt}</div></div>
  </div>

  <h3 class="sub" style="margin:28px 0 10px">Chọn nền tảng</h3>
  {khoi_tab(cf)}

  <h3 class="sub" style="margin:28px 0 6px">{len(cf["the"])} thẻ dán sẵn</h3>
  <p class="dim" style="margin:0 0 14px">{cf.get("the_mo_ta", "Thẻ A <b>dán vào ô văn bản</b>. Thẻ gộp là <b>file upload</b> — chỉ dùng khi nền tảng chặn số file.")}</p>
  {khoi_the(cf, payload)}

  <h3 class="sub" style="margin:28px 0 6px">{so_file} file tri thức</h3>
  <p class="dim" style="margin:0 0 13px">{cf["files_mo_ta"]}</p>
  {f'<div class="note stop">{cf["files_canh_bao"]}</div>' if cf.get("files_canh_bao") else ""}
  <div class="files">{khoi_file(cf, payload)}</div>

  {khoi_smoke(cf)}
</section>

<section class="sec" id="m2">
  <div class="sec-h"><span class="pre">Mục 2</span><h2>{e(muc[1])}</h2>
    <span class="bar"></span><p>{cf["prompt_intro"]}</p></div>
  {khoi_prompt(cf, payload)}
  {f'<div class="note" style="margin-top:4px">{cf["prompt_ghi"]}</div>' if cf.get("prompt_ghi") else ""}
</section>

<section class="sec" id="m3">
  <div class="sec-h"><span class="pre">Mục 3</span><h2>{e(muc[2])}</h2>
    <span class="bar"></span><p>{cf["dieu_intro"]}</p></div>
  {khoi_dieu(cf)}
</section>
{sec4}
</main>

<footer>
  <div class="wrap">
    <p><b>{e(cf["ten_agent"])}</b> — trang này sinh thẳng từ nội dung repo bằng
      <code>python tools/trang-huong-dan.py</code>, nên nút Copy luôn khớp file nguồn.</p>
    <p style="margin-bottom:0">{cf["footer"]} ·
      <a href="{cf["repo"]}" target="_blank" rel="noopener">repo trên GitHub</a></p>
  </div>
</footer>

<div class="toast" id="toast" role="status" aria-live="polite"></div>

<script id="payload" type="application/json">{json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")}</script>
<script>
(function(){{
  var DATA = {{}};
  try {{ DATA = JSON.parse(document.getElementById('payload').textContent); }} catch(e){{}}

  document.querySelectorAll('[data-peek]').forEach(function(pre){{
    var t = DATA[pre.dataset.peek]; if (t === undefined) return;
    pre.textContent = t.length > 2600 ? t.slice(0, 2600) + '\\n\\n… (còn ' +
      (t.length - 2600).toLocaleString('vi-VN') + ' ký tự — bấm Copy để lấy đủ)' : t;
  }});

  var toast = document.getElementById('toast'), tid;
  function khoe(msg){{
    toast.textContent = msg; toast.classList.add('on');
    clearTimeout(tid); tid = setTimeout(function(){{ toast.classList.remove('on'); }}, 1700);
  }}

  document.addEventListener('click', function(ev){{
    var b = ev.target.closest('[data-copy]'); if(!b) return;
    var t = DATA[b.dataset.copy]; if(t === undefined) return;
    var xong = function(){{
      var cu = b.textContent; b.textContent = 'Đã copy'; b.classList.add('done');
      khoe('Đã copy ' + t.length.toLocaleString('vi-VN') + ' ký tự');
      setTimeout(function(){{ b.textContent = cu; b.classList.remove('done'); }}, 1700);
    }};
    if (navigator.clipboard && navigator.clipboard.writeText) {{
      navigator.clipboard.writeText(t).then(xong, function(){{
        khoe('Trình duyệt chặn copy — bấm Xem nội dung rồi copy tay'); }});
    }} else {{
      var ta = document.createElement('textarea');
      ta.value = t; ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      try {{ document.execCommand('copy'); xong(); }}
      catch(err){{ khoe('Không copy được — bấm Xem nội dung rồi copy tay'); }}
      document.body.removeChild(ta);
    }}
  }});

  document.querySelectorAll('.tab').forEach(function(b){{
    b.addEventListener('click', function(){{
      document.querySelectorAll('.tab').forEach(function(x){{
        x.setAttribute('aria-selected', String(x === b)); }});
      document.querySelectorAll('.tabpanel').forEach(function(p){{
        p.hidden = p.dataset.panel !== b.dataset.tab; }});
    }});
  }});

  document.querySelectorAll('.qa-bar button').forEach(function(b){{
    b.addEventListener('click', function(){{
      var f = b.dataset.f;
      document.querySelectorAll('.qa-bar button').forEach(function(x){{
        x.setAttribute('aria-pressed', String(x === b)); }});
      document.querySelectorAll('.prompt').forEach(function(p){{
        p.hidden = (f !== 'all' && p.dataset.g !== f); }});
    }});
  }});

  var root = document.documentElement, nut = document.getElementById('theme');
  var khoa = 'hd-theme-' + {json.dumps(cf["ma"])};
  try {{ var luu = localStorage.getItem(khoa); if (luu) root.setAttribute('data-theme', luu); }} catch(e){{}}
  nut.addEventListener('click', function(){{
    var toi = root.getAttribute('data-theme') === 'dark'
      || (!root.getAttribute('data-theme') && matchMedia('(prefers-color-scheme:dark)').matches);
    var moi = toi ? 'light' : 'dark';
    root.setAttribute('data-theme', moi);
    try {{ localStorage.setItem(khoa, moi); }} catch(e){{}}
  }});
}})();
</script>
"""


def main() -> None:
    for luong in (sys.stdout, sys.stderr):
        try:
            luong.reconfigure(encoding="utf-8")
        except (AttributeError, OSError):
            pass

    cf = json.loads(CAU_HINH.read_text(encoding="utf-8"))
    trang = dung(cf)
    ra = Path(sys.argv[1]) if len(sys.argv) > 1 else RA
    ra.parent.mkdir(parents=True, exist_ok=True)
    ra.write_text(trang, encoding="utf-8")
    print(f"{ra} — {len(trang.encode('utf-8')) / 1024:,.0f} KB")
    print(f"  {len(cf['the'])} thẻ · {len(cf['files'])} file tri thức · "
          f"{len(cf['prompts'])} prompt · {len(cf.get('smoke', []))} câu smoke test")
    for the in cf["the"]:
        if the.get("tran"):
            so = len(khoi_copy(cf["brain_ngan"])) if the["ma"] == "ngan" else 0
            if so > the["tran"]:
                print(f"⛔ Thẻ {the['nhan']} vượt {the['tran']} ký tự", file=sys.stderr)
                sys.exit(1)


if __name__ == "__main__":
    main()
