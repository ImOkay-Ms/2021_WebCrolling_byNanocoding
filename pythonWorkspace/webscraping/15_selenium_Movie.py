import requests
from selenium import webdriver
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36","Accept-Language":"ko-KR,ko " }
url = "https://play.google.com/store/movies/top"
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

movies = soup.find("div",attrs={"class":"ZmHEEd"})
# print(movies.get_text())

for movie in movies:
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)

# with open("movie.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())

#scroll을 모두 내린 후 제목을 출력한다?
#1 일단 다 내린다.

#내리는 코드
2