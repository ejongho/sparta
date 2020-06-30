from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta         

import uuid

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

## API 역할을 하는 부분
@app.route('/search', methods=['GET'])
def search_prodcut():
   # keyword_receive = '/^'
   keyword_receive = request.args.get('keyword')
   # keyword_receive += '$/i'
   # print(keyword_receive)
   # 검색어 찾는 부분
   # findByBrand = list(db.prodcut.find({'brand' : keyword_receive}, {'_id' : False}))
   findByBrand = list(db.prodcut.find({'brand' : { '$regex': keyword_receive, '$options' : 'i'}}, {'_id' : False}))
   findByID = list(db.prodcut.find({'prdID' : { '$regex': keyword_receive, '$options' : 'i'}}, {'_id' : False}))
   if(findByBrand != []) :
      distinctIds = db.prodcut.find({'brand' : { '$regex': keyword_receive, '$options' : 'i'}}, {'_id' : False}).distinct('ID')
      # numOfIds = len(distinctIds)
      newJson = []
      for i in distinctIds:
         priceOfPrd = list(filter(lambda prices: prices['ID'] == i, findByBrand))
         numOfSites = len(priceOfPrd)
         newDict = {'id' : i}
         for numOfSite in range(numOfSites):
            si = priceOfPrd[numOfSite]['site']
            pr = priceOfPrd[numOfSite]['price']
            newDict[si] = pr
         newJson.append(newDict)
      print(newJson)
      return jsonify({'result':'success', 'msg': findByBrand, 'price': newJson})
   elif {findByID != []} :
      return jsonify({'result':'success', 'msg': findByID})
   #    여기서 리턴

   # 새로운 상품 ID 발급하기 위한 코드
   # siteID = uuid.uuid4().hex[:8]

   # db 구조
   # db.prodcut.insert_one({'ID': siteID, 'site' : 'mclabels', 'prdID' : 'A20HJ108723100', 'brand' : 'AMI', 'imgUrl' : 'https://cdn-images.farfetch-contents.com/comme-des-garcons-wallet-logo-print-tote-bag_14770240_25014374_1000.jpg?c=2', 'price': '138000', 'origin' : 'portugal', 'prdName' : 'Coeur T-shirt'})
   

@app.route('/test', methods=['POST'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
