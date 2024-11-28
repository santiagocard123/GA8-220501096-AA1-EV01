from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/pc_components"
    
    mongo = PyMongo(app) 
    
    from routes.component_routes import component_routes
    app.register_blueprint(component_routes)

    CORS(app)  
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)