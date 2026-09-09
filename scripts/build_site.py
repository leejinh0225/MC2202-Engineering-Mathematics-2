from pathlib import Path
import re, html, shutil, json
from note_content import PAGES,p,m,c,n,steps
from home_page import render_home
ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'site'
template=(SITE/'templates/lecture-page.template.html').read_text(encoding='utf-8')

overview='복잡한 함수를 기본 함수의 합으로 바꾸고, 내적으로 각 성분의 크기를 구합니다.'
conceptmap='<div class="grid-3">'+''.join(c(t,p(b)) for t,b in [
('01 · 벡터에서 함수로','Inner product(내적) → orthogonality(직교성) → projection(정사영). 함수의 계수가 어디서 나오는지 이해합니다.'),
('02 · 주기와 대칭','Fourier coefficient(푸리에 계수) → even/odd symmetry(짝·홀 대칭) → complex form(복소수 형식) → 문제 풀이.'),
('03 · 기저의 확장','Sturm–Liouville problem(스튀름–리우빌 문제) → eigenfunction(고유함수) → completeness(완비성)와 오차.')])+'</div>'
summary=c('핵심 질문: 어떤 기본 함수를 얼마씩 더해야 하는가?',p('Fourier series(푸리에 급수)는 함수의 좌표를 찾는 방법입니다. 기준 함수들이 orthogonal(직교)하면 목표 함수와 특정 기준 함수의 inner product(내적)를 계산해 그 성분만 골라낼 수 있습니다. 기준 함수의 norm squared(노름 제곱)로 나누면 coefficient(계수)가 됩니다.')+m(r'\text{계수}=\frac{\langle f,y_n\rangle}{\langle y_n,y_n\rangle}'))
summary+=c('주기 2L의 기본 공식과 풀이 흐름',m(r'f(x)\sim a_0+\sum_{n=1}^{\infty}\left[a_n\cos\frac{n\pi x}{L}+b_n\sin\frac{n\pi x}{L}\right]')+p('전체 period(주기)가 2L임을 먼저 확인합니다. a₀는 한 주기 평균이므로 적분 앞 계수가 1/(2L)이고, aₙ과 bₙ의 계수는 1/L입니다. Even function(짝함수)이면 사인이 사라지고, odd function(홀함수)이면 상수항·코사인이 사라집니다. 조각별 함수는 식이 바뀌는 위치에서 적분을 나눕니다.')+steps([p('주기·구간·상수항 a₀ 규약을 확인합니다.'),p('짝함수·홀함수인지 검사하여 0인 계수를 먼저 없앱니다.'),p('남은 적분을 계산하고 n=1, n=0 등 분모가 0이 되는 예외를 따로 처리합니다.'),p('일반 계수를 구한 뒤 앞의 몇 항을 펼쳐 부호와 주파수를 확인합니다.'),p('평균값과 연속점·점프점의 극한으로 답을 검사합니다.')]))
summary+=c('급수의 합과 원래 함수가 같아지는 조건',p('이 자료의 조각별 매끄러운 주기함수는 연속점에서 함수값, 점프점에서는 좌우 극한의 평균으로 수렴합니다. Piecewise continuity(조각별 연속)만으로 일반적인 점별 수렴을 단정하지 않습니다. Gibbs phenomenon(깁스 현상)은 점프 근처의 초과 진동이 좁아져도 최고 초과량이 사라지지 않는 현상입니다. Mean-square convergence(평균제곱 수렴)는 각 점의 오차와 별개로 전체 적분제곱오차가 0으로 가는 것입니다.'))
summary+=c('복소수·반구간·고유함수도 같은 원리입니다.',p('Complex form(복소수 형식)은 사인과 코사인을 eⁱⁿωᵗ로 묶는 표기입니다. Half-range expansion(반구간 전개)은 주어진 오른쪽 구간을 짝연장·홀연장해서 각각 코사인·사인 급수로 표현합니다. Sturm–Liouville problem(스튀름–리우빌 문제)의 적절한 경계조건은 서로 직교하는 eigenfunctions(고유함수)를 만들어 줍니다. 기저가 완비하면 빠진 성분이 없어 Parseval’s equality(파르세발 등식)가 성립하고, 그렇지 않으면 잔차가 남을 수 있습니다.'))
summary+=n('기호를 읽기 위한 작은 출발점',p('n은 1,2,3,…으로 움직이는 번호, aₙ은 n번째 계수입니다. π는 약 3.14159이고 2π rad은 한 바퀴입니다. ∫는 작은 값들을 촘촘하게 더하는 integration(적분), Σ는 번호를 바꾸며 항을 더하는 summation(합)을 뜻합니다. y′는 기울기, y″는 기울기의 변화율입니다.')+p('처음에는 모든 공식을 한꺼번에 외우지 않아도 됩니다. “기본 파동의 크기를 내적으로 추출한다”는 한 줄을 먼저 잡고, 각 페이지의 예시 숫자와 계산 단계를 따라가십시오. 뉴비 모드는 같은 용어를 유지하면서 필요한 고등학교 수학을 그 자리에서 다시 설명합니다.'))

match=re.search(r'        <section class="source-section".*?</section>',template,re.S)
source_template=match.group(0)
sections=[]
for i,page in enumerate(PAGES,1):
    s=source_template
    replacements={'NN':f'{i:02}','SLIDE_ROLE':page['role'],'SLIDE_HEADING':page['title'],'LECTURE_SLUG':'fourier','DESCRIPTIVE_ALT_TEXT':f"Fourier series 원본 PDF {i}쪽: {page['title']}",'CURRENT_PAGE':str(i),'PAGE_COUNT':'48','TRANSCRIPT_TIME_OR_SLIDE_ROLE':'원본 PDF · 본문 해설은 편집자 작성','SLIDE_EXPLANATION_BLOCKS':page['body']}
    for key,value in replacements.items(): s=s.replace('{{'+key+'}}',value)
    sections.append(s)
template=template[:match.start()]+'\n'.join(sections)+template[match.end():]

exam_items=[
('What is a Fourier coefficient?','A Fourier coefficient measures the contribution of a basis function, obtained by projection onto that function.','Fourier coefficient(푸리에 계수)는 특정 기준 함수가 얼마나 들어 있는지 알려 주며, 직교만 되어 있다면 노름 제곱으로 나누는 절차도 필요합니다.'),
('Why does an odd function have only sine terms?','The constant and cosine coefficients vanish because their integrands are odd over a symmetric interval.','Odd function(홀함수)의 상수항·코사인 계수 적분은 대칭 구간에서 0입니다.'),
('What does the series converge to at a jump?','Under suitable regularity conditions, it converges to the average of the left-hand and right-hand limits.','조건을 갖춘 함수의 jump discontinuity(점프 불연속점)에서는 함수의 점 값이 아니라 좌우 극한의 평균입니다.'),
('Describe the Gibbs phenomenon.','Near a jump, the oscillations become narrower as more terms are added, but the peak overshoot does not vanish.','Gibbs phenomenon(깁스 현상)의 폭 감소와 최고 초과량을 구별해 설명합니다.'),
('Find the eigenvalues and eigenfunctions.','The eigenvalues are λₙ=n² for n=1,2,…, with nonzero eigenfunctions yₙ(x)=C sin(nx). Zero and negative λ give only the trivial solution.','p.47의 boundary conditions(경계조건)에 대한 답입니다. C≠0 조건과 λ≤0을 제외한 이유를 함께 적습니다.'),
('Distinguish Bessel’s inequality from Parseval’s equality.','Bessel’s inequality bounds the captured coefficient energy by the total squared norm. For a complete orthonormal system, Parseval’s equality accounts for the entire norm.','Orthonormal system(정규직교 함수계)이라는 조건을 빼지 말고, 잔여 에너지의 유무로 구분합니다.')]
exam=''.join('<div class="exam-card"><h3>'+q+'</h3><div class="answer"><span class="answer__label">Model answer</span>'+a+'</div>'+p(k)+'</div>' for q,a,k in exam_items)
terms=[('Inner product','내적','대응 성분을 곱해 합하거나, 함수의 곱을 적분하는 연산.'),('Orthogonal','직교','정해진 내적이 0인 관계.'),('Orthonormal','정규직교','서로 직교하며 각 노름이 1인 성질.'),('Basis / completeness','기저 / 완비성','표현에 쓰는 기준 함수 / 필요한 함수를 노름 오차 없이 극한으로 근사할 수 있는 성질.'),('Projection','정사영','선택한 기준 방향에 해당하는 성분을 추출하는 연산.'),('Period / fundamental period','주기 / 기본주기','동일한 모양이 반복되는 간격 / 존재할 때의 최소 양의 주기.'),('Harmonic','고조파','기본 주파수의 정수배 주파수 성분.'),('Coefficient / partial sum','계수 / 부분합','각 기준 함수의 크기 / 유한 개 항까지의 합.'),('Even / odd function','짝함수 / 홀함수','f(−x)=f(x) / f(−x)=−f(x).'),('Convergence','수렴','정해진 의미의 오차가 0에 가까워지는 것.'),('Jump discontinuity','점프 불연속','좌우 극한이 유한하지만 서로 다른 불연속.'),('Gibbs phenomenon','깁스 현상','점프 근처에 생기는 부분합의 초과 진동.'),('Complex conjugate','켤레복소수','실수부는 유지하고 허수부의 부호를 바꾼 수.'),('Frequency / angular frequency','주파수 / 각주파수','초당 반복 횟수 Hz / 초당 위상 변화 rad/s.'),('Half-range expansion','반구간 전개','(0,L)의 함수를 짝·홀 연장하여 구성하는 급수.'),('Norm / weight function','노름 / 가중함수','함수의 크기 / 내적에서 위치별 비중을 정하는 양의 함수.'),('Eigenvalue / eigenfunction','고유값 / 고유함수','경계조건을 만족하는 비자명해를 허용하는 수 / 그 함수.'),('Trivial / nontrivial solution','자명해 / 비자명해','여기서는 항등적으로 0인 해 / 그 밖의 해.'),('Boundary condition','경계조건','구간 끝점에서 함수와 도함수에 부과하는 조건.'),('Find / determine','구하라 / 결정하라','필요한 계수나 함수와 그 조건까지 제시하라는 문제 지시.'),('Show / verify','보여라 / 검증하라','결과뿐 아니라 근거나 대입 확인을 제시하라는 문제 지시.'),('Assume / represent / approximate','가정하라 / 표현하라 / 근사하라','전제를 두라 / 등가 전개를 구하라 / 오차를 허용하여 가까운 표현을 구하라.')]
glossary='<table class="compare-table"><thead><tr><th>English(한국어)</th><th>뜻과 사용</th></tr></thead><tbody>'+''.join('<tr><td>'+a+'('+b+')</td><td>'+d+'</td></tr>' for a,b,d in terms)+'</tbody></table>'
audits=[
('전체','강의 영상·스크립트 없음','PDF와 직접 계산에 근거한 편집자 해설입니다. ASR 기록은 해당 없음입니다.'),
('2','벡터의 마지막 성분 +4와 계산의 −4 충돌','표시 벡터로는 −8. 마지막 성분을 −4로 바꿀 때만 내적 0.'),
('3–4','유한차원 합 상한 ∞, 함수 내적의 dt','유한차원은 기저 개수까지, x 함수의 적분은 dx. 무한 복원에는 완비성·수렴 조건 필요.'),
('6–7','삼각함수 곱-합 변환의 인수·부호','sin A cos B의 두 번째 항은 sin(A−B), sin A sin B는 cos(A−B)−cos(A+B). n=m을 별도 처리.'),
('9–11','사인 원시함수의 부호, 교차항 0 표기','∫sin(nx)dx=−cos(nx)/n. 0은 개별 교차항의 적분이며 목표 내적 전체가 항상 0인 것은 아님.'),
('13','S₃의 세 비영 항과 코드 n=1:3의 불일치','세 비영 항은 n=1,3,5. 기존 반복문은 n=1,3만 비영.'),
('14','조각별 연속이면 점별 수렴한다는 단정','조각별 매끄러움 등 충분조건을 명시. 예제의 f(1)=1/2와 급수 합 3/4를 구분.'),
('16–17','치환 변수의 혼용과 중간 줄의 불필요한 u','θ=πu/L, dθ=(π/L)du. 일반 주기 공식은 원본 상자와 일치.'),
('19–20','h를 g로 표기, aₙ·bₙ 선형성 중간 인자','h=f sin을 일관되게 사용. 1/(2L)을 1/L로 교정.'),
('21–22','사인 지수 변환 부호와 중복 1/2','사인 분자는 두 지수의 차. cₙ의 적분 인자는 1/(2π).'),
('23','시간 주기 실수 계수 인자 1/T','aₙ,bₙ에는 2/T. a₀,cₙ에는 1/T. f=cos(ω₀t)로 교차 확인.'),
('24','0번 복소 계수 생략','c₀=1/2를 별도 적분으로 보충. n≠0 공식에 0을 직접 대입하지 않음.'),
('26–27','제곱오차 명칭과 생략된 교차항','적분제곱오차와 평균제곱오차를 구분. 모든 교차항이 직교성으로 사라지는 과정 보충.'),
('34–35','텍스트 추출 시 루트 누락, sin² 항등식 부호','p.34 이미지의 루트는 올바름. 추출문만 보고 원본 오류로 취급하지 않음. p.35 sin² 항등식의 +는 −로 교정.'),
('36–39','직교성과 특이 끝점에 필요한 조건','자기수반 경계조건과 정칙성 조건을 명시. Bessel 차수와 영점 번호를 분리.'),
('38, 41','Legendre 번호와 합 하한 혼용','P₀=1부터 시작하고 m으로 통일. 노름은 √(2/(2m+1)), 노름 제곱은 2/(2m+1).'),
('42','sin(x) 주석과 실제 sin(πx) 계산','실제 함수를 따름. 계산 구간 [−1,1]과 그림 구간 [0,1]을 구분.'),
('43–46','정규직교 조건과 일반 적분구간','a,b 및 가중 내적 사용. 비정규화 기저에는 ||yₘ||² 유지. 불완전한 기저라도 특정 함수에는 등식 가능.'),
('29, 31, 33, 48','원본 빈 풀이 페이지','빈 페이지도 순서대로 보존. 작성한 풀이는 해당 문제 페이지에 묶음.')]
audit='<p>원본의 수식·그림을 확인하고 다시 계산한 기록입니다. 원본 이미지의 오류는 덮어쓰지 않으며, 아래와 본문에서 교정합니다. 강사의 구두 설명이나 시험 출제 의도는 추정하지 않습니다.</p><table class="compare-table"><thead><tr><th>PDF 쪽</th><th>원본 확인 사항</th><th>해설의 처리</th></tr></thead><tbody>'+''.join('<tr><td>'+a+'</td><td>'+b+'</td><td>'+d+'</td></tr>' for a,b,d in audits)+'</tbody></table>'
sources='<div class="card">'+p('<a href="materials/Fourier%20series.pdf" download="Fourier series.pdf">Fourier series.pdf</a> · Arshad Afzal · 48쪽. 주차·수업 날짜 미기재. 원본의 전 페이지를 순서대로 보존했습니다.')+p('본문의 설명·유도·완성 풀이와 뉴비 설명은 원본을 바탕으로 작성한 편집자 해설입니다. 원문에 없는 추가 예제·가정·검산은 편집자 보강으로 구분했습니다.')+p('표준 공식 대조: <a href="https://dlmf.nist.gov/1.8">NIST DLMF §1.8 · Fourier series</a> (계수 규약·수렴 조건), <a href="https://dlmf.nist.gov/18.3">§18.3 · Orthogonal polynomials</a> (Legendre 표기·노름), <a href="https://dlmf.nist.gov/10.22">§10.22 · Bessel integrals</a> (고정 차수의 가중 직교성). 외부 자료의 a₀/2 규약은 이 노트의 a₀ 규약으로 바꾸어 비교했습니다.')+'</div>'
toc=[('overview','단원 개요'),('concept-map','개념 지도'),('concept-summary','핵심 개념 요약')]+[(f'slide-{i:02}',f'{i:02} · '+v['title']) for i,v in enumerate(PAGES,1)]+[('exam-english','시험 영어'),('glossary','핵심 용어'),('asr-log','원본 검토·교정'),('sources','출처')]
replace={'LECTURE_NUMBER':'Fourier series','LECTURE_TITLE':'Fourier series','ONE_SENTENCE_DESCRIPTION':'공업수학 II 푸리에 급수: 원본 48쪽, 상세 풀이, 기본·뉴비 모드의 한국어 수업 대체 노트','WEEK':'공업수학 II','LECTURE_PROMISE':'함수의 좌표를 내적으로 구하는 원리부터 푸리에 급수와 고유값 문제까지. 원본 옆의 상세 해설과 완성 풀이로 공부합니다.','DATE_OR_날짜_미기재':'미기재','PAGE_COUNT':'48','VIDEO_SET':'PDF 기반 · 강의 영상 없음','ALL_CONTENTS_AND_PROBLEM_SOLVING_BUTTONS':'','ORIGINAL_PDF_URL':'materials/Fourier series.pdf','LECTURE_NOTE_FILENAME':'Fourier series.pdf','CORE_RELATIONSHIP_HEADLINE':overview,'CORE_RELATIONSHIP_EXPLANATION':'Inner product(내적)에서 시작해 orthogonal expansion(직교 전개)의 원리를 익히고, 주기·대칭·경계조건에 맞는 함수를 조립합니다. 원본의 모든 페이지와 상세 문제 풀이를 한 문서에서 이어 읽을 수 있습니다.','CONCEPT_MAP_HEADLINE':'내적 → 푸리에 계수 → 주기·대칭 → 고유함수','CONCEPT_MAP_BLOCKS':conceptmap,'STANDALONE_CONCEPT_SUMMARY':summary,'DISTINCT_SUMMARY_VIDEO_SECTION_IF_NEEDED':'','EXAM_SECTION_TITLE':'개념을 설명하고 풀이를 서술하는 영어 문장','BILINGUAL_GLOSSARY_TABLE':glossary,'AUDIT_SECTION_TITLE':'원본 검토·교정 기록 · 스크립트 없음','ASR_CORRECTION_TABLE':audit,'SOURCE_LIST_AND_PROVENANCE_NOTE':sources,'TABLE_OF_CONTENTS_LINKS':''.join(f'<li><a href="#{key}">{label}</a></li>' for key,label in toc)}
start=template.index('            <div class="exam-card">',template.index('id="exam-english"'))
end=template.index('\n          </div>',start)
template=template[:start]+exam+template[end:]
for key,value in replace.items():template=template.replace('{{'+key+'}}',value)
template=template.replace('MC2103 Dynamics','MC2202 Engineering Mathematics II').replace('| MC2103','| MC2202')
template=template.replace('이 부분만 읽어도 렉처의 핵심 정의, 개념 관계, 가정과 풀이 흐름을 이해할 수 있도록 작성합니다.','이 요약은 정의·공식·가정·풀이 순서를 한 흐름으로 연결합니다. 각 페이지의 상세 해설과 풀이도 아래에 모두 수록했습니다.')
template=template.replace('<span class="header-meta">Fourier series · Fourier series</span>','<button type="button" class="mode-toggle" id="mode-toggle" aria-pressed="false">뉴비 모드 켜기</button>')
template=template.replace('</head>','<link rel="stylesheet" href="assets/vendor/katex/katex.min.css"><link rel="stylesheet" href="assets/css/math-note.css?v=home-3"><script src="assets/js/mode-init.js"></script></head>')
template=template.replace('<div class="page-shell">','<div class="mode-guide"><strong id="mode-status">기본 모드 · 밝은 화면</strong><p>상단 뉴비 모드를 켜면 다크 화면으로 전환되고, 고등학교 수학부터 연결하는 부연 설명이 추가됩니다. 핵심 용어와 기본 해설·문제 풀이는 두 모드에서 같습니다.</p><noscript>JavaScript가 꺼져 있어 모든 뉴비 해설을 함께 표시합니다.</noscript></div><div class="page-shell">')
template=template.replace('</body>','<script src="assets/js/math-note.js" defer></script></body>')
# Repeated bilingual terminology in beginner cards, retaining existing bilingual phrases.
mapping={'정규직교':'orthonormal(정규직교)','짝함수':'even function(짝함수)','홀함수':'odd function(홀함수)','부분적분':'integration by parts(부분적분)','내적':'inner product(내적)','적분':'integration(적분)','직교성':'orthogonality(직교성)','고유값':'eigenvalue(고유값)','경계조건':'boundary condition(경계조건)','계수':'coefficient(계수)','사인':'sine(사인)','코사인':'cosine(코사인)'}
def bilingual(match):
    block=match.group(0)
    chunks=re.split('(<[^>]+>)',block)
    for j in range(0,len(chunks),2):
        for k,v in mapping.items():chunks[j]=re.sub(r'(?<![가-힣(])'+k+r'(?![)])',v,chunks[j])
    return ''.join(chunks)
# Process by the next card boundary, not math-div nesting.
template=re.sub(r'<div class="card newbie-note">.*?(?=<div class="(?:card|callout|quiet-card|exam-card)"|</section>)',bilingual,template,flags=re.S)
template=re.sub(r'<!--.*?-->','',template,flags=re.S)
template=template.replace('materials/Fourier%20series.pdf','materials/Fourier series.pdf')
template=template.replace('assets/css/styles.css','assets/css/styles.css?v=mc2202-1')
if re.search(r'\{\{.*?\}\}',template):raise RuntimeError('Unresolved template token')
(SITE/'fourier-series.html').write_text('\n'.join(line.rstrip() for line in template.splitlines())+'\n',encoding='utf-8')

def shell(title,body):return '<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>'+title+' | MC2202</title><link rel="stylesheet" href="assets/css/styles.css"><link rel="stylesheet" href="assets/css/math-note.css?v=home-3"><script src="assets/js/mode-init.js"></script></head><body><header class="site-header"><div class="site-header__inner"><a class="wordmark" href="index.html">MC2202 Engineering Mathematics II</a><div class="header-actions"><a class="header-link" href="downloads.html">PDF 다운로드</a><button class="mode-toggle" id="mode-toggle" aria-pressed="false" type="button">뉴비 모드 켜기</button></div></div></header><section class="hero"><div class="hero__inner"><p class="eyebrow">공업수학 II · 강의자료 정리노트</p><h1>'+title+'</h1><p class="hero__lead">원본 자료와 한국어 해설, 단계별 문제 풀이를 이어 읽는 학습 노트.</p></div></section><main class="landing-content">'+body+'</main><footer class="site-footer"><div class="site-footer__inner">MC2202 · Engineering Mathematics II</div></footer><script src="assets/js/math-note.js" defer></script></body></html>'
lecture_card = '<article class="lecture-card"><div class="lecture-card__body"><span class="status-pill">작성 완료</span><p class="section-kicker" style="margin-top:22px">공업수학 II · 날짜 미기재</p><h2>Fourier series(푸리에 급수)</h2>'+p('내적과 직교성에서 시작해 푸리에 급수, 함수 근사, Sturm–Liouville 문제와 일반화된 급수까지 상세 해설과 풀이로 연결합니다.')+'<div class="meta-row"><span class="meta-chip">원본 슬라이드 48장</span><span class="meta-chip">PDF 기반 해설</span><span class="meta-chip">기본·뉴비 모드</span></div><div class="button-row"><a class="button button--primary" href="fourier-series.html">정리노트 읽기</a><a class="button" href="fourier-series.html#slide-28">문제 풀이</a><a class="button" href="materials/Fourier series.pdf" download="Fourier series.pdf" type="application/pdf">원본 PDF 다운로드</a></div></div><div class="lecture-card__image"><img src="assets/slides/fourier/slide-01.jpg" alt="Fourier series 원본 첫 페이지 표지 슬라이드" width="1920" height="1080"></div></article>'
(SITE/'index.html').write_text(render_home(shell,lecture_card),encoding='utf-8')
size=(SITE/'materials/Fourier series.pdf').stat().st_size
(SITE/'downloads.html').write_text(shell('원본 PDF 다운로드.',c('Fourier series.pdf',p(f'Arshad Afzal · 48쪽 · {size:,} bytes · 주차·날짜 미기재')+'<div class="button-row"><a class="button button--primary" href="materials/Fourier series.pdf" download="Fourier series.pdf" type="application/pdf">Fourier series.pdf 다운로드</a><a class="button" href="fourier-series.html">정리노트</a></div>')),encoding='utf-8')
vendor=SITE/'assets/vendor/katex'
vendor.mkdir(parents=True,exist_ok=True)
src=ROOT/'tmp/katex/package'
shutil.copy2(src/'dist/katex.min.css',vendor/'katex.min.css')
shutil.copytree(src/'dist/fonts',vendor/'fonts',dirs_exist_ok=True)
shutil.copy2(src/'LICENSE',vendor/'LICENSE')
print('Built 48 source sections; static equations await render_math.cjs')
