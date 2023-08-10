from flask import Flask, jsonify, request
from flask import render_template
import time
from pymongo import MongoClient
import pymongo
import json

app = Flask(__name__)

def get_mongo_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://DipMukeshbahiPatel:Dip141100@cluster0.i0vgfb2.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we swill use the same database throughout the tutorial
    return client["final_project"]["final_project"]


def get_all_data():
    get_client = get_mongo_database()
    get_data = get_client.find({})
    return get_data

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/barChart')
def barChart():
    data = get_all_data()
    good = 0
    bad = 0
    for i in data:        
        if (int(i["so2"]) > 9.0):
            good += 1    
        else:
            bad += 1
    labels = ["Good","Bad"]
    values = [good,bad]
    return render_template("barGraph.html",labels=labels,values=values)



@app.route('/lineChart')
def lineChart():
    data = get_all_data()
    o3=[]
    no2=[]
    so2=[]
    labels=[]
    
    for i in data:
        labels.append(i["datetime"])
        o3.append(i["o3"])
        no2.append(i["no2"])
        so2.append(i["so2"])
    return render_template("lineGraph.html",labels=labels,o3=  o3,no2=no2,so2=so2)

# BONUS
@app.route('/getAll', methods=['GET'])
def get_item_by_id():
    data = get_all_data()
    response = []
    for document in data:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
