# import requests
# import re
# from bs4 import BeautifulSoup

# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
# url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
# res = requests.get(url,headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text,"lxml")

# # items = soup.find_all("dd",attrs={"class":re.compile("^search-product")})
# item = soup.find_all("div",attrs={"class":"name"})
# print(item[1].get_text())

#쿠팡 제품 출력해보기
# import requests
# from bs4 import BeautifulSoup

# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
# url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
# res = requests.get(url,headers = headers)
# soup =  BeautifulSoup(res.text,"lxml")

# items = soup.find_all("dl",attrs={"class":"search-product-wrap"})
# for item in items:
#     #
#     #제품명
#     print("제품명 : " + item.find("div",attrs={"class":"name"}).get_text())
#     #가격
#     print("가격 : " + item.find("strong",attrs={"class":"price-value"}).get_text())    
#     #rating 리뷰 100개 이상 평점 4.5 되는 것만 조회
#     rate = item.find("em",attrs={"class":"rating"})
#     if rate:
#         rate = rate.get_text()
#     else:
#         print("평점이 없는 상품입니다.")
#         continue
    
    # if float(rate)>=4.5 and :
    #     print(name,price,rate,rate_cnt  )
    #rating_count
    

#광고 제외, 평점 4.5이상 평점없는 상품 제외, Apple사 제외
#최근 5페이지 까지 조회
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

for i in range(1,6):
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(i)
    res = requests.get(url,headers = headers)
    soup =  BeautifulSoup(res.text,"lxml")

    items = soup.find_all("dl",attrs={"class":"search-product-wrap"})
    for item in items:
        #광고제거 
        ad_bedge = item.find("span",attrs={"class":"ad-badge-text"})
        if ad_bedge:
            #print("광고제거")
            continue

        #rating 평점 4.5 되는 것만 조회
        rate = item.find("em",attrs={"class":"rating"})
        if rate:
            rate = rate.get_text()
        else:
            #print("평점이 없습니다.")
            continue

        #리뷰 100개 이상 만 조회
        rate_cnt = item.find("span",attrs={"class":"rating-total-count"})
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()
            rate_cnt = rate_cnt[1:-1]
        else:
            #print("리뷰가 없습니다.")
            continue

        #바로가기 링크생성
        if float(rate) >=4.5 and int(rate_cnt) >= 100:
            print("제품명 : " + item.find("div",attrs={"class":"name"}).get_text())
            print("가격 : " + item.find("strong",attrs={"class":"price-value"}).get_text(),"원")    
            print("평점 : " ,rate)
            print("후기수 : ",rate_cnt)
            #print("바로가기 링크 : {} ".format("https://www.coupang.com" + link))
            print("*"*100)
