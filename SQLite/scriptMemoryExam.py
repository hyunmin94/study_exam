import sqlite3

try:
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()

    # 스크립트 파일 불러오기
    f = open('C:\\DBExam\SQLiteExam\scriptFile.sql', encoding='cp949')
    # 스크립트 내용 불러오기
    script = f.read()
    # 스크립트 내용 실행
    cur.executescript(script)
    # 스크립트의 테이블(phonebook) 데이터 조회
    cur.execute('select * from phonebook;')
    # 조회 결과에서 위에서 2개 레코드 출력
    for row in cur.fetchmany(2):
        print(row)

finally:
    f.close()
    conn.close()

