from flask import Flask
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

if __name__ == '__main__':
    app.run(debug=True)