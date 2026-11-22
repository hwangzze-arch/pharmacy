# 재사용 페이지가 없으므로 intro.pdf가 곧 최종본
import os, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(os.path.dirname(HERE)), "신약개발개론_13주차 보강_Non-GLP 전임상연구와 동물실험 대체법_요약정리.pdf")
shutil.copy(os.path.join(HERE, "intro.pdf"), OUT)
print(OUT)
