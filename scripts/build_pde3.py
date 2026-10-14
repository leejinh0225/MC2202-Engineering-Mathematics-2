"""Build the slide-preserving PDE III note using the established template."""
from pathlib import Path
import re
from pde3_content import PAGES,C,M,table,paths,source_review

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'site'

def summary():
    return paths(''.join([
      C('같은 방법, 다른 공간 모드', 'Separation of variables(변수분리법)는 경계가 허용하는 공간 모드를 찾고, initial / boundary data(초기 / 경계 데이터)를 직교 급수로 맞추는 방법입니다. 직사각형은 사인 곱, 축대칭 원형 막은 J₀, 축대칭 구면 문제는 Pℓ(cosφ)를 사용합니다.'),
      C('직사각형 막 · 가로·세로 두 번호', M(r'\phi_{mn}=\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b},\qquad\lambda_{mn}=c\pi\sqrt{(m/a)^2+(n/b)^2},\quad c^2=\tau/\sigma'), M(r'u=\sum_{m,n\ge1}[B_{mn}\cos(\lambda_{mn}t)+B_{mn}^{*}\sin(\lambda_{mn}t)]\phi_{mn}'), M(r'B_{mn}=\frac4{ab}\iint f\phi_{mn}\,dA,\qquad B_{mn}^{*}=\frac4{ab\lambda_{mn}}\iint g\phi_{mn}\,dA'), '적분은 0<x<a,0<y<b입니다. τ는 길이당 장력, σ는 면적당 질량입니다. g=0이면 시간 사인 항만 없어집니다. 원본 10쪽은 두 번의 부분적분으로 홀수 m,n의 계수를 구합니다.'),
      C('축대칭 원형 막 · 중심 정칙성과 고정 테두리', M(r'W_m=J_0(\alpha_mr/R),\quad J_0(\alpha_m)=0,\quad\lambda_m=c\alpha_m/R'), M(r'A_m=\frac{2\int_0^Rrf(r)W_m(r)\,dr}{R^2J_1(\alpha_m)^2},\qquad B_m=\frac{2\int_0^Rrg(r)W_m(r)\,dr}{\lambda_mR^2J_1(\alpha_m)^2}'), '각 모드에 Aₘcos(λₘt)+Bₘsin(λₘt)를 곱해 합칩니다. 중심에서 발산하는 Y₀를 제외하고 고정 테두리에서 J₀의 영점을 고릅니다. 가중함수 r, 노름의 J₁², 속도 계수의 λₘ를 유지합니다.'),
      C('구 바깥 · 무한대에서 감소하는 거리 인자', M(r'u(r,\phi)=\sum_{\ell\ge0}a_\ell(R/r)^{\ell+1}P_\ell(\cos\phi)'), M(r'a_\ell=\frac{2\ell+1}{2}\int_0^\pi f(\phi)P_\ell(\cos\phi)\sin\phi\,d\phi'), 'θ가 방위각, φ가 극각인 원본 규약입니다. u(R,φ)=f(φ), u→0을 만족시킵니다. 원점은 영역 밖이므로 1/rℓ⁺¹을 버리지 않습니다. 상수 각도 성분 ℓ=0도 1/r로 감소하므로 포함합니다.'),
      C('계산 전후 점검', '영역·좌표·대칭을 먼저 확인하고, 공간 경계로 모드 → PDE로 시간 또는 거리 변화 → 주어진 데이터로 계수 순서로 풉니다. 결과는 PDE, 경계, 초기조건과 단위에 각각 대입합니다. 급수의 미분·경계 수렴은 데이터의 매끄러움과 함께 해석합니다.')
    ]),''.join([
      C('1 · 이번 단원도 “부품과 배합비”가 핵심입니다.', '처음 모양 전체를 한 번에 풀기 어렵기 때문에 쉬운 모양들을 구한 뒤 더합니다. Boundary conditions(경계조건)는 사용할 수 있는 부품을 고르고, orthogonality(직교성)는 각 부품을 얼마나 넣을지 계산합니다. 원·구처럼 영역이 달라져도 이 흐름은 같습니다.'),
      C('2 · 직사각형 막은 두 방향의 사인을 곱합니다.', M(r'\sin(m\pi x/a)\sin(n\pi y/b)'), '가로 양 끝과 세로 양 끝에서 각각 0이므로 네 변이 모두 고정됩니다. 시간에는 cos(λt),sin(λt)를 붙입니다. 코사인 계수는 처음 높이, 사인 계수에 λ를 곱한 값은 처음 속도입니다.', M(r'\lambda_{mn}=c\pi\sqrt{(m/a)^2+(n/b)^2}'), '원본 10쪽의 f는 x다항식×y다항식이므로 계수도 두 단일적분의 곱으로 계산합니다. 부분적분을 두 번 하면 홀수 번호만 남습니다. 본문에서 부호와 끝점 값을 모두 대입합니다.'),
      C('3 · 원형 막의 낯선 함수는 새 모양의 부품입니다.', 'Bessel function(베셀 함수) J₀는 원형 공간의 미분방정식을 만족하는 함수입니다. 중심에서 매끄러운 J₀를 택하고 테두리에서 0이 되도록 입력을 조절합니다.', M(r'J_0(\alpha_m r/R),\qquad J_0(\alpha_m)=0'), 'αₘ는 함수가 0이 되는 입력입니다. 반지름 r 자체가 아닙니다. 모드의 배합비를 구할 때는 고리 면적을 반영해 r을 곱해 적분합니다. 둥근 막이라도 한쪽만 눌렀다면 이 축대칭 풀이만으로는 충분하지 않습니다.'),
      C('4 · 구 바깥 문제에는 시간 대신 거리에 따른 감소가 있습니다.', '구 표면에서 준 f(φ)를 Legendre polynomial(르장드르 다항식)으로 나누고 각 성분에 거리 인자 (R/r)ℓ⁺¹을 붙입니다. 표면에서는 이 인자가 1이라 원래 값을 유지하고 멀리서는 0으로 줄어듭니다.', M(r'\text{각도 부품 }P_\ell(\cos\phi)\quad\times\quad\text{거리 배율 }(R/r)^{\ell+1}'), 'rℓ를 버리는 이유는 무한대에서 줄어들지 않기 때문입니다. 원점은 문제 영역에 없으므로 원점에서의 발산을 기준으로 해를 버리면 안 됩니다.'),
      C('5 · 적분 앞 숫자는 자기 크기로 나눈 결과입니다.', '사인 곱의 제곱 적분은 ab/4, 원형 베셀 모드의 가중 제곱 적분은 R²J₁²/2, 르장드르 다항식의 제곱 적분은 2/(2ℓ+1)입니다. 주어진 함수에 원하는 모드를 곱해 적분한 뒤 이 크기로 나누면 계수가 됩니다. 공식마다 숫자가 다른 이유는 부품과 적분 구간이 다르기 때문입니다.')
    ]))

def demo():
    return C('직접 확인 · 원본 10쪽의 막 진동', '<div class="transform-demo"><p>편집자 계산 그림 · y=1 ft에서의 가로 단면입니다. 점선은 초기 높이, 실선은 현재 변위입니다. t=0에서는 원래 다항식, t&gt;0에서는 m,n 각각 홀수 40개(총 1,600모드)의 부분합을 표시합니다. 단면의 세로축은 변위 u이며 막의 평면 좌표 y가 아닙니다.</p><label for="membrane-time">시간 t (s) <output id="membrane-time-value" for="membrane-time">0.00</output></label><input id="membrane-time" type="range" min="0" max="3.2" step="0.01" value="0"><canvas id="membrane-demo" width="960" height="480" role="img" aria-label="원본 직사각형 막 문제의 y=1 ft 단면 변위">처음에는 u(x,1,0)=0.1x(4−x), 중앙 높이는 0.4 ft입니다. 두 끝은 항상 0입니다.</canvas><p id="membrane-caption" aria-live="polite"></p><noscript>시간 조작에는 JavaScript가 필요합니다. 바로 위의 완성 급수와 초기조건 설명은 그대로 읽을 수 있습니다.</noscript></div>')

def build():
    assert set(PAGES)==set(range(1,23))
    template=(SITE/'templates/lecture-page.template.html').read_text(encoding='utf-8')
    match=re.search(r'        <section class="source-section".*?</section>',template,re.S)
    sections=[]
    for n,p in sorted(PAGES.items()):
        body=source_review(n)+(paths(p['standard'],p['beginner']) if p['beginner'] else p['standard'])
        if n==10: body+=demo()
        vals={'NN':f'{n:02}','SLIDE_ROLE':p['role'],'SLIDE_HEADING':p['title'],'LECTURE_SLUG':'pde-iii','DESCRIPTIVE_ALT_TEXT':f'PDE III 원본 PDF {n}쪽: '+p['title'],'CURRENT_PAGE':str(n),'PAGE_COUNT':'22','TRANSCRIPT_TIME_OR_SLIDE_ROLE':'원본 PDF · 유도·해설·완성 풀이는 편집자 작성','SLIDE_EXPLANATION_BLOCKS':body}
        block=match.group(0)
        for k,v in vals.items(): block=block.replace('{{'+k+'}}',v)
        sections.append(block)
    template=template[:match.start()]+'\n'.join(sections)+template[match.end():]
    exams=[
      ('What does initially at rest mean?', 'It means that the initial velocity is zero. The initial displacement can be nonzero, and the membrane can subsequently accelerate under tension.', 'Initially at rest(처음에 정지)는 g=0입니다. f=0이나 모든 시간의 정지를 뜻하지 않습니다.'),
      ('How are rectangular membrane frequencies determined?', 'The fixed edges select sine modes in both directions. The angular frequency is the wave speed times the square root of the sum of the squared spatial wave numbers.', 'Boundary conditions(경계조건) → 두 wave numbers(파수) → angular frequency(각진동수)의 순서입니다.'),
      ('Why are only odd indices present in the rectangular example?', 'Each polynomial factor is symmetric about the midpoint of its interval. Even-index sine modes are antisymmetric there, so their coefficient integrals vanish.', '원본 10쪽의 symmetry(대칭)와 even-index mode(짝수 번호 모드)의 적분 상쇄를 설명합니다.'),
      ('Why is the second-kind Bessel function excluded?', 'It is singular at the center. A regular membrane displacement must remain finite and smooth there, so only the first-kind solution is retained.', '원형 막 중심의 regularity(정칙성) 조건입니다. 중심 변위를 0으로 강제하는 조건과 다릅니다.'),
      ('Why does the Fourier–Bessel coefficient contain a radial weight?', 'The radial eigenproblem is self-adjoint with weight r. The same weight also reflects the area of a thin circular annulus.', 'Weighted orthogonality(가중 직교성)와 annulus(고리) 면적을 연결합니다.'),
      ('Distinguish axisymmetry from spherical symmetry.', 'Axisymmetry removes dependence on the azimuthal angle but may retain polar-angle dependence. Spherical symmetry removes both angular dependencies.', '원본 규약에서 azimuthal angle(방위각)은 θ, polar angle(극각)은 φ입니다.'),
      ('Which radial solution is admissible outside the sphere?', 'The power r to minus ell minus one decays at infinity and is retained. The power r to ell does not decay. The origin is outside the domain, so regularity there is not required.', 'Exterior problem(외부 영역 문제)의 조건으로 허용 해를 선택합니다.')]
    exam=''.join('<div class="exam-card"><h3>'+q+'</h3><div class="answer"><span class="answer__label">Model answer</span>'+a+'</div><p>'+k+'</p></div>' for q,a,k in exams)
    start=template.index('            <div class="exam-card">',template.index('id="exam-english"'))
    end=template.index('\n          </div>',start)
    template=template[:start]+exam+template[end:]
    terms=[
      ('Membrane / transverse displacement(막 / 수직 변위)','장력으로 복원력을 받는 얇은 막 / 기준 평면에 수직인 높이 u.'),
      ('Tension per unit length τ(단위 길이당 장력)','막 가장자리의 길이당 당기는 힘. 질량이나 전체 힘과 구별.'),
      ('Areal mass density σ(면적당 질량밀도)','단위 면적당 질량. 체적밀도와 구별.'),
      ('Wave speed c(파동 속도)','√(τ/σ). 길이/시간 단위.'),
      ('Initial displacement / velocity(초기변위 / 초기속도)','u의 처음 값 f / uₜ의 처음 값 g.'),
      ('Fixed boundary(고정 경계)','경계에서 u=0. 전체 영역의 u=0은 아님.'),
      ('Separation of variables(변수분리법)','변수별 곱으로 모드를 찾고 중첩하여 주어진 데이터를 맞춤.'),
      ('Eigenvalue / eigenfunction(고유값 / 고유함수)','같은 경계 고유문제의 허용 상수 / 비영 공간 함수.'),
      ('Wave number / angular frequency(파수 / 각진동수)','공간 변화율의 척도 / 시간 위상 변화율. λ=ck.'),
      ('Normal mode / fundamental mode(정상모드 / 기본 모드)','공간 모양을 유지하는 진동 / 가장 낮은 허용 각진동수 모드.'),
      ('Nodal line / circle(마디선 / 마디원)','한 모드에서 모든 시간에 변위가 0인 선 / 동심원.'),
      ('Double Fourier series(이중 푸리에 급수)','두 공간 방향 번호에 대한 사인·코사인 모드 합.'),
      ('Orthogonality / norm(직교성 / 노름)','다른 모드의 내적이 0 / 모드 자신의 크기. 계수 계산에는 노름 제곱으로 나눔.'),
      ('Integration by parts(부분적분)','∫UV′=UV−∫U′V. 다항식×삼각함수의 계산에서 사용.'),
      ('Polar / cylindrical / spherical coordinates(극 / 원통 / 구면좌표)','평면의 거리·각 / 축까지 거리·각·높이 / 원점부터 거리·두 각.'),
      ('Axisymmetric(축대칭)','축을 중심으로 회전해도 같음. 원형 문제에서 별도 가정.'),
      ('Bessel function, first / second kind(베셀 함수, 제1종 / 제2종)','베셀 ODE의 독립해 Jν / Yν. 중심이 포함된 0차 문제는 Y₀ 제외.'),
      ('Order / zero index(차수 / 영점 번호)','Jν의 ν / αₘ의 m. 서로 다른 번호.'),
      ('Regularity / singularity(정칙성 / 특이성)','중심·극점에서 적절히 유한하고 매끄러움 / 발산 등 비정상 거동.'),
      ('Fourier–Bessel series(푸리에–베셀 급수)','베셀 고유함수의 급수. 이번 반지름 내적의 가중함수는 r.'),
      ('Laplace equation / harmonic function(라플라스 방정식 / 조화함수)','∇²u=0 / 이 방정식을 만족하는 함수.'),
      ('Azimuthal / polar angle(방위각 / 극각)','원본에서 θ: z축 둘레의 회전각 / φ: +z축에서 잰 각.'),
      ('Exterior boundary-value problem(외부 영역 경계값 문제)','주어진 물체 바깥에서 표면·무한대 조건을 만족시키는 문제.'),
      ('Legendre polynomial(르장드르 다항식)','P₀=1부터 시작하는 구면 축대칭 각도 모드.'),
      ('Decay at infinity(무한대에서 감소)','r→∞일 때 u→0이라는 외부 문제의 조건.')]
    audits=[
      ('전체 22쪽','모든 원본 이미지를 육안 대조했습니다. 4:3 비율을 유지한 1920×1080 틀에 배치하고 원본 PDF는 바이트 그대로 보존했습니다.'),
      ('2–3,6','2차원 파동식, 가로 a·세로 b와 네 변 고정 조건을 확인했습니다. u=0의 경계 한정, 장력·면적밀도, 두 번의 변수분리와 양의 공간 고유값 선택은 편집자 보강입니다.'),
      ('7–8','괄호 끝의 불필요한 +를 확대 이미지에서 확인했습니다. 각 슬라이드 위쪽에 공유 검토 카드 한 개만 두고 기본·뉴비 본문에서는 완성된 두 시간 항을 사용합니다.'),
      ('10','4 ft×2 ft, 12.5 lb/ft, 2.5 slugs/ft², 0.1(4x−x²)(2y−y²), 처음 정지를 확인했습니다. c²=5, 홀수 계수 409.6/(π⁶m³n³), 중앙 초기높이 0.4 ft를 검산했습니다.'),
      ('12–13,15–17','극좌표의 r⁻¹·r⁻² 인자, 축대칭 축약, Bessel’s equation이라는 지시와 중첩 진동식을 대조했습니다. 0차 베셀 식의 유도, 중심 정칙성, 영점·모드 번호, r 가중 계수와 노름 계산은 편집자 보강입니다.'),
      ('18','구면좌표의 1/r²는 대괄호 전체에 곱해져 있어 올바릅니다. θ는 방위각, φ는 극각인 원본 규약을 유지합니다. 축대칭과 구면대칭을 구별했습니다.'),
      ('19','구 바깥 영역, u(R,φ)=f(φ), u→0 및 축대칭 조건을 확인했습니다. 구체 f는 미제공이므로 일반 Legendre 급수와 계수 적분으로 완성했습니다.'),
      ('4–5,9,11,14,20–22','실제 빈 풀이 페이지 8쪽입니다. 모두 보존하고 관련 유도·완성 풀이로 연결했습니다. 제목이 있는 6·15쪽과 J₀ 그래프가 있는 16쪽은 빈 페이지로 처리하지 않았습니다.')]
    audit=C('검토 범위와 교정 기준','명확한 오식은 7·8쪽 시간 인자의 마지막 +입니다. <a href="#source-check-07">7쪽</a> · <a href="#source-check-08">8쪽</a>에서 원본과 수정 이유를 함께 볼 수 있습니다. 나머지 추가 유도·조건 설명을 원본 오류로 표시하지 않습니다. 영상·스크립트가 없어 ASR 대조는 해당하지 않습니다.')+table(['PDF 쪽','원본 대조와 편집자 처리'],audits)
    sources=C('원본 강의자료','<a href="materials/PDE  - III.pdf" download="PDE  - III.pdf">PDE  - III.pdf</a> · Arshad Afzal · 22쪽 · 날짜·주차 미기재.','한국어 설명, 상세 계산, 일반 문제의 완성 해와 비교 그림은 편집자 작성입니다. 별도 창작 계산 문제·모의시험은 추가하지 않았습니다. 시험 영어는 본문 개념을 영어로 설명하는 표현 연습입니다.')+C('수학적 대조 자료','<a href="https://dlmf.nist.gov/10.2">NIST DLMF §10.2</a> · 베셀 방정식과 J₀의 정의. <a href="https://dlmf.nist.gov/10.21">§10.21</a> · 양의 영점. <a href="https://dlmf.nist.gov/10.22.E37">10.22.37</a> · 베셀 모드의 직교성과 노름.','<a href="https://dlmf.nist.gov/14.2">NIST DLMF §14.2</a> · 르장드르 방정식. <a href="https://dlmf.nist.gov/14.17.E6">14.17.6</a> · order 0에서의 다항식 직교성. 이 항등식을 본문의 변수·구간으로 변환하고 원본 문제의 수치와 적분을 독립 계산했습니다.')
    toc=[('overview','단원 개요'),('concept-map','개념 지도'),('concept-summary','핵심 개념 요약')]+[(f'slide-{n:02}',f'{n:02} · '+p['title']) for n,p in sorted(PAGES.items())]+[('exam-english','시험 영어'),('glossary','핵심 용어'),('asr-log','원본 대조·보강'),('sources','출처')]
    concept='<div class="grid-3">'+C('01 · 직사각형 막','힘과 가속도 → 두 번의 변수분리 → 사인 곱 → 이중 푸리에 계수 → 원본 수치 문제.')+C('02 · 원형 막','극좌표·축대칭 → 0차 베셀 방정식 → 중심 정칙성 → 테두리 영점 → 가중 계수.')+C('03 · 구 바깥의 장','구면좌표·축대칭 → 르장드르 각도 모드 → 감소하는 거리 인자 → 표면 데이터 전개.')+'</div>'
    values={'LECTURE_NUMBER':'PDE III','LECTURE_TITLE':'Partial differential equations III','ONE_SENTENCE_DESCRIPTION':'공업수학 II 편미분방정식 III: 원본 22쪽, 직사각형·원형 막의 진동, 베셀 함수와 구 바깥 라플라스 문제의 상세 풀이·독립 뉴비 해설','WEEK':'공업수학 II','LECTURE_PROMISE':'막의 진동에서 베셀 함수와 구면의 르장드르 급수까지. 원본 22쪽을 보존하고, 기본·뉴비 본문에서 공식의 이유와 원본 문제의 계산을 끝까지 연결합니다.','DATE_OR_날짜_미기재':'미기재','PAGE_COUNT':'22','VIDEO_SET':'PDF 기반 · 강의 영상 없음','ALL_CONTENTS_AND_PROBLEM_SOLVING_BUTTONS':'','ORIGINAL_PDF_URL':'materials/PDE  - III.pdf','LECTURE_NOTE_FILENAME':'PDE  - III.pdf','CORE_RELATIONSHIP_HEADLINE':'경계의 모양이 공간 모드를 고릅니다.','CORE_RELATIONSHIP_EXPLANATION':'직사각형에는 사인 곱, 원형 막에는 베셀 함수, 구면에는 르장드르 다항식이 등장합니다. 좌표와 경계조건으로 함수를 선택하고 직교성으로 주어진 모양을 맞추는 공통 흐름을 익힙니다.','CONCEPT_MAP_HEADLINE':'영역·좌표 → 변수분리 → 허용 모드 → 데이터의 계수','CONCEPT_MAP_BLOCKS':concept,'STANDALONE_CONCEPT_SUMMARY':summary(),'DISTINCT_SUMMARY_VIDEO_SECTION_IF_NEEDED':'','EXAM_SECTION_TITLE':'막의 진동과 구면 해를 설명하는 영어 문장','BILINGUAL_GLOSSARY_TABLE':table(['English(한국어)','뜻과 사용'],terms),'AUDIT_SECTION_TITLE':'원본 대조·보강 기록 · 스크립트 없음','ASR_CORRECTION_TABLE':audit,'SOURCE_LIST_AND_PROVENANCE_NOTE':sources,'TABLE_OF_CONTENTS_LINKS':''.join(f'<li><a href="#{k}">{v}</a></li>' for k,v in toc)}
    template=re.sub(r'<span class="header-meta">.*?</span>','<button type="button" class="mode-toggle" id="mode-toggle" aria-pressed="false">뉴비 모드 켜기</button>',template)
    for k,v in values.items(): template=template.replace('{{'+k+'}}',v)
    template=template.replace('MC2103 Dynamics','MC2202 Engineering Mathematics II').replace('| MC2103','| MC2202')
    template=template.replace('이 부분만 읽어도 렉처의 핵심 정의, 개념 관계, 가정과 풀이 흐름을 이해할 수 있도록 작성합니다.','세 영역에서 달라지는 공간 모드와 공통 풀이 흐름을 먼저 정리합니다. 원본 순서의 본문에서 유도와 계산을 자세히 확인할 수 있습니다.')
    template=template.replace('</head>','<link rel="stylesheet" href="assets/vendor/katex/katex.min.css"><link rel="stylesheet" href="assets/css/math-note.css?v=transforms-1"><link rel="stylesheet" href="assets/css/transforms.css"><script src="assets/js/mode-init.js"></script></head>')
    template=template.replace('<div class="page-shell">','<div class="mode-guide"><strong id="mode-status">기본 모드 · 밝은 화면</strong><p>뉴비 모드는 다크 화면과 함께 본문을 기초부터 풀어 쓴 해설로 바꿉니다. 왜 변수를 나누고, 왜 특정 함수를 고르며, 적분의 부호와 계수가 어디에서 나오는지 이어 설명합니다. English(한국어 번역) 용어 표기는 두 모드에서 유지합니다.</p><p><a href="pde-ii.html">이전 단원 · PDE II</a> · <a href="#slide-10">직사각형 막 문제</a> · <a href="#slide-17">원형 막의 계수</a> · <a href="#slide-19">구 바깥 문제</a></p><noscript>JavaScript가 꺼져 있어 기본·뉴비 해설을 모두 표시합니다.</noscript></div><div class="page-shell">')
    template=template.replace('</body>','<script src="assets/js/math-note.js" defer></script><script src="assets/js/membrane-demo.js" defer></script></body>')
    template=re.sub(r'<!--.*?-->','',template,flags=re.S)
    if '{{' in template: raise RuntimeError('Unresolved PDE III template')
    (SITE/'pde-iii.html').write_text('\n'.join(line.rstrip() for line in template.splitlines())+'\n',encoding='utf-8')
    print('Built PDE III: 22 slides; 13 independent reading pairs + summary')

if __name__=='__main__': build()
