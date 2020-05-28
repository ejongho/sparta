from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

## 코딩 할 준비 ##

matrix = db.movies.find_one({'title':'매트릭스'})
db.movies.update_many({'star' : matrix['star']}, {'$set':{'star' : 0}})