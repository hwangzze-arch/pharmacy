"""녹취록 .md → 인쇄용 HTML (A4 세로). python3 md2html.py <md> <html>
지원: # ## ### 제목, 문단, - 목록, 1. 목록(3칸 들여쓰기 하위 목록), > 인용, **굵게**, `코드`"""
import re, sys, html

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    return re.sub(r'`(.+?)`', r'<code>\1</code>', t)

def convert(md):
    out, para, stack = [], [], []   # stack: [(tag, indent)]
    def flush():
        if para: out.append('<p>' + inline(' '.join(para)) + '</p>'); para.clear()
    def close(to=-1):
        while stack and stack[-1][1] > to:
            out.append(f'</li></{stack.pop()[0]}>')
    for line in md.splitlines():
        m = re.match(r'^(\s*)([-*]|\d+\.)\s+(.*)$', line)
        if m:
            flush()
            ind, tag = len(m.group(1)), ('ul' if m.group(2) in '-*' else 'ol')
            if stack and stack[-1][1] == ind:
                out.append('</li>')
            elif stack and stack[-1][1] > ind:
                close(ind); out.append('</li>')
            if not stack or stack[-1][1] < ind:
                out.append(f'<{tag}>'); stack.append((tag, ind))
            out.append('<li>' + inline(m.group(3)))
            continue
        if not line.strip():
            flush(); continue
        close(); flush()
        if line.startswith('#'):
            n = len(line) - len(line.lstrip('#'))
            out.append(f'<h{n}>{inline(line[n:].strip())}</h{n}>')
        elif line.startswith('>'):
            out.append('<blockquote>' + inline(line[1:].strip()) + '</blockquote>')
        else:
            para.append(line.strip())
    close(); flush()
    return '\n'.join(out)

CSS = '''@page { size: A4; margin: 16mm 15mm 16mm 15mm; }
body { font-family: 'Pretendard', 'Noto Sans CJK KR', sans-serif; font-size: 12.5px; line-height: 1.75; color: #1f2937; }
h1 { font-size: 21px; color: #1e3a6e; border-bottom: 3px solid #1e3a6e; padding-bottom: 6px; margin: 0 0 10px; }
h2 { font-size: 16px; color: #fff; background: #2c4f86; padding: 5px 10px; border-radius: 5px; margin: 22px 0 8px; break-after: avoid; }
h3 { font-size: 13.5px; color: #1e3a6e; border-left: 4px solid #e07b1f; padding-left: 8px; margin: 14px 0 4px; break-after: avoid; }
p { margin: 5px 0; text-align: justify; }
ul, ol { margin: 4px 0; padding-left: 22px; } li { margin: 3px 0; }
blockquote { background: #fff8dc; border-left: 5px solid #f2b705; margin: 8px 0; padding: 6px 12px; border-radius: 4px; }
code { background: #eef2f8; padding: 0 4px; border-radius: 3px; font-size: 11.5px; }
b { color: #111; }'''

if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    body = convert(open(src, encoding='utf-8').read())
    open(dst, 'w', encoding='utf-8').write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>')
