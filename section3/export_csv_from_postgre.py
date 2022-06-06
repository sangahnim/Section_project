import psycopg2
import csv
import os

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

# 커서생성
cur = connection.cursor()
sql = """COPY (SELECT * FROM top10s) TO STDOUT WITH CSV DELIMITER ',' HEADER;"""
with open("./top10s_export.csv", "w", encoding='UTF8') as file:
    cur.copy_expert(sql, file)

connection.commit()