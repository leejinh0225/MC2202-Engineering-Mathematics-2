"""Source-grounded, independently readable explanations for all 36 slides."""
from html import escape

PAGES = {}
AUDITS = []

def M(tex):
    return '<div class="math-block" data-tex="'+escape(tex, quote=True)+'"></div>'

def C(title, *parts, kind='card'):
    return '<div class="'+kind+'"><h3>'+title+'</h3>'+''.join(v if v.startswith('<') else '<p>'+v+'</p>' for v in parts)+'</div>'

def table(head, rows):
    return '<div class="table-wrap"><table class="compare-table"><thead><tr>'+''.join('<th>'+v+'</th>' for v in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+v+'</td>' for v in row)+'</tr>' for row in rows)+'</tbody></table></div>'

def add(n, title, standard, beginner=None, role='개념·유도', audit=None):
    PAGES[n] = dict(title=title, standard=''.join(standard), beginner=''.join(beginner or []), role=role)
    if audit:
        AUDITS.append((n, audit))
        PAGES[n]['audit'] = C('원본 대조 · 해설의 처리', audit, kind='callout')

def paths(standard, beginner):
    return '<div class="reading-path standard-reading"><p class="reading-path__label">기본 해설</p>'+standard+'</div><div class="reading-path beginner-reading"><p class="reading-path__label">뉴비 해설 · 이유부터 차근차근</p>'+beginner+'</div>'

add(1, 'Fourier integrals & transforms(푸리에 적분과 변환)', [
    C('이번 단원에서 연결할 질문', '앞 단원의 Fourier series(푸리에 급수)는 반복되는 함수를 다뤘습니다. 이번에는 한 번만 나타나는 신호를 연속적인 주파수 성분으로 표현하고, 마지막에는 컴퓨터에 저장된 유한 개의 숫자로 같은 생각을 구현합니다.',
      '원본은 Arshad Afzal의 36쪽 PDF입니다. 수업 날짜·주차는 적혀 있지 않습니다. 강의 영상이나 스크립트는 없으며, 아래의 유도·완성 풀이·기초 설명은 편집자 작성입니다.', kind='quiet-card')], role='표지')

add(2, '주기를 무한히 늘리면 급수는 어떻게 달라지는가?', [
    C('반복 신호에서 비주기 신호로', 'Fourier series(푸리에 급수)는 정수배 주파수의 파동을 더합니다. 동일한 펄스가 반복되는 간격을 점점 벌리면, 관찰하는 유한 구간에서는 펄스 하나만 남습니다. 이것이 nonperiodic function(비주기함수)을 주기함수의 극한으로 바라보는 출발점입니다.', M(r"\omega_n=\frac{n\pi}{L},\qquad \Delta\omega=\frac{\pi}{L}\longrightarrow0\quad(L\to\infty)")),
    C('계수의 합에서 주파수 적분으로', '이후 유도에서는 전체 period(주기)를 2L로 통일합니다. L이 커지면 허용 주파수 사이 간격이 작아집니다. 개별 coefficient(계수)는 작아지지만 항의 개수는 늘어납니다. 그 계수를 주파수 간격으로 나눈 밀도가 적분 속 함수가 됩니다.', M(r"a_n=A_L(\omega_n)\Delta\omega,\qquad \sum_n a_n\cos(\omega_nx)\ \leadsto\ \int_0^\infty A(\omega)\cos(\omega x)\,d\omega"))
], [
    C('1 · 먼저 이전 단원과 달라진 문제를 봅니다.', '같은 모양이 계속 반복되면 한 주기만 알면 됩니다. 그런데 한 번의 충격이나 켜졌다 꺼지는 펄스는 영원히 반복되지 않습니다. 그런 함수에도 파동을 섞어 표현하는 방법을 쓰고 싶은 것입니다.', '원본의 세 그림은 같은 사건의 반복 간격을 벌리는 모습으로 읽으십시오. 멀리 있는 복사본이 관찰 구간 밖으로 밀려나면, 가운데의 사건만 보입니다.'),
    C('2 · 왜 갑자기 주파수가 촘촘해질까요?', '주기가 2L이면 가장 느린 기본 파동의 angular frequency(각주파수)는 π/L입니다. n번째 파동은 그 n배입니다. 편집자 예로 L=π이면 주파수 목록은 1, 2, 3, …이고, L=10π이면 0.1, 0.2, 0.3, …입니다. 반복 간격을 늘릴수록 선택 가능한 주파수 간격은 줄어듭니다.', M(r"\omega_{n+1}-\omega_n=\frac{(n+1)\pi-n\pi}{L}=\frac{\pi}{L}=\Delta\omega")),
    C('3 · 더하기가 적분이 되는 이유', '고등학교의 정적분은 폭이 작은 직사각형의 넓이를 모두 더한 극한입니다. 여기서는 가로축이 x가 아니라 주파수 ω입니다. 각 항을 “높이 × 폭 Δω”로 써 놓아야 그 합이 integration(적분)으로 바뀝니다. 그래서 단순히 Σ 기호만 ∫로 바꾸는 것이 아니라, coefficient(계수)에서 Δω를 분리하는 계산을 다음 페이지들에서 합니다.', M(r"\sum_n \underbrace{A_L(\omega_n)\cos(\omega_nx)}_{\text{높이}}\underbrace{\Delta\omega}_{\text{폭}}\ \longrightarrow\ \int_0^\infty A(\omega)\cos(\omega x)\,d\omega"))
])

add(3, 'Fourier integral theorem(푸리에 적분 정리)', [
    C('언제 복원할 수 있는가?', '원본의 충분조건은 각 유한 구간에서 조각별 연속이고 적절한 유한 좌우 미분계수를 가지며, 실수 전체에서 absolutely integrable(절대적분 가능)하다는 것입니다. 실제로 사용할 때는 조각별 매끄러움과 절대적분 가능성을 확인하면 됩니다. 절대적분 가능성만으로 모든 점의 복원을 단정하지 않습니다.', M(r"\int_{-\infty}^{\infty}|f(v)|\,dv<\infty,\qquad f_*(x)=\frac{f(x^-)+f(x^+)}{2}")),
    C('복원 공식과 주파수별 성분', M(r"\begin{aligned}A(\omega)&=\frac1\pi\int_{-\infty}^{\infty}f(v)\cos(\omega v)\,dv,\\B(\omega)&=\frac1\pi\int_{-\infty}^{\infty}f(v)\sin(\omega v)\,dv,\\f_*(x)&=\int_0^\infty[A(\omega)\cos(\omega x)+B(\omega)\sin(\omega x)]\,d\omega.\end{aligned}"), '연속점에서는 f*=f입니다. Jump discontinuity(점프 불연속점)에서는 좌우 극한의 평균을 얻으며, 원래 정해 둔 점의 값과 다를 수 있습니다. 마지막 적분은 주파수 상한 R을 먼저 유한하게 두고 R→∞로 보내는 improper integral(이상적분)입니다.')
], [
    C('1 · 공식이 약속하는 일을 먼저 읽습니다.', '입력은 함수 f입니다. 출력은 그 함수를 만들 때 각 주파수의 cosine(코사인)과 sine(사인)을 얼마나 써야 하는지 나타내는 A와 B입니다. 다시 모든 주파수 성분을 더하면 원래 모양을 되찾습니다. “분해했다가 복원한다”는 왕복 구조입니다.'),
    C('2 · 세 글자 x, v, ω의 역할을 나눕니다.', 'x는 지금 복원하려는 위치입니다. ω는 섞을 파동의 angular frequency(각주파수)입니다. v는 원본 함수 전체를 훑을 때 잠시 사용하는 위치 변수입니다. v에 대해 적분을 끝내면 v는 사라지고 ω에 따른 숫자만 남습니다.', M(r"A(\omega)=\frac1\pi\int_{-\infty}^{\infty}\underbrace{f(v)}_{\text{원본}}\underbrace{\cos(\omega v)}_{\text{비교할 파동}}\,dv"), '원본과 비교 파동을 곱해 더하는 방식은 이전 단원의 inner product(내적)과 연결됩니다. 사인 쪽도 같은 방식으로 B를 얻습니다.'),
    C('3 · 왜 조건이 붙을까요?', '값을 무한한 구간에서 더하므로 결과가 끝없이 커질 수 있습니다. |f|의 적분이 유한하다는 조건은 부호 상쇄에 기대지 않고 전체 크기를 더해도 유한하다는 뜻입니다. 예를 들어 e⁻|x|는 양 끝에서 작아져 조건을 만족하지만, 모든 x에서 f=1인 상수함수는 전체 넓이가 무한합니다.', M(r"\int_{-\infty}^{\infty}e^{-|v|}\,dv=2,\qquad \int_{-\infty}^{\infty}1\,dv=\infty")),
    C('4 · 경계에서는 무엇을 답으로 써야 하나요?', '값이 갑자기 0에서 1로 뛰는 위치에서는 왼쪽도 오른쪽도 한쪽만 특별히 고를 이유가 없습니다. 정리는 그 지점에 두 값의 평균을 돌려줍니다. f*라는 별표는 복원한 값을 원래 점의 값과 구분하기 위한 표기입니다.', M(r"f_*(x)=\frac{f(x^-)+f(x^+)}2;\qquad \frac{0+1}{2}=\frac12"), '따라서 문제를 풀 때 함수의 구간 내부뿐 아니라 점프점도 따로 확인해야 합니다.')
])

add(4, '급수에서 적분으로 · 주파수 간격을 분리하기', [
    C('유한 주기에서 출발', M(r"\begin{aligned} f_L(x)&=a_0+\sum_{n=1}^\infty[a_n\cos(\omega_nx)+b_n\sin(\omega_nx)],\\a_0&=\frac1{2L}\int_{-L}^Lf(v)\,dv,\quad a_n=\frac1L\int_{-L}^Lf(v)\cos(\omega_nv)\,dv,\\b_n&=\frac1L\int_{-L}^Lf(v)\sin(\omega_nv)\,dv,\quad \omega_n=\frac{n\pi}{L}.\end{aligned}"), '이 노트의 상수항은 a₀ 자체이며 a₀/2 규약이 아닙니다. 원본의 일반 주기 급수와 앞 단원의 규약을 그대로 연결합니다.'),
    C('Δω가 적분의 폭이다', M(r"\frac1L=\frac{\Delta\omega}{\pi},\qquad A_L(\omega)=\frac1\pi\int_{-L}^Lf(v)\cos(\omega v)\,dv,\quad a_n=A_L(\omega_n)\Delta\omega"), M(r"|a_0|\leq\frac1{2L}\int_{-\infty}^{\infty}|f(v)|\,dv\longrightarrow0"), '사인 계수도 같은 방식입니다. 절대적분 가능성 때문에 평균항은 0으로 갑니다. 남은 합은 주파수에 대한 Riemann sum(리만 합)의 형태가 됩니다. 무한 급수의 극한 교환을 정당화하는 조건은 p.3의 정리에 맡기고, 여기서는 그 구조를 유도합니다.')
], [
    C('1 · 아는 식을 버리지 않고 다시 씁니다.', '앞 단원에서는 먼저 a₀, aₙ, bₙ을 구하고 파동에 곱해 더했습니다. 이번에도 똑같이 시작합니다. 단지 주기 2L을 아주 크게 만들 준비를 합니다. n은 파동의 번호, ωₙ=nπ/L은 그 파동의 실제 각주파수입니다.', M(r"a_n=\frac1L\int_{-L}^Lf(v)\cos(\omega_nv)\,dv")),
    C('2 · 1/L을 왜 일부러 복잡하게 바꾸나요?', '목적은 합 속에서 작은 폭 Δω를 찾아내는 것입니다. Δω=π/L이므로 1/L=Δω/π입니다. 이 등식을 coefficient(계수)에 넣으면 다음처럼 정확히 나뉩니다.', M(r"a_n=\underbrace{\left[\frac1\pi\int_{-L}^Lf(v)\cos(\omega_nv)\,dv\right]}_{A_L(\omega_n):\ \text{높이}}\Delta\omega"), '이제 aₙcos(ωₙx)는 높이 A_L(ωₙ)cos(ωₙx)에 폭 Δω를 곱한 넓이입니다. 이것이 integration(적분)으로 넘어갈 발판입니다.'),
    C('3 · 평균항 a₀는 왜 사라지나요?', '유한한 넓이를 가진 펄스를 생각해 보십시오. 평균은 펄스의 총넓이를 구간 길이 2L로 나눈 값입니다. 펄스는 그대로인데 분모만 커지므로 평균은 0으로 갑니다. 엄밀하게는 부호가 있는 넓이 대신 |f|의 넓이로 상한을 잡습니다.', M(r"0\leq |a_0|\leq\frac{\int_{-\infty}^{\infty}|f(v)|\,dv}{2L}\to0"), '모든 곳에서 1인 함수에는 이 논리를 적용할 수 없습니다. 그 함수는 분자도 구간 길이만큼 늘고, 정리의 절대적분 조건도 만족하지 않기 때문입니다.'),
    C('4 · 지금까지 얻은 모양', M(r"f_L(x)=a_0+\sum_{n=1}^\infty[A_L(\omega_n)\cos(\omega_nx)+B_L(\omega_n)\sin(\omega_nx)]\Delta\omega"), '이제 남은 일은 L을 늘려 주파수 눈금을 연속적으로 만들고, 원본을 훑는 구간도 실수 전체로 넓히는 것입니다. 다음 페이지가 그 결과입니다.')
])

add(5, '연속 주파수로 함수를 복원하기', [
    C('적분 안의 적분을 읽는 순서', M(r"f_*(x)=\frac1\pi\int_0^\infty\left[\left(\int_{-\infty}^{\infty}f(v)\cos(\omega v)\,dv\right)\cos(\omega x)+\left(\int_{-\infty}^{\infty}f(v)\sin(\omega v)\,dv\right)\sin(\omega x)\right]d\omega"), '안쪽 적분은 고정한 ω에 해당하는 성분을 추출합니다. 바깥 적분은 추출한 모든 성분을 위치 x에서 다시 합칩니다. x는 최종 출력의 변수이므로 적분 뒤에도 남아야 합니다.'),
    C('주파수 밀도의 의미', 'A(ω)는 한 점 주파수의 유한한 급수 계수 자체가 아닙니다. 폭 dω인 작은 주파수 구간이 만드는 기여는 A(ω)cos(ωx)dω입니다. 개별 주파수 간격이 0에 가까워졌을 때도 전체 기여를 유지하는 양이 주파수 밀도입니다.', '진동하는 무한구간 적분은 절대수렴하지 않을 수 있습니다. 안팎 적분 순서를 자유롭게 바꾸거나 각각의 발산 적분으로 분리해서 계산하지 않습니다.')
], [
    C('1 · 중첩된 식은 두 번의 작업입니다.', '큰 식을 한꺼번에 보지 말고 “성분표 만들기 → 성분표로 그림 다시 그리기”로 나눕니다. 첫 작업에서는 ω를 하나 정해 둡니다. 예를 들어 ω=2이면 f(v)에 cos(2v)를 곱해 전체 v에 대해 더합니다. 그러면 A(2)라는 숫자를 얻습니다.', M(r"A(2)=\frac1\pi\int_{-\infty}^{\infty}f(v)\cos(2v)\,dv")),
    C('2 · 성분표를 만든 뒤 x를 정합니다.', '복원하려는 위치가 x=0.3이라면 각 성분의 파동값 cos(0.3ω), sin(0.3ω)를 계산합니다. 여기에 성분표의 값 A(ω), B(ω)를 곱하고 모든 주파수를 더합니다. 그래서 마지막에는 x만 변수로 남습니다.', M(r"f_*(x)=\int_0^\infty[A(\omega)\cos(\omega x)+B(\omega)\sin(\omega x)]\,d\omega")),
    C('3 · 왜 dω를 빼면 안 되나요?', '지도에서 길이 1cm가 실제 얼마인지 정하는 축척처럼, 주파수 눈금의 폭도 합의 크기에 영향을 줍니다. 같은 높이를 두 배 촘촘하게 더하면 항은 두 배로 늘지만 폭은 절반이 되어야 합니다. dω는 그 균형을 보존합니다. A와 B의 1/π 역시 앞 페이지에서 폭을 분리할 때 생긴 값이므로 임의로 지울 수 없습니다.', '앞으로 문제를 풀 때는 먼저 A와 B를 구하고, 그 뒤 복원 공식을 적용하는 순서를 유지하면 중첩 적분에 압도될 필요가 없습니다.')
])

add(6, '예제 · 직사각 펄스와 Dirichlet factor(디리클레 인자)', [
    C('대칭으로 한 계수를 없앤다', M(r"f(x)=\begin{cases}1,&|x|<1,\\0,&|x|>1,\end{cases}\qquad B(\omega)=0,\qquad A(\omega)=\frac2\pi\int_0^1\cos(\omega v)\,dv=\frac{2\sin\omega}{\pi\omega}"), 'Even function(짝함수)이므로 사인 계수는 0입니다. ω=0에서는 식에 바로 대입하지 않고 극한 A(0)=2/π를 취합니다.'),
    C('복원식으로 이상적분 값을 읽는다', M(r"f_*(x)=\frac2\pi\int_0^\infty\frac{\sin\omega\cos(\omega x)}{\omega}\,d\omega"), M(r"\int_0^\infty\frac{\sin\omega\cos(\omega x)}{\omega}\,d\omega=\begin{cases}\pi/2,&|x|<1,\\\pi/4,&|x|=1,\\0,&|x|>1.\end{cases}"), '적분을 직접 끝까지 계산하지 않아도 복원 정리와 원래 함수값으로 값을 구할 수 있습니다. 경계 x=±1에서는 점프의 평균 1/2를 사용합니다.')
], [
    C('1 · 함수의 모양부터 읽습니다.', '−1과 1 사이에서는 높이 1이고 밖에서는 0인 직사각형입니다. 좌우가 거울처럼 같으므로 even function(짝함수)입니다. 여기에 sine(사인)을 곱하면 왼쪽과 오른쪽 넓이가 부호만 달라 상쇄됩니다. 그래서 B는 계산 전에 0이라고 알 수 있습니다.'),
    C('2 · 0이 아닌 구간만 적분합니다.', M(r"A(\omega)=\frac1\pi\int_{-1}^1\cos(\omega v)\,dv=\frac2\pi\left[\frac{\sin(\omega v)}\omega\right]_0^1=\frac{2\sin\omega}{\pi\omega}"), '왜 ω로 나누는지 확인하십시오. sin(ωv)를 v로 미분하면 ωcos(ωv)가 되므로, 원시함수에서는 ω를 나누어 상쇄해야 합니다. ω는 v에 대해 적분하는 동안 상수입니다.', M(r"A(0)=\frac1\pi\int_{-1}^1 1\,dv=\frac2\pi")),
    C('3 · 알고 있는 함수가 적분 문제의 답이 됩니다.', '복원 공식에 A를 넣으면 아래 식입니다. 왼쪽은 이미 알고 있는 직사각형입니다. 따라서 오른쪽 적분을 I(x)라고 놓고 양변에 π/2를 곱하면 I(x)의 값을 바로 읽을 수 있습니다.', M(r"f_*(x)=\frac2\pi I(x),\qquad I(x)=\frac\pi2 f_*(x)")),
    C('4 · 세 구간을 나누어 답합니다.', '안쪽 |x|<1에서는 f*=1이므로 I=π/2입니다. 바깥 |x|>1에서는 f*=0이므로 I=0입니다. 정확히 경계 |x|=1에서는 (1+0)/2=1/2이므로 I=π/4입니다. 원본의 마지막 구간 부등호와 안쪽 구간이 겹치면 이 세 구간 논리로 바로 확인할 수 있습니다.', M(r"I(x)=\begin{cases}\pi/2&(|x|<1),\\\pi/4&(|x|=1),\\0&(|x|>1).\end{cases}"))
], role='예제·완성 풀이', audit='원본 마지막 경우의 조건은 x&lt;1로 적혀 있어 첫 경우와 겹칩니다. 펄스 바깥의 값 0에 해당하는 조건은 x&gt;1입니다. 해설에서는 짝대칭을 포함한 |x| 기준으로 세 구간을 표시합니다.')

add(7, '주파수를 유한하게 잘랐을 때의 복원', [
    C('상한 R은 최고 주파수다', M(r"f_R(x)=\frac2\pi\int_0^R\frac{\sin\omega\cos(\omega x)}\omega\,d\omega"), '원본은 상한을 a로 쓰며 a=8, 16, 32를 비교합니다. 아래에서는 펄스 폭이나 지수 감쇠 상수와 구분하려고 R을 씁니다. R이 커질수록 급격한 모서리를 만드는 높은 주파수가 추가됩니다.'),
    C('Gibbs phenomenon(깁스 현상)을 읽는 기준', '불연속점 주변의 진동 영역은 좁아지지만 최고 초과량은 사라지지 않습니다. 각 연속점에서의 수렴과, 구간 전체에서 최대오차가 0이 되는 균등수렴은 다릅니다. 이 펄스의 점프 크기는 1이고 초과량은 극한에서 약 0.08949입니다.', M(r"f_R(x)=\frac{\operatorname{Si}(R(1+x))+\operatorname{Si}(R(1-x))}{\pi},\qquad \operatorname{Si}(z)=\int_0^z\frac{\sin t}{t}\,dt"), '마지막 식은 곱-합 공식으로 직접 얻은 편집자 보강입니다. 아래 비교 도구는 이 식과 같은 유한 적분을 계산합니다.')
], [
    C('1 · 컴퓨터는 무한히 높은 주파수를 모두 더할 수 없습니다.', '실제로 그릴 때는 “주파수 R까지만 사용한다”고 정합니다. R=8보다 R=32에서는 더 빠르게 흔들리는 파동까지 섞습니다. 빠른 파동은 좁은 구간에서 값이 급격히 변하도록 만드는 데 필요하므로 모서리 근처가 더 날카로워집니다.', M(r"f_R(x)=\frac2\pi\int_0^R\frac{\sin\omega\cos(\omega x)}\omega\,d\omega")),
    C('2 · 그런데 왜 높이 1을 넘어갈까요?', '부드러운 파동을 더해서 갑자기 0에서 1로 뛰는 모양을 만들면 경계 주변에서 파동들이 일부 위치에 겹쳐 초과 진동을 만듭니다. R을 키우면 초과하는 위치가 경계에 더 가까워지고 폭이 좁아집니다. 하지만 가장 높은 초과량 자체는 약 0.08949로 남습니다. 이것이 Gibbs phenomenon(깁스 현상)입니다.'),
    C('3 · 그래프의 어느 점을 보고 있는지 구별합니다.', 'x=0처럼 경계에서 떨어진 고정 위치는 R을 늘릴수록 올바른 값 1에 가까워집니다. 반면 매번 “가장 높게 솟는 위치”를 찾아 움직이면 그 위치도 함께 이동하므로 초과량이 계속 보입니다. 같은 점을 보는 것과 최대점을 따라다니는 것은 서로 다른 관찰입니다.', '경계 x=1에서의 목표값은 1이 아니라 1/2입니다. 유한 R에서 정확히 1/2일 필요는 없고 R→∞에서 그 값에 접근합니다. 아래 도구로 R을 바꾸며 폭, 초과량, 경계값을 따로 살펴보십시오.')
])

add(8, 'Cosine / sine transform(코사인·사인 변환)', [
    C('반구간의 함수로 전체를 표현한다', 'Even extension(짝연장)을 선택하면 B=0이므로 코사인만, odd extension(홀연장)을 선택하면 A=0이므로 사인만 사용합니다. 반구간 x&gt;0의 정보를 어느 대칭으로 연장할지에 따라 변환이 달라집니다.', M(r"\begin{aligned}C[f](\omega)&=s\int_0^\infty f(x)\cos(\omega x)\,dx,&f_*(x)&=s\int_0^\infty C[f](\omega)\cos(\omega x)\,d\omega,\\S[f](\omega)&=s\int_0^\infty f(x)\sin(\omega x)\,dx,&f_*(x)&=s\int_0^\infty S[f](\omega)\sin(\omega x)\,d\omega,\\s&=\sqrt{\frac2\pi}.\end{aligned}")),
    C('정규화 상수를 추적한다', '원본의 f_c, f_s는 여기서 C[f], S[f]로 씁니다. 짝연장에서는 A=sC[f], 홀연장에서는 B=sS[f]이므로 복원식 앞 상수는 s²=2/π가 됩니다. A와 C를 같은 기호처럼 교환하면 계수가 틀어집니다.')
], [
    C('1 · 오른쪽 절반만 주어졌을 때의 선택입니다.', '함수가 x&gt;0에서만 주어졌다면 왼쪽을 같은 높이로 복사할 수도 있고, 부호를 뒤집어 복사할 수도 있습니다. 전자는 even extension(짝연장), 후자는 odd extension(홀연장)입니다. 거울처럼 복사하면 코사인만 필요하고, 부호를 뒤집으면 사인만 필요합니다.'),
    C('2 · 코사인 변환은 무엇을 계산하나요?', M(r"C[f](\omega)=\sqrt{\frac2\pi}\int_0^\infty f(x)\cos(\omega x)\,dx"), '각 ω에 대해 원본 f와 cosine(코사인) 파동의 곱을 더합니다. 결과는 x의 함수가 아니라 ω의 함수입니다. 앞의 √(2/π)는 변환과 역변환의 상수를 같은 모양으로 맞추기로 한 normalization(정규화) 규약입니다.'),
    C('3 · 사인 변환과 두 역변환', M(r"\begin{aligned}S[f](\omega)&=\sqrt{\frac2\pi}\int_0^\infty f(x)\sin(\omega x)\,dx,\\f_*(x)&=\sqrt{\frac2\pi}\int_0^\infty C[f](\omega)\cos(\omega x)\,d\omega,\\f_*(x)&=\sqrt{\frac2\pi}\int_0^\infty S[f](\omega)\sin(\omega x)\,d\omega.\end{aligned}"), '마지막 두 줄은 서로 다른 두 복원 방법입니다. C를 구했으면 코사인으로, S를 구했으면 사인으로 복원합니다. 두 결과를 더하라는 뜻이 아닙니다.'),
    C('4 · 앞 페이지의 A와 무엇이 다른가요?', M(r"A(\omega)=\frac2\pi\int_0^\infty f(x)\cos(\omega x)\,dx=\sqrt{\frac2\pi}C[f](\omega)"), '같은 성분을 나타내도 앞에 붙인 상수가 다릅니다. 문제를 풀기 전에 “지금 구하는 것이 A인가 C인가?”를 확인하십시오. 단순한 표기 차이가 아니라 최종 답의 배율에 영향을 줍니다.')
], audit='원본의 sine inverse transform(사인 역변환) 마지막 미소량은 dx로 인쇄되어 있습니다. 그 줄은 주파수 ω를 합하므로 dω로 읽어야 합니다. 변환·역변환의 상수 √(2/π)는 유지합니다.')

add(9, '선형성과 도함수의 반구간 변환', [
    C('Linearity(선형성)', M(r"T[\alpha f+\beta g]=\alpha T[f]+\beta T[g],\qquad T=C\ \text{또는}\ S"), '변환은 곱셈과 적분으로 이루어진 선형 연산입니다. 적분이 존재하는 함수끼리의 선형결합에 적용합니다.'),
    C('도함수의 변환표 · s=√(2/π)', M(r"\begin{aligned}C[f']&=\omega S[f]-s f(0),&S[f']&=-\omega C[f],\\C[f'']&=-\omega^2C[f]-s f'(0),&S[f'']&=-\omega^2S[f]+s\omega f(0).\end{aligned}"), 'f, f′의 필요한 무한대 경계항이 0이고 해당 적분과 부분적분이 성립한다고 가정합니다. C[f′]는 f를 먼저 미분한 뒤 변환한 것이며 (C[f])′와 다릅니다. 반구간에서는 x=0이 경계이므로 f(0), f′(0)이 남습니다.')
], [
    C('1 · 변환은 더하기와 상수배를 그대로 통과시킵니다.', '함수 3f−2g를 통째로 변환해도 되고, f와 g를 각각 변환한 뒤 3배와 −2배를 해도 같습니다. 이것이 linearity(선형성)입니다. 복잡한 식을 익숙한 조각으로 나누는 근거가 됩니다.', M(r"C[3f-2g]=3C[f]-2C[g]")),
    C('2 · 미분방정식 때문에 이 표가 필요합니다.', '원래 식에 f′나 f″가 있으면 그대로 적분하기가 번거롭습니다. 그런데 transform(변환) 후에는 미분이 ω를 곱하는 계산으로 바뀝니다. 따라서 미분방정식을 더 단순한 대수식으로 바꿀 수 있습니다. 다만 오른쪽 반구간만 쓰기 때문에 출발점 x=0의 값은 따로 남습니다.'),
    C('3 · 사인과 코사인은 미분하면 서로 바뀝니다.', M(r"\frac d{dx}\sin(\omega x)=\omega\cos(\omega x),\qquad \frac d{dx}\cos(\omega x)=-\omega\sin(\omega x)"), '부분적분으로 f 쪽의 미분을 파동 쪽으로 옮기면 C와 S가 서로 교환됩니다. 그래서 S[f′]의 오른쪽에 S[f]가 다시 나오는 것은 한 번 미분한 공식과 맞지 않습니다.', M(r"C[f']=\omega S[f]-s f(0),\qquad S[f']=-\omega C[f],\quad s=\sqrt{2/\pi}")),
    C('4 · 두 번 미분하면 ω도 두 번 곱합니다.', M(r"C[f'']= -\omega^2C[f]-s f'(0),\qquad S[f'']= -\omega^2S[f]+s\omega f(0)"), 'C[f″]는 “f를 두 번 미분한 함수의 코사인 변환”입니다. 다음 페이지에서 한 번 미분 공식을 먼저 얻고 다시 적용하므로 네 개를 따로 외우기 전에 연결을 보십시오. 양 끝의 경계항을 버릴 수 있는지도 반드시 확인합니다.')
], audit='원본 S[f′] 공식에 해당하는 줄은 −ω f_s로 적혀 있습니다. 사인 적분을 부분적분하면 cosine transform(코사인 변환)이 남으므로 올바른 식은 S[f′]=−ωC[f]입니다.')

add(10, '도함수 변환을 부분적분으로 유도하기', [
    C('한 번 미분: 경계항을 먼저 쓴다', M(r"\begin{aligned}C[f']&=s[f(x)\cos(\omega x)]_0^\infty+s\omega\int_0^\infty f(x)\sin(\omega x)\,dx\\&=-s f(0)+\omega S[f],\\S[f']&=s[f(x)\sin(\omega x)]_0^\infty-s\omega\int_0^\infty f(x)\cos(\omega x)\,dx=-\omega C[f].\end{aligned}"), 'x=0에서 cos 0=1, sin 0=0입니다. 무한대에서는 f→0을 이용합니다. 부호는 부분적분의 빼기와 코사인 미분의 빼기가 만나는 위치로 확인합니다.'),
    C('두 번 미분: f를 f′로 교체', M(r"\begin{aligned}C[f'']&=\omega S[f']-s f'(0)=-\omega^2C[f]-s f'(0),\\S[f'']&=-\omega C[f']=-\omega[\omega S[f]-s f(0)]\\&=-\omega^2S[f]+s\omega f(0).\end{aligned}"), 'f′에도 한 번 미분 공식을 적용하려면 f′의 무한대 경계항 역시 소멸해야 합니다. 원본 마지막 줄의 ω 제곱 누락은 이 대입 과정으로 확인됩니다.')
], [
    C('1 · 부분적분은 곱의 미분을 거꾸로 쓴 식입니다.', M(r"(uv)'=u'v+uv'\quad\Longrightarrow\quad\int u'v\,dx=uv-\int uv'\,dx"), '지금은 u=f, v=cos(ωx)로 두어 f′의 미분을 파동 쪽으로 옮깁니다. 그러면 원래 알고 싶은 C[f′]가 이미 정의한 S[f]와 연결됩니다. 계산의 목적이 “미분을 제거하기”라는 점을 먼저 잡으십시오.'),
    C('2 · 코사인 쪽을 한 항씩 계산합니다.', M(r"C[f']=s[f\cos(\omega x)]_0^\infty+s\omega\int_0^\infty f\sin(\omega x)\,dx"), '첫 항의 대괄호는 위끝 값에서 아래끝 값을 빼라는 뜻입니다. f가 무한대에서 0으로 가면 위끝은 0, 아래끝은 f(0)×1입니다. 따라서 −sf(0)이 남습니다. 둘째 항의 s∫f sin은 S[f] 그 자체입니다.', M(r"C[f']=-s f(0)+\omega S[f]")),
    C('3 · 사인 쪽은 아래끝도 0입니다.', M(r"S[f']=s[f\sin(\omega x)]_0^\infty-s\omega\int_0^\infty f\cos(\omega x)\,dx=-\omega C[f]"), 'sin 0=0이라 아래끝 경계항이 사라집니다. 코사인 적분 앞의 s까지 묶어서 C[f]로 바꿉니다. 묶은 뒤에 s를 한 번 더 곱하면 상수를 중복으로 넣는 실수입니다.'),
    C('4 · 같은 공식을 한 번 더 쓰면 끝입니다.', M(r"\begin{aligned}C[f'']&=\omega\underbrace{S[f']}_{-\omega C[f]}-s f'(0)=-\omega^2C[f]-s f'(0),\\S[f'']&=-\omega\underbrace{C[f']}_{\omega S[f]-s f(0)}=-\omega^2S[f]+s\omega f(0).\end{aligned}"), '마지막 줄에서 −ω가 괄호 안 두 항 모두에 곱해집니다. 첫 항에는 ω², 둘째 항에는 두 음수의 곱으로 +가 생깁니다. 다음 예제의 e⁻ᵏˣ를 대입하면 경계값 f(0)=1도 직접 확인할 수 있습니다.')
], audit='원본 사인 변환 유도 중간 줄은 이미 정규화된 f_c에 바깥의 √(2/π)를 또 곱하는 형태이며, 마지막 S[f″] 식에는 ω의 제곱이 빠져 있습니다. 해설은 경계항부터 전개해 정규화 상수와 ω²를 확인합니다.')

from transforms_problems import populate as populate_problems
from transforms_fourier import populate as populate_fourier
from transforms_discrete import populate as populate_discrete
populate_problems(add, C, M, table)
populate_fourier(add, C, M, table)
populate_discrete(add, C, M, table)
assert sorted(PAGES)==list(range(1,37))
