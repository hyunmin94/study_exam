import sqlite3
from datetime import datetime

try:
    # DB 접속
    conn = sqlite3.connect('C:/DBExam/SQLiteExam/sqlite.db')
    cur = conn.cursor()

    # 단일 레코드 : 데이터 insert 처리 (3개 레코드)
    # cur.execute("INSERT INTO tblmember VALUES(?,?,?);", (3, '이순신', datetime.today()))
    # cur.execute("INSERT INTO tblmember VALUES(?,?,?);", (4, '박상철', datetime.today()))
    # cur.execute("INSERT INTO tblmember VALUES(?,?,?);", (5, '박문철', datetime.today()))

    # 다중 레코드 : 데이터 insert 처리 (3개 레코드)
    data_list = [(3, '이순신', datetime.today()),
                 (4, '박상철', datetime.today()),
                 (5, '박문철', datetime.today())]

    cur.executemany("INSERT INTO tblmember VALUES(?,?,?);", data_list)

    conn.commit()

finally:
    conn.close()

