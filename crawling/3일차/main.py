import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time

# 1단계 : 정적 웹사이트와 동적 웹사이트 이해

# **정적 웹사이트 확인**
# 브라우저에서 `https://news.ycombinator.com/` 접속

# html 태그 추출
"""
<a href="user?id=todsacerdoti" class="hnuser">todsacerdoti</a>
"""

# **동적 웹사이트 이해**
# 브라우저에서 `https://www.reddit.com` 접속

"""
<a href="user?id=todsacerdoti" class="user">todsacerdoti</a>
"""

# **실습: robots.txt 확인**

# 브라우저에서 `https://news.ycombinator.com/robots.txt` 접속

# 크롤링 허용/제한 경로 확인 (예: `Disallow: /x?fnid=`)

"""
Disallow: /x?fnid=
"""

# **주의사항**

# 요청 속도 제한

# robots.txt를 준수해 허용된 페이지만 크롤링

# 2단계 : 데이터 추출 및 CSV 저장

# response = requests.get("https://news.ycombinator.com/")
# soup = BeautifulSoup(response.text, "html.parser")
# titles = soup.select(".titleline > a")
# for title in titles[:5]:
#     print("Title:", title.text)
#     print("Link:", title["href"])

"""
# 출력내용
Title: Why Algebraic Effects?
Link: https://antelang.org/blog/why_effects/
Title: Postgres IDE in VS Code
Link: https://techcommunity.microsoft.com/blog/adforpostgresql/announcing-a-new-ide-for-postgresql-in-vs-code-from-microsoft/4414648
Title: How to Make a Living as a Writer
Link: https://thewalrus.ca/how-to-make-a-living-as-a-writer/
Title: Mermaid: Generation of diagrams like flowcharts or sequence diagrams from text
Link: https://github.com/mermaid-js/mermaid
Title: Find Your People
Link: https://foundersatwork.posthaven.com/find-your-people
"""

# csv 저장
# with open("news.csv", "w", newline="", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Title", "Link"])  # 헤더 작성
#     for title in titles[:10]:  # 상위 10개 저장
#         writer.writerow([title.text, title["href"]])
#         time.sleep(1)  # 요청 간격 1초

"""
# 출력내용
Title,Link
Why Algebraic Effects?,https://antelang.org/blog/why_effects/
Postgres IDE in VS Code,https://techcommunity.microsoft.com/blog/adforpostgresql/announcing-a-new-ide-for-postgresql-in-vs-code-from-microsoft/4414648
How to Make a Living as a Writer,https://thewalrus.ca/how-to-make-a-living-as-a-writer/
Mermaid: Generation of diagrams like flowcharts or sequence diagrams from text,https://github.com/mermaid-js/mermaid
Find Your People,https://foundersatwork.posthaven.com/find-your-people
Modification of acetaminophen to reduce liver toxicity and enhance drug efficacy,https://www.societyforscience.org/regeneron-sts/2025-student-finalists/chloe-lee/
Show HN: Genetic Boids Web Simulation,https://attentionmech.github.io/genetic-boids/
Show HN: HNRelevant – Add a "related" section to Hacker News,https://github.com/imdj/HNRelevant
Root for your friends,https://josephthacker.com/personal/2025/05/13/root-for-your-friends.html
The world of Japan's PC-98 computer,https://strangecomforts.com/the-strange-world-of-japans-pc-98-computer/
"""

# pandas 사용

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.select(".titleline > a")
data = [{"Title": title.text, "Link": title["href"]} for title in titles[:10]]
df = pd.DataFrame(data)
df.to_csv("news_pandas.csv", index=False, encoding="utf-8")
time.sleep(1)

"""
# 출력내용
Title,Link
Why Algebraic Effects?,https://antelang.org/blog/why_effects/
Postgres IDE in VS Code,https://techcommunity.microsoft.com/blog/adforpostgresql/announcing-a-new-ide-for-postgresql-in-vs-code-from-microsoft/4414648
How to Make a Living as a Writer,https://thewalrus.ca/how-to-make-a-living-as-a-writer/
Mermaid: Generation of diagrams like flowcharts or sequence diagrams from text,https://github.com/mermaid-js/mermaid
Find Your People,https://foundersatwork.posthaven.com/find-your-people
Modification of acetaminophen to reduce liver toxicity and enhance drug efficacy,https://www.societyforscience.org/regeneron-sts/2025-student-finalists/chloe-lee/
Show HN: Genetic Boids Web Simulation,https://attentionmech.github.io/genetic-boids/
"Show HN: HNRelevant – Add a ""related"" section to Hacker News",https://github.com/imdj/HNRelevant
Root for your friends,https://josephthacker.com/personal/2025/05/13/root-for-your-friends.html
The world of Japan's PC-98 computer,https://strangecomforts.com/the-strange-world-of-japans-pc-98-computer/
"""