"""Week 9-10: independently readable standard and beginner paths."""
from html import escape
PAGES={}
def M(tex): return '<div class="math-block" data-tex="'+escape(tex,quote=True)+'"></div>'
def C(title,*parts,kind='card'):
    return '<div class="'+kind+'"><h3>'+title+'</h3>'+''.join(p if p.startswith('<') else '<p>'+p+'</p>' for p in parts)+'</div>'
def table(head,rows):
    return '<div class="table-wrap"><table class="compare-table"><thead><tr>'+''.join('<th>'+v+'</th>' for v in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+v+'</td>' for v in row)+'</tr>' for row in rows)+'</tbody></table></div>'
def paths(a,b): return '<div class="reading-path standard-reading"><p class="reading-path__label">기본 해설</p>'+a+'</div><div class="reading-path beginner-reading"><p class="reading-path__label">뉴비 해설 · 이유부터 차근차근</p>'+b+'</div>'
def add(n,title,a,b=None,role='개념·유도'):
    PAGES[n]=dict(title=title,standard=''.join(a),beginner=''.join(b or []),role=role)
add(1,'Complex numbers & functions(복소수와 복소함수)',[C('수의 계산에서 평면 위 함수의 미분으로','복소수의 대수·기하 → 극형식과 근 → 영역·극한 → 복소미분과 Cauchy–Riemann equations(코시–리만 방정식) → 지수·로그·삼각함수 → 원본 연습문제 순서로 읽습니다.','Arshad Afzal의 원본 58쪽을 모두 보존했습니다. Week 9–10은 제공 파일명에 따른 구분이며 정확한 날짜·영상·스크립트는 미제공입니다. 한국어 해설, 생략된 계산과 증명, 조작 그림은 편집자 작성입니다. 별도 창작 계산 문제·모의시험을 추가하지 않았습니다.',kind='quiet-card')],role='표지')
from complex_algebra import populate as algebra
from complex_analysis import populate as analysis
from complex_elementary import populate as elementary
from complex_problems import populate as problems
for populate in (algebra,analysis,elementary,problems): populate(add,C,M,table)
