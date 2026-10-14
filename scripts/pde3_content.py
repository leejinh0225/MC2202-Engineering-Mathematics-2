"""PDE III source-page content. Each substantive page has two complete paths."""
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
    PAGES[n]=dict(title=title,standard=''.join(standard),beginner=''.join(beginner or []),role=role)

def source_review(n):
    if n not in (7,8): return ''
    return ('<div class="callout source-review" id="source-check-'+str(n).zfill(2)+'" data-review-kind="error"><h3>원본 오류 확인 · 시간 인자 끝의 불필요한 +</h3><p><strong>원본 표기:</strong> 코사인 항과 사인 항 뒤, 닫는 괄호 바로 앞에 +가 하나 더 인쇄되어 있습니다.</p>'+M(r'B_{mn}\cos(\lambda_{mn}t)+B_{mn}^{*}\sin(\lambda_{mn}t)')+'<p><strong>판단 근거:</strong> 시간 ODE의 일반해는 위 두 항으로 완성됩니다. 항이 없는 마지막 +만 제외합니다. 두 항 사이의 +와 별표 계수는 유지하며, 원본 PDF·이미지는 수정하지 않습니다.</p></div>')

add(1,'Partial differential equations(편미분방정식) · III',[
 C('줄의 진동에서 막의 진동으로, 평면에서 구면으로', '이번 단원은 rectangular membrane(직사각형 막), circular membrane(원형 막), 구 바깥의 Laplace equation(라플라스 방정식)을 다룹니다. 경계의 모양에 따라 사인, Bessel function(베셀 함수), Legendre polynomial(르장드르 다항식)이 등장하는 이유를 연결합니다.', 'Arshad Afzal의 원본 22쪽을 순서대로 보존했습니다. 표지에 III가 없어 파일명으로 단원을 구분합니다. 주차·날짜·영상·스크립트는 미제공입니다. 한국어 해설, 생략된 유도, 원본 문제의 완성 풀이와 조작 그림은 편집자 작성입니다.',kind='quiet-card')],role='표지')

add(2,'Two-dimensional wave equation(2차원 파동방정식)',[
 C('막의 수직 변위를 구합니다.', M(r'u_{tt}=c^2(u_{xx}+u_{yy}),\qquad c^2=\frac{\tau}{\sigma}'), 'u(x,y,t)는 막의 평면에 수직인 displacement(변위), τ는 단위 길이당 tension(장력), σ는 단위 면적당 mass density(질량밀도)입니다. 균일한 막, 일정하고 등방적인 장력, 작은 기울기, 무시할 수 있는 굽힘강성·감쇠·외력을 가정합니다. c는 wave speed(파동 속도)이며 c²의 단위는 길이²/시간²입니다. 앞 열방정식의 c²와 단위가 다릅니다.'),
 C('편집자 유도 · 작은 조각의 힘과 가속도', '면적 dx dy인 조각의 질량은 σ dx dy입니다. 작은 기울기에서 x방향 양 끝 장력의 수직 성분 차는 τuₓₓ dx dy, y방향 차는 τuᵧᵧ dx dy가 됩니다.', M(r'\sigma\,dx\,dy\,u_{tt}=\tau\,dx\,dy\,(u_{xx}+u_{yy})'), '공통 면적을 나누면 위 PDE를 얻습니다. 주변에 비해 솟은 봉우리는 곡률 합이 음수이므로 아래쪽 가속도를 받습니다.'),
 C('경계와 처음 상태를 구별합니다.', M(r'u|_{\partial\Omega}=0,\quad t\ge0;\qquad u(x,y,0)=f(x,y),\quad u_t(x,y,0)=g(x,y)'), '원본의 u=0은 fixed boundary(고정 경계)에서의 조건입니다. 막 전체가 항상 0이라는 뜻이 아닙니다. Initial displacement(초기변위)는 처음 모양, initial velocity(초기속도)는 처음 움직임입니다. 시간에 대한 2차 PDE이므로 둘 다 필요합니다. 경계까지 매끄러운 해를 원하면 초기 데이터도 고정 경계와 맞아야 합니다.')
],[
 C('1 · 고무막 위의 위치 하나를 지정해 봅니다.', 'x,y는 막 위의 가로·세로 위치이고 t는 시간입니다. u(x,y,t)는 그 지점이 기준 평면보다 얼마나 올라갔는지를 나타냅니다. Partial derivative(편미분)는 나머지 변수를 고정하고 한 변수만 바꾸는 미분입니다.', M(r'u_t=\text{수직 속도},\quad u_{tt}=\text{수직 가속도},\quad u_{xx},u_{yy}=\text{두 방향의 곡률}'), 'Wave equation(파동방정식)은 “막이 굽어 있으면 장력이 이를 펴려는 힘을 주고, 그 힘 때문에 가속된다”는 관계입니다. 온도가 퍼지던 이전 단원과 달리 막은 관성 때문에 평평한 곳을 지나 계속 움직일 수 있습니다.'),
 C('2 · 왜 장력을 질량밀도로 나누나요?', '같은 모양이면 팽팽하게 당길수록 힘이 크고, 무거울수록 가속도는 작습니다. Newton’s law(뉴턴 법칙)인 힘=질량×가속도를 작은 막 조각에 적용합니다.', M(r'\underbrace{\tau\,dx\,dy(u_{xx}+u_{yy})}_{\text{수직 합력}}=\underbrace{\sigma\,dx\,dy}_{\text{질량}}u_{tt}'), M(r'u_{tt}=\frac{\tau}{\sigma}(u_{xx}+u_{yy})=c^2(u_{xx}+u_{yy})'), 'τ는 길이당 힘, σ는 면적당 질량입니다. 체적밀도를 그대로 넣으면 단위가 맞지 않습니다. 이 식은 아주 크게 휘어진 막까지 그대로 적용하는 모델은 아닙니다.'),
 C('3 · 테두리의 조건과 시작 순간의 조건은 역할이 다릅니다.', 'Boundary condition(경계조건)은 “테두리는 언제나 움직이지 않는다”입니다. Initial condition(초기조건)은 “막 전체가 처음에는 어떤 모양이고 어떤 속도인가”입니다.', M(r'u|_{\partial\Omega}=0,\qquad u(x,y,0)=f(x,y),\qquad u_t(x,y,0)=g(x,y)'), '손으로 들어 올렸다가 밀지 않고 놓으면 f는 0이 아닐 수 있지만 g=0입니다. g=0이라고 이후에도 정지하는 것은 아닙니다. 휘어진 막에는 복원력이 작용합니다. 원본의 u=0을 막 전체의 조건으로 읽으면 이 처음 모양과 모순되므로 경계에 적용합니다.')
])

add(3,'Rectangular membrane(직사각형 막) · 두 번의 변수분리',[
 C('영역과 네 변을 지정합니다.', M(r'0<x<a,\quad0<y<b,\qquad u(0,y,t)=u(a,y,t)=u(x,0,t)=u(x,b,t)=0'), '원본 그림의 가로는 a, 세로는 b입니다. 먼저 u=F(x,y)G(t)로 공간·시간을 나누고, 다시 F=X(x)Y(y)로 두 공간 방향을 나눕니다.'),
 C('공간과 시간의 분리', M(r'FG^{\prime\prime}=c^2(F_{xx}+F_{yy})G\quad\Rightarrow\quad\frac{F_{xx}+F_{yy}}F=\frac{G^{\prime\prime}}{c^2G}=-\mu'), M(r'F_{xx}+F_{yy}+\mu F=0,\qquad G^{\prime\prime}+c^2\mu G=0'), '서로 독립인 좌표와 시간만의 함수가 항상 같으므로 공통 상수입니다. 함수로 나눈 단계는 0이 아닌 구간에서 수행하고, 얻은 ODE의 해는 전체 영역으로 이어집니다.'),
 C('가로와 세로의 분리', M(r'F=XY\quad\Rightarrow\quad \frac{X^{\prime\prime}}X+\frac{Y^{\prime\prime}}Y=-\mu'), M(r'\frac{X^{\prime\prime}}X=-p^2,\quad\frac{Y^{\prime\prime}}Y=-q^2,\quad\mu=p^2+q^2'), M(r'X^{\prime\prime}+p^2X=0,\quad Y^{\prime\prime}+q^2Y=0,\quad G^{\prime\prime}+c^2(p^2+q^2)G=0'), '양의 p²,q²가 필요한 이유는 다음 경계조건에서 확인합니다. Separation of variables(변수분리법)는 곱 하나로 표현되는 부품을 찾는 단계입니다. 임의의 초기함수는 여러 부품의 합으로 맞춥니다.')
],[
 C('1 · 줄 하나 대신 가로·세로가 있는 막입니다.', 'PDE I에서는 x와 t가 있었습니다. 지금은 y가 추가되어 u(x,y,t)입니다. 먼저 F(x,y)를 고정된 공간 모양, G(t)를 그 모양에 곱하는 시간별 배율이라고 생각합니다.', M(r'u=F(x,y)G(t),\quad u_{tt}=FG^{\prime\prime},\quad u_{xx}+u_{yy}=(F_{xx}+F_{yy})G'), '시간으로 미분할 때 F는 상수처럼 남고, 공간으로 미분할 때 G가 상수처럼 남습니다. 이것을 PDE에 대입한 뒤 FG와 c²를 정리합니다.'),
 C('2 · 왜 갑자기 상수가 나오나요?', M(r'\frac{F_{xx}+F_{yy}}F=\frac{G^{\prime\prime}}{c^2G}=-\mu'), '왼쪽은 x,y만, 오른쪽은 t만 봅니다. 시간을 고정하고 위치를 아무리 바꿔도 오른쪽은 그대로이므로 왼쪽도 같아야 합니다. 시간도 같은 논리입니다. 따라서 두 값은 공통 상수입니다. −μ는 나중에 사인·코사인 방정식을 편하게 쓰기 위한 이름입니다.', M(r'F_{xx}+F_{yy}=-\mu F,\qquad G^{\prime\prime}=-c^2\mu G')),
 C('3 · 남아 있는 공간 함수도 한 번 더 나눕니다.', 'F=X(x)Y(y)라고 시도하면 x를 미분할 때 Y는 상수, y를 미분할 때 X는 상수입니다.', M(r'X^{\prime\prime}Y+XY^{\prime\prime}=-\mu XY\quad\Rightarrow\quad \frac{X^{\prime\prime}}X+\frac{Y^{\prime\prime}}Y=-\mu'), '두 항의 합이 항상 일정하므로 x만의 첫 항과 y만의 둘째 항도 각각 일정해야 합니다. 첫 항을 −p², 둘째를 −q²라 부르면 합은 −(p²+q²)입니다.', M(r'\mu=p^2+q^2,\quad X^{\prime\prime}=-p^2X,\quad Y^{\prime\prime}=-q^2Y,\quad G^{\prime\prime}=-c^2(p^2+q^2)G'), '이제 세 변수 문제가 한 변수짜리 ODE(상미분방정식) 세 개가 되었습니다. 다음에는 네 변이 움직이지 않는 조건으로 p,q를 고릅니다.')
])

add(6,'Boundary conditions(경계조건)가 허용하는 사인 모드',[
 C('네 변의 고정 조건을 두 쌍으로 나눕니다.', M(r'X(0)=X(a)=0,\qquad Y(0)=Y(b)=0'), M(r'X=A\cos(px)+B\sin(px)\ \Rightarrow\ A=0,\quad\sin(pa)=0'), M(r'p_m=\frac{m\pi}{a},\quad q_n=\frac{n\pi}{b},\qquad m,n=1,2,\ldots'), '각 1차원 고정단 고유문제에서 분리상수가 0이면 직선, 음수이면 쌍곡함수가 나오지만 양 끝 조건으로 영해만 남습니다. 양의 고유값에서 사인 모드를 얻습니다. n=0 또는 m=0도 함수 자체가 0이므로 제외합니다.'),
 C('공간 고유값과 각진동수를 구별합니다.', M(r'\phi_{mn}(x,y)=\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b},\qquad \mu_{mn}=\left(\frac{m\pi}{a}\right)^2+\left(\frac{n\pi}{b}\right)^2'), M(r'\lambda_{mn}=c\sqrt{\mu_{mn}}=c\pi\sqrt{\left(\frac ma\right)^2+\left(\frac nb\right)^2}'), '원본의 λₘₙ는 시간 cos(λₘₙt)에 들어가는 angular frequency(각진동수)입니다. 공간 연산자 −∇²의 eigenvalue(고유값)는 μₘₙ입니다. 진동수는 λₘₙ/(2π), 단일 모드의 주기는 2π/λₘₙ입니다.')
],[
 C('1 · 왼쪽에서 0인 함수부터 고릅니다.', 'X″+p²X=0의 해는 사인과 코사인의 합입니다. cos 0=1이고 sin 0=0이므로 X(0)=0을 넣으면 코사인 앞의 A가 사라집니다.', M(r'X=A\cos(px)+B\sin(px),\qquad X(0)=A=0'), '이제 오른쪽 끝도 0이어야 합니다. B까지 0으로 두면 아무 움직임도 표현하지 못하므로 sin(pa)=0을 만족하는 p를 찾습니다.', M(r'pa=m\pi\quad\Rightarrow\quad X_m=\sin\frac{m\pi x}{a},\quad m=1,2,\ldots'), '같은 계산을 세로에 하면 Yₙ=sin(nπy/b)입니다. Boundary conditions(경계조건)가 사인의 길이와 번호를 골라 준 것입니다.'),
 C('2 · 0이나 음수인 분리상수는 왜 버리나요?', '0이면 X=A+Bx이고 양 끝이 0인 직선은 전부 0뿐입니다. 음수이면 X=Acosh(px)+Bsinh(px)인데 X(0)=0에서 A=0, X(a)=0에서 B=0입니다. 그래서 쓸 수 있는 비영 모드는 사인이 나오는 양의 경우입니다.'),
 C('3 · 가로·세로의 촘촘함이 진동 속도를 정합니다.', M(r'\phi_{mn}=\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}'), 'm은 가로 방향의 반파 개수, n은 세로 방향의 반파 개수입니다. 둘 중 하나라도 커지면 막이 더 자주 굽으므로 복원력이 커지고 빠르게 진동합니다.', M(r'G^{\prime\prime}=-\lambda_{mn}^2G,\qquad \lambda_{mn}=c\pi\sqrt{(m/a)^2+(n/b)^2}'), 'Angular frequency(각진동수)는 1초 동안 위상이 몇 라디안 변하는가입니다. 한 바퀴 2π 라디안이 걸리는 시간이므로 주기는 2π/λₘₙ입니다. 원본의 eigenvalue(고유값)라는 명칭과 공간 고유값 μₘₙ를 구별해서 읽습니다.')
])

add(7,'Normal mode(정상모드) · 공간 모양 × 시간 진동',[
 C('한 모드의 완성식', M(r'u_{mn}=\left[B_{mn}\cos(\lambda_{mn}t)+B_{mn}^{*}\sin(\lambda_{mn}t)\right]\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}'), 'Bₘₙ와 Bₘₙ*는 서로 독립인 실수 계수입니다. 여기의 별표는 complex conjugate(복소켤레)가 아닙니다. 초기변위와 초기속도에서 각각 결정합니다. 사인은 두 번 미분하면 음의 자기 배수가 되므로 PDE의 양변에 같은 −λₘₙ² 인자가 생깁니다.'),
 C('Nodal line(마디선)과 기본 진동', M(r'x=\frac{ja}{m}\ (j=1,\ldots,m-1),\qquad y=\frac{kb}{n}\ (k=1,\ldots,n-1)'), '한 모드에서 위 선들은 언제나 변위가 0입니다. (1,1)은 내부 마디선이 없고 가장 낮은 각진동수를 갖습니다. 같은 각진동수를 갖는 서로 다른 모드가 생길 수도 있지만 공간 모양은 독립입니다. 여러 모드를 섞으면 개별 모드의 마디선이 전체 해의 마디선으로 유지된다고 보장할 수 없습니다.')
],[
 C('1 · 세 함수의 곱을 다시 조립합니다.', '가로 모양은 Xₘ, 세로 모양은 Yₙ입니다. 시간 ODE의 해는 cos(λt),sin(λt)의 합입니다. 이들을 곱하면 normal mode(정상모드) 하나가 됩니다.', M(r'u_{mn}=\underbrace{[B_{mn}\cos(\lambda_{mn}t)+B_{mn}^{*}\sin(\lambda_{mn}t)]}_{\text{시간별 배율}}\underbrace{\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}}_{\text{고정된 공간 모양}}'), '공간 사인 안에는 x 또는 y, 시간 삼각함수 안에는 t가 있습니다. 이 위치를 섞지 마십시오. 별표가 붙었다고 곱하거나 켤레를 취하라는 뜻은 아닙니다. 두 번째 계수의 이름일 뿐입니다.'),
 C('2 · 코사인과 사인을 둘 다 쓰는 이유', M(r'G(0)=B_{mn},\qquad G^\prime(0)=\lambda_{mn}B_{mn}^{*}'), 'cos 0=1,sin 0=0이므로 처음 높이는 첫 계수가 담당합니다. 미분하면 cos는 −λsin, sin은 λcos가 되므로 처음 속도에는 두 번째 계수가 남습니다. Initial velocity(초기속도)를 계수로 바꿀 때 λ로 나눠야 하는 이유도 이것입니다.'),
 C('3 · 움직이지 않는 선을 찾는 법', '곱의 어느 한 사인이 0이면 전체 변위가 0입니다. sin(mπx/a)=0에서 x=ja/m을 얻고, 세로도 같습니다. 이러한 nodal line(마디선)은 한 모드에서 계속 정지합니다.', M(r'(m,n)=(1,1):\ \text{내부 마디선 없음};\qquad(m,n)=(2,1):\ x=a/2'), 't 때문에 순간적으로 전체 막이 0을 지나는 것과, 특정 위치가 모든 시간에 0인 마디선은 다릅니다. 또 여러 모드를 합치면 각 모드의 마디선이 서로 채워질 수 있습니다.')
])

add(8,'Double Fourier series(이중 푸리에 급수) · 두 초기조건',[
 C('모드를 중첩합니다.', M(r'u(x,y,t)=\sum_{m=1}^{\infty}\sum_{n=1}^{\infty}[B_{mn}\cos(\lambda_{mn}t)+B_{mn}^{*}\sin(\lambda_{mn}t)]\phi_{mn}(x,y)'), '선형 제차 PDE와 고정 경계조건에 대해 모드를 합칠 수 있습니다. 무한합의 미분·초기값 해석에는 데이터의 매끄러움과 수렴 조건이 필요합니다. 적절한 매끄러운 호환 데이터에서는 고전해로, 더 일반적인 데이터에서는 에너지 해 등으로 해석합니다.'),
 C('두 방향의 직교성이 계수를 골라냅니다.', M(r'\int_0^a\!\int_0^b\phi_{mn}\phi_{pq}\,dy\,dx=\frac{ab}{4}\delta_{mp}\delta_{nq}'), M(r'\boxed{B_{mn}=\frac4{ab}\int_0^a\!\int_0^b f(x,y)\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}\,dy\,dx}'), M(r'\boxed{B_{mn}^{*}=\frac4{ab\lambda_{mn}}\int_0^a\!\int_0^b g(x,y)\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}\,dy\,dx}'), 't=0에서 u=ΣBφ, uₜ=ΣλB*φ입니다. 각 방향의 사인 제곱 적분 a/2,b/2를 곱하면 ab/4이므로 계수 앞에 4/(ab)가 붙습니다. g=0이면 모든 B*=0입니다.'),
 C('조건을 만족하는 순서', '고정 경계조건으로 공간 모드를 고르고, PDE로 시간 각진동수를 정한 뒤, f와 g로 두 계수를 구합니다. 감쇠를 넣지 않은 wave equation(파동방정식)이므로 열 문제의 지수 감쇠를 붙이지 않습니다. 전체 에너지는 보존되지만 위치별 변위는 계속 달라집니다.')
],[
 C('1 · 부품의 번호가 두 개여서 합도 두 번입니다.', 'Double Fourier series(이중 푸리에 급수)는 가로 번호 m과 세로 번호 n을 모두 바꾸어 모드를 더한 것입니다. 공간 모양을 φₘₙ이라고 짧게 부릅니다.', M(r'u=\sum_{m,n\ge1}[B_{mn}\cos(\lambda_{mn}t)+B_{mn}^{*}\sin(\lambda_{mn}t)]\phi_{mn}'), '처음 시간 t=0을 넣으면 코사인은 1, 사인은 0입니다. 따라서 초기 모양 f는 ΣBₘₙφₘₙ이어야 합니다.'),
 C('2 · 왜 곱하고 적분하면 원하는 성분만 남나요?', 'Orthogonality(직교성) 때문에 서로 다른 번호의 사인 곱 적분은 0입니다. 같은 번호의 사인 제곱은 sin²z=(1−cos2z)/2를 써서 적분하면 구간 길이의 절반입니다.', M(r'\int_0^a\sin^2\frac{m\pi x}{a}\,dx=\left[\frac x2-\frac{a}{4m\pi}\sin\frac{2m\pi x}{a}\right]_0^a=\frac a2'), M(r'\int_0^a\!\int_0^b f\phi_{mn}\,dy\,dx=B_{mn}\frac a2\frac b2\quad\Rightarrow\quad B_{mn}=\frac4{ab}\int_0^a\!\int_0^b f\phi_{mn}\,dy\,dx'), '가로 번호가 같아도 세로 번호가 다르면 세로 적분에서 0이 됩니다. 두 번호가 모두 같아야 살아남습니다. δ는 같으면 1, 다르면 0을 표시하는 Kronecker delta(크로네커 델타)입니다.'),
 C('3 · 속도는 먼저 시간 미분한 뒤 맞춥니다.', M(r'u_t=\sum_{m,n\ge1}[-\lambda_{mn}B_{mn}\sin(\lambda_{mn}t)+\lambda_{mn}B_{mn}^{*}\cos(\lambda_{mn}t)]\phi_{mn}'), M(r'g=\sum_{m,n\ge1}\lambda_{mn}B_{mn}^{*}\phi_{mn}\quad\Rightarrow\quad B_{mn}^{*}=\frac4{ab\lambda_{mn}}\int_0^a\!\int_0^b g\phi_{mn}\,dy\,dx'), '초기속도의 Fourier coefficient(푸리에 계수)는 λB*입니다. 그러므로 B*만 구하려면 λ로 한 번 더 나눕니다. Initially at rest(처음에 정지)는 g=0이라는 뜻이며, 이때 시간 코사인만 남습니다. 처음 들어 올린 높이 f까지 0이 된다는 뜻은 아닙니다.')
])

add(10,'원본 문제 · 4 ft × 2 ft 막을 들어 올렸다 놓기',[
 C('주어진 값과 물성을 정확히 옮깁니다.', M(r'a=4\ \mathrm{ft},\ b=2\ \mathrm{ft},\ \tau=12.5\ \mathrm{lbf/ft},\ \sigma=2.5\ \mathrm{slug/ft^2}'), M(r'f(x,y)=0.1(4x-x^2)(2y-y^2),\qquad g(x,y)=0'), '원본의 lb/ft는 장력의 단위이므로 lbf/ft로 해석합니다. 이미 질량이 slug 단위이므로 중력가속도 32.2를 다시 곱하거나 나누지 않습니다. x,y를 ft 단위 수치로 넣으면 f는 ft로 주어지는 식입니다.', M(r'c^2=\frac{12.5}{2.5}=5\ \mathrm{ft^2/s^2},\quad c=\sqrt5\ \mathrm{ft/s},\quad\lambda_{mn}=\frac{\pi\sqrt5}{4}\sqrt{m^2+4n^2}')),
 C('곱으로 주어진 초기함수는 두 적분으로 나눕니다.', M(r'B_{mn}=\frac{4(0.1)}{4\cdot2}\left[\int_0^4x(4-x)\sin\frac{m\pi x}{4}\,dx\right]\left[\int_0^2y(2-y)\sin\frac{n\pi y}{2}\,dy\right]'), 'f가 x만의 함수와 y만의 함수의 곱이므로 직사각형 영역의 이중적분이 두 단일적분의 곱이 됩니다. 공통 모양을 Iⱼ(L)로 계산합니다.'),
 C('편집자 완성 풀이 · 부분적분 두 번', M(r'I_j(L)=\int_0^Lz(L-z)\sin(kz)\,dz,\qquad k=\frac{j\pi}{L}'), M(r'I_j=\left[-\frac{z(L-z)\cos(kz)}k\right]_0^L+\frac1k\int_0^L(L-2z)\cos(kz)\,dz'), M(r'I_j=\left[\frac{(L-2z)\sin(kz)}{k^2}\right]_0^L+\frac2{k^2}\int_0^L\sin(kz)\,dz=\frac{2[1-\cos(j\pi)]}{k^3}'), M(r'I_j(L)=\frac{2L^3[1-(-1)^j]}{j^3\pi^3}=\begin{cases}0&j\text{ even},\\4L^3/(j^3\pi^3)&j\text{ odd}.\end{cases}'), '첫 경계항은 z(L−z)=0, 두 번째는 sin0=sin(jπ)=0이어서 사라집니다. cos(jπ)=(−1)ʲ에 따라 짝수 모드는 없어집니다.'),
 C('계수와 최종 변위', M(r'B_{mn}=\frac{102.4[1-(-1)^m][1-(-1)^n]}{\pi^6m^3n^3}=\begin{cases}\dfrac{409.6}{\pi^6m^3n^3}&m,n\text{ both odd},\\0&\text{otherwise},\end{cases}\qquad B_{mn}^{*}=0'), M(r'\boxed{u(x,y,t)=\frac{409.6}{\pi^6}\sum_{\substack{m,n\ge1\\m,n\ \mathrm{odd}}}\frac{\cos\!\left(\frac{\pi\sqrt5}{4}\sqrt{m^2+4n^2}\,t\right)}{m^3n^3}\sin\frac{m\pi x}{4}\sin\frac{n\pi y}{2}}'), '이는 원본의 임의 초기변위·정지 조건을 모두 맞춘 완성 해입니다. 한 개의 사인으로 초기 포물면 곱 전체를 정확히 대체하지 않습니다.'),
 C('검산과 물리적 의미', M(r'f(2,1)=0.1\cdot4\cdot1=0.4\ \mathrm{ft},\qquad\lambda_{11}=\frac{5\pi}{4},\quad T_{11}=\frac{2\pi}{\lambda_{11}}=1.6\ \mathrm{s}'), '네 변에서 공간 사인이 0이고, t=0에서 시간 미분은 0입니다. 각 항은 PDE를 만족하며 초기 급수는 f를 재현합니다. 1.6초는 (1,1) 모드의 주기입니다. 서로 다른 각진동수의 합인 전체 막의 정확한 반복 주기라고 부르지 않습니다.')
],[
 C('1 · 구하려는 답과 주어진 모양부터 읽습니다.', '구할 것은 막의 모든 위치와 시간에서의 높이 u(x,y,t)입니다. 가로 4 ft, 세로 2 ft이고 테두리는 고정되어 있습니다. 처음 높이는 f=0.1(4x−x²)(2y−y²), 처음 속도는 0입니다.', M(r'4x-x^2=x(4-x),\qquad 2y-y^2=y(2-y)'), '이렇게 인수분해하면 x=0,4 또는 y=0,2에서 f=0임이 바로 보입니다. 시작 모양부터 고정 테두리와 맞습니다. 중앙 (2,1)은 0.4 ft 올라가 있지만 initially at rest(처음에 정지)이므로 밀어 주지는 않습니다.'),
 C('2 · 속도 c와 시간 삼각함수의 각을 계산합니다.', M(r'c^2=\frac{\tau}{\sigma}=\frac{12.5}{2.5}=5,\qquad c=\sqrt5'), '단위는 c²가 ft²/s², c가 ft/s입니다. lbf=slug·ft/s²이므로 slug 질량을 주었을 때 추가 중력가속도 변환은 없습니다.', M(r'\lambda_{mn}=\pi\sqrt5\sqrt{\frac{m^2}{16}+\frac{n^2}{4}}=\frac{\pi\sqrt5}{4}\sqrt{m^2+4n^2}'), '통분하면 분모가 16이므로 제곱근 밖으로 4가 나옵니다. 세로 길이 b=2에서 생기는 4n²를 놓치지 마십시오. g=0이면 시간 인자는 코사인만 남습니다.'),
 C('3 · 필요한 계수 공식에 f를 그대로 넣습니다.', M(r'B_{mn}=\frac4{ab}\int_0^a\!\int_0^b f(x,y)\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}\,dy\,dx'), M(r'B_{mn}=0.05\left[\int_0^4x(4-x)\sin\frac{m\pi x}{4}\,dx\right]\left[\int_0^2y(2-y)\sin\frac{n\pi y}{2}\,dy\right]'), '앞의 수는 4/(4×2)×0.1=0.05입니다. y로 적분할 때 x에 관한 부분은 상수라서 밖으로 뺄 수 있습니다. 그다음 x로 적분하면 두 적분의 곱이 됩니다. 적분 두 개는 길이만 다르고 같은 모양입니다.'),
 C('4 · 부분적분은 다항식의 차수를 낮추려고 씁니다.', 'Integration by parts(부분적분)는 곱의 미분 (UV)′=U′V+UV′를 적분해 얻은 공식입니다. 다항식은 미분하면 단순해지고 삼각함수는 적분해도 다룰 수 있으므로 이 조합에 잘 맞습니다.', M(r'\int U V^\prime dz=UV-\int U^\prime V\,dz'), M(r'I_j(L)=\int_0^Lz(L-z)\sin(kz)\,dz,\qquad k=j\pi/L'), 'U=z(L−z)이면 U′=L−2z입니다. V′=sin(kz)이면 V=−cos(kz)/k입니다. 코사인을 미분할 때 −k가 나오므로 이를 상쇄하는 −1/k가 필요합니다.', M(r'I_j=\left[-\frac{z(L-z)\cos(kz)}k\right]_0^L+\frac1k\int_0^L(L-2z)\cos(kz)\,dz'), 'z=0과 z=L에서 z(L−z)=0이므로 첫 항은 0입니다. 부분적분 공식의 빼기와 V의 빼기가 만나 남은 적분 앞은 플러스입니다.'),
 C('5 · 한 번 더 부분적분하고 끝점 값을 넣습니다.', '이제 U=L−2z, U′=−2, V′=cos(kz), V=sin(kz)/k로 잡습니다. 앞에 이미 1/k가 있으므로 곱해서 1/k²가 됩니다.', M(r'I_j=\left[\frac{(L-2z)\sin(kz)}{k^2}\right]_0^L+\frac2{k^2}\int_0^L\sin(kz)\,dz'), 'kL=jπ이므로 sin(kL)=0이고 sin0=0입니다. 경계항이 다시 없어집니다. 마지막 적분은 −cos(kz)/k를 위끝에서 계산한 값에서 아래끝 값을 빼면 됩니다.', M(r'\int_0^L\sin(kz)\,dz=\frac{-\cos(kL)+\cos0}{k}=\frac{1-(-1)^j}{k}'), M(r'I_j(L)=\frac{2L^3[1-(-1)^j]}{j^3\pi^3}'), 'cos(jπ)는 j가 짝수면 1, 홀수면 −1입니다. 따라서 짝수면 1−1=0, 홀수면 1−(−1)=2가 됩니다.'),
 C('6 · 두 길이를 넣고 숫자를 끝까지 정리합니다.', M(r'I_m(4)=\frac{256}{m^3\pi^3}\ (m\text{ odd}),\qquad I_n(2)=\frac{32}{n^3\pi^3}\ (n\text{ odd})'), M(r'B_{mn}=0.05\frac{256\cdot32}{m^3n^3\pi^6}=\frac{409.6}{m^3n^3\pi^6}\quad(m,n\text{ both odd})'), '4×4³=256, 4×2³=32, 0.05×256×32=409.6입니다. m,n 중 하나만 짝수여도 그 방향의 적분이 0이라 전체 계수도 0입니다. “둘 다 홀수”라는 조건을 붙입니다.'),
 C('7 · 계수·공간 모양·시간 배율을 합칩니다.', M(r'\boxed{u=\frac{409.6}{\pi^6}\sum_{\substack{m,n\ge1\\m,n\ \mathrm{odd}}}\frac{\sin(m\pi x/4)\sin(n\pi y/2)}{m^3n^3}\cos\!\left(\frac{\pi\sqrt5}{4}\sqrt{m^2+4n^2}\,t\right)}'), '이 식은 m=1,3,5,…와 n=1,3,5,…를 각각 넣어 모두 더하라는 뜻입니다. Fourier coefficient(푸리에 계수)는 처음 모양의 배합비, 두 사인의 곱은 공간 모양, 코사인은 시간 변화입니다. 한 가지 역할씩 조립하면 긴 식도 읽을 수 있습니다.'),
 C('8 · 처음과 테두리를 확인하면 부호 실수를 잡을 수 있습니다.', 'x=0,4와 y=0,2에서는 사인이 0이라 고정 조건이 맞습니다. t=0에서는 cos0=1이어서 처음 모양을 재현하고, 시간 미분에는 sin0=0이 있어 초기속도도 0입니다. 중앙 높이도 f(2,1)=0.4 ft와 비교합니다.', M(r'\lambda_{11}=\frac{\pi\sqrt5}{4}\sqrt5=\frac{5\pi}{4},\qquad T_{11}=\frac{2\pi}{5\pi/4}=\frac85=1.6\ \mathrm{s}'), 'Fundamental mode(기본 모드)는 1.6초마다 반복됩니다. 전체 답에는 여러 코사인이 있으므로 막 전체가 반드시 1.6초마다 처음 모양으로 돌아오는 것은 아닙니다. 아래 조작 그림은 이 원본 문제의 합을 근사해 보여 줍니다.')
],role='원본 문제 · 상세 완성 풀이')

def blank_pages():
    for n,target,label in [(4,3,'두 번의 변수분리'),(5,6,'고정 경계와 사인 모드'),(9,8,'이중 푸리에 계수'),(11,10,'직사각형 막 문제의 완성 풀이'),(14,13,'0차 베셀 방정식 유도'),(20,19,'구 바깥 문제의 변수분리'),(21,19,'르장드르 계수와 최종 해'),(22,19,'구 바깥 해의 검산')]:
        add(n,'원본 빈 풀이 페이지', [C('원본 페이지를 그대로 보존합니다.', f'원본 {n}쪽에는 설명·수식·문제가 인쇄되어 있지 않습니다. 관련 유도와 계산은 <a href="#slide-{target:02}">{target}쪽 · {label}</a>에 기본·뉴비 해설로 완성했습니다. 별도 문제를 추가한 페이지가 아닙니다.',kind='quiet-card')],role='원본 빈 페이지')

from pde3_circle import populate as populate_circle
from pde3_sphere import populate as populate_sphere
populate_circle(add,C,M,table)
populate_sphere(add,C,M,table)
blank_pages()
