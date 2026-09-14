"""Shared source of truth for homepage and original PDF downloads."""
from html import escape

LECTURES = [
    dict(title='Fourier series(푸리에 급수)', pdf='Fourier series.pdf', page='fourier-series.html', slug='fourier', pages=48, problem='28', description='내적과 직교성에서 시작해 푸리에 급수, 함수 근사, Sturm–Liouville 문제와 일반화된 급수까지 상세 해설과 풀이로 연결합니다.'),
    dict(title='Fourier integrals & transforms(푸리에 적분과 변환)', pdf='Fourier Integrals and Transforms.pdf', page='fourier-integrals-transforms.html', slug='transforms', pages=36, problem='11', description='급수가 적분으로 바뀌는 이유, 복소 푸리에 변환의 성질, 합성곱, DFT·FFT와 소리·진동 분석을 상세 풀이와 함께 연결합니다.')
]

def lecture_cards():
    cards=[]
    for v in LECTURES:
        cards.append(f'''<article class="lecture-card"><div class="lecture-card__body"><span class="status-pill">작성 완료</span><p class="section-kicker" style="margin-top:22px">공업수학 II · 날짜 미기재</p><h2>{escape(v['title'])}</h2><p>{v['description']}</p><div class="meta-row"><span class="meta-chip">원본 슬라이드 {v['pages']}장</span><span class="meta-chip">PDF 기반 해설</span><span class="meta-chip">기본·뉴비 모드</span></div><div class="button-row"><a class="button button--primary" href="{v['page']}">정리노트 읽기</a><a class="button" href="{v['page']}#slide-{v['problem']}">문제 풀이</a><a class="button" href="materials/{v['pdf']}" download="{v['pdf']}" type="application/pdf">원본 PDF 다운로드</a></div></div><div class="lecture-card__image"><img src="assets/slides/{v['slug']}/slide-01.jpg" alt="{escape(v['title'])} 원본 첫 페이지 표지 슬라이드" width="1920" height="1080"></div></article>''')
    return ''.join(cards)

def download_cards(site):
    result=[]
    for v in LECTURES:
        size=(site/'materials'/v['pdf']).stat().st_size
        result.append(f'''<div class="card"><h2>{escape(v['pdf'])}</h2><p>Arshad Afzal · {v['pages']}쪽 · {size:,} bytes · 주차·날짜 미기재</p><div class="button-row"><a class="button button--primary" href="materials/{v['pdf']}" download="{v['pdf']}" type="application/pdf">원본 PDF 다운로드</a><a class="button" href="{v['page']}">정리노트 읽기</a></div></div>''')
    return '<div class="note-stack">'+''.join(result)+'</div>'
