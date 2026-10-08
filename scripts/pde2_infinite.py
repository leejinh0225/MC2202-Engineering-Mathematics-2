"""Infinite rod, Gaussian kernel, source pulse and MATLAB interpretation."""
from html import escape

def populate(add,C,M,table):
    add(12,'Very long bar(매우 긴 막대) · 급수에서 열핵 적분으로',[
      C('끝이 없는 영역에서는 주파수가 연속입니다.', M(r'u_t=c^2u_{xx},\quad x\in\mathbb R,\ t>0,\qquad u(x,0)=f(x)'), 'Infinite bar(무한 막대)는 관심 영역에서 끝의 영향이 충분히 작다는 이상화입니다. x=0,L의 끝점 조건이 없으므로 nπ/L만 허용할 이유가 없습니다. Separation of variables(변수분리법)에서 각 실수 주파수 ω의 cos(ωx),sin(ωx)를 연속적으로 합칩니다.', M(r'u(x,t)=\int_0^\infty[A(\omega)\cos(\omega x)+B(\omega)\sin(\omega x)]e^{-c^2\omega^2t}\,d\omega'), M(r'A(\omega)=\frac1\pi\int_{-\infty}^\infty f(v)\cos(\omega v)\,dv,\quad B(\omega)=\frac1\pi\int_{-\infty}^\infty f(v)\sin(\omega v)\,dv'), '앞 단원의 Fourier integral(푸리에 적분)과 같은 규약입니다. 이 표현의 충분조건으로 f가 조각별 매끄럽고 절대적분 가능하다고 둡니다. 적절한 bounded solution(유계 해)의 범위를 생각하며, 공간 무한대에서의 성장 조건을 전혀 두지 않는다는 뜻은 아닙니다.'),
      C('편집자 유도 · 코사인 차 공식으로 하나의 적분을 만듭니다.', M(r'\cos(\omega x)\cos(\omega v)+\sin(\omega x)\sin(\omega v)=\cos[\omega(x-v)]'), M(r'u(x,t)=\int_{-\infty}^{\infty}f(v)\left\{\frac1\pi\int_0^\infty e^{-c^2t\omega^2}\cos[\omega(x-v)]\,d\omega\right\}\,dv'), 't>0에서 Gaussian factor(가우스 인자)가 주파수 적분을 감쇠시키므로 위 조건 아래 적분 순서를 교환할 수 있습니다. 중괄호가 처음 위치 v에서 현재 위치 x로 열이 퍼지는 가중치입니다.'),
      C('Gaussian integral(가우스 적분)의 계산', M(r'I(\beta)=\int_0^\infty e^{-z^2}\cos(\beta z)\,dz,\quad I^\prime(\beta)=\frac12\int_0^\infty(e^{-z^2})^\prime\sin(\beta z)\,dz=-\frac\beta2I(\beta)'), '부분적분의 경계항은 z=0에서 sin 0=0, 무한대에서 e⁻ᶻ²→0이므로 사라집니다. I′=−βI/2를 풀고 I(0)=√π/2를 넣습니다.', M(r'I(\beta)=\frac{\sqrt\pi}{2}e^{-\beta^2/4},\qquad z=c\sqrt t\,\omega,\quad\beta=\frac{x-v}{c\sqrt t}\quad(c>0)')),
      C('Heat kernel(열핵)과 convolution(합성곱)', M(r'\boxed{u(x,t)=\frac1{2c\sqrt{\pi t}}\int_{-\infty}^\infty f(v)e^{-(x-v)^2/(4c^2t)}\,dv},\qquad t>0'), M(r'H(x,t)=\frac1{\sqrt{4\pi c^2t}}e^{-x^2/(4c^2t)},\qquad u=H(\cdot,t)*f,\quad H\ge0,\quad\int_{\mathbb R}H(x,t)\,dx=1'), 'H는 폭이 √t에 비례해 넓어지는 정규화된 Gaussian(가우스 함수)입니다. f가 유계이면 열핵 적분도 잘 정의됩니다. 적분가능한 초기온도의 전체 적분은 보존됩니다. t→0⁺에서 연속점의 f로 돌아가며 점프점에서는 좌우 극한의 평균으로 갑니다. t=0을 분모에 직접 넣지 않습니다.'),
      C('앞 단원의 복소 변환으로도 같은 식을 얻습니다.', M(r'\widehat u_t=-c^2\omega^2\widehat u\quad\Rightarrow\quad\widehat u(\omega,t)=\widehat f(\omega)e^{-c^2\omega^2t}'), '정규화 1/√(2π), 지수 e⁻ⁱωˣ인 앞 단원 규약입니다. ∂ₓₓ의 변환이 −ω²배이므로 시간 ODE가 됩니다. 역변환하면 같은 heat kernel(열핵) 해입니다. 유한 막대의 이산 n과 무한 막대의 연속 ω가 맡는 역할을 비교하십시오.')
    ],[
      C('1 · L이 없어지면 nπ/L도 정해지지 않습니다.', '유한 막대에서는 두 끝에 딱 맞는 sine mode(사인 모드)만 골랐습니다. Infinite bar(무한 막대)에는 그런 두 끝이 없습니다. 따라서 간격이 정해진 주파수 목록 대신 모든 주파수를 연속적으로 써야 합니다. 이것이 Fourier series(푸리에 급수)의 합 Σ가 Fourier integral(푸리에 적분)의 ∫로 바뀌는 이유입니다.', M(r'u=\int_0^\infty[A(\omega)\cos\omega x+B(\omega)\sin\omega x]e^{-c^2\omega^2t}\,d\omega'), '열방정식이므로 각 주파수의 시간 배율은 여전히 감쇠 지수입니다. 여기서는 처음 온도 f가 주어지고, 충분히 멀리 있는 가상의 끝 온도를 새로 만들지 않습니다.'),
      C('2 · 나중 온도는 처음 온도들을 거리별로 섞은 값입니다.', '처음 위치를 v, 나중에 관찰할 위치를 x라고 구별합니다. 처음의 각 작은 구간은 f(v)만큼 뜨겁고, 그 영향이 시간에 따라 퍼집니다. 가까운 곳의 영향은 크게, 먼 곳의 영향은 작게 섞는 가중치를 H라고 부릅니다.', M(r'u(x,t)=\int_{-\infty}^\infty f(v)H(x-v,t)\,dv'), 'Convolution(합성곱)은 이처럼 두 함수의 위치 차이를 이용해 가중합을 만드는 연산입니다. x−v는 이동 거리이고 dv는 처음 막대의 아주 작은 길이입니다. 적분할 때 x와 t는 고정합니다.'),
      C('3 · 가중치 H는 어디서 나오나요?', 'Fourier integral(푸리에 적분)의 A,B에 초기함수 f의 적분을 넣습니다. 코사인·사인 두 항을 cos(A−B)=cos A cos B+sin A sin B로 묶으면 다음 중괄호가 나옵니다.', M(r'u=\int_{\mathbb R}f(v)\left\{\frac1\pi\int_0^\infty e^{-c^2t\omega^2}\cos[\omega(x-v)]\,d\omega\right\}dv'), '중괄호를 계산하려고 z=c√t·ω로 치환합니다. dω=dz/(c√t)이고, β=(x−v)/(c√t)라 쓰면 적분은 I(β)=∫₀∞e⁻ᶻ²cos(βz)dz 모양이 됩니다. c는 c²의 양의 제곱근으로 둡니다.'),
      C('4 · 어려운 적분은 미분 관계를 찾아 풉니다.', M(r'I^\prime(\beta)=-\int_0^\infty z e^{-z^2}\sin(\beta z)\,dz'), 'β로 미분하므로 cos(βz)의 미분은 −z sin(βz)입니다. 한편 e⁻ᶻ²을 z로 미분하면 −2z e⁻ᶻ²이므로 −z e⁻ᶻ²=(e⁻ᶻ²)′/2로 바꿀 수 있습니다. Integration by parts(부분적분)를 합니다.', M(r'I^\prime=\left[\frac12 e^{-z^2}\sin(\beta z)\right]_0^\infty-\frac\beta2\int_0^\infty e^{-z^2}\cos(\beta z)\,dz=-\frac\beta2 I'), M(r'I(\beta)=I(0)e^{-\beta^2/4}=\frac{\sqrt\pi}{2}e^{-\beta^2/4}'), 'I(0)은 앞 단원의 Gaussian integral(가우스 적분) 절반인 √π/2입니다. 이를 기억하지 못해도 열핵의 최종식부터 문제에 적용할 수 있습니다. 이 유도는 그 공식이 생기는 이유를 보여 주는 편집자 보강입니다.'),
      C('5 · 최종식을 읽는 순서를 고정합니다.', M(r'\boxed{u(x,t)=\frac1{2c\sqrt{\pi t}}\int_{-\infty}^\infty f(v)e^{-(x-v)^2/(4c^2t)}\,dv}'), '① 초기온도 f에 적분 변수 v를 넣습니다. ② f(v)가 0인 구간은 빼 버립니다. ③ 지수 안의 제곱을 z² 모양으로 치환합니다. ④ 새 적분 구간과 dv를 함께 바꿉니다. 앞의 1/(2c√(πt))는 가중치 전체 넓이가 1이 되도록 맞춘 수입니다.'),
      C('6 · 꼭대기는 낮아져도 총열이 사라진 것은 아닙니다.', '옆면으로도 끝으로도 열이 새지 않는 이상적인 무한 막대에서, 초기온도 적분이 유한하면 그 전체 적분은 보존됩니다. 처음의 좁고 높은 온도가 넓고 낮게 퍼집니다. 처음 차갑던 바깥쪽은 오히려 데워질 수 있습니다. t=0에는 공식의 분모가 0이 되므로 직접 대입하지 않고 t→0⁺의 극한으로 initial condition(초기조건)을 확인합니다.')
    ],role='무한 영역·완성 유도')

    add(16,'원본 예제 · −1부터 1까지만 뜨거운 무한 막대',[
      C('문제와 적용 공식', M(r'f(x)=\begin{cases}U_0,&|x|<1,\\0,&|x|>1,\end{cases}\qquad u_t=c^2u_{xx},\quad x\in\mathbb R'), '원본은 |x|<1입니다. x<1인 반무한 구간이 아닙니다. ±1에서의 값은 원문에 미지정이며, 유한 개 점의 값은 t>0의 열핵 적분을 바꾸지 않습니다. 아래 풀이는 원본 그림과 같은 구간 [−1,1]을 사용합니다.'),
      C('1 · f가 0이 아닌 구간만 남깁니다.', M(r'u(x,t)=\frac{U_0}{2c\sqrt{\pi t}}\int_{-1}^1e^{-(x-v)^2/(4c^2t)}\,dv'), 'U₀는 적분 변수 v에 의존하지 않아 밖으로 꺼냈습니다. 유한 막대의 두 끝 −1,1을 고정한 문제가 아니며, 그 바깥에도 막대가 이어집니다.'),
      C('2 · Gaussian integral(가우스 적분)로 치환합니다.', M(r'z=\frac{v-x}{2c\sqrt t},\quad dv=2c\sqrt t\,dz,\quad v=-1\Rightarrow z=\frac{-1-x}{2c\sqrt t},\quad v=1\Rightarrow z=\frac{1-x}{2c\sqrt t}'), M(r'\boxed{u(x,t)=\frac{U_0}{\sqrt\pi}\int_{(-1-x)/(2c\sqrt t)}^{(1-x)/(2c\sqrt t)}e^{-z^2}\,dz}'), '−z²에는 (x−v)²=(v−x)²가 쓰였습니다. 원본 MATLAB의 하한 −(1+x)/(2√t), 상한 (1−x)/(2√t)와 정확히 연결됩니다.'),
      C('3 · Error function(오차함수)으로 쓰는 같은 답', M(r'\operatorname{erf}(s)=\frac2{\sqrt\pi}\int_0^s e^{-z^2}\,dz,\qquad \operatorname{erf}(-s)=-\operatorname{erf}(s)'), M(r'\boxed{u(x,t)=\frac{U_0}{2}\left[\operatorname{erf}\left(\frac{1-x}{2c\sqrt t}\right)+\operatorname{erf}\left(\frac{1+x}{2c\sqrt t}\right)\right]}'), 'erf는 수치 오차를 뜻하는 변수가 아니라 이 적분에 붙인 표준 함수 이름입니다. 초등함수만의 원시함수가 없으므로 정적분형 자체도 완성 답입니다.'),
      C('4 · 극한·대칭·총열로 검산합니다.', M(r'u(-x,t)=u(x,t),\qquad u(0,t)=U_0\operatorname{erf}\left(\frac1{2c\sqrt t}\right),\qquad\int_{\mathbb R}u(x,t)\,dx=2U_0'), M(r'\lim_{t\downarrow0}u(x,t)=\begin{cases}U_0,&|x|<1,\\U_0/2,&|x|=1,\\0,&|x|>1.\end{cases}'), '원본 17쪽의 c=1,U₀=100에 대해 중심 온도는 t=0.5,1,8에서 각각 약 68.269,52.050,19.741입니다. t→∞에서 고정된 위치의 온도는 0으로 가지만 전체 온도 적분은 보존됩니다.')
    ],[
      C('1 · 그림을 먼저 읽으면 구간을 틀리지 않습니다.', '처음 뜨거운 부분은 중심의 폭 2인 구간, 즉 −1<x<1입니다. 절댓값 |x|<1이 이 뜻입니다. 바깥은 처음에 0도이고 막대는 양쪽 무한대로 이어집니다. −1과 1에 냉각 장치가 있다는 뜻이 아닙니다.', M(r'f(v)=U_0\ (-1<v<1),\qquad f(v)=0\ (|v|>1)')),
      C('2 · 무한 구간 적분이 왜 −1부터 1로 줄어드나요?', 'Heat kernel(열핵) 공식은 처음 위치 v의 온도 f(v)를 모두 더합니다. 바깥에서는 f(v)=0이므로 아무것도 보태지 않습니다. 안쪽에서는 f(v)=U₀라는 상수이므로 밖으로 꺼낼 수 있습니다.', M(r'u(x,t)=\frac{U_0}{2c\sqrt{\pi t}}\int_{-1}^{1}e^{-(x-v)^2/(4c^2t)}\,dv'), '지금 적분하는 변수는 v입니다. 관찰 위치 x와 시간 t는 정해 놓은 숫자처럼 취급합니다. 이 구별이 substitution(치환)의 첫 단계입니다.'),
      C('3 · 지수 안의 복잡한 제곱을 z²로 만듭니다.', M(r'z=\frac{v-x}{2c\sqrt t}\quad\Rightarrow\quad v=x+2c\sqrt t\,z,\quad dv=2c\sqrt t\,dz'), 'v가 −1일 때와 +1일 때의 z를 각각 계산합니다. 적분 변수만 바꾸고 구간을 그대로 두면 다른 적분이 됩니다.', M(r'v=-1:\ z=\frac{-1-x}{2c\sqrt t},\qquad v=1:\ z=\frac{1-x}{2c\sqrt t}'), 'dv에서 나온 2c√t와 적분 밖의 같은 인자가 약분됩니다. √π는 약분되지 않습니다.', M(r'u(x,t)=\frac{U_0}{\sqrt\pi}\int_{(-1-x)/(2c\sqrt t)}^{(1-x)/(2c\sqrt t)}e^{-z^2}\,dz')),
      C('4 · erf는 이 넓이를 짧게 부르는 이름입니다.', 'e⁻ᶻ² 아래의 넓이를 익숙한 다항식·삼각함수의 원시함수로 쓸 수 없어 error function(오차함수)이라는 이름을 붙입니다. 아래는 외워서 유도할 식이 아니라 정의입니다.', M(r'\operatorname{erf}(s):=\frac2{\sqrt\pi}\int_0^s e^{-z^2}\,dz'), M(r'\frac{U_0}{\sqrt\pi}\int_A^B e^{-z^2}dz=\frac{U_0}{2}[\operatorname{erf}(B)-\operatorname{erf}(A)]'), 'A=−(1+x)/(2c√t), B=(1−x)/(2c√t)를 넣습니다. erf는 odd function(홀함수)이므로 음수 입력의 마이너스를 밖으로 빼면 최종식이 더하기로 바뀝니다.', M(r'\boxed{u(x,t)=\frac{U_0}{2}\left[\operatorname{erf}\frac{1-x}{2c\sqrt t}+\operatorname{erf}\frac{1+x}{2c\sqrt t}\right]}')),
      C('5 · 답이 원래 그림으로 돌아가는지 봅니다.', 'x=0이면 두 erf의 입력이 같아 u(0,t)=U₀erf[1/(2c√t)]입니다. t가 아주 작으면 입력이 매우 커지고 erf는 1에 가까워져 중심은 U₀도가 됩니다. |x|>1에서는 두 erf가 +1과 −1로 상쇄되어 0도로 돌아갑니다. 경계 x=±1에서는 절반 U₀/2로 접근합니다.', '한 점의 값을 어떻게 지정했는지는 적분값에 영향을 주지 않습니다. 따라서 이 절반값을 원본 오류라고 하지 않습니다. t=0은 처음 직사각형을 따로 그리고, t>0에서 위 공식을 사용합니다.')
    ],role='원본 예제·완성 풀이')

    code='''c = 1; U0 = 100;
x = -2:0.02:2;
times = [0, 0.5, 1, 8];
figure; hold on
for t = times
    if t == 0
        u = U0 * double(abs(x) < 1);
    else
        u = (U0/2) * (erf((1-x)/(2*c*sqrt(t))) ...
                     + erf((1+x)/(2*c*sqrt(t))));
    end
    plot(x, u, 'DisplayName', sprintf('t = %g', t));
end
legend show; xlabel('x'); ylabel('u(x,t)'); grid on'''
    add(17,'원본 MATLAB 코드 · c=1의 수치 예와 그래프',[
      C('원본 코드의 가정과 범위를 읽습니다.', '원본은 t=0.5,U₀=100,x=−2:0.2:2를 지정합니다. 적분 상·하한에 c가 없으므로 앞 슬라이드의 일반식에서 c=1을 넣은 경우입니다. 식의 부호 오류가 아니라 생략된 매개변수 설정을 드러낸 것입니다. 코드는 한 시각을 계산하고 그림은 t=0,0.5,1,8의 여러 곡선을 보여 줍니다.', M(r'y_1=-\frac{1+x}{2\sqrt t},\quad y_2=\frac{1-x}{2\sqrt t},\quad u=\frac{U_0}{\sqrt\pi}\int_{y_1}^{y_2}e^{-z^2}\,dz')),
      C('원본 계산을 erf로 표현한 편집자 보강 코드', '<pre><code>'+escape(code)+'</code></pre>', '원본의 symbolic integration(기호 적분) 대신 MATLAB의 erf를 사용한 동등한 계산입니다. t=0은 초기함수로 따로 처리하고, 나머지는 같은 해를 시각별로 그립니다. ±1의 t=0 값은 코드에서 0으로 정했으며 t>0 해에 영향을 주지 않습니다. MATLAB 자체 실행을 확인한 결과가 아니라 수식과 독립 수치적분으로 대조한 코드입니다.'),
      C('곡선에서 확인할 물리적 의미', '초기 hot spot(뜨거운 구간) 안에서는 온도가 내려가고 밖에서는 열을 받아 올라갈 수 있습니다. 중심 온도 감소와 전체 열량 감소를 같은 뜻으로 읽지 않습니다. 그려진 −2≤x≤2 밖에도 열이 퍼져 있으므로 이 화면 안의 넓이만으로 전체 열을 판단하지 않습니다.')
    ],[
      C('1 · 코드 속 y1,y2는 막대 좌표가 아닙니다.', '원래 위치 변수 v를 z=(v−x)/(2c√t)로 치환했기 때문에, 적분 상한·하한도 새 변수 z의 값입니다. 원본의 y1과 y2는 바로 그 두 값에 붙인 코드 변수명입니다. c가 빠진 듯 보이는 것은 c=1인 계산이기 때문입니다.', M(r'y_1=\frac{-1-x}{2\sqrt t},\qquad y_2=\frac{1-x}{2\sqrt t}')),
      C('2 · 반복문은 온도계를 하나씩 옮기는 과정입니다.', 'x 배열의 첫 위치부터 끝 위치까지 하나씩 골라, 그 위치에서 적분할 두 끝값을 계산하고 e⁻ᶻ² 아래 넓이를 구합니다. 마지막으로 U₀/√π를 곱하면 실제 온도입니다. 원본 코드의 u 배열은 마지막 배율을 곱하기 전에는 온도 자체가 아니라 적분값입니다.'),
      C('3 · 같은 계산을 erf로 쓰면 기호 적분 없이 그릴 수 있습니다.', '<pre><code>'+escape(code)+'</code></pre>', 't=0을 따로 분기한 이유는 √t로 나눌 수 없기 때문입니다. t>0에서는 앞에서 구한 error function(오차함수) 답을 그대로 계산합니다. 그래프의 여러 시간을 반복하기 위해 times 목록을 썼습니다. 코드는 편집자 보강이며 MATLAB 실행 결과를 주장하지 않습니다.'),
      C('4 · “온도가 내려간다”는 말에도 위치가 필요합니다.', '중심 x=0은 t=0.5,1,8에서 약 68.269,52.050,19.741도입니다(c=1,U₀=100). 하지만 처음 0도였던 바깥 위치는 열을 받아 올라갈 수 있습니다. Infinite bar(무한 막대) 전체로는 열이 보존되고, 좁은 그래프 밖으로도 퍼져 나갑니다.')
    ],role='원본 코드·그래프 읽기')
