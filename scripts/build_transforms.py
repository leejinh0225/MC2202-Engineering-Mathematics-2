"""Render the new lecture with the established Dynamics-derived template."""
from pathlib import Path
import re
from transforms_content import PAGES, AUDITS, C, M, table, paths

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT/'site'
FILENAME = 'fourier-integrals-transforms.html'
TITLE = 'Fourier integrals &amp; transforms'

def summary():
    standard = [
        C('급수에서 변환까지 같은 질문을 확장합니다.', 'Fourier series(푸리에 급수)는 정수배 주파수의 파동을 더해 주기함수를 표현합니다. 주기 2L을 무한히 늘리면 주파수 간격 Δω=π/L이 0으로 가고, 성분 밀도를 적분하는 Fourier integral(푸리에 적분)로 이어집니다. 연속점에서는 원래 값, 적절한 점프점에서는 좌우 극한의 평균을 복원합니다.', M(r"f_*(x)=\int_0^\infty[A(\omega)\cos(\omega x)+B(\omega)\sin(\omega x)]\,d\omega")),
        C('어떤 변환을 사용할지 먼저 결정합니다.', '반구간 x&gt;0의 짝연장에는 cosine transform(코사인 변환), 홀연장에는 sine transform(사인 변환)을 사용합니다. 전체 실수 구간의 복소 변환은 사인·코사인을 동시에 담습니다. 규약과 적분구간을 정한 뒤 대칭, 미분, 이동, 스케일 성질을 적용합니다.', M(r"\begin{aligned}C[f]&=\sqrt{\frac2\pi}\int_0^\infty f(x)\cos(\omega x)\,dx,\quad S[f]=\sqrt{\frac2\pi}\int_0^\infty f(x)\sin(\omega x)\,dx,\\F(\omega)&=\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)e^{-i\omega x}\,dx.\end{aligned}")),
        C('정의에서 유도한 성질로 적분과 방정식을 단순화합니다.', M(r"\mathcal F[f']=i\omega F,\qquad\mathcal F[f(t-t_0)]=e^{-i\omega t_0}F,\qquad\mathcal F[f*g]=\sqrt{2\pi}FG"), '도함수 공식에는 경계항 소멸과 정칙성, 역변환에는 수렴 조건이 필요합니다. 원본에서 정의하지 않은 절댓값·i·주값을 임의로 추가하지 않습니다. 특히 p.11은 분자에 ω가 없는 사인 적분, p.36은 일반 역변환의 성립 조건을 따로 검토합니다.'),
        C('표본으로 옮기면 DFT, 효율적으로 계산하면 FFT입니다.', M(r"X_n=\sum_{k=0}^{N-1}f_ke^{-2\pi ink/N},\quad c_n=X_n/N,\quad f_k=\frac1N\sum_{n=0}^{N-1}X_ne^{2\pi ink/N}"), '이산 직교성으로 계수를 구하며 FFT는 같은 X를 빠르게 계산합니다. 실제 분석에서는 표본 간격으로 Hz 축을 정하고, 원시 DFT 크기와 원래 파동의 진폭을 구분합니다. 표본 수만으로 연속함수 전체를 유일하게 알아낼 수는 없습니다.')
    ]
    beginner = [
        C('1 · 왜 새 단원이 필요한가요?', '한 번 충격을 받고 끝나는 신호는 반복되는 한 주기가 없습니다. 그래도 여러 빠르기의 파동을 섞어 표현하고 싶습니다. 같은 펄스의 복사본을 아주 멀리 떨어뜨리면 가운데 하나만 남습니다. 그때 사용할 수 있는 주파수는 더 촘촘해지고, 번호를 붙여 더하던 급수가 연속적인 integration(적분)으로 바뀝니다.'),
        C('2 · 변환과 역변환은 성분표 만들기와 다시 조립하기입니다.', 'f(x)는 위치나 시간에 따른 신호, F(ω)는 파동의 빠르기별 성분표입니다. 정변환은 f에 비교 파동을 곱해 x 전체를 더합니다. 역변환은 성분표 F에 파동을 곱해 ω 전체를 더합니다. 적분을 끝낸 뒤 어느 변수가 남는지 확인하면 두 과정을 구별할 수 있습니다.', M(r"f(x)\ \xrightarrow{\ \mathcal F\ }\ F(\omega)\ \xrightarrow{\ \mathcal F^{-1}\ }\ f_*(x)"), '갑자기 값이 뛰는 위치에서는 복원값 f*가 두 옆의 평균입니다. 예를 들어 0과 1 사이의 점프에서는 1/2이 됩니다.'),
        C('3 · 계산은 대칭과 익숙한 식을 이용해 줄입니다.', '좌우가 같은 even function(짝함수)은 사인 쪽이 상쇄되어 코사인 적분만 남습니다. 원래 함수를 미분한 모양이면 변환에 iω를 곱합니다. 시간에 따라 늦어진 모양이면 e⁻ⁱωt₀를 곱합니다. 아무 공식이나 먼저 고르지 말고 “어떤 모양이어서 이 성질을 쓸 수 있나”를 확인합니다.', M(r"e^{-ax}\ (x>0)\quad\longrightarrow\quad C[f]=\sqrt{\frac2\pi}\frac{a}{a^2+\omega^2}"), '이 적분 하나를 구해 두면 여러 역적분 문제에 재사용할 수 있습니다. 다만 분자의 ω 하나나 지수의 i 하나가 바뀌면 다른 문제이므로 원문 조건을 끝까지 따라갑니다.'),
        C('4 · 컴퓨터에서 하는 일도 같은 원리입니다.', '숫자 N개에 기준 파동을 곱해 더하면 DFT입니다. 같은 번호는 남고 다른 번호는 상쇄되므로 주파수별 성분을 고를 수 있습니다. FFT는 숫자 목록을 짝수 번호와 홀수 번호로 나눠 그 합을 효율적으로 계산합니다.', M(r"X_n=\sum_{k=0}^{N-1}f_ke^{-2\pi ink/N},\qquad c_n=X_n/N"), 'X는 나누기 전의 값, c는 N으로 나눈 계수입니다. 높이 1의 사인이라도 N=8이면 원시 DFT 막대 높이가 4일 수 있습니다. 이 차이까지 이해해야 그래프를 원래 신호의 크기로 해석할 수 있습니다.')
    ]
    return paths(''.join(standard), ''.join(beginner))

def demos(page):
    if page == 7:
        return C('직접 비교 · 복원에 포함할 최고 주파수', '<div class="transform-demo"><label for="integral-cutoff">주파수 상한 R <output id="integral-cutoff-value" for="integral-cutoff">16</output></label><input id="integral-cutoff" type="range" min="4" max="64" step="4" value="16"><canvas id="integral-demo" width="960" height="400" role="img" aria-label="원본 직사각 펄스와 주파수 상한에 따른 푸리에 적분 근사">점선은 |x|&lt;1에서 높이 1인 펄스, 실선은 유한 주파수 복원입니다.</canvas><p id="integral-demo-caption" aria-live="polite">점선: 원본 펄스 · 실선: 주파수 0부터 R까지의 복원. 경계의 목표값은 1/2입니다.</p><noscript>위 원본 슬라이드에서 상한 8, 16, 32의 비교를 확인할 수 있습니다.</noscript></div>')
    if page == 31:
        return C('직접 비교 · 두 사인의 진폭과 DFT 막대', '<div class="transform-demo"><label for="dft-amplitude-one">sin x의 진폭 <output id="dft-one-value">1.0</output></label><input id="dft-amplitude-one" type="range" min="0" max="2" step="0.1" value="1"><label for="dft-amplitude-three">sin 3x의 진폭 <output id="dft-three-value">1.0</output></label><input id="dft-amplitude-three" type="range" min="0" max="2" step="0.1" value="1"><canvas id="dft-demo" width="960" height="500" role="img" aria-label="두 사인의 합과 8개 표본, 양음 주파수의 DFT 크기">진폭이 각각 1일 때 ±1, ±3 주파수의 원시 DFT 크기는 4입니다.</canvas><p id="dft-demo-caption" aria-live="polite">N=8 · 원시 DFT 크기 |X|를 표시합니다. 실제 진폭은 양의 해당 주파수에서 2|X|/8입니다.</p><noscript>위 원본 슬라이드는 두 진폭이 모두 1인 경우입니다.</noscript></div>')
    return ''

def build():
    template=(SITE/'templates/lecture-page.template.html').read_text(encoding='utf-8')
    match=re.search(r'        <section class="source-section".*?</section>',template,re.S)
    sections=[]
    for i,page in sorted(PAGES.items()):
        body=paths(page['standard'],page['beginner']) if page['beginner'] else page['standard']
        body=page.get('audit','')+body+demos(i)
        values={'NN':f'{i:02}','SLIDE_ROLE':page['role'],'SLIDE_HEADING':page['title'],'LECTURE_SLUG':'transforms','DESCRIPTIVE_ALT_TEXT':f"Fourier Integrals and Transforms 원본 PDF {i}쪽: {page['title']}",'CURRENT_PAGE':str(i),'PAGE_COUNT':'36','TRANSCRIPT_TIME_OR_SLIDE_ROLE':'원본 PDF · 해설·완성 풀이는 편집자 작성','SLIDE_EXPLANATION_BLOCKS':body}
        section=match.group(0)
        for key,value in values.items():
            section=section.replace('{{'+key+'}}',value)
        sections.append(section)
    template=template[:match.start()]+'\n'.join(sections)+template[match.end():]

    exam_items=[
        ('How does a Fourier series lead to a Fourier integral?','As the period grows, the frequency spacing tends to zero. The weighted sum over discrete frequencies becomes an integral over a continuous frequency variable.','주기 증가 → 주파수 간격 감소 → 성분 밀도의 적분이라는 논리입니다.'),
        ('State the transform convention used here.','The forward transform uses exp(−iωx), and both the forward and inverse transforms have the factor 1/√(2π).','정변환 지수의 음수와 대칭 정규화 상수를 함께 명시합니다.'),
        ('What is the Fourier transform of a derivative?','Under suitable regularity and vanishing boundary conditions, the transform of f′ is iωF, and the transform of f″ is −ω²F.','적용 조건과 한 번·두 번 미분의 부호를 연결해 답합니다.'),
        ('State the convolution theorem.','With the unnormalized convolution integral and the symmetric Fourier convention, the transform of f*g is √(2π)FG.','합성곱 정의에도 정규화 규약이 있으므로 여기의 정의를 함께 말합니다.'),
        ('Explain the difference between the DFT and the FFT.','The DFT is the discrete transform. The FFT is an efficient algorithm for computing the same transform.','변환의 정의와 계산 알고리즘을 구분합니다.'),
        ('Why is the value at a jump replaced by an average?','Under the Fourier inversion conditions, the reconstructed value at a jump is the average of the left and right limits.','원래 점 하나에 정한 값과 복원 정리가 주는 값을 구분합니다.'),
        ('Can e^(−aω)/ω be inverted as an ordinary full-line Fourier transform?','As stated, the ordinary inversion is not valid. The origin is singular, and for real nonzero a one frequency tail grows exponentially. Additional assumptions are required.','p.36 원문에 대한 조건 검토입니다. 사인 변환이나 |ω|를 임의로 추가하여 정답으로 단정하지 않습니다.')]
    exam=''.join('<div class="exam-card"><h3>'+q+'</h3><div class="answer"><span class="answer__label">Model answer</span>'+a+'</div><p>'+k+'</p></div>' for q,a,k in exam_items)
    terms=[
        ('Fourier integral(푸리에 적분)','비주기함수를 연속 주파수 성분의 적분으로 복원하는 표현.'),
        ('Fourier transform / inverse transform(푸리에 변환 / 역변환)','원래 변수의 함수에서 주파수 성분표로 / 성분표에서 함수로 바꾸는 연산.'),
        ('Angular frequency / frequency(각주파수 / 주파수)','ω는 rad/s, ν는 Hz. ω=2πν.'),
        ('Absolutely integrable(절대적분 가능)','함수 절댓값의 전체 적분이 유한한 성질.'),
        ('Improper integral(이상적분)','무한 구간이나 특이점을 유한 구간 적분의 극한으로 정의한 적분.'),
        ('Cauchy principal value(코시 주값)','특이점 양쪽 또는 양 무한대의 대칭 극한을 지정하는 적분 방식. 보통의 이상적분과 구분.'),
        ('Cosine / sine transform(코사인 / 사인 변환)','반구간의 함수를 각각 짝연장·홀연장과 연결해 표현하는 변환.'),
        ('Normalization(정규화)','변환과 역변환의 상수 배율을 정하는 규약.'),
        ('Spectrum / phase(스펙트럼 / 위상)','주파수 성분의 분포 / 복소 성분의 회전각 정보.'),
        ('Gibbs phenomenon(깁스 현상)','점프 주변에서 유한 주파수 복원에 나타나는 초과 진동.'),
        ('Linearity(선형성)','입력의 상수배와 덧셈이 출력에도 그대로 적용되는 성질.'),
        ('Modulation / time shift(변조 / 시간 이동)','복소 회전 파동의 곱으로 주파수 이동 / 원래 함수의 위치 이동.'),
        ('Scaling(스케일 변환)','함수의 입력변수에 상수를 곱해 폭을 바꾸는 연산.'),
        ('Convolution(합성곱)','한 함수를 뒤집고 이동하여 다른 함수와 곱한 뒤 전체를 더하는 연산.'),
        ('Sampling / sample(표본화 / 표본)','정해진 위치에서 값을 측정하는 과정 / 그 값.'),
        ('DFT / FFT(이산 푸리에 변환 / 고속 푸리에 변환)','유한 표본의 주파수 변환 / 같은 변환을 효율적으로 계산하는 알고리즘.'),
        ('Root of unity(1의 거듭제곱근)','어떤 정수 거듭제곱을 하면 1이 되는 복소수.'),
        ('Butterfly operation(나비 연산)','작은 DFT 결과를 공통 회전 인자로 결합해 두 출력을 얻는 연산.'),
        ('Aliasing(에일리어싱)','서로 다른 연속 주파수가 같은 표본값으로 나타나 구별되지 않는 현상.'),
        ('Harmonic / dominant frequency(고조파 / 우세 주파수)','기본 주파수의 정수배 성분 / 측정 신호에서 크게 나타나는 성분.'),
        ('Natural frequency / resonance(고유진동수 / 공진)','시스템 고유의 진동 특성 / 가진과 시스템 특성이 만나 응답이 커지는 현상.'),
        ('Find / evaluate / derive / verify(구하라 / 계산하라 / 유도하라 / 검증하라)','대상과 조건 제시 / 적분 등의 값 산출 / 근거부터 식 전개 / 독립 계산이나 대입으로 확인.')]
    audit=C('원본과 해설의 경계', '원본 이미지 36쪽을 순서대로 보존했습니다. 표기 차이는 원본 그림과 정의·직접 계산을 대조하여 아래에 기록합니다. 설명·유도·완성 풀이와 추가 예제는 편집자 작성입니다. 강의 영상·스크립트가 없어 ASR 검토는 해당하지 않습니다. 원본 문제의 출제 의도는 추정하지 않습니다.')
    audit+=table(['PDF 쪽','원본 확인 및 처리'],[(str(n),a) for n,a in sorted(AUDITS)])
    audit+=C('정상 표기와 빈 페이지도 확인했습니다.', 'p.3의 절댓값 조건, p.11의 분자에 ω가 없는 적분, p.18의 최종 변환 분모, p.28·30의 복소수 최종 답, p.34의 xe⁻ˣ², p.36의 e⁻ᵃω/ω를 이미지로 대조했습니다. p.12와 p.35는 빈 풀이 공간으로 보존했습니다.')
    sources=C('원본과 참고 자료', '<a href="materials/Fourier%20Integrals%20and%20Transforms.pdf" download="Fourier Integrals and Transforms.pdf">Fourier Integrals and Transforms.pdf</a> · Arshad Afzal · 36쪽 · 강의 날짜·주차 미기재.', '강의 자료가 제시한 개념·예제·문제를 바탕으로 작성했으며, 편집자 해설과 추가 예시는 본문에서 구분했습니다. 원본 PDF와 슬라이드 이미지는 교정하지 않았습니다.', '정의·조건 대조: <a href="https://dlmf.nist.gov/1.14">NIST DLMF §1.14 · Integral transforms</a>. DLMF의 정변환 지수 부호는 이 노트와 반대이며, 합성곱 정의에 넣는 상수도 다르므로 규약을 변환하여 대조했습니다.', '특수함수 정의: <a href="https://dlmf.nist.gov/6.2">NIST DLMF §6.2 · Exponential and sine integrals</a>. p.11의 Ei와 p.7의 Si는 이 정의를 사용하고 적분 결과는 별도로 유도·수치 검산했습니다.', 'DFT 규약·순서 대조: <a href="https://numpy.org/doc/stable/reference/routines.fft.html">NumPy · Discrete Fourier Transform</a>, <a href="https://www.mathworks.com/help/matlab/ref/fft.html">MathWorks · fft</a>. 정변환의 무정규화와 역변환의 1/N 배율을 확인했습니다.')
    toc=[('overview','단원 개요'),('concept-map','개념 지도'),('concept-summary','핵심 개념 요약')]+[(f'slide-{n:02}',f'{n:02} · '+v['title']) for n,v in sorted(PAGES.items())]+[('exam-english','시험 영어'),('glossary','핵심 용어'),('asr-log','원본 검토·교정'),('sources','출처')]
    conceptmap='<div class="grid-3">'+C('01 · 연속 주파수로 확장','주기 증가 → 주파수 간격 감소 → Fourier integral(푸리에 적분) → 코사인·사인 변환.')+C('02 · 성질로 계산 단순화','Complex transform(복소 변환) → 미분·이동·스케일 → convolution(합성곱).')+C('03 · 유한한 데이터로 계산','Sampling(표본화) → discrete orthogonality(이산 직교성) → DFT → FFT → 소리·진동 분석.')+'</div>'
    values={'LECTURE_NUMBER':'Fourier integrals &amp; transforms','LECTURE_TITLE':TITLE,'ONE_SENTENCE_DESCRIPTION':'공업수학 II 푸리에 적분과 변환: 원본 36쪽, 상세 문제 풀이, 기본·뉴비 해설과 DFT·FFT 계산','WEEK':'공업수학 II','LECTURE_PROMISE':'급수가 적분으로 바뀌는 이유부터 복소 변환과 FFT까지. 원본 36쪽에 맞춘 두 가지 본문 해설과 상세 문제 풀이로 이어 공부합니다.','DATE_OR_날짜_미기재':'미기재','PAGE_COUNT':'36','VIDEO_SET':'PDF 기반 · 강의 영상 없음','ALL_CONTENTS_AND_PROBLEM_SOLVING_BUTTONS':'','ORIGINAL_PDF_URL':'materials/Fourier%20Integrals%20and%20Transforms.pdf','LECTURE_NOTE_FILENAME':'Fourier Integrals and Transforms.pdf','CORE_RELATIONSHIP_HEADLINE':'반복되지 않는 신호도 파동으로 분해하고, 표본으로 계산합니다.','CORE_RELATIONSHIP_EXPLANATION':'Fourier series(푸리에 급수)의 주기를 늘려 적분으로 연결하고, 변환의 성질로 문제를 풉니다. 마지막에는 유한한 표본의 DFT·FFT로 이어집니다. 먼저 이전 단원의 내적·직교성·복소 지수 표현을 복습하면 연결이 자연스럽습니다.','CONCEPT_MAP_HEADLINE':'급수 → 적분 → 변환의 성질 → DFT·FFT','CONCEPT_MAP_BLOCKS':conceptmap,'STANDALONE_CONCEPT_SUMMARY':summary(),'DISTINCT_SUMMARY_VIDEO_SECTION_IF_NEEDED':'','EXAM_SECTION_TITLE':'변환의 원리와 계산을 설명하는 영어 문장','BILINGUAL_GLOSSARY_TABLE':table(['English(한국어)','뜻과 사용'],terms),'AUDIT_SECTION_TITLE':'원본 검토·교정 기록 · 스크립트 없음','ASR_CORRECTION_TABLE':audit,'SOURCE_LIST_AND_PROVENANCE_NOTE':sources,'TABLE_OF_CONTENTS_LINKS':''.join(f'<li><a href="#{key}">{label}</a></li>' for key,label in toc)}
    start=template.index('            <div class="exam-card">',template.index('id="exam-english"'))
    end=template.index('\n          </div>',start)
    template=template[:start]+exam+template[end:]
    template=re.sub(r'<span class="header-meta">.*?</span>','<button type="button" class="mode-toggle" id="mode-toggle" aria-pressed="false">뉴비 모드 켜기</button>',template)
    for key,value in values.items(): template=template.replace('{{'+key+'}}',value)
    template=template.replace('MC2103 Dynamics','MC2202 Engineering Mathematics II').replace('| MC2103','| MC2202')
    template=template.replace('이 부분만 읽어도 렉처의 핵심 정의, 개념 관계, 가정과 풀이 흐름을 이해할 수 있도록 작성합니다.','정의에서 계산으로 이어지는 이유와 적용 조건을 먼저 정리합니다. 아래에서 원본 페이지 순서의 상세 해설과 풀이를 이어 읽을 수 있습니다.')
    template=template.replace('</head>','<link rel="stylesheet" href="assets/vendor/katex/katex.min.css"><link rel="stylesheet" href="assets/css/math-note.css?v=transforms-1"><link rel="stylesheet" href="assets/css/transforms.css"><script src="assets/js/mode-init.js"></script></head>')
    template=template.replace('<div class="page-shell">','<div class="mode-guide"><strong id="mode-status">기본 모드 · 밝은 화면</strong><p>뉴비 모드를 켜면 다크 화면과 함께 본문이 기초부터 풀어 쓴 해설로 바뀝니다. 계산을 시작하는 이유, 중간 과정과 결과의 의미를 연결하며 English(한국어) 용어 표기는 유지합니다.</p><p><a href="fourier-series.html">이전 단원 · Fourier series(푸리에 급수)</a> · 연습문제: <a href="#slide-11">11쪽</a>, <a href="#slide-13">13쪽</a>, <a href="#slide-14">14쪽</a>, <a href="#slide-34">34쪽</a>, <a href="#slide-36">36쪽</a></p><noscript>JavaScript가 꺼져 있어 기본·뉴비 해설을 모두 표시합니다.</noscript></div><div class="page-shell">')
    template=template.replace('</body>','<script src="assets/js/math-note.js" defer></script><script src="assets/js/transforms-demo.js" defer></script></body>')
    template=re.sub(r'<!--.*?-->','',template,flags=re.S)
    template=template.replace('materials/Fourier%20Integrals%20and%20Transforms.pdf','materials/Fourier Integrals and Transforms.pdf')
    if '{{' in template: raise RuntimeError('Unresolved transform template')
    (SITE/FILENAME).write_text('\n'.join(line.rstrip() for line in template.splitlines())+'\n',encoding='utf-8')
    print('Built 36 transform slides with 33 independent reading pairs + summary')

if __name__=='__main__':
    build()
