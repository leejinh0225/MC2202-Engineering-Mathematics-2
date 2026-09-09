# MC2202 · Engineering Mathematics II

공업수학 II 강의자료를 바탕으로 작성한 한국어 학습 노트입니다.

- `site/fourier-series.html`: Fourier series 원본 48쪽과 개념 해설, 상세 문제 풀이.
- 기본 모드: 동역학 노트의 밝은 화면과 연속 스크롤 형식.
- 뉴비 모드: 다크 화면, 기호 읽기, 고등학교 수학부터 이어지는 부연 설명. 핵심 영어 용어는 한국어와 함께 표기합니다.
- 수식은 정적 HTML과 MathML로 포함되어 JavaScript나 외부 수식 서버 없이 표시됩니다.
- 영상·스크립트가 없는 자료입니다. 해설과 보충 풀이는 편집자 작성이며 원본의 오류·조건 누락은 본문과 교정표에서 구분합니다.

## 로컬 열기

`site/index.html`을 브라우저에서 열거나 프로젝트 루트에서 `python -m http.server 8765 --directory site`를 실행하고 `http://localhost:8765`에 접속합니다.

## 제작 파일

- `scripts/note_content.py`: 슬라이드별 해설 원문.
- `scripts/build_site.py`: 동역학 템플릿을 바탕으로 페이지 생성.
- `scripts/render_math.cjs`: KaTeX 0.16.22로 수식을 정적 HTML로 컴파일.
- `scripts/prepare_sources.py`: 원본 PDF의 1920×1080 이미지와 검토용 이미지 생성.
- `scripts/verify_math.py`: 독립적인 수치적분으로 주요 예제의 계수를 검산.
- `NOTE_AUTHORING_GUIDE.md`: 다음 자료를 위한 집필·검증 기준.

출력 사이트는 별도 빌드 없이 `site/` 자체를 정적 호스팅할 수 있습니다. 빌더 재실행에는 Python의 pypdf·Pillow, 수학 검산에는 NumPy가 필요합니다. 수식 빌더에는 공식 npm 패키지 KaTeX 0.16.22를 `tmp/katex/package`에 준비합니다. 배포 파일의 KaTeX 글꼴·CSS는 자체 포함하며 라이선스는 `site/assets/vendor/katex/LICENSE`에 있습니다.

원본 자료: Arshad Afzal, **Fourier series.pdf**, 48쪽. 강의 날짜·주차는 미기재입니다. 원본의 권리는 원저작자에게 있습니다.

연결 대상 저장소: https://github.com/leejinh0225/MC2202-Engineering-Mathematics-2
