#coding:utf-8
from flask import Flask
from controller import Controllers as ctrl

app = Flask(__name__)
@app.route('/')
def index():
    ctl = ctrl.Controllers()
    return ctl.ctl_index()

if __name__ == '__main__':
    app.debug = True
    app.run()
#デバッグモードTrueにすると変更が即反映される
#ファイルのエンコードはUTF-8で保存すること
#下記URLをブラウザに打ち込むとページが開く
#   http://127.0.0.1:5000/