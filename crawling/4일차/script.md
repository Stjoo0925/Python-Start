# 4일차: 실전 프로젝트와 윤리적 크롤링

## 학습 목표

- **실전 웹 크롤링 프로젝트 수행**: 실제 웹사이트에서 데이터를 수집하고 처리하는 실습을 통해 크롤링 기술을 익힙니다.
- **윤리적 크롤링 원칙 이해**: 웹 크롤링 시 법적, 윤리적 책임을 학습하고, 이를 프로젝트에 적용합니다.
- **에러 처리 및 안정성 강화**: 크롤링 코드에 에러 처리 로직을 추가하여 안정적인 데이터 수집을 보장합니다.

## 학습 내용

### 1. 실전 프로젝트 아이디어

웹 크롤링의 실전 적용을 위해 다음과 같은 프로젝트를 수행할 수 있습니다:

- **온라인 쇼핑몰 데이터 수집**:
  - 목표: 오픈 마켓(예: 쿠팡, 아마존)에서 상품 이름, 가격, 할인 정보 수집.
  - 활용 예: 가격 비교 분석, 시장 트렌드 조사.
- **블로그 데이터 수집**:
  - 목표: 특정 주제(예: 기술, 여행)의 블로그 포스트 제목, 게시 날짜, 요약 텍스트 수집.
  - 활용 예: 콘텐츠 트렌드 분석, 키워드 연구.
- **뉴스 기사 수집**:
  - 목표: 특정 키워드(예: "AI") 관련 뉴스 기사의 제목과 발행일 수집.
  - 활용 예: 뉴스 모니터링, 감정 분석.

#### 추가 팁

- **선택 기준**: 크롤링 대상 웹사이트는 구조가 명확하고, 크롤링이 허용된 사이트를 선택하세요(예: robots.txt 확인).
- **데이터 활용**: 수집한 데이터를 CSV, JSON 등으로 저장하여 데이터 분석에 활용 가능.

### 2. 윤리적 크롤링

윤리적 크롤링은 법적 문제와 서버 부하를 방지하며, 데이터 수집의 책임을 다하는 과정입니다. 주요 원칙은 다음과 같습니다:

- **웹사이트 이용약관 확인**:
  - 웹사이트의 `robots.txt` 파일을 확인하여 크롤링 허용 여부와 제한된 경로를 파악합니다(예: `https://example.com/robots.txt`).
  - 이용약관(Terms of Service)에서 크롤링 관련 조항을 확인합니다.
- **서버 부하 최소화**:
  - 요청 간 대기 시간(예: 1~3초)을 설정하여 서버에 과부하를 주지 않습니다.
  - `time.sleep()`을 활용하거나, 비동기 요청을 최소화합니다.
- **개인정보 보호**:
  - 이름, 이메일, 주소 등 개인 식별 정보는 수집하지 않습니다.
  - GDPR(유럽 일반 데이터 보호 규정) 및 지역 데이터 보호법 준수.
- **User-Agent 설정**:
  - 크롤러임을 명확히 식별할 수 있는 User-Agent를 설정하여 투명성을 유지합니다.
  - 예: `{"User-Agent": "MyWebCrawler/1.0 (contact: myemail@example.com)"}`.

#### 윤리적 크롤링 체크리스트

1. `robots.txt` 확인 후 허용된 경로만 크롤링.
2. 요청 빈도를 제한(초당 1~2 요청 이하).
3. 개인정보 및 민감 데이터 제외.
4. 크롤링 목적을 명확히 하고, 상업적 이용 시 웹사이트 소유자와 협의.

### 3. 에러 처리

안정적인 크롤링을 위해 다양한 에러를 처리하는 로직을 포함해야 합니다:

- **HTTP 상태 코드**:
  - `200`: 요청 성공.
  - `403`: 접근 금지(크롤링 차단 가능성).
  - `404`: 페이지 없음.
  - `429`: 요청 과다(대기 시간 증가 필요).
  - `requests.exceptions.RequestException`으로 상태 코드 확인.
- **try-except 활용**:
  - 네트워크 오류, 타임아웃, 잘못된 HTML 구조 등 예외 처리.
  - 예: `ConnectionError`, `Timeout`, `HTTPError`.
- **데이터 검증**:
  - 수집된 데이터가 누락되었거나 형식이 잘못된 경우 처리(예: `NoneType` 체크).
- **로깅**:
  - 에러 발생 시 로그 파일에 기록하여 디버깅 용이성 확보.

#### 에러 처리 예시

```python
import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout

try:
    response = requests.get("https://example.com", timeout=5)
    response.raise_for_status()  # HTTP 상태 코드 확인
except HTTPError as e:
    print(f"HTTP 오류 발생: {e}")
except ConnectionError:
    print("네트워크 연결 오류 발생")
except Timeout:
    print("요청 시간 초과")
except Exception as e:
    print(f"알 수 없는 오류: {e}")
```

### 4. 실습 과제

#### 요구사항

1. **대상**: 사용자가 선택한 오픈 마켓 웹사이트(예: 쿠팡, 아마존)에서 상품 이름과 가격 수집.
2. **데이터**: 최소 10개 상품 데이터를 CSV 파일로 저장.
3. **대기 시간**: 요청 간 1초 대기.
4. **에러 처리**: HTTP 오류, 네트워크 오류, 데이터 누락 처리.
5. **추가 요구사항**:
   - CSV 파일에 헤더 포함(Name, Price).
   - 데이터 정제: 가격에서 통화 기호 제거, 공백 제거.

#### 상세 예시 코드

아래는 가상의 오픈 마켓 사이트에서 상품 데이터를 수집하는 코드입니다. 실제 사이트에서는 CSS 선택자(`.product`, `.product-name`, `.product-price`)를 웹사이트 구조에 맞게 수정해야 합니다.

```python
import requests
from bs4 import BeautifulSoup
import csv
import time
import logging

# 로깅 설정
logging.basicConfig(filename="crawler.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# 크롤링 설정
url = "https://example.com/products"
headers = {
    "User-Agent": "MyWebCrawler/1.0 (contact: myemail@example.com)",
    "Accept-Language": "en-US,en;q=0.9"
}

# CSV 파일 초기화
csv_file = "products.csv"
data = []

try:
    # HTTP 요청
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # 상태 코드 확인

    # HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.select(".product")  # 상품 리스트 선택

    if not products:
        logging.warning("상품 요소를 찾을 수 없습니다.")
        raise ValueError("상품 요소를 찾을 수 없습니다.")

    # 최소 10개 상품 데이터 수집
    for product in products[:10]:
        try:
            name = product.select_one(".product-name")
            price = product.select_one(".product-price")

            # 데이터 검증
            if not name or not price:
                logging.warning(f"상품 데이터 누락: {product}")
                continue

            name_text = name.text.strip()
            price_text = price.text.strip().replace("$", "").replace(",", "")  # 통화 기호 및 쉼표 제거

            data.append([name_text, price_text])
            logging.info(f"수집된 상품: {name_text}, {price_text}")
            time.sleep(1)  # 1초 대기

        except AttributeError as e:
            logging.error(f"데이터 파싱 오류: {e}")
            continue

    # CSV 저장
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Price"])  # 헤더
        writer.writerows(data)  # 데이터 작성

    logging.info(f"데이터를 {csv_file}에 성공적으로 저장했습니다.")

except requests.exceptions.HTTPError as e:
    logging.error(f"HTTP 오류: {e}")
    print(f"HTTP 오류 발생: {e}")
except requests.exceptions.ConnectionError:
    logging.error("네트워크 연결 오류")
    print("네트워크 연결 오류 발생")
except requests.exceptions.Timeout:
    logging.error("요청 시간 초과")
    print("요청 시간 초과")
except Exception as e:
    logging.error(f"알 수 없는 오류: {e}")
    print(f"알 수 없는 오류: {e}")
```

#### 코드 설명

- **로깅**: `logging` 모듈로 크롤링 과정과 에러를 기록하여 디버깅 용이성 확보.
- **헤더**: User-Agent와 Accept-Language로 크롤러 식별 및 언어 설정.
- **데이터 정제**: 가격에서 통화 기호(`$`)와 쉼표(`,`) 제거.
- **에러 처리**: HTTP 오류, 네트워크 오류, 데이터 누락 등을 개별적으로 처리.
- **대기 시간**: `time.sleep(1)`로 서버 부하 방지.
- **CSV 저장**: UTF-8 인코딩으로 유니코드 문자 호환성 확보.

#### 실제 적용 시 주의사항

- **CSS 선택자 수정**: 대상 웹사이트의 HTML 구조를 분석(예: Chrome 개발자 도구)하여 `.product`, `.product-name`, `.product-price`를 적절히 변경.
- **robots.txt 확인**: 크롤링 허용 여부를 사전에 확인.
- **테스트**: 소규모 데이터(1~2개)로 먼저 테스트 후 전체 크롤링 수행.

## 추가 학습 자료

- **robots.txt 분석**:
  - 도구: `robotparser` 모듈.
  - 예: `urllib.robotparser.RobotFileParser`로 허용/비허용 경로 확인.
- **비동기 크롤링**:
  - `aiohttp`와 `asyncio`를 활용하여 효율적인 크롤링 가능.
  - 단, 서버 부하를 고려하여 제한적으로 사용.
- **Selenium 사용**:
  - JavaScript로 동적 로딩되는 페이지 크롤링 시 유용.
  - 예: `selenium.webdriver`로 브라우저 자동화.
- **추천 자료**:
  - [Scrapy 공식 문서](https://docs.scrapy.org/): 대규모 크롤링 프레임워크.
  - [BeautifulSoup 공식 문서](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): HTML 파싱 가이드.
  - [Requests 공식 문서](https://docs.python-requests.org/): HTTP 요청 상세 설명.
