from pymongo import MongoClient
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = '#fhjb23234@e3'
client = MongoClient('mongodb://localhost:27017/',username='admin',password='admin',authMechanism='SCRAM-SHA-256')
fotato_db = client['fotato']
# products_collection = fotato_db.products
# products_collection.insert({"product":"Sopu","Stock":265})

@app.route('/prod', methods=['GET'])
def get_all_prods():
  prod = fotato_db.prods
  output = []
  for s in prod.find():
    output.append({'name': s['name'], 'description': s['description'], 'price' : s['price'],'stock_availability': s['stock_availability'],"item_code" :s['item_code'],"MaxQO" :s['MaxQO'],"MinQO": s['MinQO'],  "asserts" : s['asserts'],"discount":s['discount'],"seller_details":s['seller_details'],"review": s['review'],"category" :s['category']})
  return jsonify({'result' : output})

@app.route('/prod/', methods=['GET'])
def get_one_star(name):
  prod = fotato_db.prods
  s = prod.find_one({'name' : name})
  if s:
    output = {'name': s['name'], 'description': s['description'], 'price' : s['price'],'stock_availability': s['stock_availability'],"item_code" :s['item_code'],"MaxQO" :s['MaxQO'],"MinQO": s['MinQO'],  "asserts" : s['asserts'],"discount":s['discount'],"seller_details":s['seller_details'],"review": s['review'],"category" :s['category']}
  else:
    output = "No such name"
  return jsonify({'result' : output})

@app.route('/prod', methods=['POST'])
def add_star():
  prod = fotato_db.prods
  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  stock_availability = request.json['stock_availability']
  item_code = request.json['item_code']
  MaxQO = request.json['MaxQO']
  MinQO = request.json['MinQO']
  asserts = request.json['asserts']
  discount = request.json['discount']
  seller_details = request.json['seller_details']
  review = request.json['review']
  category = request.json['category']
  star_id = prod.insert({'name': name, 'description': description, 'price' : price,'stock_availability': stock_availability,"item_code" :item_code,"MaxQO" :MaxQO,"MinQO": MinQO,  "asserts" : asserts,"discount":discount,"seller_details":seller_details,"review": review,"category" :category})
  new_star = prod.find_one({'_id': star_id })
  output = {'name': new_star['name'], 'description': new_star['description'], 'price' : new_star['price'],'stock_availability': new_star['stock_availability'],"item_code" :new_star['item_code'],"MaxQO" :new_star['MaxQO'],"MinQO": new_star['MinQO'],  "asserts" : new_star['asserts'],"discount":new_star['discount'],"seller_details":new_star['seller_details'],"review": new_star['review'],"category" :new_star['category']}
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)   
