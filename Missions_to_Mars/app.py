from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

import pymongo

# create instance of Flask app
app = Flask(__name__)

# Create connection variable

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mission_to_mars
mission_to_mars= db.mission_to_mars


@app.route("/")
def home(): 
    information = list(mission_to_mars.find())
    print(information)
    return render_template('index.html', information = information)


if __name__ == "__main__":
    app.run(debug=True)
