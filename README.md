# MC2202 · Engineering Mathematics II

공업수학 II 강의자료를 바탕으로 작성한 한국어 학습 노트입니다.

- `site/fourier-series.html`: Fourier series 원본 48쪽과 개념 해설, 상세 문제 풀이.
- `site/fourier-integrals-transforms.html`: Fourier Integrals and Transforms 원본 36쪽, 연속·이산 변환 해설, 전체 연습문제 풀이와 조건 검토, 주파수 복원·DFT 비교 도구.
- `site/pde-i.html`: PDE I 원본 22쪽, 변수분리·D’Alembert 해법·PDE 분류와 특성곡선, 삼각형 줄 문제의 전체 풀이와 두 해법 비교 도구.
- 메인 목록은 원본 첫 페이지 썸네일과 정리노트·문제 풀이·PDF 다운로드를 각 자료에 제공합니다.
- 기본 모드: 동역학 노트의 밝은 화면과 연속 스크롤 형식.
- 뉴비 모드: 다크 화면과 독립적인 본문 해설. 고등학교 수학부터 개념의 필요성, 계산 선택 이유, 중간 과정, 최종 답까지 연결합니다. 핵심 영어 용어는 한국어와 함께 표기합니다.
- 수식은 정적 HTML과 MathML로 포함되어 JavaScript나 외부 수식 서버 없이 표시됩니다.
- 영상·스크립트가 없는 자료입니다. 해설과 보충 풀이는 편집자 작성이며 원본의 오류·조건 누락은 본문과 교정표에서 구분합니다.

## 로컬 열기

`site/index.html`을 브라우저에서 열거나 프로젝트 루트에서 `python -m http.server 8765 --directory site`를 실행하고 `http://localhost:8765`에 접속합니다.

## 제작 파일

- `scripts/note_content.py`: 슬라이드별 해설 원문.
- `scripts/build_site.py`: 동역학 템플릿을 바탕으로 페이지 생성.
- `scripts/transforms_*.py`, `scripts/build_transforms.py`: 두 번째 자료의 두 모드 해설·문제 풀이와 페이지 생성.
- `scripts/pde_*.py`, `scripts/build_pde.py`: PDE I의 두 모드 해설·문제 풀이와 페이지 생성.
- `scripts/prepare_pde.py`: PDE I의 4:3 원본을 왜곡 없이 1920×1080 틀 안에 배치하고 원본 PDF 보존.
- `scripts/lecture_catalog.py`: 강의 목록·PDF 다운로드 목록의 공통 자료 정보.
- `scripts/render_math.cjs`: KaTeX 0.16.22로 수식을 정적 HTML로 컴파일.
- `scripts/prepare_sources.py`: 원본 PDF의 1920×1080 이미지와 검토용 이미지 생성.
- `scripts/verify_math.py`: 독립적인 수치적분으로 주요 예제의 계수를 검산.
- `scripts/verify_transforms.py`: 새 자료의 적분·변환 성질·DFT·FFT·조건부 역적분을 독립적으로 검산.
- `scripts/verify_pde.py`: 삼각형 계수의 독립 수치적분, D’Alembert 해 대조, 초기·경계조건 및 PDE 잔차 검증.
- `NOTE_AUTHORING_GUIDE.md`: 다음 자료를 위한 집필·검증 기준.

출력 사이트는 별도 빌드 없이 `site/` 자체를 정적 호스팅할 수 있습니다. 빌더 재실행에는 Python의 pypdf·Pillow, 수학 검산에는 NumPy가 필요합니다. 수식 빌더에는 공식 npm 패키지 KaTeX 0.16.22를 `tmp/katex/package`에 준비합니다. 배포 파일의 KaTeX 글꼴·CSS는 자체 포함하며 라이선스는 `site/assets/vendor/katex/LICENSE`에 있습니다.

세 단원의 본문을 다시 만들고 검증하는 순서:

```text
python scripts/build_site.py
node scripts/render_math.cjs
node scripts/validate_site.cjs
python scripts/verify_math.py
python scripts/verify_transforms.py
python scripts/verify_pde.py
```

`prepare_sources.py`는 첫 자료용입니다. 새 PDF는 원본 파일명을 유지해 `site/materials/`에 보존하고, 각 자료별 이미지 폴더에 1920×1080 슬라이드를 만듭니다. 원본의 수식·부호 대조 기록은 `SOURCE_RECHECK.md`와 `TRANSFORMS_SOURCE_RECHECK.md`에 있습니다. MATLAB 예제는 같은 규약의 독립 DFT·NumPy 계산으로 교차 확인하며, MATLAB 실행 여부와 구분합니다.

PDE I의 원본 대조 내역과 수학 검산 범위는 `PDE_I_SOURCE_RECHECK.md`에 있습니다.

원본 자료: Arshad Afzal, **Fourier series.pdf**, 48쪽; **Fourier Integrals and Transforms.pdf**, 36쪽; **PDE - I.pdf**, 22쪽. 강의 날짜·주차는 미기재입니다. 원본의 권리는 원저작자에게 있습니다.

연결 대상 저장소: https://github.com/leejinh0225/MC2202-Engineering-Mathematics-2
