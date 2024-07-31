import pymysql
import pandas as pd
import numpy as np


# MySQL 연결 설정

# 업로드할 파일 경로
file_path = 'redtable_report_board_20240717.xlsx'

# MySQL 연결
#conn = pymysql.connect(host='db-7ma06.pub-cdb.ntruss.com', user='redtable_openapi', password='fpemxpdlqmf5491!@#', db='redtable2021', charset='utf8') #개발db
conn = pymysql.connect(host='db-6j3k3.pub-cdb.ntruss.com', user='redtable', password='fpemxpdlqmf5491!@#',autocommit=True,cursorclass=pymysql.cursors.DictCursor, db = "redtable2021")
cur = conn.cursor(pymysql.cursors.DictCursor)


# 파일 읽기
df = pd.read_excel(file_path)
#df.replace({np.nan: None}, inplace=True)
#print(df.isnull().sum())


# 테이블 이름 지정
table_name = 'redtable_report_board'

#value = None
#cursor.execute("INSERT INTO table (`column1`) VALUES (%s)", (value,))

# 데이터베이스에 데이터 입력

for _, row in df.iterrows():
    print(row)
    row.replace({pd.NA: None}, inplace=True)
    #print(f"replcaerow:{row}")
    print("!!!!!--------------------")
    columns = ', '.join(row.index)
    print(f"col : {columns}")
    values = ', '.join(['%s' for _ in range(len(row))])
    print(values)
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
    print(query)
    cur.execute(query, tuple(row))



# 변경사항 커밋
conn.commit()

# 연결 닫기
cur.close()
conn.close()