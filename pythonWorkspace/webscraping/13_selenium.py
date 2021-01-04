# from selenium import webdriver

# browser = webdriver.Chrome("./chromedriver.exe")
# browser.get("http://naver.com")



#네이버 로그인

#1 chrome driver 실행
from selenium import webdriver
import time

browser = webdriver.Chrome("./chromedriver.exe")
browser.get("http://naver.com")
#2 로그인 버튼에 연결후 클릭
browser.find_element_by_class_name("link_login").click()
#3 아이디, 비밀번호 입력
browser.find_element_by_class_name("int").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")
browser.find_element_by_id("log.login").click()

time.sleep(1)

#4 다른 아이디 새로 입력
browser.find_element_by_class_name("int").clear()
browser.find_element_by_class_name("int").send_keys("new_id")

#5 html 정보 출력
print(browser.page_source)

#6. 브라우저 종료
browser.quit() #전체 창 종료
#browser.close() #탭종료