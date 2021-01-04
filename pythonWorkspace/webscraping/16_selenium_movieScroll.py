
#chorme 창을 띄우지 않고 실행시키고 싶을 때의 코드

#scroll을 모두 내린 후 제목을 출력한다?
#1 일단 다 내린다.

#내리는 코드
from selenium import webdriver
import time
import csv 

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)

#모니터(해상도) 높이인 1080만큼 스크롤 내리기
browser.execute_script("window.scrollTo(0,1080)")
#화면 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

#for문을 이용하여 화면 맽 밑으로 스크롤 내리기
interval = 2

#현재 문서 높이를 가져와서 측정
prev_height = browser.execute_script("return document.body.scrollHeight")

while(1):
    #스크롤을 내린다
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #잠시 기다린다
    time.sleep(interval)
    #현재 웹사이트의 길이측정
    current_height = browser.execute_script("return document.body.scrollHeight")
    #현재 문서의 길이와 스크롤 내리기전 길이가 같으면 반복문 탈출
    if current_height==prev_height:
        break
    else:
        prev_height = current_height
    

#이제 영화 정보 출력

import requests
from bs4 import BeautifulSoup

#이부분은 위의 browser.get()이 대체한다
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36","Accept-Language":"ko-KR,ko " }
# url = "https://play.google.com/store/movies/top"
# res = requests.get(url,headers=headers)
# res.raise_for_status()

soup = BeautifulSoup(browser.page_source,"lxml")

movies = soup.find("div",attrs={"class":"ZmHEEd"})
# print(movies.get_text())
print(len(movies))

idx_row = ["idx","영화제목","가격","할인된 가격","링크"]
file_name = "Google_moive_ranking.csv"
f = open(file_name,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)
writer.writerow(idx_row)


for idx, movie in enumerate(movies):
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    price = movie.find("span",attrs={"class":"SUZt4c djCuy"})

    if price:
        price = price.get_text()
    else:
        price = "할인하지 않는 영화입니다."
    
    Sale_price = movie.find("span",attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    link = movie.find("a",attrs={"class":"JC71ub"})["href"]

    # 상품 명
    print("영화제목 : ",title)
    # 가격
    print("가격 : ",price)
    # 할인 후 가격
    print("할인된 가격 : ",Sale_price)
    # 링크
    print("링크 : ",link)
    print("*"*100)

    row = [idx,title,price,Sale_price,link]
    writer.writerow(row)

browser.quit()
 

