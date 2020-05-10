# Byte Degree Python Crawling MiniProject 수행
# 2020-05-10 구르딩딩(hychoi)
# wishcat.com을 활용하여 개발관련 프로젝트 일거리 정보를 가져옵니다.


from time import sleep
from bs4 import BeautifulSoup
import requests
import time
from Modules.myLogger import Log

class WishcatJobCrawler(object):
    # 초기화
    def __init__(self):
        Log("JobCrawler Init...")
        # 위시켓의 프로젝트 목록
        self.target_url = 'https://www.wishket.com/project/'

    # 크롤링
    @staticmethod
    def crawling(self):
        # 수집 데이터 전체 저장
        project_list = []
        
        # 실제 요청
        response = requests.get(self.target_url)
        # 크롤링 딜레이(반드시 작성 1초 이상 권장)
        time.sleep(0.5)
        print(response)
    
    # 시작
    def start(self):
        print("start wishcat")
        WishcatJobCrawler.crawling(self)


if __name__ == "__main__":
    pass