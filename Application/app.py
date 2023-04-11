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

# Generate a bar chart for the data provided by the dropdowns on the front end!
@app.route("/bar",  methods=['GET'])
def generate_bar_chart():
    year = request.args.get('year')
    gender = request.args.get('gender')
    state = request.args.get('state')
    toggle = request.args.get('toggle_comparison')
    print(toggle)
    collection_name = 'state_and_year'
    collection = db.get_collection(collection_name)
    df = pd.DataFrame(list(collection.find()))
    if year != 'all':
        df = df.loc[df['Year'] == int(year)]
    if state != 'all':
        df = df.loc[df['State'] == state]
    df.sort_values(by=['Age group (years)'], inplace=True)
    if gender == 'All persons':
        description = 'All person that live in Australia that have a disablity for the year ' + str(year)
    else:
        description = 'All persons that live in Australia that identified as ' + str(gender) + ' and have a disability for the year ' + str(year)
    fig = px.bar(df, x="Age group (years)", y=gender, color="State")
    graphJSON = json.dumps(fig, cls=plt.utils.PlotlyJSONEncoder)
    header= 'People in Australia in the year ' + str(year) + ' with a disability'
    return render_template('barchart.html', graphJSON=graphJSON, header=header,description=description)

@app.route("/comparison",  methods=['GET'])
def generate_comparison_bar_chart():
    gender = request.args.get('gender')
    collection_name = 'state_and_year'
    collection = db.get_collection(collection_name)
    df = pd.DataFrame(list(collection.find()))
    df.sort_values(by=['Age group (years)'], inplace=True)
    fig = px.bar(df, x="Age group (years)", y="All persons", color="State")
    graphJSON = json.dumps(fig, cls=plt.utils.PlotlyJSONEncoder)
    header= 'People in Australia who identify as ' + str(sex) + ' with a disability'
    description = 'People in Australia who identify as ' + str(sex) + 'and have a disability for the year '
    return render_template('barchart.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')