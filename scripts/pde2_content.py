"""PDE II: independently readable standard and beginner explanations."""
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

add(1,'Partial differential equations(편미분방정식) · II',[
 C('진동에서 열의 퍼짐으로', '앞 단원의 wave equation(파동방정식)은 처음 모양과 처음 속도로 줄의 진동을 구했습니다. 이번 heat equation(열방정식)은 처음 온도로 이후의 온도를 구합니다. 공간의 Fourier modes(푸리에 모드)는 유지하면서 시간에 따른 변화가 진동에서 감쇠로 달라집니다.', 'Arshad Afzal의 원본 22쪽을 순서대로 보존했습니다. 원본 표지에는 II 표기가 없지만 제공된 파일명에 따라 PDE II로 구분합니다. 날짜·주차·영상·스크립트는 미제공입니다. 아래 한국어 해설, 생략된 유도, 완성 풀이와 조작 그림은 편집자 작성입니다.',kind='quiet-card')],role='표지')

add(2,'Heat equation(열방정식) · 열이 퍼지는 규칙',[
 C('온도의 변화율은 주변 온도 분포의 곡률과 연결됩니다.', M(r'u_t=c^2\nabla^2u,\qquad \nabla^2u=u_{xx}+u_{yy}+u_{zz},\qquad c^2=\frac{K}{\rho C}=:\alpha>0'), 'u는 temperature(온도), K는 thermal conductivity(열전도율), ρ는 density(밀도), C는 specific heat(비열)입니다. Thermal diffusivity(열확산계수) α=c²의 차원은 길이²/시간입니다. PDE I의 파동 속도 c와 물리적 단위가 다릅니다. 이 노트는 원본의 c²를 유지하고 물성값 계산에서만 α를 보조 표기로 씁니다.'),
 C('편집자 유도 · 열 보존과 Fourier’s law(푸리에 열전도 법칙)', '단면적 S인 막대의 얇은 조각 [x,x+Δx]를 생각합니다. 열유속 q는 단위 면적·단위 시간당 이동하는 열이며, 양의 x 방향을 양으로 잡습니다. 뜨거운 쪽에서 차가운 쪽으로 흐르므로 q=−Kuₓ입니다.', M(r'\rho C S\Delta x\,u_t=S[q(x,t)-q(x+\Delta x,t)]\simeq -S\Delta x\,q_x'), M(r'\rho C u_t=-q_x=K u_{xx}\quad\Rightarrow\quad u_t=\frac{K}{\rho C}u_{xx}'), '일정한 물성, 내부 발열 없음, 옆면 단열·단면 내부 온도 균일이라는 1차원 모델의 가정이 쓰였습니다. Fourier’s law(푸리에 열전도 법칙)는 물리 법칙이고, Fourier series(푸리에 급수)는 함수를 표현하는 수학 도구입니다.'),
 C('Diffusion equation(확산방정식)으로도 읽습니다.', '열 대신 농도를 미지함수로 삼아도 같은 형태가 나타납니다. 높은 봉우리의 곡률이 음수이면 온도는 내려가고 낮은 골짜기의 곡률이 양수이면 올라갑니다. 평균화가 일어나며 급한 공간 변화가 먼저 완화됩니다. 모든 위치의 온도가 반드시 감소한다는 뜻은 아닙니다.')
],[
 C('1 · u는 온도계 하나가 아니라 온도계 전체의 기록입니다.', 'u(x,t)는 “왼쪽에서 x만큼 떨어진 곳의 t초 뒤 온도”입니다. x를 고정하고 t로 미분한 uₜ는 그 온도계의 상승·하강 속도입니다. t를 고정하고 x로 미분한 uₓ는 이웃한 위치로 갈 때 온도가 얼마나 달라지는지이고, uₓₓ는 그 기울기가 다시 얼마나 달라지는지입니다.', M(r'u_t=c^2u_{xx}'), 'Heat equation(열방정식)은 주변보다 뾰족하게 뜨거운 곳이 식고, 주변보다 차가운 곳이 데워지는 관계를 나타냅니다. uₜₜ가 아니라 uₜ이므로 처음 온도만 정하면 됩니다.'),
 C('2 · 왜 기울기 앞에 마이너스가 붙나요?', '오른쪽으로 갈수록 차가우면 uₓ<0입니다. 실제 열은 오른쪽, 즉 양의 방향으로 가므로 q>0이어야 합니다. 그래서 Fourier’s law(푸리에 열전도 법칙)는 q=−Kuₓ입니다. 작은 조각으로 들어온 열이 나간 열보다 많으면 그 조각의 온도가 올라갑니다.', M(r'\text{저장되는 열의 변화율}=\text{들어오는 열유량}-\text{나가는 열유량}'), M(r'\rho C S\Delta x\,u_t\simeq-S\Delta x\,q_x\quad\Rightarrow\quad u_t=\frac{K}{\rho C}u_{xx}'), 'S와 Δx를 양변에서 나눈 뒤 q=−Kuₓ를 대입했습니다. 물질이 균일해서 K를 상수로 취급한 것입니다. 옆면으로 열이 새거나 내부에서 열을 만들면 해당 항을 추가해야 합니다.'),
 C('3 · c²는 그냥 계산해야 할 하나의 양수 계수입니다.', 'Thermal conductivity(열전도율) K가 크면 열을 잘 전달하고, ρC가 크면 같은 부피의 온도를 바꾸는 데 많은 열이 필요합니다. 이 둘의 비가 thermal diffusivity(열확산계수)입니다.', M(r'\alpha=c^2=\frac{K}{\rho C}'), '문제에서 K,ρ,C를 주면 먼저 이 비를 계산하십시오. 나중의 지수에 이미 c²가 있으므로 계산한 비를 또 제곱하면 안 됩니다. 같은 문자 c라도 앞 단원의 파동 속도와 단위가 다르다는 점도 기억합니다.')
])

add(3,'양 끝을 0도로 유지하는 막대 · 변수분리',[
 C('PDE와 조건을 먼저 한 묶음으로 씁니다.', M(r'\begin{gathered}u_t=c^2u_{xx},\quad 0<x<L,\ t>0,\\u(0,t)=u(L,t)=0,\qquad u(x,0)=f(x).\end{gathered}'), 'Boundary conditions(경계조건)는 양 끝의 온도, initial condition(초기조건)은 막대 전체의 처음 온도입니다. 끝을 0도로 유지한다는 것은 끝을 단열한다는 뜻이 아닙니다. 끝을 통해 열이 나갈 수 있습니다. 모서리까지 연속인 해를 원하면 f(0)=f(L)=0도 맞아야 합니다.'),
 C('Separation of variables(변수분리법)로 두 ODE를 얻습니다.', M(r'u=F(x)G(t)\quad\Rightarrow\quad FG^\prime=c^2F^{\prime\prime}G\quad\Rightarrow\quad \frac{F^{\prime\prime}}{F}=\frac{G^\prime}{c^2G}=-\mu'), '서로 독립인 x와 t의 함수가 항상 같으려면 공통 상수여야 합니다. −μ는 편리한 표기이며 음수를 미리 가정한 것이 아닙니다. 나눗셈은 FG≠0인 곳에서 수행하고 얻은 ODE의 해를 전체 구간에 연장합니다.', M(r'F^{\prime\prime}+\mu F=0,\quad F(0)=F(L)=0,\qquad G^\prime+c^2\mu G=0')),
 C('비영 해가 있는 분리상수만 남깁니다.', M(r'\begin{array}{c|c|c}\mu&F(x)&F(0)=F(L)=0\ \text{적용}\\\hline 0&A+Bx&A=B=0\\-q^2<0&A\cosh(qx)+B\sinh(qx)&A=B=0\\k^2>0&A\cos(kx)+B\sin(kx)&A=0,\ \sin(kL)=0\end{array}'), M(r'k_n=\frac{n\pi}{L},\qquad \mu_n=k_n^2,\qquad F_n(x)=\sin\frac{n\pi x}{L},\quad n=1,2,\ldots'), 'n=0은 사인 함수 자체가 0이므로 제외합니다. 음의 n은 양의 n과 같은 모드의 부호만 바꿉니다. 여기까지는 고정단 파동방정식과 같은 공간 문제입니다.')
],[
 C('1 · 먼저 “어디를 고정했는가”를 읽습니다.', '막대의 양 끝은 언제나 0도이고, 처음 막대 안의 온도는 f(x)입니다. u(0,t)=0의 0은 위치, u(x,0)=f(x)의 0은 시간입니다. Boundary condition(경계조건)과 initial condition(초기조건)은 같은 식이 아닙니다.', M(r'u(0,t)=u(L,t)=0,\qquad u(x,0)=f(x)'), 'Laterally insulated(옆면이 단열된)는 옆으로 열이 새지 않는다는 뜻입니다. 양 끝을 0도로 붙잡아 두면 끝으로는 열이 빠져나갈 수 있습니다.'),
 C('2 · 복잡한 답 하나 대신 만들기 쉬운 부품부터 찾습니다.', 'Separation of variables(변수분리법)는 u=F(x)G(t)라는 곱을 먼저 시도합니다. F는 공간 모양, G는 그 모양에 곱하는 시간별 배율입니다. 모든 답이 곱 하나라는 주장이 아닙니다. 뒤에서 여러 부품을 합칩니다.', M(r'u_t=F(x)G^\prime(t),\qquad u_{xx}=F^{\prime\prime}(x)G(t)'), 't로 미분할 때 F는 상수처럼 남고, x로 두 번 미분할 때 G가 상수처럼 남습니다. 이 둘을 PDE에 넣어 FG와 c²를 정리합니다.', M(r'FG^\prime=c^2F^{\prime\prime}G\quad\Rightarrow\quad \frac{F^{\prime\prime}}F=\frac{G^\prime}{c^2G}=-\mu'), '오른쪽은 x를 바꿔도 변하지 않습니다. 왼쪽도 변하면 안 되므로 상수입니다. 같은 이유로 t를 바꿔도 상수여야 합니다.'),
 C('3 · 양 끝이 0인 모양을 골라냅니다.', 'μ=0이면 F는 직선이고 두 끝이 0인 직선은 0뿐입니다. μ<0이면 F=Acosh(qx)+Bsinh(qx)인데, F(0)=0에서 A=0, F(L)=0에서 B=0입니다. 따라서 0이 아닌 모양은 μ=k²>0인 경우에서 찾습니다.', M(r'F=A\cos(kx)+B\sin(kx),\qquad F(0)=A=0'), '남은 조건 F(L)=Bsin(kL)=0에서 B까지 0으로 만들면 아무 온도도 표현하지 못합니다. 그래서 sin(kL)=0을 요구합니다. 사인이 0이 되는 각도는 π,2π,3π,…입니다.', M(r'kL=n\pi\quad\Rightarrow\quad F_n(x)=\sin\frac{n\pi x}{L},\quad \mu_n=\left(\frac{n\pi}{L}\right)^2'), '가장 큰 반파 하나, 반파 두 개, 반파 세 개가 길이 L 안에 딱 들어가는 모양을 얻었습니다. n=0은 전부 0인 모양이므로 재료에서 제외합니다.')
])

add(5,'온도 모드는 진동하지 않고 지수적으로 감쇠합니다.',[
 C('시간 방정식을 풉니다.', M(r'G^\prime=-c^2\mu_nG\quad\Rightarrow\quad G(t)=D_ne^{-c^2(n\pi/L)^2t}'), M(r'\boxed{u_n(x,t)=B_n\sin\frac{n\pi x}{L}\,e^{-\lambda_n^2t}},\qquad \lambda_n=\frac{cn\pi}{L}'), 'Bₙ는 공간·시간 해의 상수 배율을 합친 것입니다. 원본이 eigenvalue(고유값)라고 부르는 λₙ와 공간 연산자 −d²/dx²의 고유값 μₙ=(nπ/L)²는 구별합니다. 실제 decay rate(감쇠율)는 λₙ²=c²μₙ입니다. 원본 식을 오류로 바꿀 필요는 없습니다.'),
 C('공식 자체를 미분해 검산합니다.', M(r'(u_n)_t=-\lambda_n^2u_n,\qquad (u_n)_{xx}=-\left(\frac{n\pi}{L}\right)^2u_n,\qquad (u_n)_t=c^2(u_n)_{xx}'), '양 끝에서는 sin 0=sin nπ=0입니다. 높은 n일수록 감쇠율이 n²에 비례하여 커집니다. 공간적으로 자잘한 굴곡이 큰 굴곡보다 빨리 사라집니다.'),
 C('Wave(파동)와 heat(열)의 차이를 고정합니다.', M(r'\text{wave: }G^{\prime\prime}+c^2\mu_nG=0,\qquad \text{heat: }G^\prime+c^2\mu_nG=0'), '파동의 시간 인자는 코사인·사인이고, 열의 시간 인자는 감쇠 지수입니다. 열 문제에 초기속도나 시간 코사인을 넣지 않습니다.')
],[
 C('1 · 공간 모양을 찾았으니 배율 G만 남았습니다.', '앞에서 얻은 μₙ=(nπ/L)²를 G′+c²μₙG=0에 넣습니다. q=c²μₙ>0라 쓰면 G′=−qG입니다. 미분했을 때 원래 함수의 −q배가 되는 함수는 e⁻ᵠᵗ입니다.', M(r'\frac{d}{dt}e^{-qt}=-q e^{-qt}\quad\Rightarrow\quad G=D_ne^{-qt}'), '따라서 각 normal mode(정상모드)는 처음의 공간 모양을 유지하면서 배율이 작아집니다. 파동처럼 양수·음수로 반복 진동하지 않습니다.'),
 C('2 · 원본의 λₙ를 두 번 제곱하지 않습니다.', M(r'\lambda_n=\frac{cn\pi}{L},\quad \lambda_n^2=c^2\left(\frac{n\pi}{L}\right)^2,\quad u_n=B_n\sin\frac{n\pi x}{L}e^{-\lambda_n^2t}'), '원본 exponent(지수)는 −λₙ²t입니다. Thermal diffusivity(열확산계수)는 c²이고, 그것에 (nπ/L)²를 곱한 것이 decay rate(감쇠율)입니다. μₙ는 공간 문제의 eigenvalue(고유값)라는 별도 기호입니다.'),
 C('3 · 두 배로 촘촘하면 네 배로 빨리 줄어듭니다.', 'n=2의 감쇠율은 n=1의 4배이고 n=3은 9배입니다. 처음 모양이 뾰족해도 시간이 흐르면 작은 굴곡을 만드는 성분부터 사라집니다.', M(r'e^{-c^2(2\pi/L)^2t}=e^{-4c^2(\pi/L)^2t}'), '대입 검산에서도 같은 제곱이 나옵니다. 사인을 x로 두 번 미분하면 −(nπ/L)²가 붙고, 지수를 t로 한 번 미분하면 −c²(nπ/L)²가 붙습니다. 그래서 uₜ=c²uₓₓ가 정확히 맞습니다.')
])

add(6,'Fourier sine series(푸리에 사인 급수)로 초기온도를 맞춥니다.',[
 C('중첩한 뒤 t=0을 넣습니다.', M(r'u(x,t)=\sum_{n=1}^{\infty}B_n\sin\frac{n\pi x}{L}e^{-c^2(n\pi/L)^2t},\qquad f(x)=\sum_{n=1}^{\infty}B_n\sin\frac{n\pi x}{L}'), 'Linear homogeneous PDE(선형 제차 편미분방정식)와 제차 경계조건은 중첩을 허용합니다. 무한합의 항별 미분에는 수렴이 필요합니다. 이 단원의 조각별 매끄러운 초기함수는 t>0에서 지수 감쇠 덕분에 매끄러운 해가 됩니다.'),
 C('직교성을 적용하여 원하는 계수만 남깁니다.', M(r'\int_0^L\sin\frac{n\pi x}{L}\sin\frac{m\pi x}{L}\,dx=\begin{cases}0&n\ne m,\\L/2&n=m,\end{cases}'), M(r'\int_0^Lf(x)\sin\frac{m\pi x}{L}\,dx=B_m\frac L2\quad\Rightarrow\quad\boxed{B_n=\frac2L\int_0^Lf(x)\sin\frac{n\pi x}{L}\,dx}'), '원본 6쪽의 급수에서 생략된 coefficient(계수) 계산을 보강한 것입니다. 원본의 틀린 공식을 교정한 것이 아닙니다.'),
 C('풀이 순서와 장시간 거동', '① L,c²,양 끝 조건을 확인합니다. ② f를 보고 단일 사인인지 구간별 함수인지 판단합니다. ③ Bₙ를 구합니다. ④ 각 모드에 감쇠 지수를 곱합니다. ⑤ t=0, 양 끝, PDE에 대입해 확인합니다. 긴 시간이 흐르면 존재하는 모드 중 가장 작은 n이 지배합니다. B₁=0인 경우에는 첫 번째 모드가 지배한다고 말하면 안 됩니다.')
],[
 C('1 · 부품 하나로 안 되면 여러 개를 더합니다.', '각 sine mode(사인 모드)는 양 끝이 0이므로 몇 개를 더해도 양 끝은 0입니다. 서로 다른 공간 모양을 적당한 비율 Bₙ로 더하면 initial temperature(초기온도) f(x)를 만들 수 있습니다.', M(r'u=\sum_{n\ge1}B_n\sin\frac{n\pi x}{L}e^{-c^2(n\pi/L)^2t}'), 't=0에서는 모든 지수함수가 e⁰=1이 됩니다. 따라서 맨 처음 온도를 맞추는 일은 익숙한 Fourier sine series(푸리에 사인 급수)의 계수를 찾는 일입니다.'),
 C('2 · 왜 사인을 곱하고 적분하나요?', '여러 성분이 섞인 합에서 m번째만 골라내고 싶습니다. 양변에 sin(mπx/L)을 곱해 0부터 L까지 적분하면 서로 다른 사인끼리의 곱은 양·음 넓이가 상쇄되어 0이 됩니다. 같은 사인끼리는 제곱이므로 L/2가 남습니다.', M(r'\int_0^Lf(x)\sin\frac{m\pi x}{L}\,dx=0+\cdots+B_m\frac L2+\cdots+0'), M(r'B_m=\frac2L\int_0^Lf(x)\sin\frac{m\pi x}{L}\,dx'), '이 성질이 orthogonality(직교성)입니다. 같은 모드의 제곱 적분 L/2로 나누었기 때문에 2/L가 나왔습니다. 외워야 할 임의의 숫자가 아닙니다.'),
 C('3 · 처음부터 사인 하나라면 그 계수를 그대로 읽습니다.', '원본 18쪽의 100sin(πx/80)은 L=80일 때 첫 모드 그대로입니다. 그러므로 B₁=100, 나머지 계수는 0입니다. 반면 원본 21쪽의 삼각형은 사인 하나가 아니므로 구간을 나누어 적분해야 합니다. Initial condition(초기조건)을 먼저 보는 습관이 불필요한 계산을 줄여 줍니다.'),
 C('4 · 시간에 따라 무엇이 사라질까요?', '모든 모드에는 감소하는 exponential factor(지수 인자)가 붙습니다. 높은 n은 더 빨리 사라지고, 결국 남아 있는 가장 낮은 n의 모양에 가까워집니다. 양 끝이 0도로 유지되는 이 막대는 장시간 뒤 전체가 0도에 가까워집니다. 어느 점의 온도든 처음부터 계속 감소한다고 일반화하지는 마십시오.')
])

add(7,'Steady state(정상 상태) · 세 가지 경계조건',[
 C('시간 변화가 멈추면 Laplace equation(라플라스 방정식)입니다.', M(r'u_t=0\quad\Rightarrow\quad u_{xx}+u_{yy}=0'), '내부 열원이 없고 물성이 일정한 2차원 정상 열전도입니다. Steady(정상)는 시간이 지나도 온도가 변하지 않는다는 뜻입니다. 공간적으로 같은 온도라는 뜻도, 열유속이 0이라는 뜻도 아닙니다.'),
 C('경계에서 무엇을 주는가에 따라 구별합니다.', table(['조건','수학식','온도 문제의 뜻'], [('Dirichlet(디리클레)',M(r'u=g'),'경계 온도를 지정'),('Neumann(노이만)',M(r'\partial_nu=g'),'경계 바깥쪽 법선 방향의 온도 변화율 지정'),('Robin / mixed(로빈 / 혼합)',M(r'a u+b\partial_nu=g'),'온도와 법선미분의 선형 결합 지정')]), '원본의 mixed boundary condition(혼합 경계조건)은 Robin condition(로빈 조건)을 뜻합니다. 경계의 서로 다른 부분에 Dirichlet·Neumann 조건을 나누어 주는 경우도 mixed라고 부르므로 식을 보고 구분합니다. 여기서 a,b는 조건의 계수이며 다음 슬라이드의 직사각형 가로·세로 기호와 별개입니다.'),
 C('Normal derivative(법선미분)의 방향과 열유속 부호', M(r'\partial_nu=\nabla u\cdot\mathbf n,\qquad q_{\mathrm{out}}=-K\partial_nu'), M(r'x=0:\ \partial_nu=-u_x,\qquad x=a:\ \partial_nu=u_x'), 'Insulated(단열) 경계는 q_out=0, 즉 ∂ₙu=0입니다. 온도 0인 경계와 혼동하지 않습니다. 편집자 조건 보강: 열원 없는 영역 전체에 Neumann 데이터를 줄 때는 순유출입의 균형이 필요하며, 온도는 상수만큼의 차이를 남깁니다.')
],[
 C('1 · 정상 상태는 평평한 온도 그래프라는 뜻이 아닙니다.', '어떤 위치는 뜨겁고 다른 위치는 차가워도, 각 위치의 온도가 더 이상 시간에 따라 변하지 않으면 steady state(정상 상태)입니다. 들어오는 열과 나가는 열이 같을 수 있으므로 열은 계속 흐를 수 있습니다.', M(r'u_t=0\quad\Rightarrow\quad u_{xx}+u_{yy}=0'), '시간이 없어졌으므로 처음 온도 대신 영역 둘레에서 주는 boundary conditions(경계조건)를 사용해 내부 온도를 구합니다.'),
 C('2 · 온도를 고정하는 것과 열을 막는 것은 다릅니다.', 'Dirichlet condition(디리클레 조건)은 “이 벽은 언제나 몇 도”입니다. Neumann condition(노이만 조건)은 벽을 가로지르는 온도 기울기를 줍니다. 특히 단열 벽은 열이 못 지나가므로 그 기울기가 0입니다.', M(r'\text{온도 고정: }u=0,\qquad \text{단열: }\frac{\partial u}{\partial n}=0'), 'Robin condition(로빈 조건)은 온도와 그 기울기를 함께 묶어 지정합니다. 원본의 mixed(혼합)는 이 의미입니다. 단순히 “두 종류가 섞였다”로 외우지 말고 au+b∂ₙu=g라는 식까지 봅니다.'),
 C('3 · n은 번호가 아니라 벽의 바깥쪽 방향입니다.', '여기서 n은 Fourier mode(푸리에 모드)의 정수 n과 다른 표기입니다. Normal(법선)은 벽에 수직인 방향이고, outward normal(외향 법선)은 바깥쪽을 향합니다. 왼쪽 벽의 바깥은 −x 방향이므로 −uₓ, 오른쪽 벽의 바깥은 +x 방향이므로 +uₓ입니다.', M(r'\partial_nu=\nabla u\cdot\mathbf n,\qquad q_{\mathrm{out}}=-K\partial_nu'), '열유속은 온도 기울기의 반대 방향입니다. 경계조건이 열유속으로 주어지면 −K도 함께 확인해야 합니다.')
])

add(8,'직사각형의 정상 온도 · 위쪽 경계만 f(x)',[
 C('그림의 네 변을 식으로 옮깁니다.', M(r'\begin{gathered}0<x<a,\quad0<y<b,\quad u_{xx}+u_{yy}=0,\\u(0,y)=u(a,y)=u(x,0)=0,\qquad u(x,b)=f(x).\end{gathered}'), '원본 그림의 위쪽이 f(x), 나머지 세 변이 0입니다. f가 구체적인 함수로 주어지지 않았으므로 Fourier coefficient(푸리에 계수) 적분을 포함한 일반식이 완성 답입니다. 모서리까지 연속인 온도를 요구하면 f(0)=f(a)=0이 필요합니다.'),
 C('편집자 완성 유도 · x에는 사인, y에는 쌍곡사인', M(r'u=F(x)G(y)\quad\Rightarrow\quad \frac{F^{\prime\prime}}F=-\frac{G^{\prime\prime}}G=-k^2'), M(r'F^{\prime\prime}+k^2F=0,\quad G^{\prime\prime}-k^2G=0'), 'x 양 끝의 제차 Dirichlet conditions(디리클레 경계조건)로 k=kₙ=nπ/a, Fₙ=sin(kₙx)를 얻습니다. G=Ccosh(kₙy)+Dsinh(kₙy)에서 아래쪽 조건 G(0)=0을 넣으면 C=0입니다.', M(r'\sinh z=\frac{e^z-e^{-z}}2,\quad\cosh z=\frac{e^z+e^{-z}}2,\quad \frac{d^2}{dy^2}\sinh(ky)=k^2\sinh(ky)')),
 C('위쪽 경계에서 계수를 바로 읽도록 정규화합니다.', M(r'u(x,y)=\sum_{n\ge1}b_n\sin\frac{n\pi x}{a}\,\frac{\sinh(n\pi y/a)}{\sinh(n\pi b/a)}'), 'y=b이면 쌍곡사인 비가 1이므로 f(x)의 사인 급수로 바뀝니다. y=0이면 분자가 0입니다.', M(r'\boxed{b_n=\frac2a\int_0^af(x)\sin\frac{n\pi x}{a}\,dx}'), '분모 sinh(nπb/a)를 빼먹으면 위쪽 온도가 f와 맞지 않습니다. 다른 정규화로 Cₙsinh(nπy/a)를 쓰면 Cₙ=bₙ/sinh(nπb/a)입니다.'),
 C('검산은 두 공간 곡률의 상쇄입니다.', M(r'(u_n)_{xx}=-k_n^2u_n,\quad (u_n)_{yy}=+k_n^2u_n\quad\Rightarrow\quad(u_n)_{xx}+(u_n)_{yy}=0'), '이 문제에서 y는 시간 변수가 아닙니다. 공간 안쪽으로 전달되는 경계의 모양이며 e⁻λ²t 같은 시간 인자를 넣지 않습니다. 네 변의 조건과 내부 PDE를 각각 확인하면 풀이가 닫힙니다.')
],[
 C('1 · 위쪽 벽의 온도가 안쪽으로 어떻게 전달되는지 구합니다.', '가로가 a, 세로가 b인 직사각형입니다. 왼쪽·오른쪽·아래쪽 벽은 0도, 위쪽 벽은 위치 x에 따라 f(x)도입니다. 여기에는 시간이 없습니다. 이미 steady state(정상 상태)에 도달한 온도 지도를 구하는 문제입니다.', M(r'u(0,y)=u(a,y)=u(x,0)=0,\qquad u(x,b)=f(x)'), '원본에는 f(x)의 특정 모양이 없습니다. 따라서 임의로 상수 온도를 만들어 새 문제를 풀지 않고, 어떤 f에도 적용할 수 있는 coefficient(계수) 식을 남깁니다.'),
 C('2 · 이번에도 곱으로 나누지만 부호가 다릅니다.', M(r'u=F(x)G(y),\qquad F^{\prime\prime}G+FG^{\prime\prime}=0\quad\Rightarrow\quad \frac{F^{\prime\prime}}F=-\frac{G^{\prime\prime}}G=-k^2'), 'x 방향은 양 끝이 0인 모양이므로 sin(nπx/a)를 씁니다. 사인을 두 번 미분하면 마이너스가 붙습니다. 두 곡률의 합이 0이 되려면 y 방향은 두 번 미분했을 때 플러스가 붙는 함수여야 합니다.'),
 C('3 · sinh는 새 삼각함수가 아니라 지수함수의 조합입니다.', M(r'\sinh(ky)=\frac{e^{ky}-e^{-ky}}2,\qquad\cosh(ky)=\frac{e^{ky}+e^{-ky}}2'), 'eᵏʸ와 e⁻ᵏʸ를 두 번 미분하면 둘 다 k²배가 됩니다. 그래서 G=Ccosh(ky)+Dsinh(ky)가 맞습니다. 아래 벽 y=0에서는 sinh 0=0, cosh 0=1이므로 C=0만 남깁니다.', M(r'G(y)=D\sinh(ky)'), 'Hyperbolic sine(쌍곡사인) sinh는 sine(사인) sin과 철자도 미분 부호도 다릅니다.'),
 C('4 · 위쪽에서 딱 1이 되게 나눠 둡니다.', M(r'R_n(y)=\frac{\sinh(n\pi y/a)}{\sinh(n\pi b/a)},\qquad R_n(0)=0,\quad R_n(b)=1'), '그러면 bₙsin(nπx/a)Rₙ(y)는 위쪽에서 bₙsin(nπx/a)가 됩니다. 위쪽 온도 f(x)를 사인 부품으로 나눈 계수를 그대로 쓰면 됩니다.', M(r'b_n=\frac2a\int_0^af(x)\sin\frac{n\pi x}{a}\,dx'), M(r'\boxed{u(x,y)=\sum_{n=1}^{\infty}b_n\sin\frac{n\pi x}{a}\frac{\sinh(n\pi y/a)}{\sinh(n\pi b/a)}}'), '왼쪽과 오른쪽은 사인이 0, 아래쪽은 sinh가 0, 위쪽은 Fourier sine series(푸리에 사인 급수)가 f를 재현합니다. 내부에서는 −k²와 +k²가 상쇄되어 Laplace equation(라플라스 방정식)도 만족합니다.')
],role='원본 그림·완성 유도')

def blank(n, target, label):
    add(n,'원본 빈 풀이 페이지', [C('원본 페이지를 그대로 보존합니다.', f'이 페이지에는 새 식이나 문제가 없습니다. 관련 편집자 유도·풀이는 <a href="#slide-{target:02}">{label}</a>에 이어 두었습니다.',kind='quiet-card')],role='빈 풀이 페이지')
for n,target,label in [(4,3,'3쪽 변수분리'),(9,8,'8쪽 직사각형 문제'),(10,8,'8쪽 직사각형 문제'),(11,8,'8쪽 직사각형 문제'),(13,12,'12쪽 무한 막대 해법'),(14,12,'12쪽 무한 막대 해법'),(15,12,'12쪽 무한 막대 해법'),(19,18,'18쪽 구리 막대 문제'),(20,18,'18쪽 구리 막대 문제')]:
    blank(n,target,label)

from pde2_infinite import populate as infinite
from pde2_problems import populate as problems
infinite(add,C,M,table)
problems(add,C,M,table)
