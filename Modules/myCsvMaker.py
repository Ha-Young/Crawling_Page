# 파일 저장
import csv

def processList_export_csv(process_list, saveFileName):
    # CSV 파일 쓰기
    process_title = ['제목', '예상금액', '예상기간', '설명', '마감', '지원자 수', '카테고리', '서브카테고리', '스킬', '링크']
        
    # 관리자 권한 확인(윈도우), 본인이 원하는 경로 및 파일명 지정
    with open(f'./{saveFileName}.csv', 'w', encoding='utf-8') as f:
            # Writer 객체 생성 
            wt = csv.writer(f)
            # Tuple to Csv
            wt.writerow(process_title)
            
            for process_doc in process_list:
                process_row = []
                process_row.append(process_doc['title'])
                process_row.append(process_doc['price'])
                process_row.append(process_doc['priod'])
                process_row.append(process_doc['desc'])
                process_row.append(process_doc['dday'])
                process_row.append(process_doc['applier_num'])
                process_row.append(process_doc['category'])
                process_row.append(process_doc['subcategory'])
                process_row.append(process_doc['skills'])
                process_row.append(process_doc['link'])

                wt.writerow(process_row)

