# -*- coding: utf-8 -*-
"""맥머리 10판(OpenStax) 23장 본문 예제·문제 — 원서 그대로 (문제 그림 = 원서 캡처).
위: 원서 문제 그림 + 번역 / 아래: 정답(한글) + 풀이 + 원서 정답(Answer Key)·해설집(SSM) 캡처."""
import os
from PIL import Image as _Im

I = "img/"
D = os.path.dirname(os.path.abspath(__file__))


def _px(name):
    return _Im.open(os.path.join(D, "img", name + ".jpg")).width


# 모든 캡처를 같은 배율로: 원서·정답·해설집(3.2배 캡처) 글자가 본문 글자와 비슷하도록. 줄이지 않음.
K = {"tp": 0.37, "we": 0.37, "ta": 0.37, "ss": 0.34, "hw": 0.39}


def _k(name):
    for p, k in K.items():
        if name.startswith(p):
            return k
    return None


def qimg(name):
    """문제 그림 (같은 배율, 칸보다 넓을 때만 칸에 맞춤)."""
    k = _k(name)
    w = f"width:calc({round(_px(name) * k)}px * var(--ik, 1));max-width:100%" if k else "width:calc(100% * var(--ik, 1))"
    return f'<img src="{I}{name}.jpg" style="{w};display:block;margin:2px 0">'


def aimg(name, k=None):
    """정답·해설 칸 그림 (문제 그림과 같은 배율)."""
    k = _k(name) or 0.37
    return f'<img class="tbimg" src="{I}{name}.jpg" style="width:calc({round(_px(name) * k)}px * var(--ik, 1));max-width:100%;display:block;margin:2px 0">'


def KEY(n):
    return '<div class="xsec">📗 원서 정답 (Answer Key)</div>' + aimg(f"ta{n:02d}")


def SSM(n, k=None):
    """해설집 풀이. 긴 것(앞·뒤 반으로 잘라 둔 ss{n}a·b)은 두 블록으로 → 두 단에 나눠 들어감."""
    if os.path.exists(os.path.join(D, "img", f"ss{n:02d}a.jpg")):
        return (f'<div class="xsec">📘 해설집 풀이 (SSM 23.{n}) ①</div>' + aimg(f"ss{n:02d}a")
                + f'<div class="xsec">📘 해설집 풀이 (SSM 23.{n}) ②</div>' + aimg(f"ss{n:02d}b"))
    return f'<div class="xsec">📘 해설집 풀이 (SSM 23.{n})</div>' + aimg(f"ss{n:02d}")


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
