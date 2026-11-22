"""Build the Week 11–12 lecture from the shared template and per-slide readings."""
from html import escape
from pathlib import Path
import re

from complex_content import C, M, paths, table

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'
SLUG = 'complex-integration-series'
PDF = 'Week 11 - 12 (1).pdf'
TITLE = 'Complex integration & Taylor and Laurent series'
CONTENT = ('contours', 'cauchy', 'series', 'laurent')


def read_slides():
    slides = {}
    for topic in CONTENT:
        data = (ROOT / 'scripts' / f'integration_{topic}.txt').read_text(encoding='utf-8')
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
    if set(slides) != set(range(1, 59)):
        raise ValueError('Expected 58 numbered source slides')
    return slides


def link(n, label):
    return f'<a href="#slide-{n:02}">{escape(label)}</a>'


def summary():
    standard = [
        C('경로를 먼저 읽고 적분 방법을 고릅니다',
          M(r'\int_C f(z)\,dz=\int_a^b f(z(t))z^\prime(t)dt,\qquad F^\prime=f\ \Rightarrow\ \int_A^B f\,dz=F(B)-F(A)'),
          '특정 호·선분을 따라가면 매개화합니다. 영역 전체에 원시함수가 있으면 같은 양 끝점을 잇는 모든 경로의 값이 같습니다. 경로와 내부에서 함수가 해석적이면 단순폐곡선 적분은 0입니다.'),
        C('닫힌 경로에서는 특이점의 위치와 방향부터 봅니다',
          M(r'\oint_C\frac{f(z)}{(z-a)^{n+1}}dz=\frac{2\pi i}{n!}f^{(n)}(a)'),
          '반시계 단순폐곡선이 a를 한 번 감싸고 분자 f가 경계와 내부에서 해석적일 때입니다. 밖이면 분모도 내부에서 0이 되지 않아 적분이 0입니다. 경로 위의 특이점에는 이 공식을 적용할 수 없습니다.'),
        C('수렴 범위와 계수를 함께 구합니다',
          M(r'\sum_{n=0}^\infty q^n=(1-q)^{-1}\ (|q|<1),\qquad f(z)=\sum_{n=0}^\infty\frac{f^{(n)}(a)}{n!}(z-a)^n'),
          '항의 비나 근의 극한이 1보다 작으면 절대수렴합니다. 계수 비의 극한이 L이면 반경은 1/L이며 경계는 개별 검사합니다. 테일러 전개는 중심에서 해석적인 함수의 원판 전개입니다.'),
        C('고립특이점은 뚫린 원판의 Laurent series(로랑 급수)로 분류합니다',
          '음의 차수 항이 없으면 제거 가능, 유한하게 남고 최저차가 −m이면 m차 극, 무한히 남으면 본질적 특이점입니다. 같은 중심에서도 특이점까지의 거리를 넘으면 다른 전개가 필요합니다.')]
    newbie = [
        C('길을 따라 더하려면 위치와 이동량을 모두 알아야 합니다',
          '선분을 A에서 B로 가면 z=A+(B−A)t로 놓고 t를 0에서 1까지 보냅니다. 원에서는 중심에 반지름×eⁱᵗ를 더합니다. 위치를 f에 대입한 뒤 이동량 dz=z′(t)dt를 곱하면 평소의 실수 구간 적분이 됩니다. 원시함수가 있으면 끝값에서 시작값을 빼도 됩니다.'),
        C('원을 그린 뒤 분모가 0인 점을 찍습니다',
          '코시 공식에서는 원 안에 들어간 점이 기여합니다. 분모가 z−a면 분자에 a를 넣고 2πi를 곱합니다. 분모가 세제곱이면 분자를 두 번 미분하고 2!로 나눕니다. 원이 시계방향이면 부호가 반대입니다. 점이 경계에 걸리면 이 절차를 멈춥니다.'),
        C('길이가 줄어드는 공비를 만듭니다',
          '거듭제곱을 더하려면 매번 곱하는 수 q의 길이가 1보다 작은지 봅니다. 1/(1−q)=1+q+q²+…을 쓰고 난 뒤에는 q에 넣은 실제 식으로 조건도 바꿉니다. |z|가 클 때는 1/z가 작아진다는 사실이 바깥쪽 전개의 출발점입니다.'),
        C('중심에 대입할 수 있는지 보고 다음 계산을 고릅니다',
          '중심에서 해석적이면 함수값과 미분값을 차례로 맞춰 테일러 계수를 얻습니다. 중심에 구멍이 있으면 로랑 급수를 펴서 분모에 남은 거듭제곱을 셉니다. sin z/z는 남지 않아 1로 메울 수 있고, z²exp(1/z)는 끝없이 남습니다.')]
    return paths(''.join(standard), ''.join(newbie))


GLOSSARY = [
    ('Parametrization(매개화)', '실수 t를 경로 위의 복소수 z(t)에 대응시키는 식.'),
    ('Contour integral(경로적분)', '함숫값에 방향을 가진 이동분 dz를 곱해 경로를 따라 더한 값.'),
    ('Positive orientation(양의 방향)', '단순폐곡선에서는 내부를 왼쪽에 두고 반시계로 진행하는 방향.'),
    ('Simply connected domain(단일연결 영역)', '영역 안에서 모든 닫힌 고리를 한 점으로 수축할 수 있는 영역.'),
    ('Antiderivative(원시함수)', '미분하면 피적분함수가 되는 함수. 전 영역에 존재하면 적분은 경로 독립적입니다.'),
    ('Absolute convergence(절대수렴)', '각 항의 크기를 더한 실수 급수가 수렴하는 성질.'),
    ('Radius of convergence(수렴반경)', '거듭제곱급수가 절대수렴하는 중심 원판의 반지름.'),
    ('Taylor / Maclaurin series(테일러 / 맥클로린 급수)', '중심의 도함수로 계수를 정하는 급수. 중심이 0이면 맥클로린 급수입니다.'),
    ('Laurent series(로랑 급수)', '환형 영역에서 정수 지수 전체를 허용하는 전개.'),
    ('Principal part(주요부)', '중심에 대한 음의 차수 항들을 모은 부분.'),
    ('Pole(극) / zero(영점)', '극에서는 크기가 무한대로 갑니다. 영점에서는 해석함수의 값이 0입니다.'),
    ('Essential singularity(본질적 특이점)', '중심의 고립특이점 중 주요부에 음의 차수 항이 무한히 많은 경우.'),
]


def build():
    slides = read_slides()
    template = (SITE / 'templates/lecture-page.template.html').read_text(encoding='utf-8')
    section = re.search(r'        <section class="source-section".*?</section>', template, re.S)
    rendered = []
    for n, (title, body, _) in sorted(slides.items()):
        if n == 17:
            body += C('두 원에서 특이점의 위치 비교',
                      '<div class="transform-demo"><label for="contour-choice">적분 경로 <select id="contour-choice"><option value="origin">|z| = 2</option><option value="shifted">|z − i| = 1</option></select></label>'
                      '<canvas id="contour-plot" width="840" height="520" role="img" aria-describedby="contour-result" aria-label="원과 두 특이점의 상대 위치">원점 중심인 원은 두 점을, i 중심인 원은 위쪽 점만 감쌉니다.</canvas>'
                      '<p aria-live="polite" id="contour-result">|z| = 2 · 두 점 모두 내부 · 적분값 4πi</p></div>')
        role = ('표지' if n == 1 else '원본 빈 풀이란 · 편집자 검산' if n == 26 else
                '연습문제 풀이' if 24 <= n <= 27 or n >= 53 else '개념·유도·예제')
        subs = {'NN': f'{n:02}', 'SLIDE_ROLE': role, 'SLIDE_HEADING': escape(title),
                'LECTURE_SLUG': SLUG, 'DESCRIPTIVE_ALT_TEXT': f'Week 11–12 원본 PDF {n}쪽 · '+escape(title),
                'CURRENT_PAGE': str(n), 'PAGE_COUNT': '58', 'TRANSCRIPT_TIME_OR_SLIDE_ROLE': '원본 PDF · 한국어 해설과 풀이는 편집자 작성',
                'SLIDE_EXPLANATION_BLOCKS': body}
        rendered.append(re.sub(r'{{(\w+)}}', lambda m: subs[m[1]], section[0]))
    template = template[:section.start()] + '\n'.join(rendered) + template[section.end():]
    exam = [
        ('When can a contour integral be computed from its endpoints?', 'If the integrand has an antiderivative on the domain, the integral equals the change in the antiderivative between the endpoints.', '정의역에서 원시함수를 찾으면 진행 방향을 확인하고 끝값에서 시작값을 뺍니다.'),
        ('Which derivative occurs for a fourth power in the denominator?', 'For a positively oriented simple closed contour enclosing the point, the third derivative appears, multiplied by two pi i and divided by three factorial, provided the numerator is analytic on and inside the contour.', '분모 차수에서 1을 빼면 도함수의 차수입니다.'),
        ('Why specify an annulus for a Laurent expansion?', 'A function can have different Laurent expansions about the same center on different annuli. Each expansion is unique on its own annulus.', '중심과 함께 수렴하는 환형 영역을 답에 씁니다.')]
    pattern = r'            <div class="exam-card">.*?</p>\s*</div>'
    exam_template = re.search(pattern, template, re.S)[0]
    template = re.sub(pattern, lambda _: '\n'.join(exam_template.replace('{{EXAM_QUESTION}}', q).replace('{{MODEL_ANSWER}}', a).replace('{{KOREAN_ANSWER_EXPLANATION}}', k) for q,a,k in exam), template, count=1, flags=re.S)
    groups = [(2,'복소수값의 적분'),(7,'경로를 식으로 바꾸기'),(13,'닫힌 경로와 특이점'),(20,'코시 적분공식'),
              (24,'경로 연습 1–3'),(28,'수열·급수의 수렴'),(36,'거듭제곱급수와 반경'),(42,'테일러·맥클로린 급수'),
              (46,'로랑 급수와 특이점'),(53,'급수 연습 1–7')]
    toc = [('overview','개요'),('concept-map','개념 지도'),('concept-summary','핵심 개념 요약')] + [
        (f'slide-{n:02}', label) for n,label in groups] + [('exam-english','시험 영어'),('glossary','용어집'),('asr-log','원본 대조 기록'),('sources','출처')]
    guide = ('<div class="mode-guide"><strong id="mode-status">기본 모드 · 밝은 화면</strong>'
             '<p>뉴비 모드에서는 각 경로와 공식을 선택하는 이유부터 계산합니다.</p><p>'
             '<a href="complex-numbers-functions.html">이전 단원 · 복소수와 복소함수</a> · ' +
             link(24,'경로적분 연습문제')+' · '+link(53,'수열·급수 연습문제')+
             '</p><noscript>기본·뉴비 본문을 함께 표시합니다.</noscript></div>')
    audit = C('원본과 대조한 표기', '<p>'+' · '.join(f'<a href="#source-check-{n:02}">{n}쪽</a>' for n, (_,_,review) in slides.items() if review)+'</p>',
              '각 링크는 해당 슬라이드의 수식 바로 아래에 있는 공통 검토 카드로 이동합니다. 26쪽은 원본의 빈 풀이란이며, 두 경로를 직접 적분한 검산을 덧붙였습니다.')
    sources = C('강의자료와 수학 참고문헌',
                '<p>Arshad Afzal, Complex Integration &amp; Taylor and Laurent Series, 58쪽. 주차는 제공 파일명에 따랐습니다. 한국어 설명과 예제의 중간 계산은 편집자 작성입니다. <a href="materials/'+PDF+'">원본 PDF</a></p>',
                '<p>코시 적분공식의 경로 조건과 급수의 수렴 영역은 Jeremy Orloff의 MIT 18.04 강의노트와 대조했습니다. <a href="https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/resources/mit18_04s18_topic4/">Cauchy’s integral formula</a> · <a href="https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/resources/mit18_04s18_topic7/">Taylor and Laurent series</a></p>')
    values = {
        'LECTURE_NUMBER':'Week 11–12', 'LECTURE_TITLE':escape(TITLE), 'WEEK':'공업수학 II', 'PAGE_COUNT':'58',
        'ONE_SENTENCE_DESCRIPTION':'복소적분과 테일러·로랑 급수. 원본 58쪽과 경로적분·수열·급수 연습문제 10개의 기본·뉴비 풀이.',
        'LECTURE_PROMISE':'복소평면에서 어느 길을 따라 적분할지, 어느 영역에서 급수를 펼칠지 배웁니다. 원본의 예제와 연습문제 10개를 두 모드에서 단계별로 풉니다.',
        'DATE_OR_날짜_미기재':'미기재','VIDEO_SET':'PDF 기반 해설','ALL_CONTENTS_AND_PROBLEM_SOLVING_BUTTONS':'',
        'ORIGINAL_PDF_URL':'materials/'+PDF,'LECTURE_NOTE_FILENAME':PDF,
        'CORE_RELATIONSHIP_HEADLINE':'경계에서의 적분이 중심의 도함수와 급수 계수를 정합니다.',
        'CORE_RELATIONSHIP_EXPLANATION':'경로적분에서는 경로의 방향과 특이점의 위치를 먼저 봅니다. 거듭제곱급수에서는 중심과 가장 가까운 특이점까지의 거리가 전개 가능한 범위를 결정합니다.',
        'CONCEPT_MAP_HEADLINE':'경로를 따라 적분한 뒤 중심 주위의 급수로 펼칩니다.',
        'CONCEPT_MAP_BLOCKS':'<div class="grid-2">'+C('2–27쪽 · 경로와 적분',link(7,'매개화')+' → '+link(13,'해석성과 경로 변형')+' → '+link(20,'코시 적분공식')+' → '+link(24,'경로 연습'))+C('28–58쪽 · 급수와 특이점',link(32,'수렴 판정')+' → '+link(42,'테일러 계수')+' → '+link(46,'로랑 전개')+' → '+link(53,'급수 연습'))+'</div>',
        'STANDALONE_CONCEPT_SUMMARY':summary(),'DISTINCT_SUMMARY_VIDEO_SECTION_IF_NEEDED':'',
        'EXAM_SECTION_TITLE':'경로와 수렴 조건을 설명하는 영어 표현','BILINGUAL_GLOSSARY_TABLE':table(['English(한국어)','뜻과 사용'],GLOSSARY),
        'AUDIT_SECTION_TITLE':'원본 대조와 풀이 보강','ASR_CORRECTION_TABLE':audit,'SOURCE_LIST_AND_PROVENANCE_NOTE':sources,
        'TABLE_OF_CONTENTS_LINKS':''.join(f'<li><a href="#{anchor}">{label}</a></li>' for anchor,label in toc)}
    template = re.sub(r'<span class="header-meta">.*?</span>', '<button type="button" class="mode-toggle" id="mode-toggle" aria-pressed="false">뉴비 모드 켜기</button>', template)
    template = re.sub(r'{{([\w_]+)}}', lambda m: values[m[1]], template)
    template = template.replace('MC2103 Dynamics','MC2202 Engineering Mathematics II').replace('| MC2103','| MC2202')
    template = template.replace('이 부분만 읽어도 렉처의 핵심 정의, 개념 관계, 가정과 풀이 흐름을 이해할 수 있도록 작성합니다.', '적분에서는 경로의 방향과 내부 점을, 급수에서는 중심과 수렴 영역을 먼저 확인합니다.')
    template = template.replace('Transcript audit','Source review').replace('<div class="page-shell">',guide+'<div class="page-shell">')
    template = template.replace('</head>', '<link rel="stylesheet" href="assets/vendor/katex/katex.min.css"><link rel="stylesheet" href="assets/css/math-note.css?v=transforms-1"><link rel="stylesheet" href="assets/css/transforms.css"><script src="assets/js/mode-init.js"></script></head>')
    template = template.replace('</body>','<script src="assets/js/math-note.js" defer></script><script src="assets/js/complex-contour.js" defer></script></body>')
    template = re.sub(r'<!--.*?-->', '', template, flags=re.S)
    if '{{' in template:
        raise ValueError('Unresolved lecture template placeholder')
    (SITE / f'{SLUG}.html').write_text('\n'.join(line.rstrip() for line in template.splitlines())+'\n', encoding='utf-8')


if __name__ == '__main__':
    build()
