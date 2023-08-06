import sqlite3

class db_base():
    def __init__(self, db_name) -> None:
        self.db_name = db_name
        self.conn = self.connect()
        pass
    
    def connect(self):
        return sqlite3.connect(self.db_name)
    
    def get_sample(self):
        cur = self.conn.cursor()
        cur.execute('SELECT * FROM sample')
        for row in cur:
            print(row)