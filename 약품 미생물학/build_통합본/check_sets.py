# 사용법: python3 check_sets.py <build_통합본 폴더> [모듈=f_virus] [--strict]
#   세트 개수·정답-해설 O/X 번호 검사. --strict: '모두' 문항은 해설에서 보기 11개를 전부 O/X로 판정했는지까지 검사
# -*- coding: utf-8 -*-
"""세트 문항 정합성 검사: 개수·해설 O/X 번호·보기 이름"""
import re, sys
args = sys.argv[1:]
build = args[0]
mod = next((a for a in args[1:] if not a.startswith("--")), "f_virus")
strict = "--strict" in args
sys.path.insert(0, build); sys.argv = ["x"]
import importlib, core
F = importlib.import_module(mod)
C = "①②③④⑤⑥⑦⑧⑨⑩⑪"
bad = 0
for si, S in enumerate(F.SETS, 1):
    for qi, q in enumerate(S["qs"], 1):
        tag = f"{si}-{qi}"
        ans, n, box = q["ans"], q["n"], S["box"]
        errs = []
        if n != len(ans): errs.append(f"n={n} != 정답수 {len(ans)}")
        if len(set(ans)) != len(ans): errs.append("정답 중복")
        if any(a < 0 or a >= len(box) for a in ans): errs.append("정답 번호 범위 밖")
        m = re.search(r"(\d)개 고르시오|\((\d)개\)", q["q"])
        if m and int(m.group(1) or m.group(2)) != n: errs.append(f"문구 개수 {m.group(0)} != n {n}")
        if "모두" not in q["q"] and not m: errs.append("개수도 '모두'도 없는 문구")
        O, X = set(), set()
        for ln in q["exp"]:
            k = ln.split("|", 1)[0]
            if k in ("O", "X") and "::" in ln:
                lab = ln.split("|", 1)[1].split("::", 1)[0]
                idx = {C.index(c) for c in lab if c in C}
                (O if k == "O" else X).update(idx)
                if k == "O" and len(idx) == 1:
                    i = next(iter(idx))
                    toks = [t for t in re.split(r"[\s()·,]+", box[i]) if len(t) >= 2]
                    body = ln.split("::", 1)[1].lower()
                    if not any(t[:2].lower() in body for t in toks):
                        errs.append(f"해설 {C[i]}에 보기명 '{box[i]}' 흔적 없음")
        if O != set(ans): errs.append(f"해설 O {sorted(C[i] for i in O)} != 정답 {sorted(C[i] for i in ans)}")
        if X & set(ans): errs.append(f"해설 X가 정답과 겹침 {sorted(C[i] for i in X & set(ans))}")
        if strict and "모두" in q["q"]:
            miss = set(range(len(box))) - O - X
            if miss: errs.append(f"모두 문항인데 판정 안 한 보기 {''.join(C[i] for i in sorted(miss))}")
        if errs:
            bad += 1
            print(tag, q["q"][:40], "→", "; ".join(errs))
print(f"문항 {sum(len(S['qs']) for S in F.SETS)}개 검사, 문제 {bad}건")
