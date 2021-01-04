from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() #창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)

#가는날 오는날 선택
browser.find_element_by_xpath("//*[@id='l_8']/div[1]/div/div[1]/a").click()
browser.find_element_by_xpath("//*[@id='l_8']/div[1]/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/table/tbody/tr[5]/td[4]/a/b").click()
browser.find_element_by_xpath("//*[@id='l_8']/div[1]/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/table/tbody/tr[5]/td[5]/a/b").click()

browser.find_element_by_class_name("bg_gradient").click()
browser.find_element_by_link_text("항공권 검색").click()
try:
    elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
finally:
    browser.quit()

elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
print(elem.text)