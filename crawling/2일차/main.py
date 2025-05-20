import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com")

# print(response.text)

"""
<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
"""

# <h1> : Example Domain
# <p> : This domain is for use in illustrative examples in documents. You may use this
# domain in literature without prior coordination or asking for permission.
# <p> : a href="https://www.iana.org/domains/example">More information...</a>

# find() : 태그를 찾는 함수
soup = BeautifulSoup(response.text, "html.parser")
title = soup.find("h1").text
# print("Title:", title)

"""
Title: Example Domain
"""

# find_all() : 태그를 찾는 함수
links = [link.text for link in soup.find_all("a")]
# print("Links:", links)

"""
Links: ['More information...']
"""

# select() : CSS 선택자를 사용한 태그를 찾는 함수
links = [link.text for link in soup.select("a")]
print("Links (via select):", links)

"""
Links (via select): ['More information...']
"""

# BeautifulSoup 함수 정리

# find() : 태그를 찾는 함수
# find_all() : 태그를 찾는 함수
# select() : CSS 선택자를 사용한 태그를 찾는 함수