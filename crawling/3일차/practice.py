import requests
from bs4 import BeautifulSoup
import csv
import time

# **기본 과제: `https://news.ycombinator.com/` 데이터 저장**
# - 목표: 기사 제목과 링크를 CSV로 저장
# - `csv` 모듈 사용
# - 최소 10개 기사 데이터 저장
# - 요청 간 1초 대기 (`time.sleep(1)`)


# **도전 과제: 다른 웹사이트 시도**
# 정적 웹사이트(예: `https://www.example.com`)에서 `<a>` 태그 데이터 추출 후 CSV 저장
