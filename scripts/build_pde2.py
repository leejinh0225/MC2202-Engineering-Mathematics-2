"""Build PDE II from the existing Dynamics lecture-page template."""
from pathlib import Path
import re
from pde2_content import PAGES, C, M, table, paths

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'site'

def summary():
    standard=''.join([
      C('열방정식은 열의 보존과 확산을 연결합니다.', 'Heat equation(열방정식)은 초기온도에서 이후의 온도를 구합니다. 일정한 물성·내부 열원 없음·1차원 전도라는 가정 아래 uₜ=c²uₓₓ이며 c²=K/(ρC)는 thermal diffusivity(열확산계수)입니다. uₜ가 한 번 미분이므로 파동 문제와 달리 초기속도를 따로 주지 않습니다. 온도 0인 끝과 insulated end(단열 끝)를 구별합니다.', M(r'\alpha=c^2=\frac{K}{\rho C},\qquad [\alpha]=\mathrm{length^2/time}')),
      C('유한 막대: 경계조건 → 사인 모드 → 초기조건 → 계수', '0<x<L,양 끝 0이면 공간 모드는 sin(nπx/L)입니다. 각 모드의 크기는 e⁻ᶜ²⁽ⁿπ⁄ᴸ⁾²ᵗ로 줄어듭니다. 높은 n이 먼저 사라지며 온도 모양이 매끄러워집니다.', M(r'u(x,t)=\sum_{n\ge1}B_n\sin\frac{n\pi x}{L}e^{-c^2(n\pi/L)^2t},\qquad B_n=\frac2L\int_0^Lf(x)\sin\frac{n\pi x}{L}\,dx'), '원본 λₙ=cnπ/L에 대해 지수는 −λₙ²t입니다. 공간 고유값 (nπ/L)²와 구분합니다. 원본 18쪽은 단일 사인, 21쪽은 구간별 삼각형이라 계수 계산 방법이 다릅니다.'),
      C('정상 직사각형: 사인과 쌍곡사인을 곱합니다.', 'Steady state(정상 상태)는 시간 변화가 없는 상태입니다. uₓₓ+uᵧᵧ=0에서 세 변 0, 위쪽 y=b의 온도가 f(x)인 문제는 다음 식으로 풉니다.', M(r'u(x,y)=\sum_{n\ge1}b_n\sin\frac{n\pi x}{a}\frac{\sinh(n\pi y/a)}{\sinh(n\pi b/a)},\qquad b_n=\frac2a\int_0^af(x)\sin\frac{n\pi x}{a}\,dx'), 'x의 두 번 미분은 −k², y의 두 번 미분은 +k²가 되어 상쇄됩니다. Normal derivative(법선미분)의 방향과 Dirichlet·Neumann·Robin 조건을 구별합니다.'),
      C('무한 막대: 연속 주파수의 감쇠 → Gaussian 열핵', M(r'u(x,t)=\frac1{2c\sqrt{\pi t}}\int_{\mathbb R}f(v)e^{-(x-v)^2/(4c^2t)}\,dv,\qquad t>0,\ c>0'), '끝점 조건이 없는 무한 영역에서는 Fourier integral(푸리에 적분)을 씁니다. Heat kernel(열핵)은 전체 넓이가 1인 가우스 가중치입니다. 적분가능한 초기온도의 전체 적분은 보존되지만 양 끝을 0도로 냉각하는 유한 막대는 끝으로 열을 잃습니다. 사각형 초기온도에서는 적분을 −1부터 1로 줄여 erf(오차함수)로 표현합니다.'),
      C('문제를 풀기 전에 세 가지를 확인합니다.', '영역이 유한한지 무한한지, 시간 변화인지 정상 상태인지, 경계에서 온도와 열유속 중 무엇을 주었는지 확인합니다. 그다음 초기함수·경계함수의 모양에 맞춰 계수 또는 적분을 계산합니다. 마지막에는 원래 PDE, 경계조건, 초기조건과 단위를 각각 대입해 검산합니다.')])
    beginner=''.join([
      C('1 · 앞 단원과 재료는 같고 시간 변화가 다릅니다.', 'PDE I에서는 사인 모양을 더해 줄의 진동을 만들었습니다. 이번에는 사인 모양을 더해 막대의 온도 분포를 만듭니다. Wave equation(파동방정식)의 시간 인자는 왔다 갔다 진동하지만, heat equation(열방정식)의 시간 인자는 점점 작아지는 exponential(지수함수)입니다.', M(r'\text{공간 부품: }\sin\frac{n\pi x}{L},\qquad\text{시간 배율: }e^{-c^2(n\pi/L)^2t}')),
      C('2 · 공식이 갑자기 등장하는 것이 아니라 조건이 골라 줍니다.', '양 끝 온도가 0이므로 그 두 곳에서 0인 사인 부품을 고릅니다. 처음 온도 f(x)를 만들려면 각 부품을 몇 배씩 쓸지 정해야 합니다. 그 비율 Bₙ가 Fourier coefficient(푸리에 계수)입니다. 같은 사인을 곱해 적분하면 원하는 부품만 남고, 그 사인 자체의 크기 L/2로 나누므로 2/L가 붙습니다.', M(r'B_n=\frac2L\int_0^Lf(x)\sin\frac{n\pi x}{L}\,dx'), '처음부터 사인 하나면 계수를 바로 읽고, 삼각형이면 식이 바뀌는 중앙에서 적분을 나눕니다. 본문에서 두 원본 문제를 모두 계산합니다.'),
      C('3 · 온도 지도를 구하는 문제와 시간 변화를 구하는 문제를 나눕니다.', '직사각형 문제에는 시간 t가 없습니다. 이미 steady state(정상 상태)가 된 내부 온도를 네 변의 온도로 구합니다. x에는 양 끝이 0인 sin을, y에는 두 번 미분하면 플러스 부호가 나오는 sinh를 씁니다. sinh z=(eᶻ−e⁻ᶻ)/2이므로 지수함수에서 출발해 이해할 수 있습니다.'),
      C('4 · 무한 막대는 처음의 각 지점에서 퍼진 열을 더합니다.', '두 끝이 없는 infinite bar(무한 막대)에서는 주파수의 번호가 연속으로 바뀌어 합 대신 적분을 씁니다. 최종적으로 현재 위치 x의 온도는 처음 위치 v들의 온도를 거리 x−v에 따라 섞은 값입니다.', M(r'u(x,t)=\int_{\mathbb R}f(v)\frac{e^{-(x-v)^2/(4c^2t)}}{2c\sqrt{\pi t}}\,dv'), '가까운 곳은 많이, 먼 곳은 적게 섞습니다. 처음에 −1부터 1까지만 뜨거우면 그 구간만 적분합니다. 복잡한 지수 안을 z²로 만드는 치환을 한 줄씩 따라가면 원본 코드의 상한·하한까지 이해할 수 있습니다.'),
      C('5 · 계산 실수를 막는 연결 고리', 'Thermal diffusivity(열확산계수) c²는 K/(ρC)입니다. 계산한 값을 다시 제곱하지 않습니다. 온도를 0으로 유지하는 끝은 열이 나갈 수 있지만, insulated boundary(단열 경계)는 법선미분이 0입니다. 유한 막대와 무한 막대에서 총열이 보존되는지의 판단이 달라지는 이유가 여기에 있습니다.')])
    return paths(standard, beginner)

def demo():
    return C('직접 확인 · 원본 Problem 2의 냉각', '<div class="transform-demo"><p>편집자 비교 그림 · 원본과 같은 L=π,c=1입니다. 점선은 처음 삼각형, 실선은 해당 시간의 온도입니다. t=0에서는 정확한 초기함수, t>0에서는 홀수 모드 80개의 합을 사용합니다.</p><label for="heat-time">시간 t <output id="heat-time-value" for="heat-time">0.00</output></label><input id="heat-time" type="range" min="0" max="2" step="0.01" value="0"><canvas id="heat-demo" width="960" height="440" role="img" aria-label="삼각형 초기온도가 시간에 따라 매끄러워지며 감소하는 모습">L=π,c=1인 원본 문제. 처음 중앙 온도는 π/2이며 시간이 흐르면 0으로 감소합니다.</canvas><p id="heat-caption" aria-live="polite"></p><noscript>원본 위의 t=0,0.1,0.5,2 그림과 21쪽 완성 급수로 시간에 따른 변화를 확인할 수 있습니다.</noscript></div>')

def build():
    assert set(PAGES)==set(range(1,23))
    template=(SITE/'templates/lecture-page.template.html').read_text(encoding='utf-8')
    match=re.search(r'        <section class="source-section".*?</section>',template,re.S)
    sections=[]
    for n,p in sorted(PAGES.items()):
        body=paths(p['standard'],p['beginner']) if p['beginner'] else p['standard']
        if n==22: body+=demo()
        vals={'NN':f'{n:02}','SLIDE_ROLE':p['role'],'SLIDE_HEADING':p['title'],'LECTURE_SLUG':'pde-ii','DESCRIPTIVE_ALT_TEXT':f'PDE - II 원본 PDF {n}쪽: '+p['title'],'CURRENT_PAGE':str(n),'PAGE_COUNT':'22','TRANSCRIPT_TIME_OR_SLIDE_ROLE':'원본 PDF · 유도·해설·완성 풀이는 편집자 작성','SLIDE_EXPLANATION_BLOCKS':body}
        block=match.group(0)
        for k,v in vals.items(): block=block.replace('{{'+k+'}}',v)
        sections.append(block)
    template=template[:match.start()]+'\n'.join(sections)+template[match.end():]
    exams=[
      ('What is thermal diffusivity?', 'Thermal diffusivity is the thermal conductivity divided by the product of density and specific heat. Its dimension is length squared per unit time.', 'Thermal diffusivity(열확산계수)와 thermal conductivity(열전도율)를 구별합니다.'),
      ('Why do higher spatial modes decay faster?', 'The decay rate of mode n is proportional to n squared. Fine spatial variations therefore disappear faster than large-scale variations.', 'Decay rate(감쇠율)가 n²에 비례한다는 원인까지 답합니다.'),
      ('Distinguish a zero-temperature boundary from an insulated boundary.', 'A zero-temperature boundary prescribes the temperature and can exchange heat. An insulated boundary has zero normal heat flux, hence zero normal temperature derivative for positive conductivity.', 'Dirichlet(온도 지정)과 homogeneous Neumann(법선미분 0)을 구별합니다.'),
      ('Why does the rectangle solution contain a hyperbolic sine?', 'Separation gives F double prime plus k squared F equal to zero and G double prime minus k squared G equal to zero. A hyperbolic sine satisfies the second equation and vanishes at the bottom boundary.', 'Hyperbolic sine(쌍곡사인)의 2차 미분 부호와 아래쪽 경계조건을 연결합니다.'),
      ('What is the role of the heat kernel?', 'It weights the contribution of each initial position to the temperature at a later time. The Gaussian kernel has unit integral and spreads over a distance proportional to the square root of time.', 'Heat kernel(열핵)의 가중치·정규화·퍼지는 폭을 설명합니다.'),
      ('How do you find when the copper bar maximum reaches fifty degrees?', 'The initial temperature is the first sine mode. Its maximum stays at the midpoint and decays exponentially. Set one hundred times the exponential factor equal to fifty and solve for time using a logarithm.', '원본 Problem 1의 first mode(첫 모드) → midpoint(중앙) → logarithm(로그) 순서입니다.'),
      ('Why are the even coefficients zero for the triangular initial temperature?', 'The initial temperature is symmetric about the midpoint, while each even-index sine mode is antisymmetric about it. The coefficient integral therefore cancels.', '원본 Problem 2의 symmetry(대칭)와 coefficient integral(계수 적분)의 상쇄를 설명합니다.')]
    exam=''.join('<div class="exam-card"><h3>'+q+'</h3><div class="answer"><span class="answer__label">Model answer</span>'+a+'</div><p>'+k+'</p></div>' for q,a,k in exams)
    start=template.index('            <div class="exam-card">',template.index('id="exam-english"'))
    end=template.index('\n          </div>',start)
    template=template[:start]+exam+template[end:]
    terms=[
      ('Heat / diffusion equation(열 / 확산방정식)','온도·농도의 시간 변화율과 공간 곡률을 연결하는 PDE.'),
      ('Thermal conductivity K, κ(열전도율)','온도 기울기당 열유속의 비례계수. κ는 원본 구리 막대 문제의 표기.'),
      ('Thermal diffusivity c², α(열확산계수)','K/(ρC). 차원은 길이²/시간이며 파동 속도와 다름.'),
      ('Specific heat C, cₚ(비열)','단위 질량의 온도를 한 단위 올리는 데 필요한 열.'),
      ('Density ρ(밀도)','단위 부피당 질량.'),
      ('Heat flux q(열유속)','단위 면적·단위 시간당 흐르는 열. q=−K∇u.'),
      ('Laterally insulated(옆면이 단열된)','막대의 옆면으로 열이 흐르지 않는 상태. 끝의 냉각과 양립함.'),
      ('Initial / boundary condition(초기 / 경계조건)','처음 시간의 함수 / 영역 경계에서 주는 조건.'),
      ('Separation of variables(변수분리법)','변수별 함수의 곱으로 PDE를 ODE들로 분리하는 방법.'),
      ('Eigenfunction / eigenvalue(고유함수 / 고유값)','경계조건과 고유방정식을 만족하는 비영 함수 / 대응 상수. 원본 λₙ와 공간 μₙ를 구분.'),
      ('Decay rate(감쇠율)','e⁻ʳᵗ에서 r. 원본 모드에서는 r=λₙ²=c²(nπ/L)².'),
      ('Fourier sine series / coefficient(푸리에 사인 급수 / 계수)','사인 함수들의 합 / 각 사인 앞에 곱하는 크기.'),
      ('Orthogonality(직교성)','다른 모드끼리의 곱 적분이 0이 되는 성질.'),
      ('Steady state(정상 상태)','시간에 따라 변하지 않는 상태. 공간적으로 균일할 필요는 없음.'),
      ('Laplace equation(라플라스 방정식)','∇²u=0. 일정한 물성·내부 열원 없는 정상 열전도의 대표식.'),
      ('Dirichlet / Neumann / Robin(디리클레 / 노이만 / 로빈)','함숫값 / 법선미분 / 그 선형 결합을 지정하는 경계조건.'),
      ('Outward normal derivative(외향 법선미분)','경계 바깥쪽으로 향하는 단위 법선 방향의 미분 ∇u·n.'),
      ('Hyperbolic sine / cosine(쌍곡사인 / 쌍곡코사인)','sinh z=(eᶻ−e⁻ᶻ)/2, cosh z=(eᶻ+e⁻ᶻ)/2.'),
      ('Infinite bar / bounded solution(무한 막대 / 유계 해)','x∈ℝ인 이상화 / 크기가 무한히 커지지 않는 해.'),
      ('Heat kernel / convolution(열핵 / 합성곱)','초기 열의 확산 가중치 / 위치 차이를 사용한 적분 결합.'),
      ('Gaussian / error function(가우스 함수 / 오차함수)','e⁻ᶻ² 모양의 함수 / 그 정적분으로 정의한 erf.'),
      ('Maximum temperature / half-decay time(최대온도 / 절반 감쇠 시간)','주어진 시간의 공간 최댓값 / 단일 지수 크기가 절반 되는 ln2/r.'),
      ('Find / verify / impose(구하라 / 검산하라 / 조건을 적용하라)','답을 계산 / 원식과 조건에 대입 / 경계·초기조건을 해에 맞추는 지시 표현.')]
    audits=[
      ('전체 22쪽','모든 페이지를 이미지로 확인하고 4:3 원본을 비율 유지한 1920×1080 틀에 배치했습니다. PDF 원본은 그대로 보존했습니다.'),
      ('2–3','c²=K/(ρC), uₜ=c²uₓₓ, 양 끝 0과 초기함수 f를 대조했습니다. 열확산계수와 파동 속도의 단위 차이, 모델 가정을 보강했습니다.'),
      ('5–6','지수 −λₙ²t, λₙ=cnπ/L를 확인했습니다. 공간 고유값 μₙ=(nπ/L)²와 원본 명칭의 차이를 구분하고 생략된 Bₙ 적분을 유도했습니다. 원본 오류로 기록하지 않습니다.'),
      ('7–8','mixed의 식 au+b∂ₙu, 그림의 위쪽 f(x)·나머지 세 변 0·가로 a·세로 b를 확인했습니다. Robin 용어와 완성된 sinh 급수는 편집자 보강입니다.'),
      ('12','무한 영역과 초기함수만 제시되어 있습니다. 연속 주파수·열핵 유도 및 해의 적용 조건을 보강했습니다.'),
      ('16','초기함수는 |x|<1에서 U₀입니다. 텍스트 추출이 누락한 절댓값을 그림과 확대 이미지로 확인했습니다. ±1 값 미지정은 적분 해의 오류가 아닙니다.'),
      ('17','하한 −(1+x)/(2√t), 상한 (1−x)/(2√t), U₀/√π를 대조했습니다. c=1 설정을 설명하고 t=0을 별도로 처리하는 erf 코드를 보강했습니다.'),
      ('18','L=80 cm, ρ=8.92, cₚ=0.092, κ=0.95와 각각의 단위, 초기 사인 진폭 100, 목표 최대온도 50을 확인했습니다. 약 388.27초를 독립 계산했습니다.'),
      ('21–22','왼쪽 x·오른쪽 L−x·경계 L/2, 중앙 높이 L/2, 그림 L=π,c=1을 확인했습니다. 계수의 sin(nπ/2)와 시간 인자의 n²를 적분·대입으로 검산했습니다.'),
      ('4,9–11,13–15,19–20','실제 빈 풀이 페이지입니다. 원본은 보존하고 관련 편집자 유도·풀이로 연결했습니다. 5쪽은 하단 식이 있어 빈 페이지로 분류하지 않았습니다.')]
    audit=C('명백한 오식과 생략된 설명을 구별합니다.', '이번 원본에서 명백한 수식·수치 오식으로 단정할 항목은 발견하지 않았습니다. 아래는 표기 해석, 생략된 매개변수, 계산 보강의 기록입니다. 원본 PDF와 이미지의 식은 변경하지 않았습니다. 영상·스크립트가 없어 ASR 검토는 해당하지 않습니다.')+table(['PDF 쪽','대조한 내용과 해설 처리'],audits)
    sources=C('원본 강의자료', '<a href="materials/PDE - II.pdf" download="PDE - II.pdf">PDE - II.pdf</a> · Arshad Afzal · 22쪽 · 주차·날짜 미기재.', '한국어 설명, 계산 유도, 원본 예제·연습문제의 완성 풀이, 코드 보강과 비교 그림은 편집자 작성입니다. 별도 창작 계산 문제나 모의시험은 추가하지 않았습니다. 시험 영어는 본문 개념을 영어로 설명하는 표현 연습입니다.')+C('보조 대조 자료', '<a href="https://ocw.mit.edu/courses/18-152-introduction-to-partial-differential-equations-fall-2011/8547cf4208529f2a7f3ce6d881f1f3c2_MIT18_152F11_lec_02.pdf">MIT OpenCourseWare · Jared Speck, The Diffusion (aka Heat) Equation</a> · 열 보존·열유속·경계조건의 의미를 대조했습니다.', '<a href="https://www.ocw.mit.edu/courses/18-303-linear-partial-differential-equations-fall-2006/ffeff4a86a9d709cc6c394e99124c9bf_fourtran.pdf">MIT OpenCourseWare · Matthew J. Hancock, Infinite Spatial Domains and the Fourier Transform</a> · 무한 영역의 적용 조건·열핵·오차함수 표현을 대조했습니다. 보조 자료의 Fourier transform(푸리에 변환) 부호와 정규화는 앞 단원의 규약과 다르므로 본문에서는 앞 단원 규약을 유지했습니다.')
    toc=[('overview','단원 개요'),('concept-map','개념 지도'),('concept-summary','핵심 개념 요약')]+[(f'slide-{n:02}',f'{n:02} · '+p['title']) for n,p in sorted(PAGES.items())]+[('exam-english','시험 영어'),('glossary','핵심 용어'),('asr-log','원본 대조·보강'),('sources','출처')]
    concept='<div class="grid-3">'+C('01 · 유한 막대의 냉각','열 보존 → 열방정식 → 양 끝 0 → 사인 모드 → 지수 감쇠 → 구리·삼각형 문제.')+C('02 · 정상 온도 지도','시간 변화 0 → Laplace equation(라플라스 방정식) → 경계조건 → sin×sinh → 직사각형 내부 온도.')+C('03 · 무한 막대의 확산','연속 주파수 → Fourier integral(푸리에 적분) → Gaussian 열핵 → 사각형 초기온도 → erf.')+'</div>'
    values={'LECTURE_NUMBER':'PDE II','LECTURE_TITLE':'Partial differential equations II','ONE_SENTENCE_DESCRIPTION':'공업수학 II 편미분방정식 II: 원본 22쪽, 열방정식·라플라스 방정식·열핵·원본 문제 상세 풀이와 독립 뉴비 해설','WEEK':'공업수학 II','LECTURE_PROMISE':'열이 퍼지는 이유부터 사인 급수와 열핵으로 온도를 구하는 과정까지. 원본 22쪽과 기본·뉴비 해설, 상세 유도와 모든 원본 예제의 완성 풀이를 이어 읽습니다.','DATE_OR_날짜_미기재':'미기재','PAGE_COUNT':'22','VIDEO_SET':'PDF 기반 · 강의 영상 없음','ALL_CONTENTS_AND_PROBLEM_SOLVING_BUTTONS':'','ORIGINAL_PDF_URL':'materials/PDE - II.pdf','LECTURE_NOTE_FILENAME':'PDE - II.pdf','CORE_RELATIONSHIP_HEADLINE':'푸리에 성분이 감쇠하며 온도 차이가 완화됩니다.','CORE_RELATIONSHIP_EXPLANATION':'열방정식을 유한 막대·정상 직사각형·무한 막대로 나누어 풉니다. 경계가 허용하는 공간 모양과 열의 시간 변화를 구분하고, 초기온도를 맞추는 계수·적분을 원본 문제에서 끝까지 계산합니다.','CONCEPT_MAP_HEADLINE':'열 보존과 경계조건 → 변수분리 → 급수·열핵 → 온도 예측','CONCEPT_MAP_BLOCKS':concept,'STANDALONE_CONCEPT_SUMMARY':summary(),'DISTINCT_SUMMARY_VIDEO_SECTION_IF_NEEDED':'','EXAM_SECTION_TITLE':'열방정식의 풀이를 설명하는 영어 문장','BILINGUAL_GLOSSARY_TABLE':table(['English(한국어)','뜻과 사용'],terms),'AUDIT_SECTION_TITLE':'원본 대조·보강 기록 · 스크립트 없음','ASR_CORRECTION_TABLE':audit,'SOURCE_LIST_AND_PROVENANCE_NOTE':sources,'TABLE_OF_CONTENTS_LINKS':''.join(f'<li><a href="#{k}">{v}</a></li>' for k,v in toc)}
    template=re.sub(r'<span class="header-meta">.*?</span>','<button type="button" class="mode-toggle" id="mode-toggle" aria-pressed="false">뉴비 모드 켜기</button>',template)
    for k,v in values.items(): template=template.replace('{{'+k+'}}',v)
    template=template.replace('MC2103 Dynamics','MC2202 Engineering Mathematics II').replace('| MC2103','| MC2202')
    template=template.replace('이 부분만 읽어도 렉처의 핵심 정의, 개념 관계, 가정과 풀이 흐름을 이해할 수 있도록 작성합니다.','열방정식의 가정, 영역·경계에 따른 공식 선택, 초기함수에서 답까지의 흐름을 먼저 연결합니다. 아래에서 원본 순서의 상세 해설로 이어집니다.')
    template=template.replace('</head>','<link rel="stylesheet" href="assets/vendor/katex/katex.min.css"><link rel="stylesheet" href="assets/css/math-note.css?v=transforms-1"><link rel="stylesheet" href="assets/css/transforms.css"><script src="assets/js/mode-init.js"></script></head>')
    template=template.replace('<div class="page-shell">','<div class="mode-guide"><strong id="mode-status">기본 모드 · 밝은 화면</strong><p>뉴비 모드는 다크 화면과 함께 본문을 기초부터 풀어 쓴 해설로 바꿉니다. 공식 선택의 이유, 삼각함수·부분적분·치환·로그 계산과 결과의 의미까지 연결합니다. English(한국어 번역) 용어 표기는 두 모드에서 유지합니다.</p><p><a href="pde-i.html">이전 단원 · PDE I</a> · <a href="#slide-16">사각형 초기온도 예제</a> · <a href="#slide-18">구리 막대 문제</a> · <a href="#slide-21">삼각형 온도 문제</a> · <a href="#slide-22">냉각 비교 그림</a></p><noscript>JavaScript가 꺼져 있어 기본·뉴비 해설을 모두 표시합니다.</noscript></div><div class="page-shell">')
    template=template.replace('</body>','<script src="assets/js/math-note.js" defer></script><script src="assets/js/heat-demo.js" defer></script></body>')
    template=re.sub(r'<!--.*?-->','',template,flags=re.S)
    if '{{' in template: raise RuntimeError('Unresolved PDE II template')
    (SITE/'pde-ii.html').write_text('\n'.join(line.rstrip() for line in template.splitlines())+'\n',encoding='utf-8')
    print('Built PDE II: 22 slides; 12 independent reading pairs + summary')

if __name__=='__main__': build()
