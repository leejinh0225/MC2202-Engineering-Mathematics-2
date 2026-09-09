def render_home(shell, lecture_card):
    body = '''<section aria-labelledby="notes-title"><p class="section-kicker">Available notes</p><h2 class="section-title" id="notes-title">완성된 정리노트</h2><p class="section-lead">원본 첫 페이지로 자료를 확인하고, 정리노트 또는 원본 PDF를 바로 열 수 있습니다.</p>'''+lecture_card+'''</section>
<section class="home-reading" aria-labelledby="reading-title"><p class="section-kicker">Reading modes</p><h2 class="section-title" id="reading-title">익숙한 설명으로 읽고, 막히면 기초부터.</h2><p class="section-lead">상단의 뉴비 모드 버튼으로 전환합니다. 선택한 모드는 정리노트와 자료 목록에도 이어집니다.</p><div class="grid-2"><div class="card"><h3>기본 모드</h3><p>밝은 화면에서 핵심 개념, 공식의 유도, 단계별 문제 풀이를 이어 읽습니다. 원본 페이지와 해설을 함께 보며 흐름을 따라갈 수 있습니다.</p></div><div class="card"><h3>뉴비 모드</h3><p>다크 화면으로 전환하고 기호 읽기, 고등학교 수학, 계산 중간 단계를 추가합니다. English(한국어 번역) 용어 표기와 기본 해설은 그대로 유지합니다.</p></div></div></section>
<aside class="source-note"><strong>자료와 해설 안내</strong><p>강의 영상·스크립트 없이 원본 PDF를 바탕으로 작성했습니다. 보충 설명과 문제 풀이는 편집자 해설이며, 원본의 오류와 조건 누락은 각 노트의 교정 기록에서 구분합니다.</p></aside>'''
    page=shell('Engineering Mathematics II.',body)
    page=page.replace('<main class="landing-content">','<main id="main" class="home-main">')
    page=page.replace('<body>','<body><a class="skip-link" href="#main">본문으로 건너뛰기</a>')
    page=page.replace('<h1>Engineering Mathematics II.</h1>','<h1>공업수학 II를<br>기초부터 차근차근.</h1>')
    page=page.replace('원본 자료와 한국어 해설, 단계별 문제 풀이를 이어 읽는 학습 노트.','원본 강의자료의 순서에 맞춰 개념과 공식의 이유를 설명하고, 문제의 풀이 과정까지 연결한 한국어 학습 노트입니다. 수업 자료만으로 공부할 수 있도록 기본 해설과 뉴비 해설을 함께 제공합니다.')
    page=page.replace('</p></div></section><main','''</p><div class="meta-row" aria-label="자료 특징"><span class="meta-chip">원본 전 페이지 수록</span><span class="meta-chip">단계별 문제 풀이</span><span class="meta-chip">English(한국어) 용어 표기</span><span class="meta-chip">기본·뉴비 모드</span></div><div class="button-row"><a class="button button--primary" href="#notes-title">정리노트 선택하기</a><a class="button" href="downloads.html">원본 PDF 모아보기 · 1개</a></div></div></section><main''')
    return page
