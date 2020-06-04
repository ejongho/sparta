from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/order', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    # 2. articles라는 키 값으로 영화정보 내려주기
    ord_list = list(db.ords.find({}, {'_id' : 0}))

    return jsonify({'result':'success', 'list':ord_list})

## API 역할을 하는 부분
@app.route('/order', methods=['POST'])
def saving():
    customer_name = request.form['name_give']
    color = request.form['color_give']
    count = request.form['count_give']
    address = request.form['address_give']
    number = request.form['number_give']
   
    ord = {'name' : customer_name, 'color' : color, 'count' : count, 'address' : address, 'number' : number}

    db.ords.insert_one(ord)

    return jsonify({'result': 'success', 'msg':'POST 연결되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)