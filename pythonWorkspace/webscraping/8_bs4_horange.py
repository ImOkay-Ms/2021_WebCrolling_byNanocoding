import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=650305&weekday=sat"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
cartoons = soup.find_all("td",attrs={"class":"title"})
title = cartoons[1].a.get_text()
link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com"+link)

# #제목과 링크출력
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title,link)


#평점 정보출력
total_rates = 0
count = 0
cartoons = soup.find_all("div",attrs={"class":"rating_type"})

for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
    count+=1
print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates/len(cartoons))
print("웹툰개수 : ", count)

# 이렇게 하나 코드를 치는건 너무 불편할수도 있음!(compile 방식)
# inteprting 방식은 한줄씩 실행 가능 -> 터미널에 바로바로 치면 됌
