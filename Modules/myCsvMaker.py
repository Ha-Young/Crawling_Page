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