"""Week 13 residue integration study note."""
from pathlib import Path
from complex_content import C, M, paths, table
from complex_lecture_layout import link, read_slides, render_lecture

HERE = Path(__file__).parent
SLUG = 'residue-integration'
PDF = 'Week 13.pdf'


def summary():
    standard = [
        C('Laurent coefficient(로랑 계수)에서 적분값으로',
          M(r'\operatorname{Res}_a f=[(z-a)^{-1}]f,\qquad \oint_C f\,dz=2\pi i\sum_{a\ {\rm inside}\ C}\operatorname{Res}_a f'),
          '대괄호는 지정한 차수의 계수를 읽는다는 기호입니다. 경계 위에 특이점이 없는 양의 단순폐곡선에 적용합니다. 시계방향으로 한 번 돌면 적분값의 부호가 바뀝니다.'),
        C('유수를 구하는 세 방법',
          M(r'q(a)=0,\ q^\prime(a)\ne0:\quad\operatorname{Res}_a(p/q)=p(a)/q^\prime(a)'),
          M(r'g(z)=(z-a)^mf(z):\quad\operatorname{Res}_a f=g^{(m-1)}(a)/(m-1)!'),
          '단순극은 인자 하나를 약분해도 됩니다. 고차 극의 미분이 복잡하거나 본질적 특이점이면 알려진 급수에서 역일차항을 직접 읽습니다.'),
        C('실수 적분에 맞는 경로 선택',
          '삼각함수의 한 주기는 z=exp(iθ), dθ=dz/(iz)로 단위원에 옮깁니다. 실수축 전체의 유리함수 적분은 큰 반원 기여가 0인지 확인합니다. 짝함수에서 [0,∞) 적분은 실수축 전체 값의 절반입니다. Fourier integral(푸리에 적분)의 exp(isz)는 s>0이면 위쪽, s<0이면 아래쪽에서 감쇠합니다.'),
        C('실수축 위에 단순극이 있는 경우',
          M(r'\operatorname{PV}\int_{-\infty}^{\infty}f(x)\,dx=2\pi i\sum_{\operatorname{Im}a>0}\operatorname{Res}_a f+\pi i\sum_{a\in\mathbb R}\operatorname{Res}_a f'),
          '큰 원호 적분이 0이고 실수축 위 단순극들을 작은 위쪽 반원으로 우회하는 경우입니다. 보통의 이상적분은 각 극의 한쪽 적분부터 따로 수렴해야 합니다.')]
    beginner = [
        C('첫째, 어디를 도는지 그립니다',
          '분모가 0이 되는 위치를 복소평면에 점으로 찍고 원 또는 타원에 넣어 봅니다. 단위원 안쪽은 |z|<1입니다. 경로가 한 번 둘러싼 내부 점들만 고릅니다. 점이 길 위에 있다면 경로를 조금 파내야 하는 별도 상황입니다.'),
        C('둘째, 각 점에서 분모 하나짜리 항의 앞 숫자를 찾습니다',
          '점 a 부근에 B/(z−a)라는 항이 있으면, 한 바퀴를 적분해도 이 항의 기여가 남습니다. 그 앞 숫자 B가 Residue(유수)입니다. 단순극이면 (z−a)를 곱해 약분하고 a를 대입합니다. 사인이나 지수의 급수가 주어졌다면 각 항의 차수를 옮겨 −1이 된 항을 찾으세요.'),
        C('셋째, 무엇을 구하는 문제인지 보고 마무리합니다',
          '유수를 물으면 B에서 끝납니다. 닫힌 경로 적분을 물으면 내부의 B들을 더해 반시계방향은 2πi, 시계방향은 −2πi를 곱합니다. 실수 적분이면 이 닫힌 길 중 어느 부분이 원래 구간인지 다시 봅니다. 0부터 ∞까지의 짝함수 문제에서는 마지막에 2로 나눕니다.'),
        C('실수축에 극이 있으면 작은 구멍 양옆의 넓이를 봅니다',
          '1/(x−a)의 원시함수는 ln|x−a|라서 한쪽에서 a로 다가갈 때 발산합니다. 양쪽을 같은 폭으로 잘라냈을 때 서로 지워지는 값이 Cauchy principal value(코시 주값)입니다. 위쪽 작은 반원은 시계방향 반 바퀴이므로 원래 실수축 적분을 풀어 쓸 때 그 점의 유수에 +πi가 붙습니다.')]
    return paths(''.join(standard), ''.join(beginner))


def build():
    slides = read_slides([HERE/'residue_readings.txt', HERE/'residue_real_practice.txt'], 18)
    roles = {n: '개념·예제 풀이' for n in slides}
    roles.update({1:'표지', 8:'원본 빈 풀이란 · 편집자 그림', 12:'원본 빈 풀이란 · 편집자 풀이',
                  15:'원본 빈 풀이란 · 편집자 검산', 16:'연습문제 1', 17:'연습문제 2', 18:'연습문제 3'})
    diagram = C('타원과 네 극의 위치',
                '<div class="transform-demo" hidden><label for="ellipse-direction">진행 방향 <select id="ellipse-direction"><option value="positive">반시계방향</option><option value="negative">시계방향</option></select></label>'
                '<canvas id="ellipse-plot" width="760" height="590" role="img" aria-label="가로 반지름 1, 세로 반지름 3인 타원. 위아래 두 극은 내부, 좌우 두 극은 외부입니다." aria-describedby="ellipse-caption"></canvas>'
                '<p id="ellipse-caption" aria-live="polite">반시계방향 · 내부 극 ±2i · 유수의 합 −1/8 · 적분값 −πi/4</p></div>'
                '<noscript>±2i는 타원 안, ±2는 타원 밖입니다. 반시계방향의 적분값은 −πi/4이고 시계방향은 +πi/4입니다.</noscript>')
    groups = [(2,'왜 역일차항만 남는가'), (4,'극의 차수와 유수 공식'), (6,'내부 극을 고르는 예제'),
              (9,'삼각함수 적분'), (11,'무한구간 적분'), (13,'푸리에 적분'), (14,'실수축의 극과 주값'),
              (16,'연습 1 · 지수함수'), (17,'연습 2 · 코탄젠트'), (18,'연습 3 · 부분분수')]
    toc = [('overview','개요'),('concept-map','개념 지도'),('concept-summary','핵심 개념 요약')]
    toc += [(f'slide-{n:02}', title) for n, title in groups]
    toc += [('exam-english','시험 영어'),('glossary','용어집'),('asr-log','원본 대조'),('sources','출처')]
    terms = [
        ('Residue(유수)', '로랑 전개에서 (z−a)⁻¹의 계수.'),
        ('Isolated singularity(고립특이점)', '해당 점을 뺀 작은 원판 전체에서 함수가 해석적인 특이점.'),
        ('Simple pole(단순극)', '주요부가 B/(z−a) 한 항이고 B≠0인 극.'),
        ('Essential singularity(본질적 특이점)', '고립특이점 주변 로랑 급수에 음수 차수가 무한히 많이 남는 경우.'),
        ('Positive orientation(양의 방향)', '단순폐곡선 내부를 왼편에 두고 도는 반시계방향.'),
        ('Upper half-plane(상반평면)', '복소수의 허수부가 양수인 영역.'),
        ('Improper integral(이상적분)', '무한구간 또는 특이점이 있는 구간에서 각각 필요한 극한을 취한 적분.'),
        ('Cauchy principal value(코시 주값)', '실수극의 양쪽을 같은 폭으로 제외하고 극한을 취해 정하는 값.'),
        ('Partial fraction decomposition(부분분수 분해)', '유리함수를 분모 인자별로 나누어 더한 꼴로 표현하는 계산.')]
    exam = [
        ('Which coefficient is the residue at a?', 'It is the coefficient of the inverse first power of z minus a in the Laurent expansion about a.', '극의 차수와 역일차항의 계수를 구분합니다.'),
        ('Which poles contribute to the ellipse integral?', 'Only the poles at plus and minus two i lie inside the ellipse. The two real poles lie outside.', '타원의 내부 부등식으로 각 극을 검사합니다.'),
        ('Why is a principal value used on slide 14?', 'There are simple poles on the real axis. The one-sided integrals diverge, but symmetric exclusions around each pole give a finite principal value.', '각 실수극 양쪽의 한쪽 극한과 대칭 제외 극한의 차이를 설명합니다.')]
    mit = 'https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/resources/'
    sources = C('원본 강의자료와 수학 참고문헌',
                '<p>Arshad Afzal, Residue Integration, Week 13, 18쪽. 한국어 본문과 중간 계산은 편집자 해설입니다. <a href="materials/Week 13.pdf">원본 PDF</a></p>',
                '<p>유수정리의 적용 범위와 실수축의 단순극을 우회하는 코시 주값 조건은 Jeremy Orloff의 MIT 18.04 강의노트와 대조했습니다. '
                f'<a href="{mit}mit18_04s18_topic8/">The residue theorem</a> · <a href="{mit}mit18_04s18_topic9/">Definite integrals using the residue theorem</a></p>')
    audit = C('원본 표기와 적용 조건', '<p><a href="#source-check-03">3쪽 사인 급수의 부호</a> · <a href="#source-check-13">13쪽 지수 감쇠 방향</a> · <a href="#source-check-14">14쪽 실수축의 극과 주값</a></p>',
              '8·12·15쪽은 원본의 빈 풀이란입니다. 앞 문제의 타원 그림, 네제곱근 계산, 주값의 실수 검산을 각각 보강했습니다.')
    guide = ('<div class="mode-guide"><strong id="mode-status">기본 모드 · 밝은 화면</strong><p>뉴비 모드는 경로를 그리는 법과 식을 고르는 이유부터 풉니다.</p><p>'
             '<a href="complex-integration-series.html">이전 단원 · 복소적분과 테일러·로랑 급수</a> · '+
             link(14,'코시 주값 예제')+' · '+link(16,'원본 연습문제 1–3')+
             '</p><noscript>기본·뉴비 본문을 함께 표시합니다.</noscript></div>')
    values = {
        'LECTURE_NUMBER':'Week 13','LECTURE_TITLE':'Residue integration','WEEK':'공업수학 II','PAGE_COUNT':'18',
        'ONE_SENTENCE_DESCRIPTION':'복소함수의 유수, 유수정리와 실수 적분, 코시 주값을 원본 18쪽과 예제·연습문제 풀이로 공부합니다.',
        'LECTURE_PROMISE':'로랑 급수에서 한 계수를 읽어 경로적분을 구합니다. 이어서 단위원과 반원 경로를 선택해 삼각함수 적분, 무한구간 적분, 코시 주값을 계산합니다.',
        'DATE_OR_날짜_미기재':'미기재','VIDEO_SET':'PDF 기반 해설','ALL_CONTENTS_AND_PROBLEM_SOLVING_BUTTONS':'',
        'ORIGINAL_PDF_URL':'materials/'+PDF,'LECTURE_NOTE_FILENAME':PDF,
        'CORE_RELATIONSHIP_HEADLINE':'한 바퀴를 적분하면 (z−a)⁻¹의 계수가 남습니다.',
        'CORE_RELATIONSHIP_EXPLANATION':'로랑 급수의 다른 정수 차수 항은 작은 원을 한 바퀴 돌 때 상쇄됩니다. 각 특이점 주변에서 남은 기여를 더하면 큰 경로의 적분값이 됩니다.',
        'CONCEPT_MAP_HEADLINE':'유수를 구하고, 경로 안의 점을 고르고, 실수 적분으로 돌아옵니다.',
        'CONCEPT_MAP_BLOCKS':'<div class="grid-2">'+C('2–8쪽 · 복소 경로적분','<p>'+link(2,'계수의 의미')+' → '+link(4,'극의 차수')+' → '+link(6,'유수 합')+' → '+link(8,'타원과 방향')+'</p>')+
                             C('9–18쪽 · 실수 적분과 연습','<p>'+link(9,'단위원 치환')+' → '+link(11,'반원 경로')+' → '+link(14,'코시 주값')+' → '+link(16,'원본 연습문제')+'</p>')+'</div>',
        'STANDALONE_CONCEPT_SUMMARY':summary(),'DISTINCT_SUMMARY_VIDEO_SECTION_IF_NEEDED':'',
        'EXAM_SECTION_TITLE':'유수와 적분 조건을 설명하는 영어 표현','BILINGUAL_GLOSSARY_TABLE':table(['English(한국어)','뜻과 사용'],terms),
        'AUDIT_SECTION_TITLE':'원본 대조와 풀이 보강','ASR_CORRECTION_TABLE':audit,'SOURCE_LIST_AND_PROVENANCE_NOTE':sources,
        'TABLE_OF_CONTENTS_LINKS':''.join(f'<li><a href="#{anchor}">{title}</a></li>' for anchor,title in toc)}
    render_lecture(SLUG, slides, roles, {8:diagram}, exam, values, guide,
                   '먼저 특이점과 경로의 위치를 표시하고, 적분값에 기여하는 계수를 고릅니다.', 'residue-ellipse.js')


if __name__ == '__main__':
    build()
