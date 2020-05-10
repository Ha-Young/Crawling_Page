# Byte Degree Python Crawling Mini Project를 위한 Logger 제작, 모듈화
# 2020-05-10 구르딩딩(hychoi)

import datetime
import os.path as path

logFile = '{}/{}.log'.format(path.curdir, datetime.datetime.now().strftime("%Y%m%d"))

def Log(msg):
    loginfo = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if path.exists(logFile):
        with open(logFile, 'a') as f:
            f.write('{} : {}\n'.format(loginfo, msg))
    else:
        with open(logFile, 'w') as f:
            f.write('{} : {}\n'.format(loginfo, msg))

if __name__ == "__main__":
    pass
