from dbutil import DBbase

db = DBbase.DBbase("lumber.db")
data = db.exec_sql("SELECT * FROM sample")
for dt in data:
    print(dt[0])