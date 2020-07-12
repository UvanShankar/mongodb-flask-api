from pymongo import MongoClient
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = '#fhjb23234@e3'
client = MongoClient('mongodb://localhost:27017/',username='mongo_api',password='l0l0',authMechanism='SCRAM-SHA-256')
fotato_db = client['fotato']
# products_collection = fotato_db.products
# products_collection.insert({"product":"Sopu","Stock":265})

@app.route('/prod', methods=['GET'])
def get_all_prods():
  prod = fotato_db.prods
  output = []
  for s in prod.find():
    output.append({'name' : s['name'], 'distance' : s['distance']})
  return jsonify({'result' : output})

@app.route('/prod/', methods=['GET'])
def get_one_star(name):
  prod = fotato_db.prods
  s = prod.find_one({'name' : name})
  if s:
    output = {'name' : s['name'], 'distance' : s['distance']}
  else:
    output = "No such name"
  return jsonify({'result' : output})

@app.route('/prod', methods=['POST'])
def add_star():
  prod = fotato_db.prods
  name = request.json['name']
  distance = request.json['distance']
  star_id = prod.insert({'name': name, 'distance': distance})
  new_star = prod.find_one({'_id': star_id })
  output = {'name' : new_star['name'], 'distance' : new_star['distance']}
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)   