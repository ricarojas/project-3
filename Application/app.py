from flask import Flask, render_template, request, url_for, redirect
import pymongo
import plotly as plt
import plotly.express as px
from flask.json import jsonify
import pandas as pd
import json


# Set up the database connection
client = pymongo.MongoClient("localhost",27017)
# Establish the database
db = client.australian_disability

# Review that the collections have been created.
db.list_collection_names()


app = Flask(__name__)

# Get the data for NSW for a given year
@app.route("/year/2012",  methods=['GET'])
def get_for_year():
    collection_name = 'nsw_data_2012'
    collection = db.get_collection(collection_name)
    df = pd.DataFrame(list(collection.find()))
    print(df)
    fig = px.bar(df, x="Age group (years)", y="All persons")
    graphJSON = json.dumps(fig, cls=plt.utils.PlotlyJSONEncoder)
    header= "All persons in NSW in the year 2012 with a disability"
    description = "All persons that live in NSW that are male or female and have a disability for the year 2012"
    return render_template('notdash2.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')