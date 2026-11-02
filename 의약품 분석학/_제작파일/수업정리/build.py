# 수업 녹취 정리 .md → 같은 색 체계의 A4 세로 HTML (render.js로 PDF 출력)
import subprocess, sys, pathlib
src = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2])
body = subprocess.run(["pandoc", "-f", "gfm", "-t", "html", str(src)], capture_output=True, text=True, check=True).stdout
for k, cls in (("🗣️", "prof"), ("📝", "mine"), ("⚠️", "warn")):
    body = body.replace(k, f'<span class="{cls}">{k}</span>')
CSS = """
@page{size:210mm 297mm;margin:14mm 14mm 16mm 14mm;}
:root{--blue:#2c6aa0;--navy:#1f3f66;--orange:#d97a26;--muted:#5f6b78;}
body{font-family:'Noto Sans KR','Noto Color Emoji',sans-serif;color:#1d2530;font-size:11.2px;line-height:1.62;-webkit-print-color-adjust:exact;print-color-adjust:exact;margin:0;}
h1{font-size:21px;color:#fff;background:var(--navy);margin:0 0 10px;padding:12px 16px;border-radius:7px;line-height:1.35;}
h2{font-size:15.5px;color:var(--navy);border-bottom:2.5px solid var(--blue);padding-bottom:3px;margin:20px 0 8px;break-after:avoid;}
h3{font-size:12.6px;color:#fff;background:var(--blue);display:inline-block;padding:2px 10px;border-radius:5px;margin:12px 0 5px;break-after:avoid;}
p{margin:0 0 5px;} ul,ol{margin:0 0 6px;padding-left:1.35em;} li{margin:0 0 2px;}
strong{background:linear-gradient(transparent 55%,#fff07a 55%);font-weight:700;}
blockquote{margin:6px 0;background:#ecf9e6;border:1px solid #a9db95;border-left:5px solid #4caf2c;border-radius:6px;padding:7px 12px;font-size:12.2px;}
blockquote p{margin:0;}
table{border-collapse:collapse;width:100%;margin:5px 0 9px;break-inside:avoid;}
th{background:#e3edf8;color:var(--navy);text-align:left;}
th,td{border:1px solid #b9c7d6;padding:3px 7px;vertical-align:top;}
hr{border:0;border-top:1px dashed #c9cfd6;margin:14px 0;}
code{background:#f3f6fa;border-radius:3px;padding:0 4px;font-family:inherit;}
.prof{background:#e8f1fb;border-radius:3px;padding:0 2px;}
.mine{background:#fff3e2;border-radius:3px;padding:0 2px;}
.warn{background:#ffc4e3;border-radius:3px;padding:0 2px;}
h2:last-of-type{color:#7a1550;border-color:#e0559c;}
"""
html = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>{body}</body></html>"""
out.write_text(html, encoding="utf-8")
