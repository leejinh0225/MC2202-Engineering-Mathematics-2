"""Shared slide reading format and lecture template for the complex-analysis notes."""
from html import escape
from pathlib import Path
import re

from complex_content import C, M, paths

SITE = Path(__file__).resolve().parents[1] / "site"


def read_slides(files, page_count):
    slides = {}
    for path in files:
        data = path.read_text(encoding='utf-8')
        for block in re.split(r'^@@ ', data, flags=re.M)[1:]:
            heading, *lines = block.strip().splitlines()
            number, title = heading.split(' | ', 1)
            n = int(number)
            if n in slides:
                raise ValueError(f'Duplicate slide {n}')
            modes = {}
            review = ''
            for line in lines:
                if line.startswith('! '):
                    review = line[2:]
                elif line.startswith(('= ', '~ ')):
                    mode = line[0]
                    modes[mode] = [escape(line[2:])]
                elif line.startswith('$ '):
                    modes[mode].append(M(line[2:]))
                elif line.strip():
                    modes[mode].append(escape(line))
            standard = C(*modes['='])
            body = standard if n == 1 else paths(standard, C(*modes['~']))
            if review:
                body = (f'<div class="callout source-review" id="source-check-{n:02}">'
                        f'<h3>원본 표기 확인 · PDF {n}쪽</h3><p>{escape(review)}</p></div>') + body
            slides[n] = title, body, review
    if set(slides) != set(range(1, page_count + 1)):
        raise ValueError(f'Expected {page_count} numbered source slides')
    return slides


def link(n, label):
    return f'<a href="#slide-{n:02}">{escape(label)}</a>'


def render_lecture(slug, slides, roles, extras, exam, values, guide, summary_lead, script):
    week = values["LECTURE_NUMBER"]
    template = (SITE / 'templates/lecture-page.template.html').read_text(encoding='utf-8')
    section = re.search(r'        <section class="source-section".*?</section>', template, re.S)
    rendered = []
    for n, (title, body, _) in sorted(slides.items()):
        role = roles[n]
        body += extras.get(n, "")
        subs = {'NN': f'{n:02}', 'SLIDE_ROLE': role, 'SLIDE_HEADING': escape(title),
                'LECTURE_SLUG': slug, 'DESCRIPTIVE_ALT_TEXT': f'{week} 원본 PDF {n}쪽 · '+escape(title),
                'CURRENT_PAGE': str(n), 'PAGE_COUNT': str(len(slides)), 'TRANSCRIPT_TIME_OR_SLIDE_ROLE': '원본 PDF · 한국어 해설과 풀이는 편집자 작성',
                'SLIDE_EXPLANATION_BLOCKS': body}
        rendered.append(re.sub(r'{{(\w+)}}', lambda m: subs[m[1]], section[0]))
    template = template[:section.start()] + '\n'.join(rendered) + template[section.end():]
    pattern = r'            <div class="exam-card">.*?</p>\s*</div>'
    exam_template = re.search(pattern, template, re.S)[0]
    template = re.sub(pattern, lambda _: '\n'.join(exam_template.replace('{{EXAM_QUESTION}}', q).replace('{{MODEL_ANSWER}}', a).replace('{{KOREAN_ANSWER_EXPLANATION}}', k) for q,a,k in exam), template, count=1, flags=re.S)
    template = re.sub(r'<span class="header-meta">.*?</span>', '<button type="button" class="mode-toggle" id="mode-toggle" aria-pressed="false">뉴비 모드 켜기</button>', template)
    template = re.sub(r'{{([\w_]+)}}', lambda m: values[m[1]], template)
    template = template.replace('MC2103 Dynamics','MC2202 Engineering Mathematics II').replace('| MC2103','| MC2202')
    template = template.replace('이 부분만 읽어도 렉처의 핵심 정의, 개념 관계, 가정과 풀이 흐름을 이해할 수 있도록 작성합니다.', summary_lead)
    template = template.replace('Transcript audit','Source review').replace('<div class="page-shell">',guide+'<div class="page-shell">')
    template = template.replace('</head>', '<link rel="stylesheet" href="assets/vendor/katex/katex.min.css"><link rel="stylesheet" href="assets/css/math-note.css?v=transforms-1"><link rel="stylesheet" href="assets/css/transforms.css"><script src="assets/js/mode-init.js"></script></head>')
    template = template.replace('</body>',f'<script src="assets/js/math-note.js" defer></script><script src="assets/js/{script}" defer></script></body>')
    template = re.sub(r'<!--.*?-->', '', template, flags=re.S)
    if '{{' in template:
        raise ValueError('Unresolved lecture template placeholder')
    (SITE / f'{slug}.html').write_text('\n'.join(line.rstrip() for line in template.splitlines())+'\n', encoding='utf-8')
