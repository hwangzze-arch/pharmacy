# -*- coding: utf-8 -*-
"""맥머리 10판(OpenStax) 23장 본문 예제·문제 — 원서 그대로 (문제 그림 = 원서 캡처).
위: 원서 문제 그림 + 번역 / 아래: 정답(한글) + 풀이 + 원서 정답(Answer Key)·해설집(SSM) 캡처."""
import os
from PIL import Image as _Im

I = "img/"
D = os.path.dirname(os.path.abspath(__file__))


def _px(name):
    return _Im.open(os.path.join(D, "img", name + ".jpg")).width


def qimg(name):
    """문제 그림: 원서 글자 ≈ 본문 글자 크기 (실제 픽셀 × 0.5, 칸보다 넓으면 칸에 맞춤)."""
    return f'<img src="{I}{name}.jpg" style="width:{round(_px(name) * 0.5)}px;max-width:100%;display:block;margin:2px 0">'


def aimg(name, k=0.5):
    """정답·해설 칸 그림 (render.js가 --aimg로 더 줄임)."""
    return f'<img class="tbimg" src="{I}{name}.jpg" style="width:calc({round(_px(name) * k)}px * var(--aimg, 1));max-width:100%;display:block;margin:2px 0">'


def KEY(n):
    return '<div class="xsec">📗 원서 정답 (Answer Key)</div>' + aimg(f"ta{n:02d}")


def SSM(n, k=0.4):
    return f'<div class="xsec">📘 해설집 풀이 (SSM 23.{n})</div>' + aimg(f"ss{n:02d}", k)


def tb(n, part, title, kind, ko, a, exp, extra=None, **kw):
    """본문 Problem 23-n."""
    return dict(t="q", id=f"p{n}", toc=title, badge="본문", num=f"23-{n}", part=part, kind=kind,
                src=f"본문 Problem 23-{n} (원서 그대로)", title=f"Problem 23-{n} — {title}",
                q=qimg(f"tp{n:02d}") + f'<div class="term" style="margin-top:6px">번역: {ko}</div>',
                a=a, exp=exp, extra=KEY(n) if extra is None else extra, **kw)


def we(n, part, title, ko, a, exp, **kw):
    """본문 Worked Example 23.n."""
    return dict(t="q", id=f"we{n}", toc=title, badge="예제", num=f"23.{n}", part=part, kind=["ex"],
                src=f"본문 Worked Example 23.{n} (원서 그대로)", title=f"Worked Example 23.{n} — {title}",
                q=qimg(f"we{n}q") + f'<div class="term" style="margin-top:6px">번역: {ko}</div>',
                a=a, exp=exp, extra='<div class="xsec">📗 원서 풀이 (Strategy · Solution)</div>' + aimg(f"we{n}s"), **kw)


def vq(id, part, title, kind, src, q, a, exp, extra="", **kw):
    """강의 슬라이드·녹취 기반 예상 변형 문제."""
    return dict(t="q", id=id, toc=title, badge="변형", num="변형", part=part, kind=kind, src=src, title=title,
                q=q, a=a, exp=exp, extra=extra, **kw)


def hw(n, title, kind, ko, a, exp, extra="", **kw):
    """과제 23-n (23장-2 강의자료 마지막 슬라이드). 문제 그림 = 강의자료 캡처, 풀이 = 해설집."""
    from parts import P4
    return dict(t="q", id=f"hw{n}", toc=title, badge="과제", num=f"23-{n}", part=P4, kind=kind,
                src=f"과제 23-{n} (강의자료 마지막 슬라이드)", title=f"과제 23-{n} — {title}",
                q=qimg(f"hw{n}") + f'<div class="term" style="margin-top:6px">번역: {ko}</div>',
                a=a, exp=exp, extra=extra + ("" if kw.pop("nossm", False) else SSM(n)), rec=True, **kw)
