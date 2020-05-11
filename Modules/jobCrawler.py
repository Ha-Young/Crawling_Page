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
        self.wishcat_url = 'https://www.wishket.com'
        self.target_url = self.wishcat_url + '/project/'
        self.searchKeyword = keyword

    # 크롤링
    @staticmethod
    def crawling(self):
        # 수집 데이터 전체 저장
        recuriting_project_list = []
        
        # Selenium 페이지 이동
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        # self.browser = webdriver.Chrome('./Webdriver/chromedriver', options=chrome_options)
        self.browser = webdriver.Chrome('./Webdriver/chromedriver')
        self.browser.implicitly_wait(3)
        self.browser.get(self.target_url)
        
        elem = self.browser.find_element_by_id("id_q")
        elem.send_keys(self.searchKeyword)
        WebDriverWait(self.browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="form_id"]/div/input'))).click()
        time.sleep(2)

        # bs4 초기화
        soup = BeautifulSoup(self.browser.page_source, 'lxml')

        # project list를 얻는다
        page_li_list = soup.select('.pagination > li')
        print(page_li_list)
        
        if page_li_list == None or len(page_li_list) == 0:
            return None

        # 모집중인 프로젝트 리스트를 얻을때까지 계속 loop
        for i in range(1, len(page_li_list)):
            soup = BeautifulSoup(self.browser.page_source, 'lxml')
            project_list = soup.select('#project-list-box > section')
            if project_list == None:
                return None

            if len(project_list) == 1 and project_list[0]['class'][0] == 'no-result':
                return None

            # 모집마감이 발견되면 모집중인 프로젝트 크롤링이 완료. breker변수로 2중 for문 탈출
            breaker = False
            for project in project_list:
                if project['class'] and project['class'][0] == 'closed-project':
                    breaker = True
                    break

                project_dic = self.get_project_dic(project)
                
                print(project_dic)
                print("="*20)
                recuriting_project_list.append(project_dic)
            
            if breaker:
                break
            
            page_li_list = soup.select('.pagination > li')
            
            next_page_li_count = 1
            for page_li in page_li_list:
                a_tag = page_li.select_one('a')

                if a_tag == None or len(a_tag) == 0:
                    next_page_li_count += 1
                    continue

                page_number = a_tag.text.strip()
                print(page_number)
                if str(i + 1) == page_number:
                    break;
                else:
                    next_page_li_count += 1
            
            WebDriverWait(self.browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, f'#project-list-box > div > ul > li:nth-child({next_page_li_count}) > a'))).click()
            time.sleep(5)

        return recuriting_project_list



    def get_project_dic(self, project_element):
        project_dic = {}
        title_element = project_element.select_one('.project-title > a')
        project_dic['title'] = title_element.text.strip()
        project_dic['link'] = self.wishcat_url + title_element['href']
        basic_info_element = project_element.select_one('.project-unit-basic-info')
        project_dic['price'] = basic_info_element.select('span')[0].text.strip()
        project_dic['priod'] = basic_info_element.select('span')[1].text.strip()
        desc_element = project_element.select_one('.project-unit-desc')
        project_dic['desc'] = desc_element.select_one('p').text.strip()
        project_dic['dday'] = desc_element.select_one('.outer-info-upper-data > span').text.strip()
        project_dic['applier_num'] = desc_element.select_one('.outer-info-under-data > span').text.strip()
        project_dic['category'] = project_element.select_one('.project-category').text.strip()
        project_dic['subcategory'] = project_element.select_one('.project-subcategory').text.strip()
        skills = []
        skill_elements = project_element.select('.project-skills-tag-viewbox > .skills-tag')
        for skill_element in skill_elements:
            skills.append(skill_element.text.strip())
        project_dic['skills'] = ', '.join(skills)

        return project_dic

    # 시작
    def start(self):
        print("start wishcat")
        recuriting_project_list = WishcatJobCrawler.crawling(self)
        print(recuriting_project_list)
        

if __name__ == "__main__":
    pass