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
