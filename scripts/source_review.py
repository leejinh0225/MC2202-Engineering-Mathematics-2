"""Source-image errata, shared by both reading modes before their explanations."""
from note_content import p, m

REVIEWS = {}
def add(page, kind, title, observed, tex, reason):
    REVIEWS[page] = (kind, title, observed, tex, reason)

add(2,'suspect','세로 벡터의 +4와 계산식의 −4가 다릅니다',
    '위쪽 y 벡터의 마지막 성분은 +4, 아래 내적 계산의 마지막 성분은 −4입니다.',
    r'\langle(1,-2,3,-1),(4,1,-2,-4)\rangle=0',
    '아래 계산식의 합 4−2−6+4=0은 맞습니다. 세로 벡터의 +4를 그대로 사용한 별도 내적은 −8입니다. 두 표기가 충돌하므로 오타가 의심되며, 본문은 직교 예제를 이루는 아래 계산식의 −4를 따릅니다. +4가 적힌 벡터까지 직교한다고 읽지 않습니다.')
add(3,'error','유한차원 합의 상한',
    'Rⁿ의 유한 기저를 설명하는 마지막 합에 ∞가 붙어 있습니다.',
    r'\mathbf{x}=\sum_{j=1}^{n}\langle\mathbf{u}_j,\mathbf{x}\rangle\mathbf{u}_j',
    '정규직교기저가 n개인 유한차원 벡터 공간에서는 n항을 합합니다. 무한급수는 이후 함수 공간으로 확장할 때의 별도 표현입니다.')
add(4,'error','적분 변수 dt → dx',
    '함수 내적의 integrand(피적분함수)는 f(x)g(x)인데 적분 미소량은 dt입니다.',
    r'\langle f,g\rangle=\int_a^b f(x)g(x)\,dx',
    '적분 변수는 일관되어야 합니다. t로 쓰고 싶다면 f(t)g(t) dt처럼 함수의 변수도 함께 바꿉니다.')
add(6,'error','사인·코사인 곱을 합으로 바꾸는 두 번째 항',
    '두 번째 사인 항에도 (n+m)x가 반복되어 있습니다.',
    r'\sin(nx)\cos(mx)=\tfrac12\{\sin((n+m)x)+\sin((n-m)x)\}',
    '삼각함수 덧셈정리를 더하면 확인됩니다. n=m에서는 두 번째 사인 항이 0이며, 적분 과정에서 n−m으로 나누는 공식을 그대로 대입하지 않습니다.')
add(7,'error','사인·사인 곱의 부호',
    '곱-합 변환에서 두 코사인 항의 순서와 부호가 뒤집혀 있습니다.',
    r'\sin(nx)\sin(mx)=\tfrac12\{\cos((n-m)x)-\cos((n+m)x)\}',
    'n=m을 넣으면 sin²(nx)=(1−cos(2nx))/2가 되어야 합니다. n≠m일 때 최종 직교 적분이 0이라는 결론은 맞지만, 중간 항등식은 교정해야 합니다.')
add(9,'error','사인 원시함수의 음의 부호',
    '∫sin(nx) dx의 원시함수에 음의 부호가 빠져 있습니다.',
    r'\int\sin(nx)\,dx=-\frac{\cos(nx)}{n}\quad(n\ne0)',
    '오른쪽을 미분하면 sin(nx)가 됩니다. 전체 주기 양 끝의 코사인 값이 같아서 이 예제의 최종 적분 0은 유지됩니다. 최종값이 맞아도 중간 부호는 잘못된 경우입니다.')
for page,func,coeff in [(10,'cos','a'),(11,'sin','b')]:
    add(page,'caution','교차항이 0이라는 조건의 범위',
        '중간 전개의 “=0 (m≠n)”은 내적 전체가 0이라는 뜻으로 읽으면 안 됩니다.',
        rf'\int_{{-\pi}}^\pi f(x)\{func}(mx)\,dx=\pi {coeff}_m\quad(m\ge1)',
        '합 안에서 주파수가 다른 개별 교차항만 직교성으로 사라집니다. m=n인 항은 남아서 찾으려는 계수를 줍니다. 원본은 합 전체와 개별 항의 조건을 짧게 적어 범위가 불명확한 경우입니다.')
add(13,'caution','S₃와 코드 반복문의 항 개수',
    '그림의 S₃는 비영 항 세 개를 사용하지만, 코드의 n=1:3은 최고 차수가 3이라는 뜻입니다.',
    r'S_{\text{3 nonzero terms}}(x)=\frac4\pi\left(\sin x+\frac{\sin3x}{3}+\frac{\sin5x}{5}\right)',
    '이 예제의 짝수 사인 계수는 0입니다. n=1:3에서는 n=1,3 두 항만 남습니다. 그림처럼 세 비영 항을 넣으려면 n=1,3,5를 사용합니다. 부분합 번호의 규약을 먼저 정해야 합니다.')
add(14,'caution','푸리에 급수의 점별 수렴 조건',
    '원본의 piecewise continuous(조각별 연속) 조건만으로 모든 점에서의 수렴을 일반적으로 단정할 수는 없습니다.',
    r'S(x)=\frac{f(x^-)+f(x^+)}2',
    '위 결론에는 조각별 매끄러움 등 적절한 충분조건이 필요합니다. 연속점에서는 f(x), 점프점에서는 좌우 극한의 평균입니다. 이 예제의 점 값 f(1)=1/2와 급수의 합 3/4도 구별합니다. <a href="https://dlmf.nist.gov/1.8.ii">NIST DLMF의 수렴 조건</a>과 대조했습니다.')
add(17,'error','변수 치환의 불필요한 u',
    '적분 변수를 바꾸는 중간 줄의 (π/L)u du에는 u가 하나 더 곱해져 있습니다.',
    r'\theta=\frac{\pi u}{L}\quad\Longrightarrow\quad d\theta=\frac\pi L\,du',
    '치환식을 미분하면 Jacobian(변수 변환 인자)은 상수 π/L입니다. 추가 u는 나오지 않습니다. 원본 마지막 상자의 일반 주기 계수식은 맞습니다.')
add(19,'suspect','h로 정의한 함수를 g로 적은 줄',
    '사인 계수에서 h=f sin으로 정의한 뒤 중간 적분에는 g가 쓰입니다.',
    r'h(x)=f(x)\sin\frac{n\pi x}{L},\qquad b_n=\frac1L\int_{-L}^{L}h(x)\,dx',
    '코사인 계수에 쓰던 g와 사인 계수에 쓰는 h를 구분해야 합니다. 앞 줄의 기호를 복사한 오타로 보입니다.')
add(20,'error','선형성 전개의 1/(2L) → 1/L',
    'aₙ·bₙ을 두 적분으로 나누는 중간 줄의 인자가 1/(2L)로 바뀝니다.',
    r'a_n=\frac1L\int_{-L}^{L}f(x)\cos\frac{n\pi x}{L}\,dx\quad(n\ge1)',
    '적분을 더하거나 나누는 선형성 때문에 계수가 절반이 되지는 않습니다. bₙ도 1/L이며, 상수항 a₀의 1/(2L)은 그대로 맞습니다.')
add(21,'error','사인의 지수 표현은 합이 아니라 차입니다',
    '사인을 대입하는 중간 줄에서 두 지수항이 +로 연결되어 있습니다.',
    r'\sin(nx)=\frac{e^{inx}-e^{-inx}}{2i}',
    '두 지수항의 합은 코사인과 관련됩니다. 위쪽에 적힌 Euler(오일러) 관계식과 대조하면 사인 분자에는 음의 부호가 필요합니다.')
add(22,'error','복소 계수 유도에서 중복된 1/2',
    'aₙ·bₙ의 적분 인자와 바깥 1/2가 겹쳐 계수가 한 번 더 절반이 되는 중간 줄이 있습니다.',
    r'c_n=\frac{a_n-i b_n}{2}=\frac1{2\pi}\int_{-\pi}^{\pi}f(x)e^{-inx}\,dx\quad(n\ge1)',
    '이 자료에서 실수 계수 aₙ·bₙ의 적분 인자는 1/π입니다. 바깥 1/2를 곱해 1/(2π)가 됩니다. 원본 최종 cₙ 공식은 맞으며, c₀=a₀입니다.')
add(23,'error','시간 주기의 실수 계수에 빠진 2',
    '시간 주기 T의 aₙ·bₙ 적분 앞이 1/T로 적혀 있습니다.',
    r'a_n=\frac2T\int_{t_0}^{t_0+T}f(t)\cos(n\omega_0t)\,dt,\qquad\omega_0=\frac{2\pi}T',
    'bₙ도 2/T를 사용합니다. f(t)=cos(ω₀t)를 대입하면 a₁=1이어야 하는데 1/T로 계산하면 1/2가 되어 검산에 실패합니다. 상수항 a₀와 복소 계수 cₙ의 1/T는 올바릅니다.')
add(26,'caution','적분제곱오차와 평균제곱오차',
    '원본이 mean-square error라고 부르는 E에는 구간 길이로 나누는 인자가 없습니다.',
    r'E=\int_{-\pi}^{\pi}(f-F)^2\,dx,\qquad\mathrm{MSE}=\frac{E}{2\pi}',
    'E는 적분제곱오차입니다. 평균제곱오차는 여기에 1/(2π)를 곱합니다. 고정된 구간에서는 두 양을 최소화하는 계수가 같으므로 이후 최소제곱 계수 계산은 유지됩니다.')
add(27,'caution','제곱 전개에서 생략한 교차항',
    '두 번째 줄의 cos(nx)sin(mx) 적분에는 계수가 없고, 상수항·서로 다른 차수 사이의 교차항도 모두 펼쳐져 있지는 않습니다.',
    r'\int_{-\pi}^{\pi}F^2\,dx=2\pi a_0^2+\pi\sum_{n=1}^{N}(a_n^2+b_n^2)',
    '제곱을 직접 펼칠 때 교차항은 2aₙbₘ cos(nx)sin(mx)처럼 계수를 포함해야 합니다. 상수항 및 서로 다른 주파수의 교차 적분도 직교성으로 0이 됩니다. 이를 모두 제거한 위 식과 원본 최종 오차식은 맞습니다.')
add(35,'error','sin² 항등식의 + → −',
    'sin²(mx)를 바꾸는 식의 cos(2mx) 앞이 +로 인쇄되어 있습니다.',
    r'\sin^2(mx)=\frac{1-\cos(2mx)}2',
    'x=0을 넣으면 왼쪽이 0이므로 오른쪽도 0이어야 합니다. +라면 1이 되어 모순됩니다. 바로 앞 34쪽 원본 노름식의 제곱근은 정상이며 교정 대상이 아닙니다.')
add(37,'caution','고유함수 직교성에 필요한 경계조건',
    '서로 다른 고유값이면 직교한다는 결론에는 경계항이 0이라는 조건이 필요합니다.',
    r'(\lambda_m-\lambda_n)\int_a^b r(x)y_m y_n\,dx=0',
    '같은 자기수반 Sturm–Liouville(스튀름–리우빌) 문제의 경계조건을 만족하는 고유함수에 대한 결론입니다. 임의의 두 미분방정식 해가 항상 직교한다는 뜻은 아닙니다. 유도와 경계항은 아래 본문에 따로 전개합니다.')
add(38,'caution','Legendre 다항식 번호가 한 칸씩 다릅니다',
    '다항식 목록은 P₁=1부터 시작하지만, λₙ=n(n+1)과 뒤 41쪽의 전개는 P₀=1 규약을 사용합니다.',
    r'P_0(x)=1,\quad P_1(x)=x,\quad P_2(x)=\frac{3x^2-1}{2}',
    '목록을 1번부터 세는 방식 자체가 불가능한 것은 아니지만, 그 경우 고유값의 번호도 맞춰야 합니다. 이 노트는 표준인 0번 시작으로 통일합니다. 다항식의 모양이 틀린 것과 번호가 다른 것을 구별합니다.')
add(39,'caution','Bessel 차수와 영점 번호를 구별합니다',
    'Bessel 함수의 직교성에서 차수와 영점 번호를 같은 의미로 읽기 쉽습니다.',
    r'\int_0^1 xJ_\nu(j_{\nu,m}x)J_\nu(j_{\nu,n}x)\,dx=0\quad(m\ne n)',
    '이 식은 고정된 차수 ν≥0와 서로 다른 양의 영점 j<sub>ν,m</sub>, j<sub>ν,n</sub>에 대한 예입니다. x=0의 정칙성 및 같은 끝점 경계조건도 필요합니다. 차수가 다른 모든 Bessel 함수가 이 내적으로 직교한다는 주장은 아닙니다. <a href="https://dlmf.nist.gov/10.22.ii">NIST DLMF Bessel 적분</a>을 참고합니다.')
add(41,'error','합의 시작 번호와 노름 첨자',
    '합은 m=1부터라고 쓰고 바로 뒤에는 a₀P₀를 포함하며, 계수 유도의 m·n도 혼용됩니다.',
    r'f(x)\sim\sum_{m=0}^{\infty}a_mP_m(x),\qquad a_m=\frac{2m+1}{2}\int_{-1}^{1}f(x)P_m(x)\,dx',
    '상수 성분 P₀를 포함하려면 합은 0부터 시작합니다. m번째 함수의 노름 제곱은 2/(2m+1)이므로 분모 첨자도 m으로 맞춥니다.')
add(42,'suspect','주석·범례의 sin(x)와 실제 sin(πx)',
    '코드 주석과 범례의 sin(x)는 실제 계산 함수 sin(πx)와 다릅니다.',
    r'f(x)=\sin(\pi x)',
    '계수 계산과 코드 실행식은 sin(πx)를 사용합니다. 본문도 이 함수를 기준으로 풉니다. 계수의 적분 구간 [−1,1]과 일부 그림에서 보여 주는 [0,1]은 서로 다른 역할입니다.')
for page in (43,45):
    add(page,'caution','Bessel 부등식에서 정규화 조건',
        'Σaₘ²만으로 쓴 식에는 각 기준 함수의 노름이 1이라는 가정이 필요합니다.',
        r'\sum_m |a_m|^2\|y_m\|^2\le\|f\|^2,\qquad a_m=\frac{\langle f,y_m\rangle}{\|y_m\|^2}',
        '직교기저를 정규화하지 않았다면 노름 제곱을 유지합니다. 정규직교기저일 때만 ||yₘ||²=1로 생략됩니다. 내적과 노름에는 이 문제의 구간과 가중함수 r(x)를 동일하게 사용합니다.')
add(44,'error','일반 적분구간과 교차항의 계수',
    '일반 구간 [a,b]의 증명 중간에 [−π,π]가 나타나고, 교차항에 aₘ²가 쓰이면서 다른 인덱스 n의 합 범위가 빠져 있습니다.',
    r'\left\|\sum_{m=0}^{k}a_my_m\right\|^2=\sum_{m=0}^{k}\sum_{n=0}^{k}a_ma_n\langle y_m,y_n\rangle=\sum_{m=0}^{k}a_m^2\|y_m\|^2',
    '실수 계수의 제곱 전개는 aₘaₙ 이중합입니다. m≠n인 항이 직교성으로 사라지고, m=n인 항에만 aₘ²가 남습니다. 모든 적분은 같은 [a,b]와 가중함수를 사용하며, 마지막 노름 생략에는 정규화 조건도 필요합니다.')
add(46,'caution','Parseval 등식의 완비성 조건',
    '계수 제곱의 합이 함수의 전체 노름 제곱과 같다는 결론은 직교성만으로 보장되지 않습니다.',
    r'\|f\|^2=\sum_m|\langle f,y_m\rangle|^2',
    '위 표현은 정규직교 함수계에 대한 식입니다. 모든 대상 함수에서 등식을 보장하려면 함수계가 완비해야 합니다. 불완전한 함수계라도 특정 f가 그 함수계의 닫힌 선형생성공간에 속하면 등식이 성립할 수 있습니다.')

LABELS={'error':'원본 오류 확인','suspect':'원본 오타 의심','caution':'표기·조건 주의'}
def source_review(page):
    if page not in REVIEWS:return ''
    kind,title,observed,tex,reason=REVIEWS[page]
    return (f'<div class="callout source-review" id="source-check-{page:02}" data-review-kind="{kind}">'
            f'<h3>{LABELS[kind]} · {title}</h3>'
            +p('<strong>원본 표기:</strong> '+observed)+m(tex)
            +p('<strong>판단 근거:</strong> '+reason)+'</div>')

def source_review_index():
    links=' · '.join(f'<a href="#source-check-{page:02}">{page:02}쪽 {REVIEWS[page][1]}</a>' for page in sorted(REVIEWS))
    return '<div class="card source-review-index"><h3>슬라이드 아래의 표기 검토 안내</h3>'+p('원본 이미지와 직접 계산을 대조한 편집자 검토입니다. <strong>원본 오류 확인</strong>은 수식·단위·자료 내부 모순이 확인된 경우, <strong>원본 오타 의심</strong>은 문맥상 오타로 보이는 경우, <strong>표기·조건 주의</strong>는 가정과 기호 해석을 보충하는 경우입니다. 같은 안내가 기본·뉴비 모드에 모두 표시됩니다.')+p(links)+'</div>'
