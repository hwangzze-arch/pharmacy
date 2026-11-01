# -*- coding: utf-8 -*-
"""그림이 읽기 어려울 만큼 작아지는 쪽을 찾아 자동으로 쪽을 나눈다.
build → render(AUDIT) → _autosplit.json 갱신 → 반복. 마지막에 PDF 출력.
  python3 fit.py ../../CH22_기말대비_마스터요약.pdf"""
import json, os, subprocess, sys
D = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(D, "_autosplit.json")
out = sys.argv[1]
auto = {"qsplit": [], "unpair": [], "csplit": {}}
json.dump(auto, open(F, "w"), ensure_ascii=False, indent=1)
for it in range(6):
    subprocess.run([sys.executable, "build.py"], cwd=D, check=True)
    subprocess.run(["node", "render.js", "/tmp/_fit.pdf"], cwd=D, check=True, env=dict(os.environ, AUDIT="1"), capture_output=True)
    need = json.load(open("/tmp/need.json")); ch = False
    for n in need:
        t, k = n["t"], n["k"]
        if t == "unpair":
            for kk in (k, n.get("k2")):
                if kk and kk not in auto["unpair"]: auto["unpair"].append(kk); ch = True
        elif t == "qsplit" and k not in auto["qsplit"]:
            auto["qsplit"].append(k); ch = True
        elif t in ("csplit", "csplit2"):
            cur = auto["csplit"].get(k, 0)
            lv = min(2, cur + 1) if t == "csplit" else (3 if ("overflow" in n["small"] or cur >= 2) else 2)
            if auto["csplit"].get(k, 0) < lv: auto["csplit"][k] = lv; ch = True
    print("pass", it + 1, "남은 작은 그림 쪽:", [(n["i"], n["t"], n["small"]) for n in need])
    json.dump(auto, open(F, "w"), ensure_ascii=False, indent=1)
    if not ch: break
subprocess.run(["node", "render.js", out], cwd=D, check=True)
