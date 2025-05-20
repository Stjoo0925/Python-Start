# 파이썬 웹 크롤링 초보자 연습 커리큘럼

이 커리큘럼은 파이썬을 사용한 웹 크롤링을 처음 배우는 사람들을 위해 설계되었습니다. 각 단계는 이론과 실습으로 구성되며, 약 4주 동안 주 2~3시간 학습을 기준으로 진행됩니다.

## 1일차: 웹 크롤링 기초와 환경 설정

### 학습 목표
- 웹 크롤링의 개념 이해
- 필요한 파이썬 라이브러리 설치 및 기본 사용법 익히기

### 학습 내용
- **웹 크롤링이란?**: 웹사이트에서 데이터를 자동으로 수집하는 과정
- **필요한 도구**:
  - Python 3.x
  - `requests`: HTTP 요청을 보내 웹페이지 데이터를 가져오는 라이브러리
  - `BeautifulSoup`: HTML을 파싱하여 원하는 데이터를 추출하는 라이브러리
- **환경 설정**:
  - Python 설치 확인
  - `pip install requests beautifulsoup4` 명령어로 라이브러리 설치

### 실습 과제
1. Python과 pip가 제대로 설치되었는지 확인하세요.
2. `requests`와 `beautifulsoup4`를 설치하고, 다음 코드를 실행해 간단한 웹페이지를 요청해본다:
   ```python
   import requests
   response = requests.get("https://example.com")
   print(response.text)
   ```

## 2일차: HTML 구조 이해와 데이터 추출

### 학습 목표
- HTML 기본 구조와 태그 이해
- BeautifulSoup을 사용한 데이터 추출

### 학습 내용
- **HTML 기초**:
  - `<div>`, `<p>`, `<a>`, `<h1>` 등의 기본 태그
  - 클래스(`class`)와 아이디(`id`) 속성
- **BeautifulSoup 사용법**:
  - `find()`, `find_all()` 메서드로 특정 태그 찾기
  - CSS 선택자를 이용한 데이터 추출 (`select()`)

### 실습 과제
1. 다음 웹사이트에서 제목(`<h1>`)과 모든 링크(`<a>`)의 텍스트를 추출해보세요:
   - 대상: `https://example.com`
   - 코드 예시:
     ```python
     from bs4 import BeautifulSoup
     import requests
     response = requests.get("https://example.com")
     soup = BeautifulSoup(response.text, "html.parser")
     title = soup.find("h1").text
     links = [link.text for link in soup.find_all("a")]
     print("Title:", title)
     print("Links:", links)
     ```

## 3일차: 동적 웹사이트 크롤링과 데이터 저장

### 학습 목표
- 동적 웹사이트와 정적 웹사이트의 차이 이해
- 간단한 데이터 저장 (CSV 파일로 저장)

### 학습 내용
- **정적 vs 동적 웹사이트**:
  - 정적: HTML로 바로 데이터가 로드됨
  - 동적: JavaScript로 데이터가 나중에 로드됨 (간단한 동적 크롤링 소개)
- **CSV 저장**:
  - `pandas` 또는 `csv` 모듈로 데이터를 파일에 저장
- **주의사항**:
  - 요청 속도 제한 (예: `time.sleep(1)`)
  - 웹사이트의 robots.txt 확인

### 실습 과제
1. 간단한 뉴스 웹사이트(예: `https://news.ycombinator.com/`)에서 기사 제목과 링크를 추출한 뒤 CSV 파일로 저장하세요.
   - 코드 예시:
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
         writer.writerow(["Title", "Link"])
         for title in titles:
             writer.writerow([title.text, title["href"]])
             time.sleep(1)  # 요청 간격 조절
     ```

## 4일차: 실전 프로젝트와 윤리적 크롤링

### 학습 목표
- 실제 웹사이트에서 데이터를 수집하는 프로젝트 수행
- 웹 크롤링 시 윤리적 고려사항 학습

### 학습 내용
- **실전 프로젝트 아이디어**:
  - 온라인 쇼핑몰에서 상품 이름과 가격 수집
  - 특정 주제의 블로그 포스트 제목과 날짜 수집
- **윤리적 크롤링**:
  - 웹사이트 이용약관 확인
  - 과도한 요청으로 서버 부하 방지
  - 개인정보 수집 금지
- **에러 처리**:
  - `try-except`로 요청 실패 처리
  - HTTP 상태 코드 확인 (예: 403, 404)

### 실습 과제
1. 사용자가 선택한 웹사이트(예: 오픈 마켓 사이트)에서 상품 이름과 가격을 수집해 CSV로 저장하는 코드를 작성하세요.
2. 다음 요구사항을 포함:
   - 최소 10개 상품 데이터 수집
   - 요청 간 1초 대기
   - 에러 처리 로직 추가
   - 예시 코드:
     ```python
     import requests
     from bs4 import BeautifulSoup
     import csv
     import time

     url = "https://example.com/products"
     headers = {"User-Agent": "Mozilla/5.0"}
     try:
         response = requests.get(url, headers=headers)
         response.raise_for_status()
         soup = BeautifulSoup(response.text, "html.parser")
         products = soup.select(".product")
         with open("products.csv", "w", newline="", encoding="utf-8") as f:
             writer = csv.writer(f)
             writer.writerow(["Name", "Price"])
             for product in products[:10]:
                 name = product.select_one(".product-name").text
                 price = product.select_one(".product-price").text
                 writer.writerow([name, price])
                 time.sleep(1)
     except requests.exceptions.RequestException as e:
         print("Error:", e)
     ```

## 추가 학습 자료
- **공식 문서**:
  - [Requests](https://docs.python-requests.org/)
  - [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- **추천 튜토리얼**:
  - YouTube: "Python Web Scraping Tutorial" 검색
  - 온라인 강의 플랫폼 (예: Udemy, Coursera)
- **고급 주제** (선택 학습):
  - `Selenium`으로 동적 웹사이트 크롤링
  - `Scrapy` 프레임워크 사용

## 학습 팁
- 매주 실습 코드를 직접 작성하고 실행해보며 에러를 디버깅하세요.
- 작은 프로젝트부터 시작해 점차 복잡도를 높이세요.
- 웹사이트 구조가 자주 바뀔 수 있으니, 크롤링 코드가 작동하지 않을 경우 HTML 구조를 다시 확인하세요.