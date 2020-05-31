import sqlite3

try:
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    # 테이블 생성
    cur.execute('create table phonebook(name varchar(10),tel varchar(20), address varchar(50));')

    phoneList = (('Hong', '010-2030-2034', '서울시 강남구'),
                 ('Chang', '010-8989-1234', '서울시 강북구'),
                 ('Choi', '010-1123-5664', '서울시 강동구'))

    # 테이블 데이터 삽입 (총 3개 레코드)
    cur.executemany('insert into phonebook values(?, ?, ?)', phoneList)

    # 해당 위치에 sql파일 생성
    fill_write = open('C:\\DBExam\SQLiteExam\scriptFile.sql','w')

    # 트랜잭션이 close 되기전까지의 작업을 sql 파일에 작성
    for row in conn.iterdump():
        fill_write.write("{}\n".format(row))

finally:
    fill_write.close()
    conn.close()