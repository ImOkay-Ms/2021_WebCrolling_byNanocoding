#네이버 웹툰 사이트를 크롤링
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml") #네이버 웹툰의 HTML코드를 가져옴
# print(soup.tilte) #soup객체를 통해 html 태그에 쉽게 접근 가능
# print(soup.a) #처음으로 만나는 a태그의 정보를 추출
# print(soup.a.attrs)
# print(soup.a["href"]) # a element의 href 속성값 추출 가능

#이렇게 하는것은 페이지에 대한 지식이 있을때나 가능ㅠ

#그래서 우리는 find 기능을 이용

# #웹툰 올리기
# #class 가 Nbtn_upload인 a element를 찾아줘
# print(soup.find("a",attrs={"class":"Nbtn_upload"}))
# #class가 Nbtn_upload인 element를 찾아줘
# print(soup.find(attrs={"class":"Nbtn_upload"}))
 
rank1 = soup.find("li",attrs={"class":"rank01"})
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())

rank2 = rank3.previous_sibling.previous_sibling
# print(rank1.parent)

rank2 = rank1.find_next_sibling("li")
print(rank2.a.get_text())
rank3 = rank2.find_next_siblings("li")

print(rank3.get_text())

