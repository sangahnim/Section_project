# 캐글데이터
# 해당블로그참조
# https://velog.io/@rsj9987/TIL21.07.16-python-psycopg2%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%9C-postgresql-%EC%A0%91%EC%86%8D
# https://www.psycopg.org/psycopg3/docs/basic/copy.html
# psycopg2.errors.SyntaxError: syntax error at or near


# 데이터베이스 연결

import psycopg2
import csv

# breakpoint()

# postgresql 접속
My_host = ""
My_database = ''
My_user = ''
My_password = ''

connection = psycopg2.connect(
    host=My_host,
    database=My_database,
    user=My_user,
    password=My_password
)

# print(connection)
# breakpoint()

# 커서생성
cur = connection.cursor()
print(cur)

cur.execute("DROP TABLE IF EXISTS top10s;")

# table 생성
cur.execute("""CREATE TABLE top10s (
                id  INTEGER NOT NULL PRIMARY KEY,
                artist  VARCHAR(60),
                top_genre VARCHAR(60),
                year INTEGER,
                bpm_tempo INTEGER,
                energy INTEGER,
                danceability INTEGER,
                decibel INTEGER,
                live INTEGER,
                length INTEGER,
                acoustic INTEGER,
                speechiness INTEGER,
                popular INTEGER,
                positive VARCHAR(32));
""")

# 데이터베이스에 저장할 csv file
with open('flask_app/data/top10s_preprocessing.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    datas = [x for x in reader] # csv 파일 리스트로 저장


# print(reader)
# print(datas)
'''for i in datas:
    print(i)'''
#print('')

# header 삭제
datas.pop(0)

# Id 추가
#print('id추가—————————')
for i in range(len(datas)):
    datas[i].insert(0, i)
'''for i in datas:
    print(i)'''
#print('—————————')

# 다중 삽입문을 위한 빈 텍스트 생성
insert_text = ""

# 튜플형태로 변경하고 ','로 나누어 데이터 삽입하기 위해 for문으로 삽입문 정의
#print('튜플—————————')
for i,text in enumerate(datas):
    insert_text += str(tuple(text)) # 튜플로 변경하여 저장
    insert_text += "," # ','로 데이터 나눔
#print(insert_text)
#print('—————————')
#print('튜플,—————————')
insert_text = insert_text[:-1] # 삽입문의 마지막 ',' 제거
#print(insert_text)
#print('—————————')


# 삽입문 전송
# cur.execute("INSERT INTO top10s (id,artist,top_genre,year,bpm_tempo,energy,danceability,decibel,live,length,acoustic,speechiness,popular,positive) VALUES {};".format(insert_text))

cur.execute("INSERT INTO top10s (id,artist,top_genre,year,bpm_tempo,energy,danceability,decibel,live,length,acoustic,speechiness,popular,positive) VALUES {};".format(insert_text))

# 데이터 베이스에 내용 전송
connection.commit()

# 데이터 베이스에 제대로 저장되었는지 확인
cur.execute("SELECT * FROM top10s") 
result = cur.fetchall()
# print(result[:])

