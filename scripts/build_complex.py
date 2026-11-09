"""Week 9-10 source-preserving lecture page, using the shared layout."""
from pathlib import Path
import re
from complex_content import PAGES,C,M,table,paths
from complex_reviews import REVIEWS,source_review
ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'site'

def summary():
    return paths(''.join([
      C('1 · 직교형식은 덧셈, 극형식은 곱셈과 거듭제곱에 적합합니다.',M(r'z=x+iy=re^{i\theta},\quad r=\sqrt{x^2+y^2},\quad\bar z=x-iy,\quad z\bar z=r^2'),M(r'\frac{z_1}{z_2}=\frac{z_1\bar z_2}{|z_2|^2}\quad(z_2\ne0)'), 'Argument(편각)은 2π의 정수배만큼 여러 값이며 principal argument(편각의 주값)는 −π<Arg z≤π로 선택합니다. 0에는 편각을 정하지 않습니다. 각도는 사분면까지 확인합니다.'),
      C('2 · 근은 크기를 n제곱근, 각을 n등분하여 구합니다.',M(r'z^m=r^me^{im\theta}\quad(m\in\mathbb Z),\qquad w_k=r^{1/n}e^{i(\theta+2\pi k)/n},\ k=0,\ldots,n-1'), '정수 음의 지수는 z≠0에서 쓰며 n제곱근은 z≠0일 때 서로 다른 n개입니다. Root of unity(1의 거듭제곱근)는 단위원 위 정n각형의 꼭짓점입니다. √ 기호의 한 가지와 모든 제곱근을 구별합니다.'),
      C('3 · 모든 접근 방향에서 같은 극한이 필요합니다.',M(r'f^\prime(z_0)=\lim_{h\to0}\frac{f(z_0+h)-f(z_0)}h'), '경로 두 개의 값이 다르면 극한은 없습니다. 여러 경로가 같다는 사실만으로 존재가 증명되지는 않습니다. Complex differentiability(복소미분가능성)는 한 점의 성질, analyticity(해석성)는 그 점의 열린 근방 전체에서의 미분가능성입니다. 미분가능하면 연속이지만 역은 성립하지 않습니다.'),
      C('4 · CR을 검사한 뒤 충분조건과 영역을 확인합니다.',M(r'f=u+iv:\quad u_x=v_y,\quad u_y=-v_x,\qquad f^\prime=u_x+iv_x=v_y-iu_y'),M(r'u_r=\frac1r v_\theta,\quad u_\theta=-rv_r,\quad f^\prime=e^{-i\theta}(u_r+iv_r)\quad(r>0)'), 'CR은 미분가능성의 필요조건입니다. 편도함수가 근방에서 존재하고 검사점에서 연속이면 CR은 그 점의 미분가능성에 충분합니다. Entire function(전해석함수)는 복소평면 전체에서 해석적입니다.'),
      C('5 · 지수는 주기적이고 로그는 가지를 선택합니다.',M(r'e^{x+iy}=e^x(\cos y+i\sin y),\qquad e^{z+2\pi ik}=e^z'),M(r'\log z=\{\ln|z|+i(\operatorname{Arg}z+2\pi k):k\in\mathbb Z\},\quad\operatorname{Log}z=\ln|z|+i\operatorname{Arg}z'),M(r'(\operatorname{Log}z)^\prime=1/z\quad\text{on }\mathbb C\setminus(-\infty,0]'), '본 노트는 원본의 대소문자 규약을 사용합니다. 일반 로그의 값 집합과 주값을 섞지 않습니다. 주값의 곱셈 로그법칙에는 2πi 차이가 생길 수 있습니다.'),
      C('6 · 초등함수도 정의와 가지 조건부터 봅니다.',M(r'\cos z=\frac{e^{iz}+e^{-iz}}2,\quad\sin z=\frac{e^{iz}-e^{-iz}}{2i},\quad\cosh z=\frac{e^z+e^{-z}}2,\quad\sinh z=\frac{e^z-e^{-z}}2'),M(r'z^c=e^{c\log z},\qquad\text{principal value: }e^{c\operatorname{Log}z}'), 'sin,cos,sinh,cosh는 전해석이지만 역함수는 로그·제곱근의 여러 가지를 가집니다. 복소 사인·코사인의 크기는 실수에서처럼 1 이하로 제한되지 않습니다. 원본 51–54쪽에서 역함수와 거듭제곱의 계산을 풉니다.'),
      C('원본 연습문제 접근 순서','<p><a href="#slide-55">55쪽 거듭제곱</a>: 극형식 → 드무아브르 → 역수 검산. <a href="#slide-56">56쪽 극한</a>: 축과 대각선 비교. <a href="#slide-57">57쪽 CR</a>: 네 편도함수 → CR → 충분조건 → 열린 근방 확인. <a href="#slide-58">58쪽 증명</a>: 출력 차이를 차분몫×입력 차이로 분해.</p>')
    ]),''.join([
      C('1 · 복소수는 두 숫자로 표시하는 평면의 점입니다.', 'x+iy의 x는 좌우, y는 위아래 위치입니다. 덧셈·뺄셈은 같은 종류끼리 계산합니다. 곱셈에서는 i²=−1을 사용합니다. 나눗셈에서는 분모의 conjugate(켤레)를 곱해 분모를 양의 실수로 바꿉니다.',M(r'(x+iy)(x-iy)=x^2+y^2')),
      C('2 · 거듭제곱할 때는 거리와 각도로 바꿉니다.',M(r'z=r(\cos\theta+i\sin\theta)=re^{i\theta}'), 'Polar form(극형식)에서 곱셈은 거리의 곱과 각도의 합입니다. n번 곱하면 거리 rⁿ, 각 nθ가 됩니다. 반대로 n제곱근은 거리를 n제곱근으로 바꾸고 θ+2πk를 n으로 나눕니다. 원래 각은 한 바퀴를 돌아 같지만 n으로 나누면 서로 다른 답들이 생깁니다.',M(r'w_k=r^{1/n}e^{i(\theta+2\pi k)/n},\quad k=0,1,\ldots,n-1')),
      C('3 · 평면에서는 점으로 다가가는 길이 많습니다.','실수에서는 좌우로 접근했지만 복소수에서는 수평·수직·대각선·곡선 등 모든 방향으로 접근합니다. Limit(극한)이 있으려면 이 길들에서 같은 하나의 값으로 가야 합니다. 그래서 두 길에서 다른 값만 찾아도 극한이 없음을 증명할 수 있습니다. 두 길에서 같으면 아직 나머지 길을 확인하지 않은 상태입니다.'),
      C('4 · 복소미분은 모든 방향에서 같은 기울기를 요구합니다.',M(r'\frac{f(z+h)-f(z)}h'), '위의 difference quotient(차분몫)는 출력 변화량을 입력 변화량으로 나눈 값입니다. 수평으로 계산한 값과 수직으로 계산한 값이 같아야 한다는 요구에서 Cauchy–Riemann equations(코시–리만 방정식)이 나옵니다.',M(r'u_x=v_y,\qquad u_y=-v_x'), 'u는 실수부, v는 허수부입니다. 먼저 네 편도함수를 구하고 두 식을 확인합니다. 그다음 편도함수의 연속성도 확인해야 이 검사만으로 실제 미분가능성을 결론 내릴 수 있습니다.'),
      C('5 · 한 점의 미분과 근방 전체의 미분은 다른 요구입니다.','Differentiable at a point(한 점에서 미분가능)는 그 점 하나의 검사입니다. Analytic at a point(한 점에서 해석적)는 그 주위의 작은 열린 원판 전체에서 미분가능해야 합니다. 원본 57쪽은 축 위에서 미분가능하지만, 어느 작은 원판에도 미분 불가능한 축 밖 점이 있어 해석적이지 않습니다.'),
      C('6 · 로그가 여러 값인 이유는 지수의 회전 때문입니다.',M(r'e^{x+iy}=e^x(\cos y+i\sin y)'), 'x는 출력의 거리, y는 각도를 정합니다. y에 한 바퀴 2π를 더해도 출력이 같습니다. 따라서 출력에서 입력을 찾는 log에는 2πi씩 다른 답이 생깁니다.',M(r'\log z=\ln|z|+i(\operatorname{Arg}z+2\pi k),\quad k\in\mathbb Z'), '그중 정해진 각 범위의 한 값을 고르는 것이 principal value(주값)입니다. 다만 음의 실수축을 위아래로 건너면 고른 각이 π에서 −π로 뛰므로, 주가지의 미분은 그 선과 원점을 뺀 영역에서 합니다.'),
      C('7 · 어려운 새 공식도 지수식으로 되돌려 풉니다.','Sine(사인)와 cosine(코사인)은 eⁱᶻ,e⁻ⁱᶻ를 더하거나 빼서 정의합니다. 역삼각함수는 그 지수값을 미지수 q로 놓으면 이차방정식이 됩니다. q를 푼 다음 로그를 취합니다. 복소 거듭제곱도 zᶜ=eᶜˡᵒᵍᶻ로 계산하므로 여러 로그 값과 선택한 한 값을 구별하는 것이 핵심입니다. 본문은 이 치환·부호·각도 선택을 생략하지 않습니다.'),
      C('마지막 네 문제에서 확인할 것','<p><a href="#slide-55">거듭제곱</a>은 사분면과 음의 지수, <a href="#slide-56">극한</a>은 다른 두 경로, <a href="#slide-57">미분</a>은 CR과 연속인 편도함수, <a href="#slide-58">연속성 증명</a>은 이미 알고 있는 차분몫을 만드는 이유를 확인합니다. 별도 창작 문제 없이 원본 문제를 끝까지 풉니다.</p>')
    ]))

def roots_demo():
    return C('직접 확인 · 1의 3·4·5제곱근','<div class="transform-demo"><p>편집자 그림 · 원본 20–21쪽의 세 경우입니다. 모든 점의 크기는 1이고 이웃한 점의 각 차이는 2π/n입니다.</p><label for="roots-order">근의 개수 n <select id="roots-order"><option value="3">3 · 세제곱근</option><option value="4">4 · 네제곱근</option><option value="5">5 · 다섯제곱근</option></select></label><canvas id="roots-demo" width="960" height="600" role="img" aria-label="단위원 위에 같은 각 간격으로 놓인 1의 거듭제곱근">3제곱근의 각은 0,2π/3,4π/3, 4제곱근은 0,π/2,π,3π/2, 5제곱근은 0,2π/5,4π/5,6π/5,8π/5입니다.</canvas><p id="roots-caption" aria-live="polite">n=3 · 각 간격 2π/3 · 모든 근을 세제곱하면 1입니다.</p><noscript>선택 그림에는 JavaScript가 필요합니다. 원본 그림과 바로 위의 전체 해는 그대로 읽을 수 있습니다.</noscript></div>')

def build():
    assert set(PAGES)==set(range(1,59))
    assert all(PAGES[n]['standard'] and PAGES[n]['beginner'] for n in range(2,59))
    template=(SITE/'templates/lecture-page.template.html').read_text(encoding='utf-8')
    match=re.search(r'        <section class="source-section".*?</section>',template,re.S)
    sections=[]
    for n,p in sorted(PAGES.items()):
        body=source_review(n,M)+(paths(p['standard'],p['beginner']) if p['beginner'] else p['standard'])
        if n==21: body+=roots_demo()
        vals={'NN':f'{n:02}','SLIDE_ROLE':p['role'],'SLIDE_HEADING':p['title'],'LECTURE_SLUG':'complex-numbers-functions','DESCRIPTIVE_ALT_TEXT':f'Week 9–10 원본 PDF {n}쪽: '+p['title'],'CURRENT_PAGE':str(n),'PAGE_COUNT':'58','TRANSCRIPT_TIME_OR_SLIDE_ROLE':'원본 PDF · 한국어 해설·상세 풀이는 편집자 작성','SLIDE_EXPLANATION_BLOCKS':body}
        block=match.group(0)
        for k,v in vals.items(): block=block.replace('{{'+k+'}}',v)
        sections.append(block)
    template=template[:match.start()]+'\n'.join(sections)+template[match.end():]
    exams=[
      ('What is the difference between an argument and the principal argument?','An argument is defined up to an integer multiple of two pi. The principal argument selects one angle in the prescribed interval. Zero has no argument.','Argument(편각)은 여러 값, principal argument(편각의 주값)는 정해진 범위의 한 값입니다.'),
      ('How are the nth roots distributed?','For a nonzero complex number, there are n distinct roots. They have equal moduli and equally spaced arguments, with angular separation two pi divided by n.','Distinct roots(서로 다른 근), modulus(크기), angular separation(각 간격)을 연결합니다.'),
      ('How can a path comparison disprove a limit?','If two paths approaching the same point produce different limiting values, the limit does not exist. Agreement along two paths alone does not prove existence.','경로 비교는 반증에는 충분하지만 두 경로의 일치만으로 존재를 증명하지는 못합니다.'),
      ('State a sufficient Cauchy–Riemann criterion.','Suppose the real and imaginary parts have first partial derivatives in a neighborhood, continuous at the point. If the Cauchy–Riemann equations hold there, the function is complex differentiable at that point.','Sufficient condition(충분조건)에 편도함수의 연속성 가정을 포함합니다.'),
      ('Distinguish differentiability from analyticity.','Differentiability concerns a point. Analyticity at a point requires differentiability throughout some open neighborhood of that point.','Open neighborhood(열린 근방)이라는 추가 범위를 말합니다.'),
      ('Why is the complex logarithm multivalued?','The exponential function has period two pi i. Its inverse therefore includes values that differ by integer multiples of two pi i. A branch chooses values consistently on a suitable domain.','Period(주기) → inverse(역관계) → branch(가지)의 논리입니다.'),
      ('Where is the principal logarithm analytic?','It is analytic on the complex plane with the nonpositive real axis removed. On that domain its derivative is one over z.','Principal branch(주가지)의 domain(정의역)을 도함수와 함께 씁니다.'),
      ('Does complex differentiability imply continuity?','Yes. The change in the function equals the difference quotient times the input change. The quotient has a finite limit and the input change tends to zero.','원본 58쪽 증명의 핵심을 영어로 설명합니다.')]
    exam=''.join('<div class="exam-card"><h3>'+q+'</h3><div class="answer"><span class="answer__label">Model answer</span>'+a+'</div><p>'+k+'</p></div>' for q,a,k in exams)
    start=template.index('            <div class="exam-card">',template.index('id="exam-english"'))
    end=template.index('\n          </div>',start)
    template=template[:start]+exam+template[end:]
    terms=[
      ('Complex number / imaginary unit(복소수 / 허수단위)','z=x+iy, i²=−1. 실수 x,y가 한 복소수를 결정합니다.'),
      ('Real / imaginary part(실수부 / 허수부)','Re z=x, Im z=y. 허수부는 iy가 아니라 실수 y입니다.'),
      ('Complex conjugate(켤레복소수)','z̄=x−iy. 실수축 대칭이며 z z̄=|z|²입니다.'),
      ('Modulus / absolute value(크기 / 절댓값)','|z|=√(x²+y²). 평면에서 원점까지의 거리입니다.'),
      ('Argument / principal argument(편각 / 편각의 주값)','arg z=Arg z+2πk. 원본의 주값 구간은 (−π,π]입니다.'),
      ('Cartesian / polar form(직교형식 / 극형식)','x+iy / r(cosθ+i sinθ)=reⁱᶿ.'),
      ('Euler formula(오일러 공식)','eⁱᶿ=cosθ+i sinθ.'),
      ('De Moivre formula(드무아브르 공식)','정수 거듭제곱은 극형식의 각도에 지수를 곱합니다.'),
      ('Root of unity(1의 거듭제곱근)','wⁿ=1을 만족하는 단위원 위 n개 점입니다.'),
      ('Triangle / reverse triangle inequality(삼각 / 역삼각부등식)','|z₁+z₂|≤|z₁|+|z₂|, ||z₁|−|z₂||≤|z₁+z₂|.'),
      ('Simple / closed curve(단순 / 닫힌 곡선)','자기 교차가 없는 곡선 / 시작점과 끝점이 같은 곡선입니다.'),
      ('Neighborhood / punctured neighborhood(근방 / 뚫린 근방)','중심 주위 열린 원판 / 그 원판에서 중심만 제외한 집합입니다.'),
      ('Interior / exterior / boundary point(내점 / 외점 / 경계점)','어떤 근방 전체가 집합 안 / 밖 / 모든 근방이 안팎을 모두 만나는 점입니다.'),
      ('Open / closed set(열린 / 닫힌 집합)','모든 점이 내점인 집합 / 모든 경계점을 포함하는 집합입니다.'),
      ('Domain / connectedness(영역 / 연결성)','공집합이 아닌 열린 연결집합 / 서로 떨어진 두 상대적 열린 조각으로 나뉘지 않는 성질입니다.'),
      ('Limit / continuity(극한 / 연속성)','모든 접근 방향에서 하나의 값으로 수렴 / 극한과 그 점의 함숫값이 일치합니다.'),
      ('Difference quotient(차분몫)','[f(z+h)−f(z)]/h. h≠0에서 정의하여 h→0을 봅니다.'),
      ('Complex derivative(복소도함수)','모든 복소 방향의 차분몫이 공유하는 유한한 극한입니다.'),
      ('Partial derivative(편도함수)','다른 변수를 고정하고 한 변수로 미분합니다.'),
      ('Cauchy–Riemann equations(코시–리만 방정식)','uₓ=vᵧ, uᵧ=−vₓ. 충분성에는 추가 정칙성 가정을 확인합니다.'),
      ('Analytic / holomorphic(해석적 / 정칙)','열린 근방 전체에서 복소미분가능하다는 뜻으로 사용합니다.'),
      ('Entire function(전해석함수)','복소평면 전체에서 해석적인 함수입니다.'),
      ('Chain / quotient rule(연쇄 / 몫의 미분법)','합성함수의 바깥·안쪽 미분 곱 / 분모가 0이 아닐 때의 몫 미분법입니다.'),
      ('Power series / factorial(거듭제곱 급수 / 계승)','거듭제곱 항들의 무한합 / n!=1·2···n, 0!=1입니다.'),
      ('Periodic function / fundamental region(주기함수 / 기본 영역)','일정 입력 이동 후 출력 반복 / 출력 중복을 제거하도록 고른 영역입니다.'),
      ('Multivalued logarithm / principal value(다가 로그 / 주값)','가능한 로그 값 전체 log z / 선택한 한 값 Log z입니다.'),
      ('Branch / branch cut / branch point(가지 / 가지절단 / 분기점)','다가 관계에서 일관되게 고른 함수 / 그 선택을 위해 제외한 선 / 그 주위를 돌 때 가지가 달라지는 점입니다.'),
      ('Trigonometric / hyperbolic function(삼각 / 쌍곡함수)','복소 지수의 합·차로 정의되며 허수 입력을 통해 서로 연결됩니다.'),
      ('Inverse function / reciprocal(역함수 / 역수)','입력을 되찾는 함수 / 1을 값으로 나눈 수입니다. sin⁻¹과 csc를 구별합니다.'),
      ('Principal power(거듭제곱의 주값)','eᶜᴸᵒᵍᶻ. 여러 로그 값으로 만든 전체 거듭제곱 집합과 구별합니다.')]
    audit=C('원본 확인과 편집자 보강을 구분합니다.','58쪽 전체를 렌더링하여 대조했습니다. 명확한 오식·조건 보강은 해당 원본 바로 아래의 공유 검토 카드 한 곳에 표시합니다. 아래 목록은 그 위치를 찾는 색인입니다. 루트·첨자·괄호가 텍스트 추출 과정에서 빠진 경우에는 원본 이미지를 기준으로 읽었습니다. 영상·스크립트가 없어 ASR 검토는 해당하지 않습니다.')
    audit+=table(['PDF 쪽','검토 분류·이동'],[(str(n),f'<a href="#source-check-{n:02}">{v[0]}</a>') for n,v in REVIEWS.items()])
    audit+=C('오독 방지 확인','13·55쪽은 √3, 51·52쪽은 √2입니다. 13쪽의 7π/6, 15쪽의 5π/4는 주값 구간 밖이지만 올바른 편각입니다. 10쪽 삼각부등식 증명의 켤레와 절댓값, 39쪽 CR 증명의 괄호는 원본대로 유효합니다. 표기를 단순히 낯설다는 이유로 오류로 분류하지 않았습니다.','원본 예제·연습문제의 수치, 부호, 선택한 가지를 독립 계산하고 역대입했습니다. 숫자 검산은 일반 정리의 증명을 대신하지 않으며 일반 논리는 본문의 유도로 제공합니다.')
    sources=C('원본 강의자료','<a href="materials/Week 9 - 10.pdf" download="Week 9 - 10.pdf">Week 9 - 10.pdf</a> · Arshad Afzal · COMPLEX NUMBER &amp; FUNCTIONS · 58쪽. Week 9–10은 파일명 기준이며 정확한 날짜는 미기재입니다.','한국어 해설, 추가 중간 계산과 증명, 원본 3·4·5제곱근의 조작 그림은 편집자 작성입니다. 별도 창작 계산 문제·모의시험은 추가하지 않았습니다. 시험 영어는 본문 개념의 영어 표현 연습입니다.')
    sources+=C('정의역·가지 조건의 대조 자료','<a href="https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/330e301bd727c7bdaa679cf44cb75fe3_MIT18_04S18_topic2.pdf">MIT OCW 18.04, Topic 2</a> · 복소미분·CR의 필요조건과 충분조건 구분.','<a href="https://dlmf.nist.gov/4.2">NIST DLMF §4.2</a> · 로그·거듭제곱·주가지의 정의역. <a href="https://dlmf.nist.gov/4.23">§4.23</a> · 역삼각함수와 로그 표현. <a href="https://dlmf.nist.gov/4.37">§4.37</a> · 역쌍곡함수와 가지 선택. DLMF의 대소문자 표기와 강의의 log / Log 규약은 다르므로 본문은 원본 규약을 유지했습니다.')
    toc=[('overview','단원 개요'),('concept-map','개념 지도'),('concept-summary','핵심 개념 요약')]+[(f'slide-{n:02}',f'{n:02} · '+p['title']) for n,p in sorted(PAGES.items())]+[('exam-english','시험 영어'),('glossary','핵심 용어'),('asr-log','원본 대조·보강'),('sources','출처')]
    concept='<div class="grid-3">'+C('01 · 평면의 수와 계산','2–21쪽 · 사칙연산 → 켤레·거리 → 극형식 → 오일러·드무아브르 → n제곱근.')+C('02 · 평면 위 함수와 미분','22–40쪽 · 곡선·영역 → 함수·극한 → 모든 방향의 미분 → CR → 해석성.')+C('03 · 초등함수와 가지','41–54쪽 · 지수의 주기 → 로그의 여러 값 → 삼각·쌍곡함수 → 역함수·복소 거듭제곱. 55–58쪽 · 원본 연습문제 완성 풀이.')+'</div>'
    values={'LECTURE_NUMBER':'Week 9–10','LECTURE_TITLE':'Complex numbers & functions','ONE_SENTENCE_DESCRIPTION':'공업수학 II 복소수와 복소함수: 원본 58쪽, 사칙연산·극형식·근·복소미분·CR·로그·역함수의 기본 및 독립 뉴비 해설과 전체 예제·연습문제 풀이','WEEK':'공업수학 II','LECTURE_PROMISE':'복소수의 계산에서 모든 방향의 미분과 로그의 가지까지. 원본 58쪽과 예제·연습문제를 보존하고, 기본·뉴비 해설에서 계산을 고르는 이유와 중간 과정을 끝까지 연결합니다.','DATE_OR_날짜_미기재':'미기재','PAGE_COUNT':'58','VIDEO_SET':'PDF 기반 · 강의 영상 없음','ALL_CONTENTS_AND_PROBLEM_SOLVING_BUTTONS':'','ORIGINAL_PDF_URL':'materials/Week 9 - 10.pdf','LECTURE_NOTE_FILENAME':'Week 9 - 10.pdf','CORE_RELATIONSHIP_HEADLINE':'복소수는 계산하는 수이자 평면의 점입니다.','CORE_RELATIONSHIP_EXPLANATION':'거리와 각도로 곱셈을 이해하고, 평면의 모든 방향으로 접근하는 극한으로 미분을 정의합니다. 지수의 회전과 주기를 익히면 로그·제곱근·역함수에서 여러 값과 가지가 등장하는 이유까지 연결됩니다.','CONCEPT_MAP_HEADLINE':'수와 기하 → 영역과 극한 → 복소미분 → 초등함수와 가지','CONCEPT_MAP_BLOCKS':concept,'STANDALONE_CONCEPT_SUMMARY':summary(),'DISTINCT_SUMMARY_VIDEO_SECTION_IF_NEEDED':'','EXAM_SECTION_TITLE':'복소수·미분·가지 조건을 설명하는 영어 문장','BILINGUAL_GLOSSARY_TABLE':table(['English(한국어)','뜻과 사용'],terms),'AUDIT_SECTION_TITLE':'원본 대조·보강 기록 · 스크립트 없음','ASR_CORRECTION_TABLE':audit,'SOURCE_LIST_AND_PROVENANCE_NOTE':sources,'TABLE_OF_CONTENTS_LINKS':''.join(f'<li><a href="#{k}">{v}</a></li>' for k,v in toc)}
    template=re.sub(r'<span class="header-meta">.*?</span>','<button type="button" class="mode-toggle" id="mode-toggle" aria-pressed="false">뉴비 모드 켜기</button>',template)
    for k,v in values.items(): template=template.replace('{{'+k+'}}',v)
    template=template.replace('MC2103 Dynamics','MC2202 Engineering Mathematics II').replace('| MC2103','| MC2202')
    template=template.replace('이 부분만 읽어도 렉처의 핵심 정의, 개념 관계, 가정과 풀이 흐름을 이해할 수 있도록 작성합니다.','계산에 쓰는 형식, 미분의 조건, 여러 값과 가지를 먼저 연결합니다. 원본 순서의 본문에서는 예제·증명의 중간 과정을 자세히 확인할 수 있습니다.')
    template=template.replace('</head>','<link rel="stylesheet" href="assets/vendor/katex/katex.min.css"><link rel="stylesheet" href="assets/css/math-note.css?v=transforms-1"><link rel="stylesheet" href="assets/css/transforms.css"><script src="assets/js/mode-init.js"></script></head>')
    template=template.replace('<div class="page-shell">','<div class="mode-guide"><strong id="mode-status">기본 모드 · 밝은 화면</strong><p>뉴비 모드는 다크 화면과 함께 본문을 기초부터 풀어 쓴 해설로 바꿉니다. 왜 극형식으로 바꾸는지, 왜 모든 경로를 고려하는지, CR과 가지 조건을 언제 확인하는지 이어 설명합니다. English(한국어 번역) 용어 표기는 두 모드에서 유지합니다.</p><p><a href="pde-iii.html">이전 단원 · PDE III</a> · <a href="#slide-04">사칙연산 예제</a> · <a href="#slide-38">제곱근과 가지</a> · <a href="#slide-44">로그 예제</a> · <a href="#slide-55">원본 연습문제 1–4</a></p><noscript>JavaScript가 꺼져 있어 기본·뉴비 해설을 모두 표시합니다.</noscript></div><div class="page-shell">')
    template=template.replace('</body>','<script src="assets/js/math-note.js" defer></script><script src="assets/js/complex-roots.js" defer></script></body>')
    template=re.sub(r'<!--.*?-->','',template,flags=re.S)
    if '{{' in template: raise RuntimeError('Unresolved complex template')
    (SITE/'complex-numbers-functions.html').write_text('\n'.join(line.rstrip() for line in template.splitlines())+'\n',encoding='utf-8')
    print('Built complex numbers/functions: 58 slides; 57 independent reading pairs + summary')

if __name__=='__main__': build()
