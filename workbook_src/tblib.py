# -*- coding: utf-8 -*-
"""교수님 테스트뱅크(TB) 문제 페이지 — 시험대비 요약노트에 끼워 넣는다.
문제 dict: n(번호), sec(요약 페이지 0-based 인덱스), title, diff(1–3), kind('MC'|'SA'),
en(원문 html), ko(번역 html), answer(html), explain(html)"""
from helpers import *

TB_CSS = r'''
.mcq { margin: .25em 0 .1em 1.6em; padding: 0; }
.mcq li { margin: .12em 0; padding-left: .2em; }
.tba { display: flex; flex-direction: column; gap: 1mm; margin: .3em 0; }
.tba .row { display: flex; gap: 2.4mm; align-items: baseline; }
.tba .L { flex: none; background: #0f766e; color: white; font-weight: 900; border-radius: 6px; padding: 0 2.4mm; font-family: 'JetBrains Mono'; }
.tba .e { font-family: 'Noto Serif'; color: #0f172a; font-weight: 700; }
.tba .k { color: #334155; }
.tbnote { font-size: .9em; color: #b45309; background: #fffbeb; border: 1px solid #fcd34d; border-radius: 6px; padding: .3em .7em; margin-top: .4em; }
'''


def mcq(stem, opts):
    return f'<p>{stem}</p><ol class="mcq" type="A">' + ''.join(f'<li>{o}</li>' for o in opts) + '</ol>'


def ans(letter, en, ko, note=''):
    """객관식 정답: 기호 + 영어 + 한국어"""
    n = f'<div class="tbnote">{note}</div>' if note else ''
    return f'<div class="tba"><div class="row"><b class="L">{letter}</b><span class="e">{en}</span></div><div class="row"><b class="L" style="visibility:hidden">{letter}</b><span class="k">{ko}</span></div></div>{n}'


def sa(en, ko):
    """주관식 정답: 영어 줄 + 한국어 줄"""
    return f'<div class="tba"><div class="row"><b class="L">EN</b><span class="e">{en}</span></div><div class="row"><b class="L" style="background:#15803d">KO</b><span class="k">{ko}</span></div></div>'


def render_tb(it, ch, strip='', sec_label=''):
    kind = '객관식' if it.get('kind', 'MC') == 'MC' else '서술형'
    return f'''
<div class="ph"><div class="badge" style="background:#0f766e"><small>교수님 기출</small><b>{ch}-{it['n']}</b></div>
 <div class="ttl"><span class="ko">{it['title']}</span><span class="en">Test Bank Q{it['n']} · 관련 요약 ▸ {sec_label}</span></div>
 <div class="meta"><span class="tag">{kind} · Difficulty {it['diff']}</span>{stars(it['diff'])}</div></div>
<div class="cols">
 <div class="col">
  <div class="blk orig"><span class="lab">ORIGINAL · 원문</span>{it['en']}</div>
  <div class="blk trans"><span class="lab">번역</span>{it['ko']}</div>
  <div class="blk blank"><span class="lab">풀이 · 직접 풀어 보기</span><span class="hint">오른쪽을 가리고 풀어 보세요</span></div>
  {strip}
 </div>
 <div class="col">
  <div class="blk ans"><span class="lab">정답 · ANSWER</span>{it['answer']}</div>
  <div class="blk exp"><span class="lab">풀이</span>{it['explain']}</div>
 </div>
</div>'''
