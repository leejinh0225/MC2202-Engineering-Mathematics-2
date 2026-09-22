"""Continuous complex transform, properties, and convolution: slides 15–24."""
def populate(add, C, M, table):
    add(15, '코사인 차 공식으로 두 적분 묶기', [
        C('사인과 코사인을 하나의 커널로', M(r"\cos(\omega v)\cos(\omega x)+\sin(\omega v)\sin(\omega x)=\cos[\omega(x-v)]"), M(r"f_*(x)=\frac1\pi\int_0^\infty\left[\int_{-\infty}^{\infty}f(v)\cos[\omega(x-v)]\,dv\right]d\omega"), 'p.5의 두 항에서 f(v)를 모두 포함시킨 다음 삼각함수 항등식을 사용합니다. x−v는 복원하려는 위치와 원본을 훑는 위치 사이의 차입니다.'),
        C('짝함수인 것은 코사인 커널이다', M(r"K_x(\omega)=\int_{-\infty}^{\infty}f(v)\cos[\omega(x-v)]\,dv,\qquad K_x(-\omega)=K_x(\omega)"), M(r"f_*(x)=\frac1{2\pi}\lim_{R\to\infty}\int_{-R}^R K_x(\omega)\,d\omega"), '코사인이 ω에 대해 짝함수이므로 주파수 구간을 양쪽으로 확장하고 1/2을 붙일 수 있습니다. 일반적인 complex Fourier transform(복소 푸리에 변환) 자체가 항상 짝함수라는 뜻은 아닙니다.')
    ], [
        C('1 · 긴 괄호 안에 아는 공식이 숨어 있습니다.', '코사인 성분과 사인 성분을 동시에 더하던 식을 더 짧게 쓰려는 단계입니다. 고등학교의 cos(A−B)=cos A cos B+sin A sin B에 A=ωx, B=ωv를 넣어 보십시오.', M(r"\cos(\omega x)\cos(\omega v)+\sin(\omega x)\sin(\omega v)=\cos[\omega(x-v)]")),
        C('2 · 왜 두 변수의 차가 나오나요?', 'x는 결과를 그리는 위치이고, v는 입력을 읽는 위치입니다. 두 파동을 곱해 연결하던 것이 위치 차 x−v에 대한 하나의 파동으로 묶였습니다. 원본 f(v)는 두 항 모두에 곱해져 있어야 합니다.', M(r"f_*(x)=\frac1\pi\int_0^\infty\int_{-\infty}^{\infty}f(v)\cos[\omega(x-v)]\,dv\,d\omega")),
        C('3 · 음의 주파수까지 늘리는 대신 절반을 취합니다.', 'ω 대신 −ω를 넣으면 코사인 안의 부호가 바뀝니다. cos(−θ)=cos θ이므로 값은 같습니다. 따라서 양쪽에서 더한 넓이는 양의 쪽만 더한 넓이의 두 배입니다. 적분구간을 늘리면서 계수를 1/π에서 1/(2π)로 바꾸는 이유입니다.', M(r"\frac1\pi\int_0^R K_x(\omega)\,d\omega=\frac1{2\pi}\int_{-R}^R K_x(\omega)\,d\omega")),
        C('4 · 아직 모든 푸리에 변환이 짝함수라는 말은 아닙니다.', '지금 대칭을 이용한 대상은 cos[ω(x−v)]를 포함하는 Kₓ입니다. 곧 등장할 복소 변환 F에는 사인 정보도 들어가므로 일반적으로 짝함수가 아닙니다. 서로 다른 중간식을 원본에서 비슷한 F 기호로 표현하더라도 역할은 나누어 읽습니다.')
    ], audit='원본 중간 전개에서는 f(v)가 두 삼각함수 항 모두에 곱해진다는 괄호가 불명확합니다. 또한 이 페이지에서 짝함수라고 한 대상은 코사인 커널의 ω 의존성입니다. 일반 복소 변환 F와 구분하여 Kₓ로 표기합니다.')

    add(16, 'Euler’s formula(오일러 공식)로 복소 지수 만들기', [
        C('0이 되는 사인 항을 더한다', M(r"\int_{-R}^R\left[\int_{-\infty}^{\infty}f(v)\sin[\omega(x-v)]\,dv\right]d\omega=0"), 'ω에 대한 홀함수이므로 대칭 주파수 구간에서 사인 항이 상쇄됩니다. 여기에 i를 곱해 더해도 전체 복원값은 변하지 않습니다.'),
        C('복소 지수의 곱으로 분해', M(r"\cos\theta+i\sin\theta=e^{i\theta},\qquad e^{i\omega(x-v)}=e^{i\omega x}e^{-i\omega v}"), M(r"f_*(x)=\frac1{2\pi}\lim_{R\to\infty}\int_{-R}^R\left[\int_{-\infty}^{\infty}f(v)e^{-i\omega v}\,dv\right]e^{i\omega x}\,d\omega"), '유한 R에서는 절대적분 가능한 f에 대해 적분 재배열이 가능하고, 이후 복원 정리의 조건으로 R→∞를 취합니다. 복소수 사용은 정보를 추가하는 것이 아니라 두 실수 성분을 한 식에 묶는 표현 방식입니다.')
    ], [
        C('1 · 실수 함수를 복원하는데 왜 i가 등장하나요?', 'i는 i²=−1인 imaginary unit(허수단위)입니다. 복소수 a+ib는 실수 a와 b 두 값을 한 묶음으로 표현할 수 있습니다. 여기서는 cosine(코사인)과 sine(사인)을 따로 쓰는 대신 복소 지수 한 개로 관리하려는 것입니다.'),
        C('2 · 마음대로 사인을 더해도 되는 것이 아닙니다.', '먼저 음의 주파수와 양의 주파수를 같은 범위로 적분합니다. sin[−ω(x−v)]=−sin[ω(x−v)]이므로 양쪽이 정확히 상쇄됩니다. 그 사인 적분 전체가 0이라는 사실을 확인한 뒤에만 i배를 더합니다.', M(r"\int_{-R}^R\sin[\omega(x-v)]\,d\omega=0")),
        C('3 · 덧셈이 지수의 곱으로 바뀝니다.', M(r"\cos[\omega(x-v)]+i\sin[\omega(x-v)]=e^{i\omega(x-v)}=e^{i\omega x}e^{-i\omega v}"), 'Euler’s formula(오일러 공식)는 실수 지수의 증가·감소를 말하는 식과 다릅니다. eⁱθ는 복소평면의 단위원 위를 도는 점이고, 실수부가 cos θ, 허수부가 sin θ입니다. 지수의 덧셈 법칙을 적용하면 x에 관한 인자와 v에 관한 인자를 분리할 수 있습니다.'),
        C('4 · 분해식과 복원식이 보이기 시작합니다.', M(r"f_*(x)=\frac1{2\pi}\lim_{R\to\infty}\int_{-R}^R\underbrace{\left[\int_{-\infty}^{\infty}f(v)e^{-i\omega v}\,dv\right]}_{\text{주파수별 정보를 추출}}\underbrace{e^{i\omega x}}_{\text{위치 }x\text{에서 복원}}\,d\omega"), '안쪽에는 −iωv, 바깥에는 +iωx가 들어갑니다. 분해할 때와 다시 조립할 때 회전 방향이 반대라고 생각하면 부호를 기억하는 데 도움이 됩니다. 다음 페이지는 1/(2π)를 두 단계에 공평하게 나누어 정의합니다.')
    ])

    add(17, 'Fourier transform(푸리에 변환)과 역변환의 정의', [
        C('이 단원에서 사용할 대칭 규약', M(r"\boxed{F(\omega)=\mathcal F[f](\omega)=\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)e^{-i\omega x}\,dx}"), M(r"\boxed{f_*(x)=\mathcal F^{-1}[F](x)=\frac1{\sqrt{2\pi}}\lim_{R\to\infty}\int_{-R}^RF(\omega)e^{i\omega x}\,d\omega}"), '소문자 f는 원래 변수의 함수, 대문자 F는 frequency domain(주파수 영역)의 함수입니다. 정변환과 역변환에 각각 1/√(2π)를 붙여 두 상수의 곱이 1/(2π)가 되도록 합니다. 복원에는 p.3의 정칙성 조건을 함께 사용합니다.'),
        C('다른 책의 공식과 비교할 때', '정변환에 상수를 붙이지 않고 역변환에 1/(2π)를 붙이는 규약도 있습니다. 이 노트는 원본의 대칭 규약을 유지합니다. 지수 부호·상수·주파수가 rad/s인지 Hz인지 세 가지를 먼저 확인해야 공식들을 섞지 않습니다.', M(r"\omega=2\pi\nu\quad(\nu:\ \mathrm{Hz}),\qquad |e^{-i\omega x}|=1"), '절대적분 가능한 f라면 변환 F는 유계·연속이고 먼 주파수에서 0으로 갑니다. 역적분이 항상 절대수렴하는 것은 아니므로, 여기서는 대칭 상한의 복원 극한을 명시했습니다.')
    ], [
        C('1 · 변환은 함수를 보는 좌표를 바꾸는 일입니다.', '시간이나 위치 x로 신호를 보면 “어디에서 얼마나 큰가”를 알 수 있습니다. ω로 변환하면 “얼마나 빠른 파동이 얼마나 들어 있는가”를 볼 수 있습니다. 새로운 신호를 만든 것이 아니라 같은 정보를 다른 기준으로 표현한 것입니다.'),
        C('2 · 정변환: x를 없애고 ω를 남깁니다.', M(r"F(\omega)=\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)e^{-i\omega x}\,dx"), 'ω를 하나 정해 f(x)에 비교 파동 e⁻ⁱωˣ를 곱하고 x 전체를 더합니다. dx로 적분했으므로 x는 사라집니다. ω를 바꾸어 반복하면 결과 F(ω)가 됩니다. F는 일반적으로 복소수이므로 크기와 phase(위상), 즉 회전 방향 정보까지 가집니다.'),
        C('3 · 역변환: ω를 없애고 x를 남깁니다.', M(r"f_*(x)=\frac1{\sqrt{2\pi}}\lim_{R\to\infty}\int_{-R}^RF(\omega)e^{i\omega x}\,d\omega"), '이번에는 복원할 x를 정합니다. 모든 주파수 성분 F(ω)를 해당 파동 eⁱωˣ에 곱해 더합니다. 적분 대상은 ω이므로 dω이고, 적분 안에 들어가는 입력도 f(x)가 아니라 F(ω)입니다. 각 단계에서 무엇을 없애고 무엇을 남기는지 보면 변수 실수를 줄일 수 있습니다.'),
        C('4 · 상수와 부호를 한 세트로 기억합니다.', M(r"\frac1{\sqrt{2\pi}}\times\frac1{\sqrt{2\pi}}=\frac1{2\pi},\qquad\text{정변환: }-i\omega x,\quad\text{역변환: }+i\omega x"), '정규화는 정의에서 정한 약속이며, 한번 선택한 뒤 모든 성질과 문제 풀이에서 일관되게 따라야 합니다. 정의 자체와, 이 정의로 원래 함수를 복원할 수 있다는 정리는 구분합니다. 정리에는 p.3에서 확인한 수렴 조건이 필요합니다.')
    ], audit='원본 역변환 적분 안에는 원래 함수 f(x)가 다시 적혀 있습니다. 주파수의 함수를 입력해야 하므로 F(ω)로 표기합니다. 원본에서 원래 함수와 변환을 모두 f로 쓰던 표기도 f와 F로 구분했습니다.')

    add(18, '예제 · 한쪽 지수함수의 복소 변환', [
        C('0이 아닌 오른쪽만 적분한다', M(r"f(x)=\begin{cases}e^{-ax},&x>0,\\0,&x<0,\end{cases}\quad a>0"), M(r"F(\omega)=\frac1{\sqrt{2\pi}}\int_0^\infty e^{-(a+i\omega)x}\,dx=\frac1{\sqrt{2\pi}}\left[-\frac{e^{-(a+i\omega)x}}{a+i\omega}\right]_0^\infty=\frac1{\sqrt{2\pi}(a+i\omega)}")),
        C('실수부·허수부와 크기', M(r"F(\omega)=\frac{a-i\omega}{\sqrt{2\pi}(a^2+\omega^2)},\qquad |F(\omega)|=\frac1{\sqrt{2\pi}\sqrt{a^2+\omega^2}}"), '분모의 켤레 a−iω를 곱하면 실수부와 허수부가 드러납니다. 원래 함수가 짝함수가 아니므로 F는 일반적으로 복소수입니다. 원점의 함수값을 0이나 1로 지정해도 변환은 같고, 역변환의 점프점 값은 1/2입니다.')
    ], [
        C('1 · 왼쪽 구간이 0이라는 조건을 먼저 사용합니다.', '이 함수는 왼쪽에는 신호가 없고, 오른쪽에서 1로 시작해 지수적으로 줄어듭니다. 전체 실수에 대한 변환이지만 왼쪽 적분은 0이므로 0부터 ∞까지만 계산하면 됩니다. a&gt;0은 오른쪽으로 갈수록 작아지게 하는 조건입니다.'),
        C('2 · 두 지수함수는 지수를 더해 묶습니다.', M(r"e^{-ax}e^{-i\omega x}=e^{-(a+i\omega)x}"), 'a+iω는 x에 대해 상수입니다. 실제로 적분하는 동안 ω도 고정합니다. 실수 상수 b에 대해 ∫e⁻ᵇˣdx=−e⁻ᵇˣ/b였던 계산을 복소 상수 a+iω에도 적용합니다.', M(r"\int_0^\infty e^{-(a+i\omega)x}\,dx=\left[-\frac{e^{-(a+i\omega)x}}{a+i\omega}\right]_0^\infty=\frac1{a+i\omega}")),
        C('3 · 위끝에서 정말 0이 되나요?', 'e⁻ⁱωˣ는 계속 회전하지만 크기는 1입니다. e⁻ᵃˣ의 크기는 a&gt;0일 때 0으로 갑니다. 따라서 둘의 곱도 크기가 0이 되어 위끝이 사라집니다. 아래끝 x=0에서는 지수가 0이므로 값은 1입니다.', M(r"\boxed{F(\omega)=\frac1{\sqrt{2\pi}(a+i\omega)}}")),
        C('4 · 그래프의 높이는 복소수의 크기입니다.', '복소수 a+iω를 좌표 (a,ω)로 보면 원점에서의 거리는 피타고라스 정리에 의해 √(a²+ω²)입니다. 역수의 크기는 거리의 역수이므로 다음 식이 됩니다.', M(r"|F(\omega)|=\frac1{\sqrt{2\pi}\sqrt{a^2+\omega^2}}"), '원본의 스펙트럼 곡선은 이 크기입니다. 크기만 보면 좌우대칭이지만 F 자체의 허수부는 부호가 바뀝니다. 또한 x=0의 복원은 왼쪽 0과 오른쪽 1의 평균 1/2입니다.')
    ], role='예제·완성 풀이', audit='원본 첫 변환 줄의 적분 미소량은 dω로, 원시함수의 지수에는 x가 빠진 형태로 적혀 있습니다. x를 적분하는 과정과 e⁻⁽ᵃ⁺ⁱω⁾ˣ를 모두 표시했습니다. 최종 1/[√(2π)(a+iω)]의 정규화는 그대로 유지합니다.')

    add(19, '예제 · 양쪽 지수함수 e⁻ᵃ|ˣ|', [
        C('짝대칭이면 허수부가 사라진다', M(r"f(x)=e^{-a|x|},\quad a>0,\qquad F(\omega)=\frac2{\sqrt{2\pi}}\int_0^\infty e^{-ax}\cos(\omega x)\,dx=\sqrt{\frac2\pi}\frac{a}{a^2+\omega^2}"), 'f·sin은 홀함수여서 적분이 0입니다. f·cos는 짝함수여서 양의 구간 적분의 두 배입니다. 따라서 F는 실수 짝함수이며 이 예제에서는 양수입니다.'),
        C('반쪽 함수 두 개를 더해도 같은 답', M(r"F(\omega)=\frac1{\sqrt{2\pi}}\left(\frac1{a+i\omega}+\frac1{a-i\omega}\right)=\frac{2a}{\sqrt{2\pi}(a^2+\omega^2)}"), '오른쪽 지수함수와 그 좌우반사를 더하면 e⁻ᵃ|ˣ|입니다. p.18의 복소수 답 두 개가 서로 켤레라 허수부가 상쇄됩니다. p.14의 반구간 코사인 변환과 같은 수식이 나온 이유도 이 짝연장입니다.')
    ], [
        C('1 · 절댓값 하나가 함수 전체 모양을 바꿉니다.', 'x&gt;0이면 |x|=x라서 e⁻ᵃˣ입니다. x&lt;0이면 |x|=−x라서 eᵃˣ입니다. 양쪽 끝에서 모두 0으로 가고 가운데 x=0에서 1이 됩니다. 앞 페이지와 달리 왼쪽이 0인 함수가 아닙니다.'),
        C('2 · e⁻ⁱωˣ를 실수부와 허수부로 나눕니다.', M(r"e^{-i\omega x}=\cos(\omega x)-i\sin(\omega x)"), 'f는 좌우대칭입니다. f에 사인을 곱하면 왼쪽과 오른쪽이 부호만 달라 상쇄됩니다. 코사인을 곱한 것은 좌우가 같으므로 오른쪽 넓이의 두 배입니다. 여기서 2를 빼먹으면 답이 절반이 됩니다.', M(r"F(\omega)=\frac2{\sqrt{2\pi}}\int_0^\infty e^{-ax}\cos(\omega x)\,dx")),
        C('3 · 이미 구한 적분을 가져옵니다.', M(r"\int_0^\infty e^{-ax}\cos(\omega x)\,dx=\frac{a}{a^2+\omega^2}\quad\Longrightarrow\quad\boxed{F(\omega)=\sqrt{\frac2\pi}\frac{a}{a^2+\omega^2}}"), 'p.14에서 부분적분 두 번으로 구한 식입니다. 새로운 적분처럼 다시 시작할 필요 없이, 함수의 대칭을 확인해 익숙한 적분으로 줄이는 것이 풀이의 핵심입니다.'),
        C('4 · ω=0으로 배율을 검사합니다.', '주파수가 0이면 비교 파동이 1이 되므로 원래 함수의 전체 넓이만 남습니다. 오른쪽 넓이는 1/a, 왼쪽 넓이도 1/a이므로 전체는 2/a입니다.', M(r"F(0)=\frac1{\sqrt{2\pi}}\frac2a=\sqrt{\frac2\pi}\frac1a"), '최종 답에 ω=0을 넣어도 같은 값이 나옵니다. 정규화 상수나 좌우 두 배를 빠뜨렸는지 빠르게 확인하는 방법입니다.')
    ], role='예제·완성 풀이', audit='원본 중간 줄은 전구간 적분을 0부터 ∞까지로 바꾸면서 필요한 2가 빠진 형태입니다. 해설에서는 짝대칭의 2를 유지하고, 원본의 올바른 최종 답 √(2/π)a/(a²+ω²)과 대조했습니다.')

    add(20, '선형성과 도함수의 복소 푸리에 변환', [
        C('기본 성질과 성립 조건', M(r"\mathcal F[\alpha f+\beta g]=\alpha F+\beta G,\qquad\mathcal F[f']=i\omega F,\qquad\mathcal F[f'']=-\omega^2F"), 'f와 필요한 도함수가 적분 가능하고 충분히 매끄러우며, 해당 무한대 경계항이 사라지는 상황에서 사용합니다. 전구간 적분이므로 반구간 공식의 f(0) 항은 없습니다.'),
        C('부분적분으로 iω 확인', M(r"\mathcal F[f']=\frac1{\sqrt{2\pi}}[fe^{-i\omega x}]_{-\infty}^{\infty}+i\omega\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}fe^{-i\omega x}\,dx=i\omega F"), M(r"\mathcal F[f'']=i\omega\mathcal F[f']=(i\omega)^2F=-\omega^2F"), '지수 미분의 −iω와 부분적분의 빼기가 만나 +iω입니다. 한쪽 지수함수처럼 원점에서 점프하는 함수를 구간 내부의 도함수 −af만으로 처리하면 점프 기여를 잃습니다. 이런 함수에는 매끄러움 가정을 확인하거나 분포 도함수를 별도로 사용해야 합니다.')
    ], [
        C('1 · 미분이 곱셈으로 바뀌는 것이 변환의 장점입니다.', 'f′가 들어 있는 방정식은 함수를 구해야 하는 문제입니다. 그런데 변환하면 f′가 iωF로 바뀝니다. f″는 −ω²F입니다. 같은 미지수 F에 숫자를 곱하는 형태이므로 대수적으로 정리하기 쉬워집니다.', M(r"\mathcal F[f']=i\omega F,\qquad \mathcal F[f'']=-\omega^2F")),
        C('2 · 미분을 파동 쪽으로 옮깁니다.', M(r"\int f'(x)e^{-i\omega x}\,dx=f(x)e^{-i\omega x}-\int f(x)(-i\omega)e^{-i\omega x}\,dx"), 'integration by parts(부분적분)를 썼습니다. 두 번째 항에는 바깥의 −와 지수 미분의 −가 동시에 있으므로 +가 됩니다. 함수 f가 양끝에서 0으로 가면 첫 경계항은 사라지고 iω 곱셈만 남습니다.'),
        C('3 · 두 번 미분의 음수는 어디서 나오나요?', M(r"i\omega(i\omega F)=i^2\omega^2F=-\omega^2F"), 'i²=−1이므로 음수가 붙습니다. “두 번 미분하면 −ω²”를 무조건 외우기보다 한 번 미분할 때 iω를 곱한다는 규칙을 두 번 쓰면 됩니다. 반구간과 달리 여기서는 구간 끝이 ±∞라 x=0의 경계항은 없습니다.'),
        C('4 · 갑자기 뛰는 함수에는 주의합니다.', 'p.18의 한쪽 지수함수는 x=0에서 갑자기 0에서 1로 바뀝니다. 오른쪽에서의 기울기 −ae⁻ᵃˣ만 계산하면 그 점프 자체를 놓칩니다. 이 성질은 우선 매끄러운 함수에 적용한다고 이해하십시오. p.34의 e⁻ˣ²는 매끄럽고 양끝에서 빠르게 줄어들므로 이 성질로 안전하게 풀 수 있습니다.')
    ])

    add(21, 'Frequency shifting / time shifting(주파수·시간 이동)', [
        C('주파수 이동: 회전 지수를 곱한다', M(r"g(t)=e^{i\omega_0t}f(t)\quad\Longrightarrow\quad G(\omega)=F(\omega-\omega_0)"), M(r"G(\omega)=\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(t)e^{i\omega_0t}e^{-i\omega t}\,dt=\frac1{\sqrt{2\pi}}\int f(t)e^{-i(\omega-\omega_0)t}\,dt"), '실수 지수 e^ω₀t를 곱하는 것은 진폭의 지수적 변화이며 같은 주파수 이동 성질이 아닙니다.'),
        C('시간 이동: 스펙트럼에 위상을 곱한다', M(r"g(t)=f(t-t_0)\quad\Longrightarrow\quad G(\omega)=e^{-i\omega t_0}F(\omega)"), M(r"u=t-t_0\quad\Longrightarrow\quad e^{-i\omega t}=e^{-i\omega(u+t_0)}=e^{-i\omega t_0}e^{-i\omega u}"), 'f(t−t₀)는 t₀&gt;0일 때 오른쪽으로 이동합니다. |G|=|F|이므로 크기 스펙트럼은 같고 위상만 달라집니다. 이동한 함수가 t&lt;t₀에서 0이라고 말하려면 원래 f가 t&lt;0에서 0인 causal signal(인과 신호)이라는 조건이 추가로 필요합니다.')
    ], [
        C('1 · 두 이동은 서로 다른 조작입니다.', 'time shifting(시간 이동)은 같은 파형을 나중에 시작하도록 옆으로 옮기는 것입니다. frequency shifting(주파수 이동)은 성분표의 주파수 위치를 옮기는 것입니다. 이름이 비슷해도 원래 함수에 하는 계산은 다릅니다.'),
        C('2 · 주파수 이동의 부호를 지수끼리 합쳐 봅니다.', M(r"e^{i\omega_0t}e^{-i\omega t}=e^{-i(\omega-\omega_0)t}"), '변환 정의 속 ω가 ω−ω₀로 바뀌었습니다. 그러므로 결과도 F(ω−ω₀)입니다. ω₀&gt;0이면 원래 ω=0에 있던 성분은 새 식의 ω=ω₀에서 나타나므로 오른쪽으로 이동합니다.', M(r"\mathcal F[e^{i\omega_0t}f(t)]=F(\omega-\omega_0)"), '여기에는 i가 반드시 있어야 합니다. eⁱω₀t의 크기는 1이지만 e^ω₀t의 크기는 시간에 따라 커집니다.'),
        C('3 · 시간 이동은 고등학교 그래프 이동과 같습니다.', '예를 들어 f가 t=0에서 가장 높았다면 f(t−3)은 t=3에서 가장 높습니다. 괄호 안이 0이 되는 위치가 오른쪽으로 옮겨진 것입니다. u=t−t₀로 치환하면 t=u+t₀이므로 다음 인자가 나옵니다.', M(r"\mathcal F[f(t-t_0)]=e^{-i\omega t_0}F(\omega)")),
        C('4 · 시간이 늦어져도 주파수의 크기는 그대로입니다.', M(r"|e^{-i\omega t_0}|=1\quad\Longrightarrow\quad |G(\omega)|=|F(\omega)|"), '복소수에 크기 1인 수를 곱하면 길이는 그대로이고 방향만 회전합니다. 이것이 phase(위상) 변화입니다. 그래서 크기 스펙트럼만으로는 두 신호의 시작 시각 차이를 알 수 없습니다. 원본 그림의 지연 전 0 구간은 원래 신호가 0 이전에는 없었다는 조건에서 읽습니다.')
    ], audit='원본 주파수 이동의 지수 e^ω₀t에는 i가 빠져 있습니다. 정의에 대입하면 eⁱω₀t가 맞습니다. 시간 이동 유도에서는 a와 t₀, f와 g가 혼용되어 t₀와 원래 함수 f로 통일하고, 지연 전 0이라는 서술에는 인과성 조건을 명시합니다.')

    add(22, 'Scaling(스케일 변환) · 좁은 신호와 넓은 스펙트럼', [
        C('스케일 변환을 변수 치환으로 유도한다', M(r"g(t)=f(\lambda t),\quad\lambda>0\quad\Longrightarrow\quad G(\omega)=\frac1\lambda F\left(\frac\omega\lambda\right)"), M(r"u=\lambda t,\quad dt=\frac{du}\lambda\quad\Longrightarrow\quad G=\frac1{\lambda\sqrt{2\pi}}\int_{-\infty}^{\infty}f(u)e^{-i(\omega/\lambda)u}\,du")),
        C('폭과 높이가 함께 바뀐다', 'λ&gt;1이면 원래 변수에서 신호 폭은 1/λ배이고, 주파수 축에서는 폭이 λ배입니다. 변환의 높이에는 1/λ가 붙습니다. 음의 λ까지 확장하면 구간 방향 반전을 반영하여 1/|λ|를 사용합니다.', M(r"\mathcal F[f(\lambda t)](\omega)=\frac1{|\lambda|}F(\omega/\lambda),\qquad\lambda\ne0"), '이 페이지는 shift(이동)가 아니라 폭을 바꾸는 scaling(스케일 변환)입니다. 다음 합성곱에서도 치환으로 인한 배율을 주의해서 추적합니다.')
    ], [
        C('1 · f(2t)는 무엇이 두 배일까요?', 'f가 t=1에서 어떤 값을 가졌다면 f(2t)는 t=1/2에서 그 값을 갖습니다. 원래 그림을 가로로 절반으로 압축한 것입니다. 세로 높이를 두 배로 만든 2f(t)와는 다릅니다.'),
        C('2 · 적분변수를 바꾸면 두 변화가 나타납니다.', M(r"u=\lambda t,\qquad t=u/\lambda,\qquad dt=du/\lambda\quad(\lambda>0)"), 'f(λt)를 f(u)로 단순하게 바꾸는 대신, 지수 속 t도 u/λ로 바뀝니다. 따라서 주파수는 ω/λ로 보입니다. 또 작은 구간의 폭 dt도 du/λ로 바뀌므로 앞에 1/λ가 생깁니다.', M(r"G(\omega)=\frac1\lambda F(\omega/\lambda)")),
        C('3 · λ=2를 넣어 해석합니다.', M(r"f(2t)\ \longleftrightarrow\ \frac12F(\omega/2)"), '시간 파형은 절반 폭으로 압축됩니다. 주파수 그래프 F(ω/2)는 같은 값을 얻으려면 ω가 두 배 필요하므로 가로로 두 배 늘어납니다. 그리고 전체 높이는 1/2배가 됩니다. 짧고 급한 사건을 만들려면 더 빠른 파동까지 필요하다는 직관과 연결됩니다.'),
        C('4 · λ가 음수이면 좌우반사도 포함됩니다.', '예를 들어 λ=−1이면 f(−t)는 시간의 좌우반사입니다. 적분구간의 양끝 순서도 뒤집히므로 단순히 1/λ=−1을 남기면 안 됩니다. 순서 반전의 음수까지 반영한 일반식은 1/|λ|입니다.', M(r"G(\omega)=\frac1{|\lambda|}F(\omega/\lambda)\quad(\lambda\ne0)"))
    ], audit='원본 소제목은 frequency shifting(주파수 이동)이지만 수식과 그림은 λ&gt;0인 scaling(스케일 변환)입니다. 원본의 양수 조건에서는 1/λ가 맞으며, 음수까지 확장한 보강식에만 1/|λ|를 사용합니다.')

    add(23, 'Convolution(합성곱)의 정의와 변환', [
        C('정의: 뒤집고 옮긴 함수를 곱해 더한다', M(r"h(x)=(f*g)(x)=\int_{-\infty}^{\infty}f(p)g(x-p)\,dp=(g*f)(x)"), 'x를 고정하면 g(x−p)는 p에 대한 g의 좌우반사와 이동입니다. f(p)와 겹치는 부분을 곱해 적분하므로, 한 점의 곱 f(x)g(x)와 다릅니다. p↔x−p 치환으로 교환법칙이 성립합니다.'),
        C('Convolution theorem(합성곱 정리)', M(r"\boxed{\mathcal F[f*g]=\sqrt{2\pi}\,FG}\qquad\Longleftrightarrow\qquad(f*g)(x)=\int_{-\infty}^{\infty}F(\omega)G(\omega)e^{i\omega x}\,d\omega"), '여기서 합성곱의 정의에는 정규화 상수를 넣지 않았습니다. 따라서 대칭 푸리에 변환 규약과 결합할 때 √(2π)가 필요합니다. f,g가 절대적분 가능하면 정변환의 곱 공식이 성립합니다. 역적분의 점별 복원에는 별도의 수렴 조건을 함께 사용합니다.'),
        C('편집자 예제 · 두 상자의 겹침은 삼각형', M(r"f(x)=g(x)=\mathbf1_{[0,1]}(x)\quad\Longrightarrow\quad(f*g)(x)=\begin{cases}0,&x<0,\\x,&0\le x\le1,\\2-x,&1<x\le2,\\0,&x>2.\end{cases}"), '둘 다 1인 p의 구간은 [0,1]과 [x−1,x]의 교집합입니다. 그 길이가 처음에는 늘고, x=1에서 1이 된 뒤 다시 줄어듭니다. 합성곱을 겹침의 넓이로 읽는 예입니다.')
    ], [
        C('1 · 한 점의 곱과 무엇이 다른가요?', 'f(x)g(x)는 같은 x 위치의 두 값을 곱하고 끝납니다. convolution(합성곱)은 출력 위치 x를 고정한 뒤 가능한 모든 입력 위치 p를 살펴봅니다. 입력 f(p)가 출력에 얼마나 기여하는지 g(x−p)로 가중하여 더합니다.', M(r"(f*g)(x)=\int_{-\infty}^{\infty}f(p)g(x-p)\,dp")),
        C('2 · x−p는 입력 위치에서 출력 위치까지의 차이입니다.', '시간 신호라면 p는 입력이 발생한 시각, x는 결과를 보는 시각입니다. g(x−p)는 그 입력이 발생한 뒤 얼마가 지났는지에 따른 반응입니다. p를 바꾸며 여러 시각의 입력이 남긴 효과를 더하면 x에서의 전체 결과가 됩니다. 이 해석은 선형·시간불변 시스템의 응답을 이해할 때 사용합니다.'),
        C('3 · 숫자로 확인할 수 있는 두 상자 예시', 'f와 g가 각각 0부터 1까지 값 1이라고 해 봅니다. f(p)가 1이려면 0≤p≤1이고, g(x−p)가 1이려면 x−1≤p≤x입니다. 둘을 동시에 만족하는 구간의 길이가 적분값입니다.', table(['출력 위치 x', '겹치는 p 구간', '합성곱 값'], [['0.5','[0, 0.5]','0.5'],['1','[0, 1]','1'],['1.5','[0.5, 1]','0.5'],['2.5','없음','0']]), 'x를 움직이며 그리면 높이가 올랐다 내려오는 삼각형이 됩니다. 다음 페이지의 계산은 이런 합성곱을 주파수 영역에서 쉽게 다루는 이유를 보여 줍니다.'),
        C('4 · 주파수에서는 보통의 곱으로 바뀝니다.', M(r"\mathcal F[f*g](\omega)=\sqrt{2\pi}F(\omega)G(\omega)"), '두 함수를 각각 변환하고 같은 주파수의 값끼리 곱하면 됩니다. 앞의 √(2π)는 이 노트의 정의에서 생긴 배율입니다. 다른 자료에 FG만 적혀 있다면 먼저 정규화 규약이 같은지 확인하십시오.')
    ])

    add(24, '합성곱 정리의 유도와 지수함수 예제', [
        C('이중적분을 두 변환의 곱으로 분리', M(r"\begin{aligned}\mathcal F[f*g](\omega)&=\frac1{\sqrt{2\pi}}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}f(p)g(x-p)e^{-i\omega x}\,dp\,dx\\&=\frac1{\sqrt{2\pi}}\left[\int f(p)e^{-i\omega p}\,dp\right]\left[\int g(v)e^{-i\omega v}\,dv\right]\\&=\frac1{\sqrt{2\pi}}[\sqrt{2\pi}F][\sqrt{2\pi}G]=\sqrt{2\pi}FG.\end{aligned}"), 'v=x−p, x=v+p로 치환합니다. f,g∈L¹이면 이중 적분의 절댓값 적분이 ||f||₁||g||₁로 유한하여 적분 순서 교환이 정당합니다.'),
        C('편집자 예제 · 두 지수 반응의 합성곱', M(r"f(x)=e^{-ax}\mathbf1_{x\ge0},\quad g(x)=e^{-bx}\mathbf1_{x\ge0},\quad a,b>0"), M(r"(f*g)(x)=\int_0^x e^{-ap}e^{-b(x-p)}\,dp=e^{-bx}\int_0^xe^{(b-a)p}\,dp=\frac{e^{-ax}-e^{-bx}}{b-a}\quad(x\ge0,\ a\ne b)"), 'x&lt;0에서는 0이고, a=b이면 적분함수가 e⁻ᵃˣ로 일정하므로 xe⁻ᵃˣ입니다.'),
        C('변환으로 독립 검산', M(r"\mathcal F[f*g]=\frac1{\sqrt{2\pi}(a+i\omega)(b+i\omega)}=\frac1{b-a}\left[\frac1{\sqrt{2\pi}(a+i\omega)}-\frac1{\sqrt{2\pi}(b+i\omega)}\right]"), 'p.18의 역변환 쌍을 적용하면 같은 두 지수의 차를 얻습니다. a=b를 차이의 분모에 직접 대입하지 않고 원래 적분이나 극한을 쓰는 것이 중요합니다.')
    ], [
        C('1 · 왜 x−p를 새 변수 v로 정하나요?', '합성곱에는 f(p)와 g(x−p)가 엮여 있습니다. g 안의 x−p를 v라고 이름 붙이면 g(v)가 됩니다. 대신 x=v+p가 되어 복소 지수도 두 개의 곱으로 나뉩니다.', M(r"v=x-p\quad\Longrightarrow\quad e^{-i\omega x}=e^{-i\omega p}e^{-i\omega v}")),
        C('2 · p에 관한 것과 v에 관한 것을 따로 모읍니다.', M(r"\mathcal F[f*g]=\frac1{\sqrt{2\pi}}\left[\int f(p)e^{-i\omega p}\,dp\right]\left[\int g(v)e^{-i\omega v}\,dv\right]"), '첫 괄호는 f의 변환에서 1/√(2π)만 빠진 값, 둘째는 g의 변환에서 같은 상수만 빠진 값입니다. 따라서 각 괄호는 √(2π)F, √(2π)G입니다. 상수가 하나 없어지고 둘이 새로 붙으므로 최종적으로 하나가 남습니다.', M(r"\frac1{\sqrt{2\pi}}\times\sqrt{2\pi}\times\sqrt{2\pi}=\sqrt{2\pi}")),
        C('3 · 두 지수함수로 직접 계산해 봅니다.', '다음은 원본 정리를 이해하기 위한 추가 예제입니다. f(p)=e⁻ᵃᵖ는 p≥0에서만 있고, g(x−p)=e⁻ᵇ⁽ˣ⁻ᵖ⁾는 x−p≥0에서만 있습니다. 두 조건을 합치면 0≤p≤x입니다. 그래서 x&lt;0일 때는 겹침이 없고, x≥0일 때만 적분합니다.', M(r"h(x)=\int_0^xe^{-ap}e^{-b(x-p)}\,dp=e^{-bx}\int_0^xe^{(b-a)p}\,dp")),
        C('4 · 상수가 다른 경우와 같은 경우를 나눕니다.', M(r"h(x)=\begin{cases}\dfrac{e^{-ax}-e^{-bx}}{b-a},&a\ne b,\\xe^{-ax},&a=b,\end{cases}\quad x\ge0"), 'a≠b이면 지수의 원시함수를 구해 위끝과 아래끝을 뺍니다. a=b이면 e⁽ᵇ⁻ᵃ⁾ᵖ=e⁰=1이어서 적분은 구간 길이 x입니다. 분모가 0인 식에 억지로 대입하지 않고, 왜 그 예외가 생겼는지 원래 적분으로 돌아가 확인합니다.'),
        C('5 · 변환 정리로 계산한 답도 같습니다.', M(r"\sqrt{2\pi}FG=\frac1{\sqrt{2\pi}(a+i\omega)(b+i\omega)}"), '분모의 두 인자를 partial fractions(부분분수)로 나누면 p.18에서 풀었던 지수함수 두 개의 변환이 됩니다. 직접 적분과 변환 방법이 같은 결과를 내므로 부호와 √(2π) 배율까지 함께 검사할 수 있습니다.')
    ])
