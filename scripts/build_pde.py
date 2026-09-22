"""Build PDE I using the same lecture-page template as the other notes."""
from pathlib import Path
import re
from pde_content import PAGES, C, M, table, paths

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'site'

def summary():
    standard=''.join([
      C('PDE와 데이터를 구별합니다.', 'Partial differential equation(편미분방정식)은 여러 변수의 함수와 편도함수 사이의 관계입니다. Order(차수), linearity(선형성), homogeneity(제차성)를 구분합니다. 줄의 파동 문제는 PDE 외에 양 끝의 boundary conditions(경계조건), 처음 모양 f와 속도 g의 initial conditions(초기조건)가 필요합니다.', M(r"u_{tt}=c^2u_{xx},\quad u(0,t)=u(L,t)=0,\quad u(x,0)=f(x),\quad u_t(x,0)=g(x)")),
      C('고정단이 공간 모드를 고르고, 초기조건이 계수를 고릅니다.', 'Separation of variables(변수분리법) u=FG에서 F″+μF=0, G″+c²μG=0을 얻습니다. 비영 공간해는 μₙ=(nπ/L)², Fₙ=sin(nπx/L)이고 λₙ=cnπ/L입니다. 서로 직교하는 모드를 합쳐 초기데이터를 맞춥니다.', M(r"\begin{aligned}u&=\sum_{n\ge1}(B_n\cos\lambda_nt+B_n^*\sin\lambda_nt)\sin\frac{n\pi x}{L},\\B_n&=\frac2L\int_0^Lf(x)\sin\frac{n\pi x}{L}\,dx,\quad B_n^*=\frac2{L\lambda_n}\int_0^Lg(x)\sin\frac{n\pi x}{L}\,dx.\end{aligned}")),
      C('이동 좌표로 보면 두 진행파와 특성곡선이 보입니다.', 'v=x+ct, w=x−ct로 바꾸면 Uᵥw=0이 되어 u=Φ(v)+Ψ(w)입니다. 초기조건을 맞추면 D’Alembert formula(달랑베르 공식)가 됩니다. 고정단 유한 줄에서는 f,g를 홀수 2L-주기 연장한 f̃,g̃를 사용합니다.', M(r"u=\frac12[\widetilde f(x+ct)+\widetilde f(x-ct)]+\frac1{2c}\int_{x-ct}^{x+ct}\widetilde g(s)\,ds"), 'A uₓₓ+2B uₓᵧ+C uᵧᵧ의 주부분은 Δ=B²−AC의 부호로 쌍곡형(양수), 포물형(0), 타원형(음수)으로 분류합니다. 파동방정식은 쌍곡형이며 x±ct=상수가 두 특성곡선족입니다.')])
    beginner=''.join([
      C('1 · 한 점의 움직임에서 줄 전체의 움직임으로', '높이 u를 알려면 “어디 x에서, 언제 t에?”를 함께 물어야 합니다. t를 고정해 x로 미분하면 줄의 공간 기울기·곡률이고, x를 고정해 t로 미분하면 한 점의 속도·가속도입니다. Partial differential equation(편미분방정식)은 이 변화들을 연결합니다. 처음 모양만으로는 부족하고 처음 속도와 양 끝을 어떻게 잡는지도 알아야 움직임이 결정됩니다.'),
      C('2 · 복잡한 모양을 기본 사인 모양의 합으로 만듭니다.', '양 끝이 0인 공간 모양 중 간단한 후보를 먼저 구합니다. u=F(x)G(t)를 넣고 변수별로 정리하면 서로 다른 변수의 식이 항상 같아야 하므로 같은 상수입니다. 양 끝을 고정하면 줄 안에 반파가 정수 개 들어가는 사인 모양만 남습니다. 이를 normal modes(정상모드)라 합니다.', M(r"\sin\frac{\pi x}{L},\quad\sin\frac{2\pi x}{L},\quad\sin\frac{3\pi x}{L},\ldots"), '이 재료들을 섞어 처음 모양을 만들려면 Fourier coefficients(푸리에 계수)를 구합니다. 처음 속도는 시간 미분을 한 뒤 맞추므로 사인항 계수에 1/λₙ가 추가됩니다. g=0이면 시간 코사인만 남습니다.'),
      C('3 · 같은 답을 “좌우로 이동하는 모양”으로 볼 수도 있습니다.', 'x−ct가 일정하면 오른쪽 진행파를 따라가고 x+ct가 일정하면 왼쪽 진행파를 따라갑니다. 이 좌표로 바꾸면 두 진행파의 합이 해가 됩니다. 처음에 가만히 놓았다면 처음 모양 절반씩을 좌우로 옮겨 더합니다.', M(r"g=0\quad\Rightarrow\quad u=\tfrac12[\widetilde f(x+ct)+\widetilde f(x-ct)]"), '줄 밖의 함수값은 임의로 계산하지 않습니다. 끝점에서 높이가 상쇄되도록 모양을 뒤집어 연결하고 2L마다 반복한 함수가 f̃입니다. 마지막 문제와 조작 그림에서 이 반사와 사인 급수 풀이가 같은 결과를 주는지 확인합니다.'),
      C('4 · 분류 공식은 방향을 찾는 이차방정식과 연결됩니다.', 'A uₓₓ+2B uₓᵧ+C uᵧᵧ에서 A,B,C를 읽습니다. 가운데 계수는 2B라는 점을 주의하십시오. Characteristic curve(특성곡선)의 기울기는 Am²−2Bm+C=0으로 찾습니다. 고등학교 근의 공식 안에 B²−AC가 들어가므로 그 부호로 쌍곡형·포물형·타원형을 구별합니다. 파동방정식의 두 방향이 바로 x±ct=상수입니다.')])
    return paths(standard,beginner)

def demo():
    return C('직접 확인 · 삼각형 줄의 진동과 두 해법 비교', '<div class="transform-demo"><p>편집자 비교 실험 · 위치 ξ=x/L, 시간 τ=ct/L, 높이 u/k로 정규화했습니다(k≠0). 파란 실선은 유한 푸리에 급수, 주황 점선은 홀수 주기 연장을 사용한 D’Alembert 해입니다.</p><label for="wave-time">시간 τ = ct/L <output id="wave-time-value" for="wave-time">0.00</output></label><input id="wave-time" type="range" min="0" max="2" step="0.01" value="0"><label for="wave-terms">포함할 홀수 모드 수 <output id="wave-terms-value" for="wave-terms">8</output></label><input id="wave-terms" type="range" min="1" max="40" step="1" value="8"><canvas id="wave-demo" width="960" height="430" role="img" aria-label="삼각형 초기변위의 유한 푸리에 급수와 달랑베르 해 비교">시간 τ=0에서 높이 1인 삼각형, 0.5에서 수평선, 1에서 뒤집힌 삼각형, 2에서 처음 모양입니다.</canvas><p id="wave-caption" aria-live="polite"></p><noscript>시간 τ=0, 0.5, 1, 2에서의 모양은 각각 삼각형, 수평선, 뒤집힌 삼각형, 처음 삼각형입니다. 수평선 통과 시에도 속도는 0이 아닙니다.</noscript></div>')

def build():
    template=(SITE/'templates/lecture-page.template.html').read_text(encoding='utf-8')
    match=re.search(r'        <section class="source-section".*?</section>',template,re.S)
    sections=[]
    for n,p in sorted(PAGES.items()):
        body=paths(p['standard'],p['beginner']) if p['beginner'] else p['standard']
        if n==21: body+=demo()
        vals={'NN':f'{n:02}','SLIDE_ROLE':p['role'],'SLIDE_HEADING':p['title'],'LECTURE_SLUG':'pde-i','DESCRIPTIVE_ALT_TEXT':f'PDE - I 원본 PDF {n}쪽: '+p['title'],'CURRENT_PAGE':str(n),'PAGE_COUNT':'22','TRANSCRIPT_TIME_OR_SLIDE_ROLE':'원본 PDF · 유도·해설·완성 풀이는 편집자 작성','SLIDE_EXPLANATION_BLOCKS':body}
        s=match.group(0)
        for k,v in vals.items(): s=s.replace('{{'+k+'}}',v)
        sections.append(s)
    template=template[:match.start()]+'\n'.join(sections)+template[match.end():]
    exams=[
      ('What is the difference between the order and linearity of a PDE?', 'The order is the highest derivative order. Linearity requires the unknown function and all its derivatives to enter linearly, with coefficients independent of the unknown.', '차수는 미분 횟수, 선형성은 미지함수·도함수의 결합 방식입니다.'),
      ('Solve u_xx − u = 0 for u(x,y).', 'For each fixed y, solve the ODE in x. The general solution is u(x,y) = A(y)e^x + B(y)e^(−x), where A and B are arbitrary functions compatible with the required regularity.', '다른 변수에 의존하는 임의함수를 남겨야 합니다.'),
      ('Why is the separation expression a constant?', 'One side depends only on x and the other only on t. Equality for independent x and t forces both sides to be the same constant.', '서로 독립인 변수들을 바꿔도 등식이 유지되어야 한다는 근거입니다.'),
      ('How are the coefficients determined by the initial conditions?', 'Expand the initial displacement in a Fourier sine series to obtain B_n. Expand the initial velocity to obtain λ_n B_n*, and divide by λ_n.', '초기속도 계수의 λₙ를 빠뜨리지 않습니다.'),
      ('What modification is needed to apply d’Alembert’s formula to a fixed-end string?', 'Use the odd, 2L-periodic extensions of both initial functions. The antisymmetry at each endpoint enforces the fixed-end boundary conditions.', '초기조건뿐 아니라 끝점 조건을 만족시키기 위한 함수 연장입니다.'),
      ('Classify A u_xx + 2B u_xy + C u_yy = F.', 'Where the second-order principal part is nonzero, the equation is hyperbolic if B²−AC is positive, parabolic if it is zero, and elliptic if it is negative.', '혼합항의 계수가 2B라는 규약을 먼저 확인합니다.'),
      ('Why do even modes vanish for a centered triangular pluck?', 'The initial displacement is symmetric about the midpoint. Even sine modes are antisymmetric about the midpoint, so their coefficient integrals cancel.', '중앙 대칭과 직교 계수 적분의 상쇄로 설명합니다.')]
    exam=''.join('<div class="exam-card"><h3>'+q+'</h3><div class="answer"><span class="answer__label">Model answer</span>'+a+'</div><p>'+k+'</p></div>' for q,a,k in exams)
    start=template.index('            <div class="exam-card">',template.index('id="exam-english"'))
    end=template.index('\n          </div>',start)
    template=template[:start]+exam+template[end:]
    terms=[
      ('Partial derivative(편도함수)','다른 독립변수를 고정한 채 한 변수에 대해 미분한 함수.'),
      ('PDE / ODE(편미분방정식 / 상미분방정식)','여러 독립변수의 함수와 편도함수 / 한 독립변수의 함수와 도함수를 다루는 방정식.'),
      ('Order / linearity(차수 / 선형성)','최고 미분 횟수 / 미지함수·모든 도함수에 대한 선형 결합 성질.'),
      ('Homogeneous / nonhomogeneous(제차 / 비제차)','선형식을 L[u]=r로 쓸 때 외부항 r이 0 / 0이 아닌 경우.'),
      ('Classical / weak solution(고전해 / 약한 해)','필요한 미분이 존재하여 점별로 만족하는 해 / 시험함수로 적분한 관계를 만족하도록 확장한 해. 모서리에서는 구분 필요.'),
      ('Superposition principle(중첩 원리)','제차 선형방정식의 해들의 상수 선형결합도 해라는 성질. 무한합에는 수렴 검토 필요.'),
      ('Boundary / initial conditions(경계조건 / 초기조건)','영역의 경계에서 주는 조건 / 시작 시간에 주는 조건.'),
      ('Separation of variables(변수분리법)','변수별 함수의 곱을 시도하여 PDE를 여러 ODE로 나누는 방법.'),
      ('Eigenvalue / eigenfunction(고유값 / 고유함수)','주어진 연산자·경계조건에서 비영 해를 허용하는 값 / 그 해 함수. 원본의 λₙ와 공간 고유값 μₙ를 구별.'),
      ('Normal mode / node(정상모드 / 마디)','고정된 공간 형태의 독립 진동 / 해당 모드에서 변위가 항상 0인 점.'),
      ('Angular frequency / frequency(각주파수 / 진동수)','시간당 위상 변화 λₙ(rad/s) / 초당 반복 횟수 νₙ(Hz), λₙ=2πνₙ.'),
      ('Spectrum(스펙트럼)','이 고정단 줄에 허용되는 고유 각주파수의 목록.'),
      ('Orthogonality / Fourier coefficient(직교성 / 푸리에 계수)','서로 다른 모드의 곱 적분이 0인 성질 / 전개에서 각 모드에 곱하는 수.'),
      ('Standing / travelling wave(정상파 / 진행파)','마디와 공간 형태가 고정된 파동 / 형태가 공간을 따라 이동하는 파동.'),
      ('Chain rule(연쇄법칙)','합성된 여러 변수의 변화 경로별 미분 기여를 더하는 규칙.'),
      ('Odd periodic extension(홀수 주기 연장)','원래 구간 밖을 부호 반전 대칭과 주기 반복으로 정의하는 방법.'),
      ('Domain of dependence(의존영역)','특정 지점의 해를 결정하는 초기데이터의 범위.'),
      ('Principal part / quasilinear(주부분 / 준선형)','최고차 미분항들 / 최고차 도함수에 대해 선형인 식.'),
      ('Hyperbolic / parabolic / elliptic(쌍곡형 / 포물형 / 타원형)','2변수 2차 PDE에서 Δ=B²−AC가 각각 양수 / 0 / 음수인 유형.'),
      ('Characteristic curve(특성곡선)','최고차 미분 구조가 특정 방향으로 퇴화하는 곡선. 파동에서는 정보의 전파 방향과 연결.'),
      ('Find / derive / verify(구하라 / 유도하라 / 검증하라)','해와 조건을 제시 / 앞선 원리에서 과정을 전개 / 방정식·조건에 대입하거나 독립 방법으로 확인.')]
    audits=[
      ('전체','원본 22쪽을 이미지로 대조했습니다. 원본 PDF는 그대로 제공하고, 4:3 슬라이드는 비율을 유지한 채 좌우 여백을 추가했습니다. 빈 페이지도 빠짐없이 포함했습니다.'),
      ('2–3','확산식의 c², 변수계수 bx, 비선형식 u·uₓ와 (uₓ)²를 확인했습니다. 물리적 단위와 차수·선형성의 차이를 보강했습니다.'),
      ('4','문제는 uₓₓ−u=0입니다. 다른 독립변수 이름이 없어 해설에서 y를 지정하고 A(y)eˣ+B(y)e⁻ˣ로 완성했습니다.'),
      ('5–12','양 끝 0, 초기변위 f, 초기속도 g를 확인했습니다. 원본이 생략한 변수분리·분리상수의 세 경우·직교 계수 유도를 편집자 풀이로 보강했습니다.'),
      ('9–10','원본의 λₙ=cnπ/L 및 Bₙ*를 확인했습니다. λₙ는 원본에서 고유값이라 부르는 각주파수이며 공간 연산자의 고유값 μₙ와 구분했습니다. 별표는 독립 계수 표기입니다.'),
      ('13–16','v=x+ct, w=x−ct, Φ의 +ct와 Ψ의 −ct, 적분구간 x−ct→x+ct, 인자 1/(2c)를 대조했습니다. 유한 고정단에 필요한 홀수 2L-주기 연장 조건을 보강했습니다.'),
      ('17, 19','주부분의 2B, Δ=B²−AC, 특성방정식의 −2By′를 대조했습니다. 준선형의 범위, 퇴화한 주부분, 수직 방향과 A=0에서의 나눗셈 제한을 설명했습니다.'),
      ('21','두 구간의 2k/L, 경계 L/2, 오른쪽의 L−x, 초기속도 0을 확인했습니다. 가운데·끝점은 연속적으로 채우고 두 구간 부분적분과 최종해를 각각 검산했습니다.'),
      ('6, 7, 8, 11, 18, 20, 22','실제 빈 풀이 페이지입니다. 새로운 원본 내용이 있는 것처럼 설명하지 않고 해당 개념·문제의 편집자 풀이로 연결했습니다.')]
    audit=C('원본과 편집자 해설을 구분합니다.', '이미지와 수식 대조에서 명백한 산술·부호 오류로 단정할 항목은 발견하지 않았습니다. 아래 기록은 원본의 생략된 계산과 적용 조건을 보강한 내역입니다. 강의 영상·스크립트가 없으므로 ASR 검토는 해당하지 않습니다. 강사의 구두 설명이나 출제 의도는 추정하지 않습니다.')+table(['PDF 쪽','확인한 내용과 해설의 처리'],audits)
    sources=C('원본 강의 자료', '<a href="materials/PDE - I.pdf" download="PDE - I.pdf">PDE - I.pdf</a> · Arshad Afzal · 22쪽 · 수업 날짜·주차 미기재.', '개념·원본 문제의 근거는 위 PDF입니다. 한국어 설명, 생략된 유도와 완성 풀이, 추가 예제 및 비교 그림은 편집자 작성입니다. 원본 이미지와 PDF 자체는 교정하지 않았습니다.')+C('보조 대조 자료', '<a href="https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-fall-2006/22ead9d70b36836a68d13c7393e19649_waveeqni.pdf">MIT OpenCourseWare · Matthew J. Hancock, The 1-D Wave Equation (18.303, 2006)</a> · 줄 모델의 가정, 변수분리, D’Alembert 해와 고정단의 홀수 주기 연장 조건을 대조했습니다. 보조 자료의 무차원 변수·고유값 기호는 본문에서 원본의 L,c,λₙ 규약에 맞추어 구별했습니다. 본문의 계산 과정과 추가 예제는 독립적으로 전개·검산했습니다.')
    toc=[('overview','단원 개요'),('concept-map','개념 지도'),('concept-summary','핵심 개념 요약')]+[(f'slide-{n:02}',f'{n:02} · '+p['title']) for n,p in sorted(PAGES.items())]+[('exam-english','시험 영어'),('glossary','핵심 용어'),('asr-log','원본 검토·보강'),('sources','출처')]
    concept='<div class="grid-3">'+C('01 · 규칙과 조건','PDE의 정의 → 차수·선형·제차 → 해와 중첩 → 초기·경계조건.')+C('02 · 고정된 기본 모양','변수분리 → 양 끝에 맞는 사인 모드 → 푸리에 계수 → 삼각형 줄의 진동.')+C('03 · 움직이는 파동','x±ct 좌표 → D’Alembert 해 → 고정단 반사 → PDE 분류와 특성곡선.')+'</div>'
    values={'LECTURE_NUMBER':'PDE I','LECTURE_TITLE':'Partial differential equations I','ONE_SENTENCE_DESCRIPTION':'공업수학 II 편미분방정식 I: 원본 22쪽, 변수분리·달랑베르 해법·특성곡선·삼각형 줄 문제의 상세 풀이와 뉴비 해설','WEEK':'공업수학 II','LECTURE_PROMISE':'편미분의 뜻부터 줄의 진동을 완성하는 두 해법까지. 원본 22쪽과 독립적인 기본·뉴비 해설, 생략 없는 주요 유도와 연습문제 풀이를 이어 읽습니다.','DATE_OR_날짜_미기재':'미기재','PAGE_COUNT':'22','VIDEO_SET':'PDF 기반 · 강의 영상 없음','ALL_CONTENTS_AND_PROBLEM_SOLVING_BUTTONS':'','ORIGINAL_PDF_URL':'materials/PDE - I.pdf','LECTURE_NOTE_FILENAME':'PDE - I.pdf','CORE_RELATIONSHIP_HEADLINE':'푸리에 급수로 줄의 움직임을 구하고, 진행파로 같은 답을 봅니다.','CORE_RELATIONSHIP_EXPLANATION':'Partial differential equation(편미분방정식)의 기본 언어를 익힌 뒤 파동방정식을 풉니다. 경계조건이 공간 모드를 정하고 초기조건이 계수를 정하는 논리를 따라가며, D’Alembert 해법과 특성곡선으로 연결합니다.','CONCEPT_MAP_HEADLINE':'PDE와 조건 → 변수분리·푸리에 급수 → 진행파·특성곡선','CONCEPT_MAP_BLOCKS':concept,'STANDALONE_CONCEPT_SUMMARY':summary(),'DISTINCT_SUMMARY_VIDEO_SECTION_IF_NEEDED':'','EXAM_SECTION_TITLE':'PDE의 분류와 풀이를 설명하는 영어 문장','BILINGUAL_GLOSSARY_TABLE':table(['English(한국어)','뜻과 사용'],terms),'AUDIT_SECTION_TITLE':'원본 대조·보강 기록 · 스크립트 없음','ASR_CORRECTION_TABLE':audit,'SOURCE_LIST_AND_PROVENANCE_NOTE':sources,'TABLE_OF_CONTENTS_LINKS':''.join(f'<li><a href="#{k}">{v}</a></li>' for k,v in toc)}
    template=re.sub(r'<span class="header-meta">.*?</span>','<button type="button" class="mode-toggle" id="mode-toggle" aria-pressed="false">뉴비 모드 켜기</button>',template)
    for k,v in values.items(): template=template.replace('{{'+k+'}}',v)
    template=template.replace('MC2103 Dynamics','MC2202 Engineering Mathematics II').replace('| MC2103','| MC2202')
    template=template.replace('이 부분만 읽어도 렉처의 핵심 정의, 개념 관계, 가정과 풀이 흐름을 이해할 수 있도록 작성합니다.','방정식과 조건의 역할, 두 해법의 논리, 공식의 적용 범위를 먼저 정리합니다. 아래에서 원본 순서의 상세 해설과 완성 풀이로 이어집니다.')
    template=template.replace('</head>','<link rel="stylesheet" href="assets/vendor/katex/katex.min.css"><link rel="stylesheet" href="assets/css/math-note.css?v=transforms-1"><link rel="stylesheet" href="assets/css/transforms.css"><script src="assets/js/mode-init.js"></script></head>')
    template=template.replace('<div class="page-shell">','<div class="mode-guide"><strong id="mode-status">기본 모드 · 밝은 화면</strong><p>뉴비 모드는 다크 화면과 함께 본문 자체를 기초부터 설명하는 내용으로 바꿉니다. 편미분의 의미, 공식을 선택하는 이유, 중간 계산과 결과의 검산까지 연결하며 English(한국어) 용어 표기를 유지합니다.</p><p><a href="fourier-series.html">선수 개념 · 푸리에 급수</a> · <a href="fourier-integrals-transforms.html">이전 단원 · 푸리에 적분과 변환</a> · <a href="#slide-04">4쪽 문제 풀이</a> · <a href="#slide-21">21쪽 삼각형 줄 문제·비교 그림</a></p><noscript>JavaScript가 꺼져 있어 기본·뉴비 해설을 모두 표시합니다.</noscript></div><div class="page-shell">')
    template=template.replace('</body>','<script src="assets/js/math-note.js" defer></script><script src="assets/js/pde-demo.js" defer></script></body>')
    template=re.sub(r'<!--.*?-->','',template,flags=re.S)
    if '{{' in template: raise RuntimeError('Unresolved PDE template')
    (SITE/'pde-i.html').write_text('\n'.join(line.rstrip() for line in template.splitlines())+'\n',encoding='utf-8')
    print('Built PDE I: 22 slides, 14 independent reading pairs + summary')

if __name__=='__main__': build()
