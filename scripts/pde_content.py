"""PDE I: source-checked, independently readable standard and beginner text."""
from html import escape

PAGES = {}

def M(tex):
    return '<div class="math-block" data-tex="'+escape(tex, quote=True)+'"></div>'

def C(title, *parts, kind='card'):
    return '<div class="'+kind+'"><h3>'+title+'</h3>'+''.join(p if p.startswith('<') else '<p>'+p+'</p>' for p in parts)+'</div>'

def table(head, rows):
    return '<div class="table-wrap"><table class="compare-table"><thead><tr>'+''.join('<th>'+v+'</th>' for v in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+v+'</td>' for v in row)+'</tr>' for row in rows)+'</tbody></table></div>'

def paths(standard, beginner):
    return '<div class="reading-path standard-reading"><p class="reading-path__label">기본 해설</p>'+standard+'</div><div class="reading-path beginner-reading"><p class="reading-path__label">뉴비 해설 · 이유부터 차근차근</p>'+beginner+'</div>'

def add(n, title, standard, beginner=None, role='개념·유도'):
    PAGES[n] = dict(title=title, standard=''.join(standard), beginner=''.join(beginner or []), role=role)

add(1, 'Partial differential equations(편미분방정식) · I', [C('여러 위치에서 동시에 일어나는 변화를 구합니다.', '한 물체의 위치를 시간의 함수로 구하던 ordinary differential equation(상미분방정식, ODE)에서, 줄 전체의 모양처럼 위치와 시간에 함께 의존하는 partial differential equation(편미분방정식, PDE)으로 확장합니다. 앞 단원의 Fourier series(푸리에 급수)가 실제 방정식을 푸는 도구로 쓰입니다.', 'Arshad Afzal의 원본 PDF 22쪽을 모두 보존했습니다. 강의 영상·스크립트와 수업 날짜·주차는 제공되지 않았습니다. 아래의 유도, 완성 풀이, 기초 해설과 비교 실험은 편집자 작성입니다. 원본 4:3 화면은 자르거나 늘리지 않고 16:9 틀 안에 배치했습니다.', kind='quiet-card')], role='표지')

add(2, 'PDE의 뜻 · 차수 · 선형성과 제차성', [
 C('미지수는 숫자가 아니라 여러 변수의 함수입니다.', 'u(x,t)에서 x는 위치, t는 시간입니다. Partial derivative(편도함수)는 다른 독립변수를 고정한 채 하나의 변수에 대해서만 미분합니다. 아래 첨자는 미분 횟수·변수를 나타내며 곱셈이 아닙니다.', M(r"u_x=\frac{\partial u}{\partial x},\quad u_t=\frac{\partial u}{\partial t},\quad u_{xx}=\frac{\partial^2u}{\partial x^2},\quad u_{xt}=\frac{\partial^2u}{\partial t\partial x}"), 'Order(차수)는 방정식에 등장하는 가장 높은 미분 차수입니다. 시간 미분이 한 번뿐이어도 공간 2차 미분이 있으면 2차 PDE입니다.'),
 C('Linear(선형)와 homogeneous(제차)를 따로 판단합니다.', 'Linear PDE(선형 편미분방정식)는 u와 그 도함수가 일차로 더해지고, 계수가 독립변수에만 의존합니다. u·uₓ, (uₓ)², sin u처럼 미지량끼리 곱하거나 비선형 함수를 취하면 선형이 아닙니다. 선형식을 L[u]=r로 정리했을 때 r=0이면 homogeneous(제차), 주어진 외부항 r이 0이 아니면 nonhomogeneous(비제차)입니다.', M(r"a(x,t)u_{xx}+b(x,t)u_t+d(x,t)u=r(x,t)")),
 C('원본의 네 식을 읽는 순서', M(r"\begin{aligned}u_{tt}&=c^2u_{xx} &&\text{wave equation}\\u_t&=c^2u_{xx} &&\text{diffusion equation}\\u_{xx}+u_{yy}&=0 &&\text{Laplace equation}\\u_{xx}+u_{yy}&=f(x,y) &&\text{Poisson equation}\end{aligned}"), 'Wave equation(파동방정식)은 줄의 진동, diffusion equation(확산방정식)은 열 등의 퍼짐을 나타냅니다. Laplace equation(라플라스 방정식)은 원천 없는 정상 상태, Poisson equation(푸아송 방정식)은 주어진 원천항이 있는 경우의 대표식입니다. 모두 2차 선형이고, 앞의 셋은 제차입니다. 마지막 식은 f≠0일 때 비제차입니다. 같은 c² 표기를 써도 확산식의 c²는 확산계수이며 파동 속도의 제곱과 물리적 단위가 다릅니다.')
], [
 C('1 · u(x,t)는 한 장의 사진보다 많은 정보를 담습니다.', '줄의 왼쪽에서 x만큼 떨어진 점을 잡고, t초 뒤 그 점의 높이를 재면 u(x,t)입니다. t를 고정하고 x를 바꾸면 그 순간의 줄 모양입니다. x를 고정하고 t를 바꾸면 한 점이 위아래로 움직인 기록입니다. “변수가 두 개”란 이 두 선택을 모두 해야 높이가 정해진다는 뜻입니다.'),
 C('2 · 편미분은 익숙한 미분을 한 변수씩 합니다.', '편집자 예제로 u=x²t+3t를 봅시다. x로 미분할 때 t는 고정된 숫자처럼 두고, t로 미분할 때는 x를 고정합니다.', M(r"u=x^2t+3t\quad\Rightarrow\quad u_x=2xt,\quad u_{xx}=2t,\quad u_t=x^2+3,\quad u_{tt}=0"), 'Partial derivative(편도함수)의 ∂는 “다른 변수는 고정했다”는 표시입니다. uₓₓ는 x를 곱한 것이 아니라 x로 두 번 미분했다는 뜻입니다.'),
 C('3 · 차수와 선형성은 다른 질문입니다.', 'Order(차수)는 “미분을 최대 몇 번 했나?”입니다. Linear(선형)는 “u와 미분한 것들을 일차로만 조합했나?”입니다. uₓₓ는 두 번 미분했지만 선형이고, (uₓ)²는 한 번 미분했지만 제곱했으므로 비선형입니다. 변수 x가 계수로 붙는 것은 괜찮지만 미지함수 u가 또 붙으면 곱셈이 생깁니다.', M(r"u_{xx}+x u_t=0\quad\text{2차, 선형};\qquad (u_x)^2+u_t=0\quad\text{1차, 비선형}")),
 C('4 · 방정식은 변화들 사이의 규칙입니다.', 'Wave equation(파동방정식) uₜₜ=c²uₓₓ는 “한 점의 가속도는 그 주변 줄의 휘어진 정도에 비례한다”는 규칙입니다. 꼭대기처럼 아래로 굽으면 아래쪽 가속도가 생깁니다. Diffusion equation(확산방정식)은 가속도가 아닌 변화율 uₜ를 곡률에 연결합니다.', M(r"u_{tt}-c^2u_{xx}=0,\qquad u_t-c^2u_{xx}=0"), 'Homogeneous(제차)는 이처럼 미지함수 항을 모았을 때 오른쪽이 0이라는 뜻입니다. u 자체가 항상 0이라는 뜻은 아닙니다. Laplace equation(라플라스 방정식) uₓₓ+uᵧᵧ=0도 같은 분류이고, Poisson equation(푸아송 방정식) uₓₓ+uᵧᵧ=f(x,y)는 별도로 주어진 f가 0이 아닐 때 비제차입니다.')
])

add(3, '변수계수와 비선형을 구별하는 세 예제', [
 C('x가 계수에 들어가도 선형입니다.', M(r"a u_t+b x u_x=0"), 'a,b가 주어진 상수라면 bx는 독립변수 x의 함수입니다. u와 u의 도함수에는 일차 연산만 하므로 linear variable-coefficient PDE(선형 변수계수 편미분방정식)입니다. 적어도 하나의 미분항이 남는 경우 1차이며 제차입니다.'),
 C('미지함수끼리 곱하거나 도함수를 제곱하면 비선형입니다.', M(r"u u_x+b u_y=0,\qquad a(u_x)^2+b u_y=0"), '첫 식의 u·uₓ는 미지량의 곱이고, 둘째 식의 (uₓ)²는 도함수의 제곱입니다. 두 식 모두 1차 미분까지만 등장하므로 1차 PDE입니다. 둘째 식은 a≠0일 때 비선형이라는 전제가 필요합니다. 첫 식은 최고차 도함수 uₓ,uᵧ 자체에는 선형인 quasilinear(준선형) 예이기도 합니다.'),
 C('선형성의 직접 점검 · 편집자 검산', '선형 연산자 L에는 L[αu+βv]=αL[u]+βL[v]가 성립합니다. N[u]=u·uₓ에는 배율을 두 번 받는 항이 생깁니다.', M(r"L[2u]=2L[u],\qquad N[2u]=(2u)(2u_x)=4u u_x\ne2N[u]\quad\text{in general}"))
], [
 C('1 · 기준은 x가 아니라 u입니다.', '이 방정식에서 구하려는 것은 u입니다. x는 우리가 선택하는 위치 숫자입니다. 그래서 a uₜ+bx uₓ=0에서 bx가 위치마다 달라져도 “알려진 숫자 × 미지량”입니다. 이를 variable coefficient(변수계수)라 부르며 linear(선형) 성질은 유지됩니다.', M(r"a u_t+b x u_x=0")),
 C('2 · u·uₓ는 왜 안 될까요?', 'u를 두 배로 바꾸면 uₓ도 두 배가 됩니다. 그러면 둘을 곱한 값은 네 배입니다. 입력을 두 배로 했을 때 출력도 두 배가 되는 선형 연산의 규칙과 맞지 않습니다.', M(r"u\mapsto2u\quad\Rightarrow\quad u u_x\mapsto(2u)(2u_x)=4u u_x"), 'u uₓ+b uᵧ=0은 이런 항을 포함하므로 nonlinear PDE(비선형 편미분방정식)입니다. 오른쪽이 0이라는 사실만으로 선형이라고 판단하면 안 됩니다.'),
 C('3 · 제곱과 두 번 미분을 구별합니다.', M(r"(u_x)^2=(\text{x로 한 번 미분한 값})^2,\qquad u_{xx}=\text{x로 두 번 미분한 값}"), 'a(uₓ)²+b uᵧ=0에서 a≠0이면 도함수의 제곱 때문에 비선형입니다. 하지만 order(차수)는 1차입니다. “제곱이 있으니 2차 PDE”라고 쓰지 않도록 괄호 위치를 확인하십시오. a=0이면 그 비선형 항이 사라지므로 남은 식을 다시 판단해야 합니다.')
])

add(4, '해와 중첩 원리 · uₓₓ − u = 0 완성 풀이', [
 C('Solution(해)은 식을 영역 전체에서 만족하는 함수입니다.', 'Classical solution(고전해)은 필요한 도함수가 존재하고 각 점에서 PDE를 만족합니다. Homogeneous linear PDE(제차 선형 편미분방정식)의 해 u₁,u₂에 상수를 곱해 더해도 해입니다. 단, 같은 비제차 우변을 가진 해를 단순히 더하면 우변도 두 배가 됩니다.', M(r"L[u_1]=L[u_2]=0\quad\Rightarrow\quad L[c_1u_1+c_2u_2]=c_1L[u_1]+c_2L[u_2]=0"), 'PDE의 해라는 것과 지정된 initial/boundary conditions(초기·경계조건)까지 맞는 것은 별개입니다. 무한합은 미분과 합의 교환 등 수렴 조건도 확인해야 합니다.'),
 C('원본 문제 · x에 대해서 풀고 나머지 변수는 남깁니다.', M(r"u_{xx}-u=0"), '원본은 다른 독립변수의 이름을 지정하지 않았으므로 여기서는 u=u(x,y)로 둡니다. y를 고정하면 x에 대한 상미분방정식입니다. 지수함수 eʳˣ를 대입하면 특성방정식 r²−1=0이 나옵니다.', M(r"r^2-1=0\ \Rightarrow\ r=\pm1,\qquad \boxed{u(x,y)=A(y)e^x+B(y)e^{-x}}"), 'A,B는 상수에 한정되지 않는 임의함수입니다. 다른 독립변수가 t라면 A(t),B(t)로 씁니다. y방향 미분을 요구하지 않는 이 식 자체에는 y방향 조건이 없으며, 요구하는 해의 정칙성에 맞게 A,B를 택합니다.'),
 C('대입 검산과 임의함수의 의미', M(r"u_x=A(y)e^x-B(y)e^{-x},\qquad u_{xx}=A(y)e^x+B(y)e^{-x}=u"), '따라서 PDE가 성립합니다. 편집자 예로 A(y)=y², B(y)=sin y도 가능합니다. 경계·초기조건이 없으므로 하나의 특정 함수로 결정할 수 없습니다. A,B를 단순 상수로 쓰면 해의 일부만 제시한 것입니다.')
], [
 C('1 · 방정식을 푼다는 것은 함수를 찾아 확인하는 일입니다.', '숫자 방정식 x+2=5의 답은 숫자 3이지만, PDE의 답은 함수입니다. 이번 문제 uₓₓ−u=0은 “x로 두 번 미분하면 자기 자신이 되는 함수를 찾아라”입니다. eˣ는 두 번 미분해도 eˣ이고, e⁻ˣ도 두 번 미분하면 부호가 두 번 바뀌어 e⁻ˣ가 됩니다.', M(r"(e^x)''=e^x,\qquad (e^{-x})'=-e^{-x},\qquad (e^{-x})''=e^{-x}")),
 C('2 · 왜 두 함수를 더해도 될까요?', '미분은 더하기와 상수배를 그대로 통과합니다. 그래서 eˣ에 어떤 수를 곱하고 e⁻ˣ에 다른 수를 곱해 더해도 두 번 미분하면 그대로 돌아옵니다. 이것이 superposition principle(중첩 원리)입니다. 단, homogeneous linear equation(제차 선형방정식)에 적용하는 원리이며 아무 비선형 식에나 적용하지 않습니다.'),
 C('3 · “상수”가 A(y)라는 함수가 되는 이유', 'u(x,y)를 생각하고 y=1에 줄 하나, y=2에 다른 줄 하나를 그린다고 상상하십시오. x로 미분하는 동안 y는 고정되어 있으므로 각 줄마다 다른 계수를 써도 됩니다. y가 달라질 때 계수가 바뀌는 것을 A(y), B(y)로 기록합니다.', M(r"u(x,y)=A(y)e^x+B(y)e^{-x}"), '예를 들어 y=1에서는 A(1)=1, y=2에서는 A(2)=4인 A(y)=y²를 써도 됩니다. 원본은 y라는 이름을 쓰지 않았으므로, 남은 변수가 t라면 그대로 A(t),B(t)로 바꾸면 됩니다.'),
 C('4 · 한 줄씩 검산하면 끝납니다.', M(r"\begin{aligned}u_x&=A(y)e^x-B(y)e^{-x},\\u_{xx}&=A(y)e^x+B(y)e^{-x},\\u_{xx}-u&=0.\end{aligned}"), 'A(y)는 x로 미분할 때 숫자처럼 취급합니다. 이것이 partial derivative(편도함수)의 핵심입니다. 추가 조건이 없으므로 A,B의 구체적인 모양을 더 정할 근거는 없습니다.')
], role='개념·문제 풀이')

from pde_wave import populate as populate_wave
populate_wave(add, C, M, table)
from pde_travel import populate as populate_travel
populate_travel(add, C, M, table)
from pde_practice import populate as populate_practice
populate_practice(add, C, M, table)

for n, target, label in [(6,5,'변수분리와 경계조건'),(7,5,'분리상수의 세 경우'),(8,9,'시간해와 정상모드'),(11,10,'초기조건과 푸리에 계수'),(18,17,'PDE 분류'),(20,19,'특성곡선'),(22,21,'삼각형 초기변위 문제')]:
    add(n, '원본 빈 풀이 페이지', [C('원본 페이지 보존', f'이 페이지에는 페이지 번호·하단 표식 이외의 식이나 문제가 없습니다. 관련 편집자 유도와 풀이는 <a href="#slide-{target:02}">{target}쪽 · {label}</a>에 모았습니다.', kind='quiet-card')], role='빈 풀이 공간')

assert sorted(PAGES) == list(range(1,23))
