import os, base, part12, part34
pages = base.pages
total = len(pages)
html = ''.join(p.replace('{PN}', f'{i} / {total}') for i, p in enumerate(pages, 1))
css = open(os.path.join(base.HERE, 'style3.css'), encoding='utf-8').read()
open(os.path.join(base.HERE, 'out.html'), 'w', encoding='utf-8').write(
    f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>4-6주차 확산 마스터 요약본</title><style>{css}</style></head><body>{html}</body></html>')
print(total, 'pages')
