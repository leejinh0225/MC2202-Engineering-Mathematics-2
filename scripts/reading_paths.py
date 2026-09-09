"""Compose complete alternative explanations while keeping source material shared."""
import re
from note_content import c,p,m
from beginner_content import B
import beginner_periodic, beginner_problems, beginner_advanced

assert set(B)==set(range(2,49))-{29,31,33,48}, 'Missing beginner explanation'

def cards(body):
    depth=0
    start=0
    for token in re.finditer(r'<div\b[^>]*>|</div>',body):
        if token.group().startswith('</'):
            depth-=1
            if depth==0:
                yield body[start:token.end()]
        else:
            if depth==0: start=token.start()
            depth+=1
    assert depth==0

def paths(standard,beginner):
    return ('<div class="reading-path standard-reading"><p class="reading-path__label">기본 해설</p>'+standard+'</div>'
            '<div class="reading-path beginner-reading"><p class="reading-path__label">뉴비 해설 · 이유부터 차근차근</p>'+beginner+'</div>')

def source_body(page,body):
    if page not in B: return body
    blocks=list(cards(body))
    shared=''.join(x for x in blocks if 'id="fourier-canvas"' in x)
    standard=''.join(x for x in blocks if 'class="card newbie-note"' not in x and 'id="fourier-canvas"' not in x)
    return paths(standard,B[page])+shared

def summary_body(body):
    standard=''.join(x for x in cards(body) if 'class="card newbie-note"' not in x)
    beginner=c('1. 이 단원에서 하려는 일부터 잡습니다.',p('복잡한 그래프 하나를 쉬운 그래프 여러 개의 합으로 나타내려 합니다. 예를 들어 f(x)=2+3cos x−sin 2x는 높이 2인 수평선, 세 배로 키운 코사인, 위아래를 뒤집은 사인을 같은 x에서 더한 것입니다. Fourier series(푸리에 급수)는 주어진 그래프에서 이 2, 3, −1 같은 숫자를 거꾸로 찾아내는 방법입니다.')+p('Coefficient(계수)는 각 그래프 앞의 숫자입니다. Σ는 번호를 바꾸며 더하라는 뜻이고, ∫는 아주 작은 구간의 값을 촘촘히 더하는 integration(적분) 기호입니다. 이 기호들이 무엇을 하는지는 해당 페이지에서 다시 풀어 설명합니다.'))
    beginner+=c('2. 왜 갑자기 곱하고 적분하나요?',p('우리가 원하는 것은 여러 파동 중 한 파동의 크기만 알아내는 것입니다. 그냥 적분하면 사인과 코사인은 양수·음수 부분이 서로 지워져 원하는 파동까지 사라집니다. 대신 찾고 싶은 파동과 같은 함수를 먼저 곱합니다. 같은 함수의 곱은 제곱이 되어 양수로 남고, 서로 다른 파동의 곱은 한 주기 동안 더하면 0이 됩니다. 이것이 orthogonality(직교성)를 이용하는 이유입니다.')+p('이제 남은 값에는 기준 함수 자신의 크기도 곱해져 있으므로 그것으로 나눕니다. “골라내기 → 기준 크기로 나누기”가 계수 공식의 구조입니다.')+m(r'\text{계수}=\frac{\text{목표 함수와 기준 함수의 곱을 적분}}{\text{기준 함수의 제곱을 적분}}'))
    beginner+=c('3. 문제에서는 어떤 순서로 생각하나요?',p('먼저 그래프가 어디까지 갔다가 반복되는지 확인합니다. 그 길이가 period(주기)입니다. 주기에 맞는 사인·코사인을 정한 다음, 좌우 대칭을 살펴봅니다. Even function(짝함수)이면 사인 계수는 0이고, odd function(홀함수)이면 상수·코사인 계수는 0이므로 남은 것만 계산하면 됩니다. 왜 0인지는 곱한 그래프의 부호를 따라 확인합니다.')+p('함수의 식이 중간에서 바뀌면 적분도 그 위치에서 나눕니다. 계수를 구한 뒤에는 첫 몇 항을 직접 쓰고 평균값·함숫값을 대입해 검사합니다. 본문의 문제 풀이는 이 선택 이유, 계산 중간 단계, 최종 답, 검산을 연결합니다.'))
    beginner+=c('4. 뒤에서 다른 함수와 미분방정식이 나오는 이유는 무엇인가요?',p('앞에서는 사인·코사인을 기준으로 삼았지만 상황에 따라 다른 기준 함수가 더 잘 맞습니다. 끝점에서 값이 0이어야 한다는 boundary condition(경계조건) 등을 만족하는 함수를 미분방정식에서 찾아 쓰기도 합니다. 그때 허용되는 수를 eigenvalue(고유값), 해당 함수를 eigenfunction(고유함수)이라고 합니다.')+p('기준이 달라져도 각 성분을 골라내는 원리는 같습니다. 마지막에는 “몇 개의 기준만 쓰면 오차가 얼마나 남는가”, “계속 더하면 모든 성분을 표현할 수 있는가”를 따집니다. 어려운 용어를 먼저 외우기보다, 각 페이지에서 해결하려는 질문부터 따라가십시오.'))
    return paths(standard,beginner)
