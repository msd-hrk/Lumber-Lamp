import sqlite3

class DBbase():
    def __init__(self, db_name) -> None:
        self.db_name = db_name
        self.conn = self.connect()
        pass
    
    def connect(self):
        # コネクションの取得
        return sqlite3.connect(self.db_name)
    
    def exec_sql(self, sql):
        cur = self.conn.cursor()
        # sql文でデータベースから値を検索
        return cur.execute(sql)
