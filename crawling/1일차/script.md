# 파이썬 웹 크롤링 초보자 연습 커리큘럼: 1일차

## 1일차: 웹 크롤링 기초와 환경 설정

### 학습 목표
- 웹 크롤링의 개념 이해
- 파이썬과 필수 라이브러리(`requests`, `beautifulsoup4`) 설치 및 기본 사용법 익히기

### 학습 내용
1. **웹 크롤링이란?**
   - 웹사이트에서 데이터를 자동으로 수집하는 프로세스
   - 예: 뉴스 제목, 상품 가격, 블로그 포스트 수집
2. **필요한 도구**
   - Python 3.x (최신 버전 권장, 예: 3.8 이상)
   - `requests`: 웹페이지 데이터를 가져오는 라이브러리
   - `beautifulsoup4`: HTML에서 데이터를 추출하는 라이브러리
3. **환경 설정**
   - Python 설치 확인
   - `pip`를 사용해 라이브러리 설치

---

## 실습 가이드

### 1단계: Python 설치 확인
1. Python이 설치되어 있는지 확인:
   ```bash
   python --version
   ```
   또는
   ```bash
   python3 --version
   ```
   - Python 3.x 버전이 출력되어야 함
   - 설치가 안 되어 있다면 [Python 공식 사이트](https://www.python.org/downloads/)에서 다운로드 및 설치
2. `pip` 설치 확인:
   ```bash
   pip --version
   ```
   - 문제가 있다면 Python 재설치 또는 `pip` 별도 설치 필요

### 2단계: 라이브러리 설치
1. 터미널에서 다음 명령어로 라이브러리 설치:
   ```bash
   pip install requests beautifulsoup4
   ```
2. 설치 확인:
   ```bash
   python -c "import requests, bs4"
   ```
   - 에러가 없으면 설치 성공

### 3단계: 간단한 웹페이지 요청 실습
`requests`를 사용해 실제 웹페이지를 요청해보기:
1. Python 에디터(예: VSCode, PyCharm) 또는 Python 대화형 모드(`python` 입력) 실행
2. 다음 코드를 작성하고 실행:
   ```python
   import requests
   response = requests.get("https://example.com")
   print(response.text)
   ```
   - **설명**:
     - `requests.get()`: 지정한 URL의 웹페이지 데이터를 가져옴
     - `response.text`: 웹페이지의 HTML 소스를 문자열로 출력
   - **예상 출력**: `https://example.com`의 HTML 코드, `<h1>Example Domain</h1>` 등 포함
3. 실행 결과에서 `<title>` 태그(예: `<title>Example Domain</title>`)가 포함되어 있는지 확인

---

## 실습 과제
1. 위 코드를 실행한 뒤, 출력된 HTML에서 `<title>` 태그의 내용을 눈으로 찾아보세요.
2. 다른 웹사이트로 요청해보기:
   - URL을 `https://www.python.org`로 변경해 실행
   - 코드:
     ```python
     import requests
     response = requests.get("https://www.python.org")
     print(response.text)
     ```
   - **주의**: 일부 웹사이트는 요청을 차단할 수 있음(403/404 에러 발생 시 다른 URL 시도)

---

## 추가 팁
- **에러 대처**:
  - `ModuleNotFoundError`: 라이브러리 설치 확인 또는 Python 환경 점검
  - `requests.exceptions.RequestException`: 네트워크 문제 또는 웹사이트 요청 차단, 다른 URL 시도
- **다음 단계 준비**:
  - 2주차에서는 HTML 구조와 `BeautifulSoup`으로 데이터 추출 학습 예정
  - 이번 주에는 `requests`로 HTML 가져오기에 익숙해지기
- **궁금한 점**: 코드 실행 문제나 특정 부분 이해 어려움이 있으면 질문!