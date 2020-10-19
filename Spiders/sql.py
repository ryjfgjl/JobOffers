# connect to mysql

import pymysql

class Sql:

    def __init__(self):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.passwd = 'root'

    def conn(self):
        pass
       
    def conn_db(self, db):
        db_conn = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=db,charset='utf8')
        return db_conn

    def exec_sql(self, db_conn, sql, data=[]):
        cur = db_conn.cursor()
        if data:
            cur.executemany(sql, data)
        else:
            for s in sql.split(';'):
                if s == '':
                    continue
                cur.execute(s)
        db_conn.commit()
        cur.close()

        return cur

