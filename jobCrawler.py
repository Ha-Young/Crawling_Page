class JobCrawler(object):
    # 초기화
    def __init__(self):
        # 다음뉴스의 IT 섹션의 기사를 대상으로 합니다.
        self.target_url = 'https://news.daum.net/breakingnews/digital?page='
        # 크롤링 페이지 범위를 지정합니다.
        # 기본값은 1 ~ 10 (총 10페이지)
        self.range = {'s_page': 1, 'e_page': 10}
    
    
    # 범위 지정
    def set_page_range(self, s_page, e_page):
        self.range['s_page'] = s_page
        self.range['e_page'] = e_page
    
    
    # 크롤링
    @staticmethod
    def crawling(self):
        # 수집 데이터 전체 저장
        article_list = []
        # 시작페이지 -> 끝 페이지
        for number in range(self.range['s_page'], self.range['e_page'] + 1):
            # 페이지 URL 완성
            URL = self.target_url + str(number)
            
            # URL 확인
            # print(URL)
            
            # 실제 요청
            response = requests.get(URL)
            # 크롤링 딜레이(반드시 작성 1초 이상 권장)
            time.sleep(0.5)
            
            # 수신 데이터 확인(주석 해제 후 확인)
            # 수신 헤더 정보
            # print(response.headers)
            # 수신 인코딩 정보
            # print(response.encoding)
            # 수신 데이터 수신 OK
            # print(response.ok)
            # 수신 컨텐츠 정보
            # print(response.content)
            # 수신 텍스트
            # print(response.text)
            
            # bs4 선언 및 파싱
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 이 부분에서 본인이 원하는 내용을 파싱
            # 본 예제에서는 간단하게 제목, 본문 미리보기 파싱
            # 신문 본문 클릭 후 상세 내용도 직접 구현해 보세요.
            
            # 기사 본문 전체 영역
            article_body = soup.select('div.box_etc > ul.list_news2 > li')
            
            # 각 부분 파싱
            for body in article_body:
                # 신문사
                paper_info = body.select_one('span.info_news').text.strip()
                # 기사 제목
                title = body.select_one('strong.tit_thumb > a.link_txt').text.strip()
                # 기사 본문(미리보기)
                content = body.select_one('span.link_txt').text.strip()
                
                article_list.append((paper_info, title, content))
        
        # CSV 파일 저장
        self.export_csv(article_list)
    
    
    # 파일 저장
    def export_csv(self, args):
        # CSV 파일 쓰기
        # 관리자 권한 확인(윈도우), 본인이 원하는 경로 및 파일명 지정
        with open('./result_article.csv', 'w', encoding='utf-8') as f:
             # Writer 객체 생성 
             wt = csv.writer(f)
             # Tuple to Csv
             for c in args:
                 wt.writerow(c)
    
    
    # 시작
    def start(self):
        DaumArticleCrawler.crawling(self)


if __name__ == "__main__":
    pass