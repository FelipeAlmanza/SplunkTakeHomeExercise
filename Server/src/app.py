from collections import defaultdict
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import yaml

DB_CONFIG = "../Database/dbconfig.yaml"

with open(DB_CONFIG) as dbConfigFile:
    dbConfig = yaml.safe_load(dbConfigFile)

app = Flask(__name__)
app.config["MONGO_URI"] = dbConfig["client"] + "/" + dbConfig["database"]
mongo = PyMongo(app)

@app.route('/')
def index():
    return 'Splunk Take Home Exercise REST API'

@app.route('/overview', methods=["GET"])
def get_overview():
    objects = mongo.db[dbConfig["collection"]].find()

    # Counts ocurrences of type values
    objectCounter = defaultdict(int)
    for object in objects:
        objectCounter[object["type"]] += 1

    objectCounterDic = dict(objectCounter)

    response = jsonify({"Overview" : objectCounterDic})

    return response


@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        "message" : "Resource not found: " + request.url,
        "status" : 404
    })
    response.status_code = 404
    return response
        

if __name__ == '__main__':
    app.run(debug=True)