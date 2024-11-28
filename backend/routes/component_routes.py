from flask import Blueprint, request, jsonify
from flask_pymongo import PyMongo
from flask import current_app
from bson import ObjectId  

component_routes = Blueprint('components', __name__)

@component_routes.route('/components', methods=['POST'])
def add_component():
    data = request.json
    mongo = PyMongo(current_app)  
    
    
    result = mongo.db.components.insert_one(data)
    
    
    data['_id'] = str(result.inserted_id)  
    
    return jsonify(data), 201

@component_routes.route('/components', methods=['GET'])
def get_components():
    mongo = PyMongo(current_app)  
    components = list(mongo.db.components.find())
    
    
    for component in components:
        component['_id'] = str(component['_id']) 

    return jsonify(components), 200

@component_routes.route('/components/<id>', methods=['PUT'])
def update_component(id):
    data = request.json
    mongo = PyMongo(current_app)  
    
    
    if '_id' in data:
        del data['_id']  

    mongo.db.components.update_one({'_id': ObjectId(id)}, {"$set": data})  
    return jsonify(data), 200

@component_routes.route('/components/<id>', methods=['DELETE'])
def delete_component(id):
    mongo = PyMongo(current_app)  
    mongo.db.components.delete_one({'_id': ObjectId(id)})  
    return '', 204