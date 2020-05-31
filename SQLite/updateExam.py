import sqlite3

try:
    # DB 접속
    conn = sqlite3.connect('C:/DBExam/SQLiteExam/sqlite.db')
    cur = conn.cursor()

    # 데이터 update 처리 (id가 3이상인 데이터 id를 id+10값으로 수정)
    cur.execute('update tblmember set id = id+10 where id >= 3;')
    conn.commit()

finally:
    conn.close()

