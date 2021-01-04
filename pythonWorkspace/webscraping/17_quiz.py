#동적페이지가 아니므로 requests 사용
import requests
from bs4 import BeautifulSoup
import re
import csv

#파일 생성을 위한 구문
filename = "apartment_info.csv"
f = open(filename,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)

#Requests 모델을 이용하여 HTML 데이터 가져오기
url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

#이제 Soup 객체를 이용해서  부동산 정보를 가져오자

#부동산정보가 적혀있는 div 정보 가져오기
estates = soup.find("table",attrs={"class":"tbl"})
# print(len(estates))
rows_data = estates.find_all("tr")
print(len(rows_data))

for idx,row in enumerate(rows_data):
    row = row.get_text().split("  ")
    row = row[1:-1]
    #원하는 정보를 지니지 않은 row는 pass    
    if len(row) <= 1:
        columns = ["거래","공급/전용면적","매물가(만원)","동","층"]
        writer.writerow(columns)
        continue
    
    writer.writerow(row)
    transaction = row[0]
    square = row[1]
    price = row[2]
    dong = row[3]
    ho = row[4]

    print("="*10+" 매물 "+ str(idx) +" "+"="*10)
    print("거래 :",transaction)
    print("면적 :",square)
    print("가격 :",price)
    print("동 :",dong)
    print("층 :",ho)

# for idx,row in enumerate(rows_data):
#     if len(row) <= 1 :
#         continue

#     columns = row.find_all("div",attrs={"class":"txt_ac"})
#     print(len(columns))
#     transaction = columns[1]
#     square = columns[1]
#     price = columns[2]
#     dong = columns[3]
#     ho = columns[4]


    # transaction = row.find("div",attrs={"class":"txt_ac"})[0]
    # square = row.find("div",attrs={"class":"txt_ac"})[1]
    # price = row.find("div",attrs={"class":"txt_ac"})[2]
    # dong = row.find("div",attrs={"class":"txt_ac"})[3]
    # ho = row.find("div",attrs={"class":"txt_ac"})[4]

    # print("="*10+"매물 "+ idx +"*"*10)
    # print("거래 : ",transaction)
    # print("면적 : ",square)
    # print("가격 : ",price)
    # print("동 : ",dong)
    # print("층 : ",ho)

    # ================ 매물 1 ===========
    #거래 : 매매
    #면적 : 84/59 (공급/전용)
    #가격 : 165,000 (만원)
    #동 : 214동
    #층 : 고/23

# for idx,estate in enumerate(estates): 