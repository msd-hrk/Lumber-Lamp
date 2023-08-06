from flask import render_template
from dbutil import DBbase

class Controllers():
    def __init__(self) -> None:
        pass
    
    def ctl_index(self):
        db = DBbase.DBbase("lumber.db")
        tb_name = "sample"
        data = db.exec_sql(f"SELECT * FROM {tb_name}")

        return render_template(
            'index.html'
            ,text="hello　woああああrld"
            ,text2=data
            ,page_title="お試しページ"
            )
