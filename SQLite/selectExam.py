import sqlite3

try:
    # DB 접속
    conn = sqlite3.connect('C:/DBExam/SQLiteExam/sqlite.db')
    cur = conn.cursor()

    # tblmember 테이블의 데이터 조회
    cur.execute('select * from tblmember;')

    # 조회된 전체 레코드 출력
    for row in cur:
        print(row)
finally:
    conn.close()