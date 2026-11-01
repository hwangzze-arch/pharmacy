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
}
