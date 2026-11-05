# -*- coding: utf-8 -*-
CSS = """
@page { size: 1134pt 708.96pt; margin: 0 }
* { box-sizing: border-box; margin: 0; padding: 0 }
body { font-family: 'Pretendard', 'Noto Color Emoji', sans-serif; color: #1f2633; background: #fff }
.pg { width: 1134pt; height: 708.96pt; page-break-after: always; position: relative; overflow: hidden }
.pg:last-child { page-break-after: auto }
sub { font-size: 70%; vertical-align: -0.25em; line-height: 0 }

/* 표지 */
.cv { display: grid; grid-template-columns: 430pt 1fr; height: 100% }
.cv-l { background: linear-gradient(160deg, #13294b 0%, #1d3557 55%, #2b4c7e 100%); color: #fff; padding: 46pt 38pt; position: relative }
.cv-l .k { font-size: 11pt; letter-spacing: 2pt; opacity: .8; font-weight: 600 }
.cv-l h1 { font-size: 40pt; line-height: 1.18; margin: 14pt 0 10pt; font-weight: 900; letter-spacing: -.5pt }
.cv-l h1 em { font-style: normal; color: #ffd166 }
.cv-l .sub { font-size: 13pt; line-height: 1.6; opacity: .92 }
.cv-l .pill { display: inline-block; margin: 18pt 6pt 0 0; padding: 4pt 11pt; border-radius: 14pt; background: rgba(255,255,255,.14); font-size: 10.5pt; font-weight: 700 }
.cv-l .bot { position: absolute; left: 38pt; right: 38pt; bottom: 36pt; font-size: 9.5pt; opacity: .75; line-height: 1.6 }
.cv-r { padding: 34pt 40pt 30pt 36pt; display: flex; flex-direction: column; gap: 11pt }
.cv-r h2 { font-size: 13pt; color: #1d3557; font-weight: 800; letter-spacing: .3pt; display: flex; align-items: center; gap: 8pt }
.cv-r h2:after { content: ''; flex: 1; height: 1pt; background: #dde3ee }
.chs { display: grid; grid-template-columns: repeat(5, 1fr); gap: 9pt }
.chc { border-radius: 9pt; padding: 11pt 10pt; color: #fff; min-height: 128pt; display: flex; flex-direction: column }
.chc .n { font-size: 26pt; font-weight: 900; line-height: 1 }
.chc .n small { font-size: 12pt; font-weight: 700 }
.chc .t { font-size: 12pt; font-weight: 800; margin-top: 6pt; line-height: 1.25 }
.chc .e { font-size: 8pt; opacity: .85; margin-top: 2pt }
.chc .p { margin-top: auto; font-size: 9pt; font-weight: 700; background: rgba(255,255,255,.2); border-radius: 6pt; padding: 3pt 6pt }
.how { display: grid; grid-template-columns: repeat(4, 1fr); gap: 9pt }
.hw { border: 1pt solid #e1e6f0; border-radius: 8pt; padding: 9pt 10pt; font-size: 9.6pt; line-height: 1.5; background: #fafbfe }
.hw b.t { display: block; font-size: 10.5pt; margin-bottom: 3pt; color: #1d3557 }
.chip { display: inline-block; font-size: 8pt; font-weight: 800; padding: 1pt 6pt; border-radius: 6pt; color: #fff; vertical-align: 1pt }
.legend { display: flex; flex-wrap: wrap; gap: 6pt 14pt; font-size: 9.5pt; align-items: center }
.sw { display: inline-block; width: 22pt; height: 10pt; border-radius: 3pt; vertical-align: -1pt; margin-right: 4pt }

/* 장 표지 */
.dv { display: grid; grid-template-columns: 300pt 1fr; height: 100% }
.dv-l { color: #fff; padding: 46pt 32pt; position: relative }
.dv-l .k { font-size: 11pt; letter-spacing: 2pt; font-weight: 700; opacity: .85 }
.dv-l .n { font-size: 96pt; font-weight: 900; line-height: 1; margin-top: 10pt }
.dv-l .n small { font-size: 34pt }
.dv-l h1 { font-size: 30pt; font-weight: 900; margin-top: 12pt; line-height: 1.2 }
.dv-l .e { font-size: 11pt; opacity: .85; margin-top: 4pt }
.dv-l .st { position: absolute; left: 32pt; bottom: 40pt; right: 32pt; font-size: 11pt; line-height: 1.8 }
.dv-l .st b { font-size: 15pt }
.dv-r { padding: 34pt 34pt 26pt 30pt }
.dv-r h2 { font-size: 12.5pt; color: #1d3557; font-weight: 800; margin-bottom: 10pt; display: flex; gap: 8pt; align-items: center }
.dv-r h2:after { content: ''; flex: 1; height: 1pt; background: #dde3ee }
.toc { columns: 2; column-gap: 26pt; font-size: 11pt }
.toc.dense { font-size: 10pt }
.tr { display: flex; align-items: baseline; gap: 6pt; padding: 4.6pt 0; border-bottom: .6pt dotted #d5dbe6; break-inside: avoid }
.toc.dense .tr { padding: 3.1pt 0 }
.tr .no { font-weight: 800; min-width: 54pt; color: #1d3557; white-space: nowrap }
.tr .tt { flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap }
.tr .pp { font-weight: 700; color: #6b7686; min-width: 22pt; text-align: right }
.kd { font-size: 7.6pt; font-weight: 800; padding: .5pt 5pt; border-radius: 5pt; color: #fff; white-space: nowrap }
.kd.본문 { background: #1d3557 } .kd.예제 { background: #6d4bc4 } .kd.과제 { background: #e07a1f } .kd.참고 { background: #8a95a5 }
.foot { position: absolute; right: 30pt; bottom: 16pt; font-size: 8.6pt; color: #6b7686 }
"""
