#이 Project의 의미

import requests
import re
from bs4 import BeautifulSoup


def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    return soup

#날씨정보

# [오늘의 날씨]
# 흐림, 어제보다 OO℃ 높아요
# 현재 OOº (최저 00℃/최고 OO℃)
# 오전 강수확률 OO% / 오후 강수확률 OO%
# 미세먼지 oo㎛/㎥ 좋음 
# 초 미세먼지 oo㎛/㎥ 좋음

def scrape_weather():
    #웹페이지 정보 가져오기 requests, bs
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    #날씨 정보 가져오기
    # 흐림, 어제보다 OO℃ 높아요
    cast = soup.find("p",attrs={"class":"cast_txt"}).get_text()
    # 현재 OOº (최저 00℃/최고 OO℃)
    now_temp = soup.find("span",attrs={"span","todaytemp"}).get_text()
    min_temp = soup.find("span",attrs={"class","min"}).get_text()
    max_temp = soup.find("span",attrs={"class","max"}).get_text()
    # 오전 강수확률 OO% / 오후 강수확률 OO%
    rain_rate_am = soup.find("span",attrs={"class","point_time morning"}).find("span",attrs={"class","num"}).get_text()
    rain_rate_pm = soup.find("span",attrs={"class","point_time afternoon"}).find("span",attrs={"class","num"}).get_text()
    # 미세먼지
    dust = soup.find("dl",attrs={"class":"indicator"})
    pm10 = dust.find_all("dd",attrs={"class":"lv1"})[0].get_text()
    pm25 = dust.find_all("dd",attrs={"class":"lv1"})[1].get_text()          
    #출력 num
    print(cast)
    print("현재 {}℃  ( 최저 : {}/ 최고 : {})".format(now_temp,min_temp,max_temp))
    print("오전 강수확률 {}% / 오후 강수확률 {}%".format(rain_rate_am,rain_rate_pm))
    print("미세먼지 : {}".format(pm10))
    print("초 미세먼지 : {}".format(pm25))
    # 미세먼지 oo㎛/㎥ 좋음 
# 초 미세먼지 oo㎛/㎥ 좋음

#헤드라인 뉴스
#1. 기사제목 ...
#(링크)
#2. 기사제목 ...
#(링크)
def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com/"
    soup = create_soup(url)
    news_list = soup.find("ul",attrs={"class":"hdline_article_list"}).find_all("li",limit=3) 
    for idx,news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url+news.find("a")["href"]
        print("{}. {}".format(idx+1,title))
        print("링크 : {}".format(link))

#IT뉴스 정보 가져오기
def scrape_IT_news():
    print("[오늘의 IT기사]")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul",attrs={"class":"type06_headline"}).find_all("li",limit=3)
    #짝수번째만 저장해야 함!

    #이미지면 idx 1(두번째) 의 data를 사용한다.
    for idx,news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1
        title = news.find_all("a")[a_idx].get_text().strip()
        link = news.find("a")["href"]
        print("IT 기사 {}. {}".format(idx+1,title))
        print("링크 : {}".format(link))

#해커스 어학원 정보 가져오기
def Hakers():
    print("[오늘의 영어 표현]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    
    sentens = soup.find_all("div",attrs={"class":"conv_txt"})

    english_sentences = sentens[1].find_all("div",attrs={"id":re.compile("^conv_kor_t")})
    korean_sentences = sentens[0].find_all("div",attrs={"id":re.compile("^conv_kor_t")})

    #영어문장
    print("<영어표현>")
    for idx,sentence in enumerate(english_sentences):
        temp = sentence.get_text().strip()
        print(temp)

    print()

    #한글문장
    print("<한글표현>")
    for idx,sentence in enumerate(korean_sentences):
        temp = sentence.get_text().strip()
        print(temp)


if __name__ == "__main__":
    scrape_weather() #오늘의 날씨 정보 가져오기
    print()
    scrape_headline_news() #헤드라인 뉴스 가져오기
    print()
    scrape_IT_news()
    print()
    Hakers()
    