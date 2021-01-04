import requests
import csv 
from bs4 import BeautifulSoup

#주소를 res, soup 변수에 각각 저장
url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0"

filename = "시가총액_1-200.csv"
f = open(filename,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)
index_row = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(index_row)

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

table = soup.find("table",attrs={"summary":"코스피 시세정보를 선택한 항목에 따라 정보를 제공합니다."})
rows = table.find("tbody").find_all("tr")

#print("rows의 type",type(rows))
for row in rows:
    #print(row)
    columns = row.find_all("td")
    if len(columns) <= 1:
        continue
    data = [column.get_text().strip() for column in columns]
    #print(data)
    writer.writerow(data)
