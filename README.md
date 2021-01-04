# 2021_WebCrolling_byNanocoding
데이터분석의 시작은 데이터의 수집! Python의 request, selenium, BeautifulSoup 모듈을 이용해 웹사이트에서 원하는 정보를 수집하는 방법에 대한 self study 입니다.

코딩 유투더 나노코딩 님의 강의를 참고하였습니다.

유투버 나노코딩 님의 강의 링크
https://www.youtube.com/watch?v=yQ20jZwDjTE

나노코딩 의 채널 링크
https://www.youtube.com/channel/UC7iAOLiALt2rtMVAWWl4pnw



HTML CSS JavaScript 에대한 개념 설명

HTML XPath 어떤 element의 경로를 의미함
ex) <button id ="search_btn" type="submit"
title="검색" class="btn_submit">
xpath는 element의 속성 특징을 이용하여 생성함
fullpath는 상위경로까지 나타냄

HTML에서의 부모 자식 관계

Chorme 엡 브라우저는 웹 정보를 읽어오는데 매우 편리함 F12의 개발자 모드를 이용

정규식 규칙을 가진 어떤 문자열을 이용하는 식
EX)주민등록 번호, 이메일 주소, 차량번호
등을 이용함
(ca.e) 하나의 문자
(^de) 문자열의 시작
(se$) 문자열의 끝 
match() 처음부터 일치하는지
search()일치하는 게 있는지
findall() 일치하는 것 모두 리스트로

User-Agent 
서버에서 권한을 주지 않을 시 사용
어떤 페이지를 보여줄까?
근데 진짜 사람맞아?

Request
웹페이지(html) 읽어오기
빠르다
동적 웹 페이지에는 사용 불가

Selenium
웹페이지 자동화
느리다 , 메모리차지있음
동적 웹 페이지도 가능

불다 웹페이지 문서를 가져올 방법의 차이일 뿐

BeautifulSoup을 이용하여 사용 가능 하다.
문제 없겠죠?
res.raise_for_status()

Selenium
로그인, 어떤 결과에 대한 필터링 등 어떤 동작을 해야 하는 경유
※크럼 버전에 맞는 chrome driver.exe가 있어야 함
find_elements(s)_by_id         id로 찾기
by_class_name        class name으로 찾기
by_link_text        링크 text로 찾기
bt_xpath        xpath 로 찾기
click()        클릭
send_keys()        글자입력

Selenium
때로는 기다려 주세요 ex)네이버 항공권
elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By_XPATH,"//*[@ID='content']")))

스크롤을 내려주세요
import time
interval = 2 #2초에 한번씩 스크롤 내림

#현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")
#반복수행
while True:
        #스크롤을 가장 아래로 내림browser.execute_script("window.scrollTo(0,do
cument.bod)")

#현재 문서 높이를 가져와서 저장
curr_height = browser.execute_script("return document.body.scrollHeight")
if curr_height == prev.height:
        break
prev.height = curr_height

BeautifulSoup
find        조건에 맞는 첫 번째 element
find_all        조건에 맞는 모든 element  리스트로
find_next_sibling(s)        다음 형제 찾기
find_previous_sibling(s)        이전 형제 찾기
soup["href"]        속성값 가져오기
soup.get_text()        텍스트 가져오기

이미지 다운로드
with open("파일명","wb") as f:
        f.write(res.content)

CSV 파일 생성
import csv
f = open(filename, "w",encoding="uft-8-sig",newline="")

Headless Chrome
브라우저를 띄우지 않고 동작
떄로는 User-Agent 정의 필요
59 버전부터 (최신 버전이면 모두 가능)

※주의사항※
무분별한 웹 크롤링 / 웹 스크래핑은 대상 서버에 부하
-> 계정/ip 차단

데이터 사용 주의 
-> 이미지,텍스트 등 데이터 무단 활용 시 저작권 침해 요소, 법적 제재

robots.txt
-> 법적효력 x, 대상 사이트의 권고

find_all 에 limit 사용가능!
.sprit()을 통해 공백 제거가능
  
