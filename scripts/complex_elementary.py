"""Source pages 41-54: entire functions, branches, inverse functions, powers."""
def populate(add,C,M,table):
 add(41,'Complex exponential(복소지수함수) · 급수 정의',[
  C('지수급수는 상수항 1부터 시작합니다.',M(r'e^z=\sum_{n=0}^{\infty}\frac{z^n}{n!}=1+z+\frac{z^2}{2!}+\frac{z^3}{3!}+\cdots'), '모든 z에서 절대수렴하는 power series(거듭제곱 급수)이므로 eᶻ는 entire(전해석)입니다. 항별 미분하면 자기 자신이 됩니다. n=0의 0!=1을 포함합니다.'),
  C('직교형식과 CR 확인',M(r'e^{x+iy}=e^x(\cos y+i\sin y),\quad u_x=v_y=e^x\cos y,\quad u_y=-v_x=-e^x\sin y'), '36쪽의 편도함수 검사와 같은 결론입니다. 41쪽은 함수의 급수 정의까지 연결합니다. eᶻ는 절대로 0이 되지 않습니다. 크기가 eˣ>0이기 때문입니다.')
 ],[
  C('1 · 실수 지수함수를 복소수 입력으로 확장합니다.',M(r'e^z=1+z+\frac{z^2}{2}+\frac{z^3}{6}+\cdots'), 'Factorial(계승) n!은 1부터 n까지 곱한 값이고 0!=1입니다. 첫 항을 빼면 z=0에서 0이 되어 e⁰=1과 맞지 않습니다. 이 급수는 모든 복소수에서 수렴합니다.'),
  C('2 · 실수부는 크기, 허수부는 방향을 조절합니다.',M(r'e^{x+iy}=e^xe^{iy}=e^x(\cos y+i\sin y),\quad|e^z|=e^x'), 'x가 바뀌면 반지름이 바뀌고 y가 바뀌면 회전합니다. 지수함수에 i가 들어간다는 것은 값이 이상해지는 것이 아니라 회전 정보를 표현한다는 뜻입니다.'),
  C('3 · 모든 점에서 미분할 수 있습니다.',M(r'u_x=e^x\cos y=v_y,\quad u_y=-e^x\sin y=-v_x'), '편도함수가 연속이고 CR을 만족하므로 entire function(전해석함수)입니다. 출력 크기가 항상 양수여서 eᶻ=0을 만드는 입력은 없습니다. 다음 로그의 정의역에서 0을 빼는 이유입니다.')
 ])
 add(42,'복소지수의 덧셈법칙과 주기 2πi',[
  C('도함수와 지수법칙',M(r'(e^z)^\prime=u_x+iv_x=e^z,\qquad e^{z_1}e^{z_2}=e^{z_1+z_2}'), '크기는 eˣ¹eˣ²=eˣ¹⁺ˣ², 각도는 y₁+y₂로 합쳐져 지수법칙을 만족합니다.'),
  C('허수 방향의 주기',M(r'e^{z+2\pi i}=e^ze^{2\pi i}=e^z'), 'Fundamental region(기본 영역)으로 −π<Im z≤π인 수평 띠를 택하면 0이 아닌 모든 출력이 정확히 한 번씩 나타납니다. 위·아래 경계를 둘 다 포함하면 같은 출력이 중복됩니다. 이 반열린 띠는 한 값 선택용이며 열린 해석 영역과 구별합니다.')
 ],[
  C('1 · 곱하면 거리와 각도가 각각 합쳐집니다.',M(r'e^{x_1+iy_1}e^{x_2+iy_2}=e^{x_1+x_2}e^{i(y_1+y_2)}'), '앞에서 익힌 polar multiplication(극형식 곱셈)입니다. 그래서 실수에서 익숙한 지수법칙이 복소수에서도 성립합니다.'),
  C('2 · 왜 2π가 아니라 2πi만큼 이동하나요?',M(r'z=x+iy\quad\Rightarrow\quad z+2\pi i=x+i(y+2\pi)'), '이동하는 것은 각도 역할의 y입니다. y에 한 바퀴 2π를 더해도 cos,sin이 같아 출력은 같습니다. x에 2π를 더하면 크기가 e²π배가 되어 다른 값입니다.'),
  C('3 · 띠 하나면 모든 출력을 만들 수 있습니다.','x는 모든 실수로 움직여 모든 양의 반지름 eˣ를 만들고, y는 길이 2π인 구간에서 모든 방향을 만듭니다. 따라서 원본의 수평 strip(띠)을 택합니다. 위·아래 경계 중 하나만 포함해야 같은 방향을 두 번 세지 않습니다.')
 ])
 add(43,'eᶻ¹=eᶻ²가 되는 조건',[
  C('입력은 2πi의 정수배만큼 다를 수 있습니다.',M(r'e^{z_1}=e^{z_2}\iff z_1-z_2=2\pi ik,\quad k\in\mathbb Z'),M(r'e^z=1\iff z=2\pi ik'), '크기를 비교하면 Re z₁=Re z₂이고, 방향을 비교하면 Im z₁−Im z₂=2πk입니다.'),
  C('로그가 여러 값을 갖는 이유','서로 다른 입력들이 같은 지수 출력을 만들기 때문에 지수함수 전체에는 한 값짜리 역함수가 없습니다. 출력에서 입력을 되찾는 log는 이 모든 2πi 차이를 포함해야 합니다.')
 ],[
  C('1 · 같은 점이 되려면 거리와 방향이 같아야 합니다.',M(r'e^{x_1}=e^{x_2}\Rightarrow x_1=x_2,\qquad y_1=y_2+2\pi k'), '실수 지수는 크기가 같으면 입력이 같지만, 방향은 한 바퀴씩 달라도 같습니다. 둘을 묶으면 z₁=z₂+2πik입니다.'),
  C('2 · eᶻ=1의 답은 0 하나가 아닙니다.',M(r'|1|=1\Rightarrow e^x=1\Rightarrow x=0,\qquad y=2\pi k'),M(r'z=2\pi ik'), 'k=0이 z=0이지만 다른 정수도 모두 됩니다. 이 입력들 중 하나를 골라 역함수로 쓰는 규칙이 다음의 principal logarithm(로그의 주값)입니다.')
 ])
 add(44,'Complex logarithm(복소로그) · 원본 log(1+i)',[
  C('지수함수의 역문제로 정의합니다.',M(r'w\in\log z\iff e^w=z,\qquad z\ne0'),M(r'\log z=\{\ln|z|+i(\operatorname{Arg}z+2\pi k):k\in\mathbb Z\}'),M(r'\operatorname{Log}z=\ln|z|+i\operatorname{Arg}z,\qquad-\pi<\operatorname{Arg}z\le\pi'), '원본 규약을 따라 log는 다가 값, Log는 주값으로 씁니다. 실수 양수의 자연로그는 ln으로 구분합니다. 문헌에 따라 대소문자 규약이 다르므로 공식의 뜻을 대조합니다.'),
  C('원본 1+i의 로그 계산',M(r'|1+i|=\sqrt2,\quad\operatorname{Arg}(1+i)=\pi/4'),M(r'\log(1+i)=\left\{\tfrac12\ln2+i(\pi/4+2\pi k):k\in\mathbb Z\right\},\quad\operatorname{Log}(1+i)=\tfrac12\ln2+i\pi/4'), '지수로 되돌리면 e^(ln√2)eⁱ⁽π⁄⁴⁺²πᵏ⁾=√2eⁱπ⁄⁴=1+i입니다.')
 ],[
  C('1 · 로그는 “어떤 지수 입력이 이 출력을 만드는가”입니다.',M(r'w=a+ib,\qquad e^w=e^a(\cos b+i\sin b)'), '출력 z의 크기가 r이면 eᵃ=r라서 a=ln r입니다. 출력 방향이 θ이면 b=θ+2πk입니다. 따라서 log z에는 실수 부분 ln r과 여러 허수 부분이 있습니다.',M(r'w=\ln r+i(\theta+2\pi k)')),
  C('2 · 원본 1+i는 거리 √2, 각 π/4입니다.',M(r'\ln\sqrt2=\ln(2^{1/2})=\tfrac12\ln2'),M(r'\log(1+i)=\tfrac12\ln2+i\left(\frac\pi4+2\pi k\right),\quad k\in\mathbb Z'), '허수부의 2πk를 없애면 전체 로그가 아니라 선택한 값 하나만 남습니다. Principal value(주값)를 구하라고 하면 Arg 범위에 맞는 π/4를 선택해 Log(1+i)=½ln2+iπ/4라고 씁니다.'),
  C('3 · 0의 로그가 없는 이유','eᵃ는 어떤 유한한 a에도 0이 되지 않습니다. 따라서 eʷ=0의 해가 없어서 log0은 정의하지 않습니다. 음수는 크기와 편각 π를 사용해 로그 값을 만들 수 있지만, 주값 함수의 연속성과는 별도의 문제입니다.')
 ],role='개념·원본 예제')
 add(45,'로그 법칙 · 다가 값과 주값을 섞지 않습니다.',[
  C('항상 맞는 식과 가지에 의존하는 식',M(r'e^{\operatorname{Log}z}=z\ (z\ne0),\qquad\operatorname{Log}x=\ln x\ (x>0)'),M(r'\log(z_1z_2)=\log z_1+\log z_2,\quad\log(z_1/z_2)=\log z_1-\log z_2,\quad\log(1/z)=-\log z'), '마지막 줄은 가능한 값들의 집합으로 해석할 때 성립합니다. 각 항에서 임의로 고른 주값끼리는 등식이 성립하지 않을 수 있습니다. 고정한 값끼리는 2πik 차이를 추적해야 합니다.'),
  C('원본 z₁=z₂=−1의 반례',M(r'\operatorname{Log}(-1)=i\pi,\qquad\operatorname{Log}((-1)(-1))=\operatorname{Log}1=0'),M(r'\operatorname{Log}(-1)+\operatorname{Log}(-1)=2\pi i\ne0'), '두 편각 π를 합쳐 2π가 되었지만 곱 1의 주값 편각은 0입니다. 주값 범위로 되돌리는 과정에서 2πi 차이가 납니다.')
 ],[
  C('1 · 복소로그는 여러 층 중 하나를 선택합니다.','log z의 값들은 세로 방향으로 2πi씩 떨어져 있습니다. 두 로그를 더하면 어떤 층의 값인지는 맞출 수 있지만, 양쪽에서 각각 고른 principal value(주값)가 같은 층인 것은 아닙니다.'),
  C('2 · 원본 −1 두 개를 직접 계산합니다.',M(r'-1=e^{i\pi},\quad\operatorname{Log}(-1)=\ln1+i\pi=i\pi'),M(r'\operatorname{Log}(1)=0,\qquad i\pi+i\pi=2\pi i'), '곱한 뒤 로그를 취하면 0, 각각의 주값 로그를 더하면 2πi입니다. 실수 로그의 법칙을 주값에 무조건 옮기면 이 차이를 놓칩니다.'),
  C('3 · 다가 집합으로는 모순이 아닙니다.',M(r'\log1=\{2\pi ik:k\in\mathbb Z\}'), '0도 2πi도 모두 1의 로그입니다. “어떤 값을 골랐는가”가 다를 뿐입니다. 역수의 로그도 값 전체로는 −log z이지만 선택한 주값에는 같은 주의가 필요합니다.')
 ])
 add(46,'Log z의 미분 · 가지절단의 의미',[
  C('열린 절단평면에서 주가지를 미분합니다.',M(r'\Omega=\mathbb C\setminus(-\infty,0],\quad\operatorname{Log}z=\ln r+i\theta,\quad-\pi<\theta<\pi'),M(r'u_r=1/r,\quad u_\theta=0,\quad v_r=0,\quad v_\theta=1'),M(r'(\operatorname{Log}z)^\prime=e^{-i\theta}(u_r+iv_r)=\frac{e^{-i\theta}}r=\frac1z'), '선택한 analytic branch(해석적 가지) 안에서 성립합니다. 원본의 주값 정의는 음의 실수에도 값을 주지만, 그 선을 포함하는 근방에서는 주값 함수가 연속이 아닙니다. 0에서는 정의 자체가 없습니다.'),
  C('음의 실수축 양쪽에서의 점프',M(r'\lim_{\epsilon\downarrow0}\operatorname{Log}(-a+i\epsilon)=\ln a+i\pi,\quad\lim_{\epsilon\downarrow0}\operatorname{Log}(-a-i\epsilon)=\ln a-i\pi\quad(a>0)'), '위아래 극한이 2πi만큼 다릅니다. 다른 위치의 절단선을 택하면 해당 음의 점 근방의 로그 가지를 만들 수 있지만, 지금의 principal branch(주가지)와는 다른 선택입니다.')
 ],[
  C('1 · 로그 미분 공식에도 사용 가능한 영역이 있습니다.','실수에서는 ln x를 x>0에서 미분했습니다. 복소수에서는 연속된 angle(편각)을 고른 영역에서 미분합니다. 주가지는 원점과 음의 실수축을 잘라 낸 영역에서 해석적입니다.',M(r'u=\ln r,\quad v=\theta\quad\Rightarrow\quad u_r=1/r,\ v_r=0')),
  C('2 · 극좌표 도함수 공식에 넣습니다.',M(r'f^\prime=e^{-i\theta}(u_r+iv_r)=\frac1r e^{-i\theta}=\frac1{re^{i\theta}}=\frac1z'), '거리 r의 역수와 각도 −θ가 합쳐져 1/z입니다. 단순히 공식이 나온다고 절단선 위까지 미분가능한 것은 아닙니다.'),
  C('3 · 위에서와 아래에서 도착하는 각이 다릅니다.','음의 실수축 위로 접근하면 편각이 π, 아래로 접근하면 −π에 가까워집니다. 출력의 허수부가 약 2π만큼 뛰므로 주값 로그는 그 선에서 연속이 아닙니다. 원점은 로그 값을 아예 정할 수 없습니다. Branch cut(가지절단)은 이 불연속을 경계로 빼내는 선택입니다.')
 ])
 add(47,'Complex sine / cosine(복소 사인·코사인) · 정의',[
  C('급수와 지수 표현',M(r'\cos z=\sum_{n=0}^{\infty}\frac{(-1)^nz^{2n}}{(2n)!},\quad\sin z=\sum_{n=0}^{\infty}\frac{(-1)^nz^{2n+1}}{(2n+1)!}'),M(r'\cos z=\frac{e^{iz}+e^{-iz}}2,\qquad\sin z=\frac{e^{iz}-e^{-iz}}{2i}'), '두 급수는 모든 복소수에서 수렴하고 실수축에서는 원래 삼각함수와 일치합니다. cos의 상수항 1, sin의 첫 항 z를 포함합니다.'),
  C('몫으로 정의되는 나머지 함수',M(r'\tan z=\frac{\sin z}{\cos z},\quad\cot z=\frac{\cos z}{\sin z},\quad\sec z=\frac1{\cos z},\quad\csc z=\frac1{\sin z}'), '분모가 0인 점은 제외합니다. cos z=0은 z=π/2+kπ, sin z=0은 z=kπ입니다. sin,cos는 entire(전해석)이지만 이 몫 함수들은 전체 평면에서 전해석이 아닙니다.')
 ],[
  C('1 · 복소수 각도도 계산할 수 있게 정의를 확장합니다.',M(r'\cos z=1-\frac{z^2}{2!}+\frac{z^4}{4!}-\cdots,\quad\sin z=z-\frac{z^3}{3!}+\frac{z^5}{5!}-\cdots'), '실수에서 익숙한 함수를 같은 거듭제곱 급수로 확장한 것입니다. 항의 번호 n은 0부터입니다. n=1부터 시작하면 중요한 첫 항이 없어집니다.'),
  C('2 · 두 지수식을 더하거나 빼면 됩니다.',M(r'e^{iz}=\cos z+i\sin z,\qquad e^{-iz}=\cos z-i\sin z'), '더하면 2cos z, 빼면 2i sin z이므로 분모가 각각 2와 2i가 됩니다. Sine(사인)의 지수식은 합이 아니라 차라는 점을 확인하십시오.'),
  C('3 · tan은 여전히 sin/cos입니다.','Tangent(탄젠트), cotangent(코탄젠트), secant(시컨트), cosecant(코시컨트)는 위 두 함수의 비나 역수입니다. 복소수라고 0으로 나눌 수 있는 것은 아니므로 분모의 영점을 제외합니다.')
 ])
 add(48,'삼각함수의 미분·덧셈정리·주기',[
  C('지수식을 미분합니다.',M(r'(\sin z)^\prime=\frac{ie^{iz}+ie^{-iz}}{2i}=\cos z,\qquad(\cos z)^\prime=-\sin z'),M(r'\sin(-z)=-\sin z,\quad\cos(-z)=\cos z,\quad\sin^2z+\cos^2z=1')),
  C('덧셈정리와 실수 방향의 주기',M(r'\sin(z_1+z_2)=\sin z_1\cos z_2+\cos z_1\sin z_2'),M(r'\cos(z_1+z_2)=\cos z_1\cos z_2-\sin z_1\sin z_2'),M(r'\sin(z+2\pi k)=\sin z,\quad\cos(z+2\pi k)=\cos z'), '여기서는 주기가 실수 2π입니다. 지수함수 eᶻ의 주기 2πi와 구별합니다. sin²z+cos²z=1이 |sin z|²+|cos z|²=1이라는 뜻은 아닙니다.')
 ],[
  C('1 · 안쪽의 i와 −i도 미분에 포함합니다.',M(r'\frac{d}{dz}e^{iz}=ie^{iz},\quad\frac{d}{dz}e^{-iz}=-ie^{-iz}'), 'sin z의 분자에서 이미 빼기가 있으므로 두 번째 항을 미분하면 +i e⁻ⁱᶻ가 됩니다.',M(r'(\sin z)^\prime=\frac{ie^{iz}+ie^{-iz}}{2i}=\frac{e^{iz}+e^{-iz}}2=\cos z')),
  C('2 · 덧셈정리에서는 두 입력을 모두 사용합니다.',M(r'\sin(A+B)=\sin A\cos B+\cos A\sin B'),M(r'\cos(A+B)=\cos A\cos B-\sin A\sin B'), 'A,B가 복소수여도 맞습니다. 첫 항을 sin A cos A처럼 같은 입력으로 두 번 쓰면 B의 정보가 사라져 틀립니다.'),
  C('3 · 제곱과 절댓값 제곱은 다릅니다.',M(r'\sin^2z+\cos^2z=1'), '여기의 제곱은 함수값을 그대로 곱한 것입니다. 복소수의 absolute square(절댓값 제곱)는 켤레를 곱하는 별도 연산입니다. 따라서 복소 사인·코사인의 크기가 항상 1 이하라고 결론 내리면 안 됩니다.')
 ])
 add(49,'복소 삼각함수의 실수부·허수부',[
  C('지수의 실수·허수 부분을 분리합니다.',M(r'e^{iz}=e^{-y}e^{ix},\qquad e^{-iz}=e^ye^{-ix}\quad(z=x+iy)'),M(r'\cos z=\tfrac12[e^{-y}(\cos x+i\sin x)+e^y(\cos x-i\sin x)]'),M(r'\boxed{\cos(x+iy)=\cos x\cosh y-i\sin x\sinh y}')),
  C('사인도 같은 방식입니다.',M(r'\boxed{\sin(x+iy)=\sin x\cosh y+i\cos x\sinh y}'),M(r'\cosh y=\frac{e^y+e^{-y}}2,\qquad\sinh y=\frac{e^y-e^{-y}}2'), '허수 방향의 변화는 hyperbolic function(쌍곡함수)으로 나타납니다. |sin(x+iy)|²=sin²x+sinh²y이므로 복소 사인은 크기가 무한히 커질 수 있습니다.')
 ],[
  C('1 · i를 괄호에 곱할 때 i²를 사용합니다.',M(r'iz=i(x+iy)=ix-y,\qquad-iz=y-ix'), '그래서 지수의 크기는 각각 e⁻ʸ와 eʸ가 됩니다. 여기의 마이너스를 놓치면 마지막 허수부 부호가 뒤집힙니다.'),
  C('2 · 코사인 지수식에 넣고 같은 종류끼리 묶습니다.',M(r'\cos z=\cos x\frac{e^y+e^{-y}}2-i\sin x\frac{e^y-e^{-y}}2'), '첫 분수가 cosh y, 두 번째 분수가 sinh y라는 새 이름입니다. 따라서 cos z=cos x cosh y−i sin x sinh y입니다.'),
  C('3 · 사인은 지수의 차를 2i로 나눕니다.',M(r'\sin z=\sin x\frac{e^y+e^{-y}}2+i\cos x\frac{e^y-e^{-y}}2'), '결과는 sin x cosh y+i cos x sinh y입니다. y=0이면 cosh0=1,sinh0=0이라 원래 실수 삼각함수로 돌아옵니다. y가 커지면 지수 항이 커지므로 크기가 1 이하라는 실수 직관은 적용되지 않습니다.')
 ])
 add(50,'Hyperbolic functions(쌍곡함수) · 삼각함수와의 연결',[
  C('지수의 합과 차로 정의합니다.',M(r'\cosh z=\frac{e^z+e^{-z}}2,\quad\sinh z=\frac{e^z-e^{-z}}2'),M(r'\tanh z=\sinh z/\cosh z,\quad\coth z=\cosh z/\sinh z,\quad\operatorname{sech}z=1/\cosh z,\quad\operatorname{csch}z=1/\sinh z'), '몫과 역수는 분모가 0인 점을 제외합니다. sinh는 홀함수,cosh는 짝함수이며 (sinh z)′=cosh z,(cosh z)′=sinh z입니다.'),
  C('항등식과 덧셈정리',M(r'\cosh^2z-\sinh^2z=1'),M(r'\sinh(A+B)=\sinh A\cosh B+\cosh A\sinh B'),M(r'\cosh(A+B)=\cosh A\cosh B+\sinh A\sinh B')),
  C('입력에 i를 곱하면 서로 연결됩니다.',M(r'\cosh(iz)=\cos z,\quad\sinh(iz)=i\sin z,\quad\sin(iz)=i\sinh z,\quad\cos(iz)=\cosh z'), '복소수 관점에서는 삼각함수와 쌍곡함수가 같은 지수함수의 서로 다른 조합입니다.')
 ],[
  C('1 · h는 지수함수로 만든 쌍곡함수라는 표시입니다.',M(r'\cosh z=\frac{e^z+e^{-z}}2,\qquad\sinh z=\frac{e^z-e^{-z}}2'), 'cos,sin과 이름은 비슷하지만 sinh의 분모는 2i가 아니라 2입니다. z의 부호를 바꾸면 두 지수가 교환되므로 cosh는 그대로, sinh는 부호가 반대입니다.'),
  C('2 · 제곱의 차를 계산해 봅니다.',M(r'\cosh^2z-\sinh^2z=\frac{(e^z+e^{-z})^2-(e^z-e^{-z})^2}{4}=e^ze^{-z}=1'), '실수 삼각함수의 제곱 합과 달리 cosh²−sinh²에는 빼기가 있습니다. 덧셈정리에서는 cosh(A+B)의 두 항 사이가 플러스입니다.'),
  C('3 · iz를 대입해 관계를 직접 확인합니다.',M(r'\sinh(iz)=\frac{e^{iz}-e^{-iz}}2=i\sin z'),M(r'\sin(iz)=\frac{e^{-z}-e^z}{2i}=i\sinh z,\quad\cos(iz)=\cosh z'), '1/i=−i 때문에 앞의 빼기가 바뀝니다. tanh,coth,sech,csch는 각각 위 두 함수의 비·역수이며 분모가 0인 곳을 제외합니다.')
 ])
 add(51,'Inverse trigonometric functions(역삼각함수) · 로그로 풀기',[
  C('역함수는 지수에 대한 이차방정식으로 구합니다.',M(r'z=\sin w=\frac{e^{iw}-e^{-iw}}{2i},\quad q=e^{iw}\ne0'),M(r'q^2-2izq-1=0\quad\Rightarrow\quad q=iz\pm\sqrt{1-z^2},\quad w=-i\log q'), 'sqrt와 log의 값 선택이 inverse sine(역사인)의 여러 가지를 만듭니다. 특정 해석적 가지를 쓰려면 정의역과 일관된 제곱근·로그를 선택해야 합니다.'),
  C('코사인·탄젠트의 역관계',M(r'z=\cos w\Rightarrow q^2-2zq+1=0,\quad w=-i\log(z\pm i\sqrt{1-z^2})'),M(r'\tan^{-1}z=\frac{i}{2}\log\left(\frac{i+z}{i-z}\right)'), '역탄젠트 식은 가능한 로그 값들을 통한 다가 관계입니다. 0 근방에서 0을 주는 가지의 도함수는 1/(1+z²)입니다.'),
  C('역함수 미분은 선택한 가지에서 적용합니다.',M(r'(\sin^{-1}z)^\prime=\frac1{\sqrt{1-z^2}},\quad(\cos^{-1}z)^\prime=-\frac1{\sqrt{1-z^2}},\quad(\tan^{-1}z)^\prime=\frac1{1+z^2}'), '첫 두 식은 각각 해당 가지에 맞는 제곱근을 써야 합니다. 분기점 ±1, 역탄젠트의 ±i 및 선택한 절단선을 확인합니다. sin⁻¹은 역함수이며 1/sin과 다릅니다.'),
  C('원본 예제 · sin w=√2의 시작',M(r'1-(\sqrt2)^2=-1,\quad q=i\sqrt2\pm i=i(\sqrt2\pm1)'), '두 양수 √2±1에 i를 곱한 수의 로그를 다음 페이지에서 구합니다.')
 ],[
  C('1 · sin⁻¹은 “sin을 적용하기 전 값”을 묻습니다.','sin⁻¹z는 sin w=z인 w를 찾으라는 뜻입니다. 1/sin z는 cosecant(코시컨트)라는 다른 함수입니다. 복소수에서는 주기와 제곱근 때문에 w가 여러 개일 수 있습니다.'),
  C('2 · 지수를 q라고 두면 익숙한 이차방정식입니다.',M(r'z=\frac{q-q^{-1}}{2i}\Rightarrow2izq=q^2-1\Rightarrow q^2-2izq-1=0'),M(r'q=\frac{2iz\pm\sqrt{(-2iz)^2+4}}2=iz\pm\sqrt{1-z^2}'), 'q=eⁱʷ이므로 로그를 취해 iw=log q, 양변을 i로 나누면 w=−i log q입니다. 로그의 여러 값도 함께 남겨야 합니다.'),
  C('3 · 탄젠트의 부호는 역으로 확인합니다.',M(r'\tan w=\frac{e^{2iw}-1}{i(e^{2iw}+1)}=z\Rightarrow e^{2iw}=\frac{1+iz}{1-iz}'),M(r'w=\frac1{2i}\log\frac{1+iz}{1-iz}=\frac i2\log\frac{i+z}{i-z}'), '마지막 두 분수는 서로 역수이고, 다가 로그의 부호를 바꿔 같은 값 집합으로 읽습니다. 정해진 주값을 임의로 분해하는 법칙은 아닙니다.'),
  C('4 · 원본 √2를 넣어 제곱근부터 구합니다.',M(r'q=i\sqrt2\pm\sqrt{1-2}=i(\sqrt2\pm1)'), '√2+1과 √2−1은 둘 다 양수라 두 q 모두 양의 허수축 위입니다. 각각 크기는 √2±1, 편각은 π/2+2πk입니다. 여기서 로그 공식을 적용하면 다음 페이지의 모든 답을 얻습니다.'),
  C('5 · 미분 공식도 역관계를 미분한 것입니다.',M(r'\sin w=z\Rightarrow\cos w\,w^\prime=1,\quad w^\prime=1/\cos w'), 'cos²w=1−z²이므로 cos w에 맞는 제곱근을 분모로 씁니다. 가지를 바꾸면 이 부호도 함께 달라집니다. arccos는 −1/sin w,arctan은 1/(1+z²)로 같은 방식으로 유도합니다.')
 ],role='개념·원본 예제 유도')
 add(52,'sin⁻¹√2 완성 · Inverse hyperbolic functions(역쌍곡함수)',[
  C('원본 예제의 모든 값',M(r'\log[i(\sqrt2\pm1)]=\ln(\sqrt2\pm1)+i(\pi/2+2\pi k)'),M(r'w=\frac\pi2+2\pi k-i\ln(\sqrt2\pm1)=\boxed{\frac\pi2+2\pi k\ \pm i\ln(\sqrt2+1)},\quad k\in\mathbb Z'), '두 ± 표현은 같은 집합입니다. (√2+1)(√2−1)=1이므로 두 로그는 부호가 반대입니다. 실제로 sin(π/2±iL)=cosh L=√2입니다. 원본은 모든 값을 구하며 별도 가지를 지정하지 않았으므로 주값 하나로 제한하지 않습니다.'),
  C('역쌍곡함수도 지수의 이차방정식으로 풉니다.',M(r'\sinh^{-1}z=\log(z+\sqrt{z^2+1}),\qquad\cosh^{-1}z=\log(z+\sqrt{z^2-1})'),M(r'\tanh^{-1}z=\frac12\log\frac{1+z}{1-z}'), '제곱근·로그는 선택한 가지와 일관되어야 합니다. 위 식은 일반 역관계의 표현이며 모든 곳에서 주값 제곱근을 무조건 끼워 넣는 공식은 아닙니다. 특히 주 arcosh의 표준 표현은 Log(z+√(z−1)√(z+1))로 절단과 제곱근을 맞춥니다.'),
  C('미분과 가지 조건',M(r'(\sinh^{-1}z)^\prime=\frac1{\sqrt{z^2+1}},\quad(\cosh^{-1}z)^\prime=\frac1{\sqrt{z^2-1}},\quad(\tanh^{-1}z)^\prime=\frac1{1-z^2}'), '제곱근 분모는 해당 역함수 가지의 cosh w 또는 sinh w와 일치하도록 선택합니다. 역삼각함수와 구별합니다.')
 ],[
  C('1 · 로그를 계산한 뒤 −i를 분배합니다.',M(r'w=-i[\ln(\sqrt2\pm1)+i(\pi/2+2\pi k)]'),M(r'w=\pi/2+2\pi k-i\ln(\sqrt2\pm1)'), '−i×i=−i²=+1이라 실수 부분의 각도는 플러스입니다. 앞의 −i 부호를 유지해야 원본 최종 줄과 일치합니다.'),
  C('2 · 두 로그는 서로 반대입니다.',M(r'(\sqrt2+1)(\sqrt2-1)=2-1=1'),M(r'\ln(\sqrt2-1)=-\ln(\sqrt2+1)'), '양의 실수 로그라 이 계산에는 주값 문제 없이 보통 로그 법칙을 쓸 수 있습니다. 따라서 두 답 계열은 π/2+2πk±i ln(√2+1)입니다.'),
  C('3 · 실수에서는 불가능했던 sin w=√2를 검산합니다.',M(r'\sin(\pi/2+iL)=\sin(\pi/2)\cosh L+i\cos(\pi/2)\sinh L=\cosh L'),M(r'L=\ln(\sqrt2+1)\Rightarrow\cosh L=\frac{(\sqrt2+1)+(\sqrt2-1)}2=\sqrt2'), '허수부가 있는 입력은 사인 크기가 1을 넘을 수 있으므로 답이 존재합니다. −iL도 cosh가 짝함수라 같은 답을 만듭니다.'),
  C('4 · 역쌍곡함수도 q=eʷ로 두면 풀립니다.',M(r'\sinh w=z\Rightarrow q^2-2zq-1=0\Rightarrow q=z\pm\sqrt{z^2+1}'),M(r'\cosh w=z\Rightarrow q^2-2zq+1=0\Rightarrow q=z\pm\sqrt{z^2-1}'),M(r'\tanh w=z\Rightarrow e^{2w}=\frac{1+z}{1-z}'), 'q를 구한 뒤 w=log q를 취합니다. tanh는 2w의 식이므로 로그 앞에 1/2가 붙습니다. 각 식에는 로그와 제곱근의 값 선택이 함께 들어 있습니다.'),
  C('5 · 역함수 미분에서 h를 빠뜨리지 않습니다.',M(r'\sinh w=z\Rightarrow\cosh w\,w^\prime=1,\qquad\cosh^2w=1+z^2'),M(r'\cosh w=z\Rightarrow\sinh w\,w^\prime=1,\qquad\sinh^2w=z^2-1'), '따라서 분모는 각각 가지에 맞는 √(1+z²),√(z²−1)입니다. tanh의 미분은 1−tanh²w이므로 역함수 도함수는 1/(1−z²)입니다. 분모가 0인 분기점과 선택한 절단선에서는 이 공식을 무조건 사용하지 않습니다.')
 ],role='원본 예제·역쌍곡함수')
 add(53,'Complex power(복소 거듭제곱) · 로그의 가지를 고정합니다.',[
  C('일반 지수 c는 로그로 정의합니다.',M(r'z^c=\left\{\exp\left(c[\operatorname{Log}z+2\pi ik]\right):k\in\mathbb Z\right\}\quad(z\ne0)'),M(r'\text{principal value: }\exp(c\operatorname{Log}z)'), 'c가 정수이면 모든 값이 같고, 기약분수 p/q이면 q개, 무리 실수 또는 허수부가 0이 아닌 지수이면 일반적으로 무한히 많은 값입니다. 복소 지수에도 크기·편각 계산이 먼저입니다.'),
  C('같은 해석적 로그 L(z)를 고정한 거듭제곱',M(r'F_c(z)=e^{cL(z)},\quad F_{-c}=1/F_c,\quad F_cF_d=F_{c+d},\quad F_c^n=F_{nc}\ (n\in\mathbb Z)'),M(r'F_c^\prime=ce^{cL(z)}L^\prime(z)=\frac czF_c(z)'), '이는 같은 가지에서의 등식입니다. 여러 가지에서 값을 각각 독립적으로 골라 곱하면 같은 법칙을 무조건 적용할 수 없습니다. (zᶜ)ᵈ=zᶜᵈ를 일반적인 주값 법칙으로 사용하지 않습니다.')
 ],[
  C('1 · 분수·복소 지수는 “로그 → 곱하기 → 지수”입니다.',M(r'z^c=e^{c\log z}'), '먼저 z의 로그 값을 구하고 c를 곱한 뒤 지수함수에 넣습니다. log z가 여러 값이면 zᶜ도 여러 값이 생깁니다. Principal value(주값)를 요구하면 Log z를 사용합니다.'),
  C('2 · 정수 지수에서는 여러 값이 하나로 합쳐집니다.',M(r'e^{c(\operatorname{Log}z+2\pi ik)}=e^{c\operatorname{Log}z}e^{2\pi ick}'), 'c가 정수면 마지막 인자가 항상 1입니다. c=1/2이면 마지막 인자가 (−1)ᵏ라 두 부호가 생깁니다. 이는 앞에서 구한 두 제곱근과 같습니다.'),
  C('3 · 계산 법칙은 같은 로그 값을 쓰는지 확인합니다.',M(r'e^{cL}e^{dL}=e^{(c+d)L},\qquad e^{-cL}=1/e^{cL}'), '같은 L을 쓸 때는 익숙한 지수법칙이 그대로 나옵니다. 중간에 다른 가지를 골라 버리면 앞의 계산과 연결되지 않습니다. 특히 principal value(주값)를 단계마다 다시 고르는 연산은 주의해야 합니다.'),
  C('4 · 미분은 연쇄법칙 한 번입니다.',M(r'\frac{d}{dz}e^{cL(z)}=e^{cL(z)}\cdot c\cdot\frac1z=\frac cz z^c'), 'c는 상수이고 L′=1/z인 해석적 로그 가지 안에서 계산합니다. 제곱근·로그와 마찬가지로 공식만 적지 말고 그 가지의 정의역도 함께 확인합니다.')
 ])
 add(54,'원본 예제 · (1+i)¹⁄²의 주값',[
  C('주값 로그를 반으로 나눕니다.',M(r'\operatorname{Log}(1+i)=\tfrac12\ln2+i\pi/4'),M(r'(1+i)^{1/2}_{\rm principal}=\exp(\tfrac14\ln2+i\pi/8)=2^{1/4}(\cos(\pi/8)+i\sin(\pi/8))')),
  C('정확한 직교형식과 수치',M(r'\boxed{\sqrt{\frac{\sqrt2+1}{2}}+i\sqrt{\frac{\sqrt2-1}{2}}}\simeq1.098684114+0.455089861i'), '제곱하면 실수부 차는 1, 허수부의 두 배 곱도 1입니다. 다른 제곱근은 이 값의 음수이지만 원본은 주값만 요구합니다.')
 ],[
  C('1 · 주값을 물었으므로 각도는 π/4 하나를 택합니다.',M(r'|1+i|=\sqrt2,\quad\operatorname{Arg}(1+i)=\pi/4,\quad\operatorname{Log}(1+i)=\tfrac12\ln2+i\pi/4'), '전체 로그의 2πk를 추가하지 않는 것은 principal value(주값)를 구하라는 지시 때문입니다.'),
  C('2 · 지수 c=1/2를 괄호 전체에 곱합니다.',M(r'\tfrac12(\tfrac12\ln2+i\pi/4)=\tfrac14\ln2+i\pi/8'),M(r'e^{(\ln2)/4}e^{i\pi/8}=2^{1/4}(\cos(\pi/8)+i\sin(\pi/8))'), '반지름 √2의 제곱근은 2¹⁄⁴이고, 각도 π/4의 절반은 π/8입니다. n제곱근 공식으로 풀어도 같은 값입니다.'),
  C('3 · 반각공식으로 좌표를 정확하게 씁니다.',M(r'\cos\frac\pi8=\sqrt{\frac{1+\cos(\pi/4)}2},\quad\sin\frac\pi8=\sqrt{\frac{1-\cos(\pi/4)}2}'), 'π/8은 제1사분면이라 두 제곱근에 양의 부호를 택합니다. 2¹⁄⁴을 곱하면 실수부 a=√((√2+1)/2),허수부 b=√((√2−1)/2)입니다.'),
  C('4 · 제곱하여 원래 수인지 확인합니다.',M(r'a^2-b^2=1,\quad2ab=2\sqrt{\frac{(\sqrt2+1)(\sqrt2-1)}4}=1'),M(r'(a+ib)^2=(a^2-b^2)+2abi=1+i'), '수치로는 약 1.098684114+0.455089861i입니다. 부호를 둘 다 바꾼 값도 제곱하면 같지만, 주값은 위의 제1사분면 값입니다.')
 ],role='원본 예제 · 상세 풀이')
