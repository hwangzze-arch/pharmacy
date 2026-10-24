P0 = "읽기 전에"
P1 = "PART 1 · 19.1 전자전달 사슬"
P2 = "PART 2 · 19.2 ATP 합성"
P3 = "PART 3 · 19.3 조절 · 활성산소"
P4 = "PART 4 · 19.4–19.5 미토콘드리아의 다른 얼굴"
P5 = "PART 5 · 광합성 명반응 (광인산화)"
P6 = "PART 6 · 20.1 캘빈 회로 (탄소 고정)"
PF = "FINAL"

NUM = "①②③④⑤⑥⑦⑧"
ALPHA = "ABCDE"


def opts(*xs):
    """한글 보기 ①–⑤"""
    return '<ul class="opts">' + "".join(f"<li>{NUM[i]} {x}</li>" for i, x in enumerate(xs)) + "</ul>"


def eopts(*xs):
    """영어 원문 보기 A–E"""
    return '<ul class="opts">' + "".join(f"<li>{ALPHA[i]}. {x}</li>" for i, x in enumerate(xs)) + "</ul>"


def ox(*rows):
    """보기별 O/X 해설: ox(("①", True, "설명"), ...)"""
    return "".join(f'<div><b>{n}</b> {"⭕" if ok else "❌"} {t}</div>' for n, ok, t in rows)


def _stars(d):
    return "★" * d + "☆" * (3 - d)


def _warn(w):
    return f'<div class="card trap" style="margin-top:5px"><div class="ct">⚠️ 테스트뱅크 정답 확인</div>{w}</div>' if w else ""


def tbm(ch, n, part, diff, title, en, eo, ko, ko_o, ans, aen, ako, steps, opx=None, one="", warn=None):
    """테스트뱅크 객관식: 원문(영어) + 번역, 정답(영어 + 한글), 쉬운 풀이"""
    return dict(t="q", id=f"tb{ch}-{n}", part=part, kind=["tb", "mc"], badge=f"기출 {ch}-{n}", title=title,
                src=f"교수님 테스트뱅크 Ch.{ch} Q{n} · 난이도 {_stars(diff)}",
                en=en + eopts(*eo), q=ko + eopts(*ko_o), a=f"{ans} — {ako}", aen=f"{ans.split()[0]}) {aen}",
                steps=steps, opx=ox(*opx) if opx else "", extra=_warn(warn), one=one)


def tbs(ch, n, part, diff, title, en, ko, aen, ako, steps, one="", warn=None, extra=""):
    """테스트뱅크 주관식(Short Answer)"""
    return dict(t="q", id=f"tb{ch}-{n}", part=part, kind=["tb", "sa"], badge=f"기출 {ch}-{n}", title=title,
                src=f"교수님 테스트뱅크 Ch.{ch} Q{n} (Short Answer) · 난이도 {_stars(diff)}",
                en=en, q=ko, a=ako, aen=aen, steps=steps, extra=extra + _warn(warn), one=one)
