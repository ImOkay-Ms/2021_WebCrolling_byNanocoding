#태블릿이나 스마트폰이 아는 크롤링 프로그램이 접근할 경우
#서버에서 차단할 경우가 있음(requests로 접근 시)
#이를 user agent로 해결가능

import requests
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
res = requests.get("http://nadocoding.tistory.com",headers=headers)
res.raise_for_status()

print("응답코드 : ", res.status_code) 

with open("nadocoding.html","w",encoding="utf8") as f:
    f.write(res.text)





