# 파이썬 웹 크롤링 초보자 연습 커리큘럼: 3일차

## 3일차: 동적 웹사이트 크롤링과 데이터 저장

### 학습 목표

- 정적 웹사이트와 동적 웹사이트의 차이 이해
- 추출한 데이터를 CSV 파일로 저장하는 방법 학습
- 웹 크롤링 시 주의사항(요청 속도 제한, robots.txt) 익히기

### 학습 내용

1. **정적 vs 동적 웹사이트**
   - **정적 웹사이트**: HTML 소스에 모든 데이터가 포함되어 즉시 로드됨 (예: `https://example.com`)
   - **동적 웹사이트**: JavaScript로 데이터가 나중에 로드됨 (예: AJAX, React 기반 사이트)
   - 초보자용: 동적 웹사이트의 간단한 이해 및 `requests`로 크롤링 가능한 동적 데이터 소개
2. **CSV 저장**
   - `csv` 모듈: 기본적인 CSV 파일 작성
   - `pandas` (선택): 데이터프레임으로 데이터를 구조화해 저장
3. **주의사항**
   - **요청 속도 제한**: 과도한 요청으로 서버 부하 방지 (예: `time.sleep(1)`)
   - **robots.txt 확인**: 웹사이트의 크롤링 허용 여부 점검 (예: `https://news.ycombinator.com/robots.txt`)

---

## 실습 가이드: 단계별 학습

### 1단계: 정적 vs 동적 웹사이트 이해

1. **정적 웹사이트 확인**
   - 브라우저에서 `https://news.ycombinator.com/` 접속
   - 개발자 도구(F12 또는 오른쪽 클릭 → "검사")로 HTML 소스 확인
   - `<a class="titleline">` 태그가 HTML에 직접 포함되어 있는지 확인 (정적 데이터)
2. **동적 웹사이트 이해**
   - 동적 웹사이트 예: `https://www.reddit.com` (일부 데이터가 JavaScript로 로드)
   - 개발자 도구 → "Network" 탭 → "JS" 또는 "XHR" 필터로 JavaScript 요청 확인
   - **참고**: 동적 데이터는 `requests`만으로 추출 어려움, `Selenium` 필요 (4일차에서 소개)
3. **실습: robots.txt 확인**
   - 브라우저에서 `https://news.ycombinator.com/robots.txt` 접속
   - 크롤링 허용/제한 경로 확인 (예: `Disallow: /x?fnid=`)
   - **팁**: `robots.txt`를 준수해 허용된 페이지만 크롤링

### 2단계: 데이터 추출 및 CSV 저장

1. **환경 점검**
   - `requests`와 `beautifulsoup4` 설치 확인:
     ```bash
     python -c "import requests, bs4, csv"
     ```
   - 필요 시 설치:
     ```bash
     pip install requests beautifulsoup4
     ```
2. **기본 추출: `https://news.ycombinator.com/`**

   - 목표: 기사 제목과 링크 추출
   - 코드:

     ```python
     import requests
     from bs4 import BeautifulSoup

     response = requests.get("https://news.ycombinator.com/")
     soup = BeautifulSoup(response.text, "html.parser")
     titles = soup.select(".titleline > a")
     for title in titles[:5]:  # 상위 5개만 출력
         print("Title:", title.text)
         print("Link:", title["href"])
     ```

   - **설명**:
     - `.select(".titleline > a")`: CSS 선택자로 `<a>` 태그 선택
     - `title.text`: 기사 제목
     - `title["href"]`: 링크 URL
   - **예상 출력**:
     ```
     Title: Example News Title
     Link: https://example.com/news/123
     ...
     ```

3. **CSV 저장: `csv` 모듈 사용**

   - 추출한 데이터를 `news.csv` 파일로 저장:

     ```python
     import requests
     from bs4 import BeautifulSoup
     import csv
     import time

     response = requests.get("https://news.ycombinator.com/")
     soup = BeautifulSoup(response.text, "html.parser")
     titles = soup.select(".titleline > a")
     with open("news.csv", "w", newline="", encoding="utf-8") as f:
         writer = csv.writer(f)
         writer.writerow(["Title", "Link"])  # 헤더 작성
         for title in titles[:10]:  # 상위 10개 저장
             writer.writerow([title.text, title["href"]])
             time.sleep(1)  # 요청 간격 1초
     ```

   - **결과**: `news.csv` 파일이 생성되며, 열은 "Title"과 "Link"로 구성

4. **선택 실습: `pandas` 사용**

   - `pandas`로 동일 작업 수행:

     ```python
     import requests
     from bs4 import BeautifulSoup
     import pandas as pd
     import time

     response = requests.get("https://news.ycombinator.com/")
     soup = BeautifulSoup(response.text, "html.parser")
     titles = soup.select(".titleline > a")
     data = [{"Title": title.text, "Link": title["href"]} for title in titles[:10]]
     df = pd.DataFrame(data)
     df.to_csv("news_pandas.csv", index=False, encoding="utf-8")
     time.sleep(1)
     ```

   - **설명**: `pandas`로 데이터프레임 생성 후 CSV 저장, 설치 필요 시 `pip install pandas`

### 3단계: 실습 과제 수행

1. **기본 과제: `https://news.ycombinator.com/` 데이터 저장**
   - 목표: 기사 제목과 링크를 CSV로 저장
   - 위 2단계의 `csv` 모듈 코드 실행
   - **확인**: `news.csv` 파일 열어 데이터 확인
   - **요구사항**:
     - 최소 10개 기사 데이터 저장
     - 요청 간 1초 대기 (`time.sleep(1)`)
2. **도전 과제: 다른 웹사이트 시도**

   - 다른 정적 웹사이트(예: `https://www.example.com`)에서 `<a>` 태그 데이터 추출 후 CSV 저장
   - 코드 예시:

     ```python
     import requests
     from bs4 import BeautifulSoup
     import csv
     import time

     response = requests.get("https://example.com")
     soup = BeautifulSoup(response.text, "html.parser")
     links = soup.find_all("a")
     with open("example_links.csv", "w", newline="", encoding="utf-8") as f:
         writer = csv.writer(f)
         writer.writerow(["Text", "Link"])
         for link in links:
             text = link.text.strip()
             href = link.get("href", "No link")
             if text:  # 텍스트가 있는 경우만 저장
                 writer.writerow([text, href])
             time.sleep(1)
     ```

   - **주의**:
     - `link.get("href")` 사용: `href` 속성이 없는 태그 처리
     - 동적 웹사이트는 데이터가 안 나올 수 있음

---

## 추가 팁

- **에러 대처**:
  - `AttributeError: 'NoneType' object has no attribute 'text'`: `select()` 또는 `find_all()` 결과 확인
  - `requests.exceptions.HTTPError`: HTTP 403/429 에러 시 `headers` 추가:
    ```python
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    ```
  - `UnicodeEncodeError`: CSV 저장 시 `encoding="utf-8"` 확인
- **robots.txt 점검**:
  - 크롤링 전 `https://<사이트>/robots.txt` 확인
  - 예: `User-agent: * Disallow: /search` → 검색 페이지는 크롤링 금지
- **요청 속도 제한**:
  - `time.sleep(1)`로 서버 부하 방지
  - 과도한 요청 시 IP 차단 가능성 주의
- **다음 단계 준비**:
  - 4일차에서는 실전 프로젝트와 윤리적 크롤링 학습
  - 이번 주에는 CSV 저장과 요청 간격 조절에 익숙해지기
