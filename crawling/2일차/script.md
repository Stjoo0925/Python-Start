# 파이썬 웹 크롤링 초보자 연습 커리큘럼: 2일차

## 2일차: HTML 구조 이해와 데이터 추출

### 학습 목표
- HTML의 기본 구조와 주요 태그 이해
- `BeautifulSoup`을 사용해 웹페이지에서 원하는 데이터 추출

### 학습 내용
1. **HTML 기초**
   - 주요 태그: `<div>`, `<p>`, `<a>`, `<h1>` 등
   - 속성: `class`와 `id`를 사용한 태그 식별
   - HTML 계층 구조: 부모, 자식, 형제 태그
2. **BeautifulSoup 사용법**
   - `find()`: 첫 번째 일치하는 태그 반환
   - `find_all()`: 일치하는 모든 태그 리스트 반환
   - `select()`: CSS 선택자를 사용한 유연한 데이터 추출

---

## 실습 가이드: 단계별 학습

### 1단계: HTML 구조 이해
1. **HTML 기본 구조 학습**
   - HTML 문서는 트리 구조로 구성됨
   - 예시 HTML:
     ```html
     <html>
       <body>
         <h1>Example Domain</h1>
         <p>This is a <a href="https://example.com">link</a>.</p>
       </body>
     </html>
     ```
   - 주요 태그:
     - `<h1>`: 제목 (헤딩)
     - `<p>`: 문단
     - `<a>`: 하이퍼링크 (`href` 속성으로 링크 URL 지정)
     - `<div>`: 콘텐츠 블록
   - 속성:
     - `class`: 태그의 스타일 또는 그룹 식별
     - `id`: 태그의 고유 식별자
2. **실습: HTML 구조 확인**
   - 브라우저에서 `https://example.com`에 접속
   - 마우스 오른쪽 버튼 → "검사" 또는 "개발자 도구" 클릭
   - HTML 소스에서 `<h1>`, `<a>`, `<p>` 태그를 찾아보세요

### 2단계: BeautifulSoup으로 데이터 추출
1. **환경 점검**
   - 1일차에서 설치한 `requests`와 `beautifulsoup4`가 준비되어 있는지 확인:
     ```bash
     python -c "import requests, bs4"
     ```
2. **기본 추출 실습: `find()` 사용**
   - 다음 코드를 작성해 `<h1>` 태그 추출:
     ```python
     import requests
     from bs4 import BeautifulSoup

     response = requests.get("https://example.com")
     soup = BeautifulSoup(response.text, "html.parser")
     title = soup.find("h1").text
     print("Title:", title)
     ```
   - **예상 출력**: `Title: Example Domain`
3. **여러 태그 추출: `find_all()` 사용**
   - `<a>` 태그의 텍스트를 모두 추출:
     ```python
     links = [link.text for link in soup.find_all("a")]
     print("Links:", links)
     ```
   - **예상 출력**: `Links: ['More information...']`
4. **CSS 선택자: `select()` 사용**
   - `<a>` 태그를 CSS 선택자로 추출:
     ```python
     links = [link.text for link in soup.select("a")]
     print("Links (via select):", links)
     ```
   - **설명**: `select()`는 CSS 선택자 문법을 사용해 더 유연하게 태그를 선택

### 3단계: 실습 과제 수행
1. **과제: `https://example.com` 데이터 추출**
   - 목표: `<h1>` 태그의 제목과 모든 `<a>` 태그의 텍스트 추출
   - 코드:
     ```python
     import requests
     from bs4 import BeautifulSoup

     response = requests.get("https://example.com")
     soup = BeautifulSoup(response.text, "html.parser")
     title = soup.find("h1").text
     links = [link.text for link in soup.find_all("a")]
     print("Title:", title)
     print("Links:", links)
     ```
   - **예상 출력**:
     ```
     Title: Example Domain
     Links: ['More information...']
     ```
2. **도전 과제: 다른 웹사이트 시도**
   - `https://www.python.org`에서 `<h1>` 태그와 `<a>` 태그의 텍스트를 추출
   - 코드 수정:
     ```python
     import requests
     from bs4 import BeautifulSoup

     response = requests.get("https://www.python.org")
     soup = BeautifulSoup(response.text, "html.parser")
     title = soup.find("h1").text.strip()  # 공백 제거
     links = [link.text.strip() for link in soup.find_all("a") if link.text.strip()]
     print("Title:", title)
     print("Links:", links)
     ```
   - **주의**:
     - `<h1>` 태그가 없을 경우 `AttributeError` 발생 가능. 이 경우 `soup.find("h1")`이 `None`인지 확인:
       ```python
       title = soup.find("h1")
       print("Title:", title.text.strip() if title else "No h1 tag found")
       ```
     - `<a>` 태그의 텍스트가 비어 있을 수 있으므로 `if link.text.strip()`로 필터링

---

## 추가 팁
- **에러 대처**:
  - `AttributeError: 'NoneType' object has no attribute 'text'`: `find()`가 태그를 찾지 못함. HTML 구조를 개발자 도구로 확인
  - `requests.exceptions.RequestException`: 네트워크 문제 또는 요청 차단. 다른 URL 시도
- **HTML 구조 확인 방법**:
  - 브라우저 개발자 도구(F12 또는 오른쪽 클릭 → "검사")로 태그와 속성 확인
  - `print(soup.prettify())`로 파싱된 HTML 구조 출력 가능
- **BeautifulSoup 팁**:
  - `find()` vs `find_all()`: 단일 태그 vs 모든 태그
  - `select()`는 `class`나 `id`를 활용할 때 유용 (예: `.class-name`, `#id-name`)
- **다음 단계 준비**:
  - 3일차에서는 동적 웹