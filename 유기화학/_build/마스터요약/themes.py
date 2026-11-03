# -*- coding: utf-8 -*-
"""배치는 그대로, 색·꾸밈만 바꾸는 테마. THEME=pastel / note"""

THEMES = {
"": "",

# B. 파스텔 카드: 흰 바탕 + 둥근 그림자 카드 + 그라데이션 머리띠
"pastel": """
:root{--paper:#ffffff;--line:#eef0f4;}
.page{background:linear-gradient(180deg,#f7fbff 0,#ffffff 70px) !important;}
.hd{border-bottom:none !important;background:linear-gradient(90deg,#e7f5ff,#f3f0ff 60%,#fff0f6);border-radius:14px;padding:7px 12px !important;}
.hd .bd{background:linear-gradient(135deg,#4dabf7,#9775fa) !important;border-radius:10px !important;box-shadow:0 2px 6px rgba(77,171,247,.35);}
.hd.q .bd{background:linear-gradient(135deg,#38d9a9,#4dabf7) !important;}
.hd .pt,.hd.q .pt{background:#fff !important;color:#7048e8 !important;box-shadow:0 1px 4px rgba(112,72,232,.15);}
.hd h1{color:#343a63 !important;}
.core{background:linear-gradient(90deg,#fff9db,#fff4e6) !important;border:none !important;box-shadow:0 2px 8px rgba(250,176,5,.18);border-radius:12px !important;}
.one{background:linear-gradient(90deg,#748ffc,#9775fa) !important;border-radius:14px !important;box-shadow:0 3px 10px rgba(116,143,252,.35);}
.card,.fig,.mband{border:none !important;box-shadow:0 2px 10px rgba(52,58,99,.10);border-radius:12px !important;}
.card.rec{background:#fff0f6 !important;} .card.my{background:#fff9fb !important;border:1.5px dashed #faa2c1 !important;box-shadow:none;}
.card.trap{background:#fff5f5 !important;}
.qcard{border:none !important;box-shadow:0 2px 10px rgba(52,58,99,.10);border-radius:14px !important;background:#ffffff !important;}
.work{border:2px dashed #b197fc !important;background-color:#fbfaff !important;background-image:radial-gradient(#e5dbff 1.1px,transparent 1.1px) !important;border-radius:14px !important;}
.acol{background:linear-gradient(180deg,#f3fcf8,#f8f9ff) !important;border:none !important;box-shadow:0 2px 10px rgba(52,58,99,.10);border-radius:14px !important;}
.al{background:linear-gradient(135deg,#38d9a9,#20c997) !important;border-radius:8px !important;}
.ans{border:none !important;background:#fffbe6 !important;box-shadow:inset 4px 0 0 #fcc419;border-radius:10px !important;}
.qk{border-radius:10px !important;}
.page.pair .qhalf + .qhalf{border-top:2px dashed #d0bfff !important;}
.page.pair .bd2{background:linear-gradient(135deg,#38d9a9,#4dabf7) !important;}
table.t th{background:#f3f0ff !important;color:#5f3dc4 !important;}
.ft{border-top:none !important;color:#adb5bd !important;}
""",

# C. 필기 노트: 모눈 종이 + 형광펜 제목 + 마스킹테이프 라벨 + 포스트잇 정답
"note": """
:root{--paper:#fffdf7;}
.page{background-color:#fffdf7 !important;background-image:linear-gradient(#f1ede2 1px,transparent 1px),linear-gradient(90deg,#f1ede2 1px,transparent 1px) !important;background-size:22px 22px !important;}
.hd{border-bottom:none !important;}
.hd h1{display:inline;background:linear-gradient(transparent 58%,#ffe066 58%) !important;color:#2b2b2b !important;padding:0 3px;}
.hd .bd{background:#ffd8a8 !important;color:#7a3f00 !important;border-radius:3px !important;transform:rotate(-2deg);box-shadow:1px 1px 0 rgba(0,0,0,.08);}
.hd.q .bd{background:#b2f2bb !important;color:#1b5e20 !important;}
.hd .pt,.hd.q .pt{background:#e7f5ff !important;color:#1971c2 !important;border-radius:3px !important;}
.core{background:#fff !important;border:2px solid #ffe066 !important;border-radius:4px !important;}
.one{background:#fff3bf !important;color:#5c3d00 !important;border-left:6px solid #fab005;border-radius:4px !important;}
.one .lb{background:#fab005 !important;color:#fff !important;}
.card,.fig,.mband{border-radius:4px !important;}
.card.rec{background:#fff0f6 !important;border:1px solid #fcc2d7 !important;}
.card.my{background:#fff !important;border:1.5px dashed #ff8787 !important;}
.qcard{background:#ffffff !important;border:1.5px solid #ced4da !important;border-radius:4px !important;box-shadow:3px 3px 0 #e9ecef;}
.work{background:transparent !important;border:2px dashed #adb5bd !important;border-radius:4px !important;background-image:none !important;}
.acol{background:#fff9db !important;border:none !important;border-radius:2px !important;box-shadow:2px 3px 6px rgba(0,0,0,.12);transform:rotate(.25deg);}
.al{background:#fab005 !important;color:#fff !important;border-radius:3px !important;}
.ans{background:#fff !important;border:none !important;border-left:4px solid #40c057 !important;border-radius:2px !important;}
.page.pair .qhalf + .qhalf{border-top:2px dashed #ced4da !important;}
.page.pair .bd2{background:#b2f2bb !important;color:#1b5e20 !important;border-radius:3px !important;}
""",

# D. 21장 내필기 정리본 스타일 (남색 배지 · 문제 상자 · 줄 없는 메모 · 크림색 정답과 해설)
"mid21": """
:root{--paper:#ffffff;--navy:#1d3557;--nblue:#0f3f8c;--line:#dfe5ee;--indigo:#1d3557;--indigo-soft:#eef3fa;}
html,body,.page{background:#fff !important;}
.h21{display:flex;align-items:center;gap:14px;border-bottom:3px solid var(--navy);padding-bottom:7px;flex:none;}
.b21{background:var(--navy);color:#fff;border-radius:9px;padding:3px 14px 4px;display:flex;flex-direction:column;align-items:center;line-height:1.15;flex:none;min-width:64px;}
.b21 span{font-size:10.5px;opacity:.9;} .b21 b{font-size:21px;}
.h21 .tt{flex:1;min-width:0;}
.h21 h1{margin:0;font-size:21px;line-height:1.3;font-weight:700;color:var(--navy);}
.h21 .sb{font-size:11px;color:#6b7686;}
.h21 .pills{display:flex;gap:6px;flex:none;}
.pill{border:1px solid #c3cad6;background:#f6f8fc;color:var(--nblue);border-radius:13px;font-size:10.5px;font-weight:500;padding:2px 11px;white-space:nowrap;}
.sec{color:var(--nblue) !important;}
.core{background:#fffbe6 !important;border:1px solid #f1e1b6 !important;border-left:5px solid #e89b1c !important;border-radius:9px !important;}
.core .lb{background:#e89b1c !important;color:#fff !important;border:none !important;}
.one{background:var(--navy) !important;}
.card.rec{background:#fff0f3 !important;border:1px solid #f3a6b8 !important;} .card.rec .ct{color:#d1335b !important;}
.card.my{background:#fffcf3 !important;border:1px solid #f1e1b6 !important;} .card.my .ct{color:#b06a00 !important;}
.card.trap{background:#fff0f3 !important;border-color:#f3a6b8 !important;}
.card.tip,.card.ana{background:#eef3fa !important;border-color:#d3deee !important;}
.mband,.fig{border-color:#dfe5ee !important;}
.mband .mbl{color:var(--nblue) !important;background:#eef3fa !important;}
table.t th{background:#eef3fa !important;color:var(--nblue) !important;}
.ft{border-top:1px solid #e5e9f0 !important;color:#8b95a5 !important;align-items:center;}
.ft .lg{display:flex;align-items:center;gap:4px;}
.ft .lg i{display:inline-block;width:16px;height:8px;border-radius:2px;margin-left:8px;}
.ft .lg i.y{background:#fff1a8;} .ft .lg i.g{background:#c9f0c4;} .ft .lg i.p{background:#ffd3e1;} .ft .lg i.b{background:#d8e8ff;}
/* 문제 쪽 (세로) */
.v21{gap:0;}
.pbx{flex:none;margin-top:9px;background:#eef3fa;border-radius:10px;border-left:5px solid var(--navy);padding:8px 14px;overflow:hidden;}
.plb{display:inline-block;background:var(--navy);color:#fff;font-weight:700;letter-spacing:.04em;font-size:.82em;border-radius:5px;padding:1px 9px;margin-right:7px;}
.pbx .qtext{margin-top:5px;}
.memo{flex:1;min-height:60px;margin-top:8px;border:1.5px dashed #c3cad6;border-radius:10px;background:#fff;position:relative;}
.memo .ml2{position:absolute;top:6px;left:12px;font-size:.8em;color:#8b95a5;}
.abx{flex:none;margin-top:8px;background:#fffcf3;border:1px solid #f1e1b6;border-radius:12px;padding:8px 12px;overflow:hidden;}
.ah{display:flex;align-items:flex-start;gap:10px;}
.alb{flex:none;background:#e89b1c;color:#fff;font-weight:700;font-size:.9em;border-radius:7px;padding:3px 11px;margin-top:2px;}
.abar{flex:1;min-width:0;background:#d8e8ff;border-left:4px solid #1d5fc4;border-radius:6px;padding:3px 11px;color:#0f3f8c;font-weight:700;}
.abar p{margin:0 0 2px 0;}
.agrid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:7px;}
.agrid.one1{grid-template-columns:1fr;}
.xc{background:#fff;border:1px solid #f1e1b6;border-radius:9px;padding:6px 11px;min-width:0;overflow:hidden;}
.xc:empty{display:none;}
.xsec{font-weight:700;color:#b85c00;margin-bottom:2px;}
.xc .afig{border-color:#f1e1b6;margin-top:3px;}
.pcols{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:4px;}
.pbx{--aimg:1;}
.pbx img{max-width:100%;max-height:var(--pimgh,230px);object-fit:contain;object-position:left center;}
/* 세로로 안 들어가는 문제: 문제·메모 왼쪽, 정답과 해설 오른쪽 */
.v21.side{display:grid;grid-template-columns:.92fr 1.08fr;grid-template-rows:auto auto 1fr;column-gap:14px;}
.v21.side .h21{grid-column:1/3;}
.v21.side .pbx{grid-column:1;grid-row:2;}
.v21.side .memo{grid-column:1;grid-row:3;min-height:0;}
.v21.side .abx{grid-column:2;grid-row:2/4;margin-top:9px;}
.v21.side .agrid{grid-template-columns:1fr;}
.v21.side .pbx .tbimg{width:100% !important;}
.agrid{grid-template-columns:1fr 1.25fr;}
.nextp{flex:none;text-align:right;color:#b85c00;font-weight:700;font-size:.9em;margin-top:5px;}
.v21.aonly .abx{flex:1;min-height:0;}
.v21.aonly .agrid.one1 .xc{border:none;background:transparent;padding:2px 4px;}
.ovl{position:absolute;left:0;top:0;width:297mm;height:210mm;pointer-events:none;z-index:60;}
.memo.hasn{overflow:hidden;}
.mnote{position:absolute;inset:6px 12px 6px 12px;overflow:hidden;color:#c92a2a;font-size:var(--nfs,1em);line-height:1.55;}
.mnote .mnt{display:inline-block;font-size:.8em;font-weight:700;color:#fff;background:#e03131;border-radius:5px;padding:0 8px;margin-bottom:3px;}
.mnote p{margin:0 0 4px 0;} .mnote ul{margin:0 0 4px 0;padding-left:1.2em;} .mnote li{margin:0 0 2px 0;}
.mnote b{color:#b02525;} .mnote u2{color:#1c4ed8;text-decoration:none;} .mnote u2 b{color:#1c4ed8;}
.memo .mgo{position:absolute;right:12px;bottom:8px;font-size:.85em;font-weight:700;color:#e03131;}
.npage .nbox{flex:1;min-height:0;margin-top:9px;border:1.5px dashed #f08c8c;border-radius:10px;background:#fffafa;position:relative;}
.mnote.big{inset:10px 16px;}
.top10 .tgrid{flex:1;min-height:0;display:grid;grid-template-columns:1.05fr 1fr;gap:10px;margin-top:9px;}
.top10 .tcol{display:flex;flex-direction:column;gap:10px;min-height:0;}
.top10 .tc{border-radius:11px;padding:8px 12px;overflow:hidden;}
.top10 .t1{background:#fff8e1;border:1.5px solid #f2c94c;} .top10 .t2{background:#eef3fa;border:1.5px solid #a9c1e8;} .top10 .t3{background:#eef8ec;border:1.5px solid #a9d9a0;}
.top10 .tct{font-weight:700;color:#1d3557;font-size:1.05em;margin-bottom:4px;}
.top10 .tsub{color:#6b7686;font-size:.92em;margin:0 0 5px 0;}
.top10 .tr{display:flex;gap:8px;margin:0 0 6px 0;align-items:flex-start;}
.top10 .rk{flex:none;background:#1d3557;color:#fff;border-radius:6px;font-weight:700;font-size:.85em;padding:1px 8px;margin-top:2px;}
.top10 .t1 .rk{background:#e89b1c;}
.npage.n28{display:grid;grid-template-columns:.78fr 1.22fr;grid-template-rows:auto 1fr;column-gap:12px;}
.npage.n28 .h21{grid-column:1/3;} .npage.n28 .pbx{grid-column:1;grid-row:2;align-self:start;}
.npage.n28 .nbox{grid-column:2;grid-row:2;}
.npage.n20 .pbx img{max-height:118px !important;width:auto !important;}
.topb{flex:none;display:inline-flex;align-items:center;gap:7px;border-radius:999px;padding:5px 16px 5px 5px;color:#fff;font-weight:700;box-shadow:0 2px 6px rgba(0,0,0,.18);white-space:nowrap;}
.topb i{font-style:normal;background:#fff;border-radius:999px;padding:1px 8px;font-size:11px;}
.topb b{font-size:24px;line-height:1;} .topb em{font-style:normal;font-size:11px;opacity:.95;}
.topb.g1{background:linear-gradient(90deg,#e8590c,#f59f00);} .topb.g1 i{color:#e8590c;}
.topb.g2{background:linear-gradient(90deg,#1c7ed6,#4dabf7);} .topb.g2 i{color:#1c7ed6;}
.topb.g3{background:linear-gradient(90deg,#2b8a3e,#51cf66);} .topb.g3 i{color:#2b8a3e;}
.topb.sm{padding:1px 9px 1px 3px;margin-left:6px;vertical-align:middle;} .topb.sm b{font-size:14px;} .topb.sm i,.topb.sm em{font-size:9.5px;}
.h21.istop{border-bottom-color:#e8590c;}
.pbx.top.g1{border-left-color:#e8590c !important;background:#fff4e6 !important;} .pbx.top.g2{border-left-color:#1c7ed6 !important;background:#e7f5ff !important;} .pbx.top.g3{border-left-color:#2b8a3e !important;background:#ebfbee !important;}
.pbx.top{border-left-width:8px !important;}
.pc{display:flex;flex-direction:column;min-height:0;min-width:0;}
.pc .qh{font-weight:700;color:var(--navy);margin-top:6px;}
.pc .bd2{background:var(--navy);color:#fff;border-radius:6px;font-size:.82em;padding:1px 8px;margin-right:4px;}
""",
}
