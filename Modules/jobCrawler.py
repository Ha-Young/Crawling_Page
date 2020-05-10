# Byte Degree Python Crawling MiniProject 수행
# 2020-05-10 구르딩딩(hychoi)
# wishcat.com을 활용하여 개발관련 프로젝트 일거리 정보를 가져옵니다.


from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import requests
import time
from Modules.myLogger import Log

class WishcatJobCrawler(object):
    # 초기화
    def __init__(self, keyword):
        Log("JobCrawler Init...")
        # 위시켓의 프로젝트 목록
        self.target_url = 'https://www.wishket.com/project/'
        self.searchKeyword = keyword

    # 크롤링
    @staticmethod
    def crawling(self):
        # 수집 데이터 전체 저장
        recuriting_project_list = []
        
        # Selenium 페이지 이동
        self.browser = webdriver.Chrome('./Webdriver/chromedriver')
        self.browser.implicitly_wait(5)
        self.browser.get(self.target_url)
        
        elem = self.browser.find_element_by_id("id_q")
        elem.send_keys(self.searchKeyword)
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="form_id"]/div/input'))).click()
        time.sleep(2)

        # bs4 초기화
        soup = BeautifulSoup(self.browser.page_source, 'lxml')

        page_li_list = soup.select('.pagination > li')
        
        for page_li in page_li_list:
            pass

        project_list = soup.select('#project-list-box > section')
        
        for project in project_list:
            print(project.select_one('.project-title').text.strip())

    # 시작
    def start(self):
        print("start wishcat")
        WishcatJobCrawler.crawling(self)


# if __name__ == "__main__":
#     pass