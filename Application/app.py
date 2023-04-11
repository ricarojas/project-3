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
    # Get all the variables from the query
    year = request.args.get('year')
    gender = request.args.get('gender')
    state = request.args.get('state')
    collection_name = 'state_and_year'
    collection = db.get_collection(collection_name)
    df = pd.DataFrame(list(collection.find()))
    df = df.loc[df['Year'] == int(year)]
    df = df.loc[df['State'] == state]

    # Sort the values of the dataframe.
    df.sort_values(by=['Age group (years)'], inplace=True)

    # Attempt to set dynamic headers based on input.
    if gender == 'All persons':
        description = 'All person that live in Australia that have a disablity for the year ' + str(year)
    else:
        description = 'All persons that live in Australia that identified as ' + str(gender) + ' and have a disability for the year ' + str(year)
    fig = px.bar(df, x="Age group (years)", y=gender, color="State")
    graphJSON = json.dumps(fig, cls=plt.utils.PlotlyJSONEncoder)
    header= 'People in Australia in the year ' + str(year) + ' with a disability'
    # Return the graph to our barchart template for rendering.
    return render_template('barchart.html', graphJSON=graphJSON, header=header,description=description)

@app.route("/vs_bar",  methods=['GET'])
def generate_vs_bar_chart():
    # Get all the variables from the query
    year1 = request.args.get('year1')
    gender1 = request.args.get('gender1')
    state1 = request.args.get('state1')
    year2 = request.args.get('year2')
    gender2 = request.args.get('gender2')
    state2 = request.args.get('state2')

    collection_name = 'state_and_year'
    collection = db.get_collection(collection_name)
    df = pd.DataFrame(list(collection.find()))

    # Set up the first dataframe.
    df1 = df.loc[df['Year'] == int(year1)]
    df1 = df1.loc[df['State'] == state1]
    df1_gender = df1[['Year','State',gender1,'Age group (years)']].copy()
    df1_gender.rename(columns={gender1:"Count"}, inplace=True)
    df1_gender['Gender'] = gender1

    # Set up the second dataframe.
    df2 = df.loc[df['Year'] == int(year2)]
    df2 = df2.loc[df['State'] == state2]
    df2_gender = df2[['Year','State',gender2,'Age group (years)']].copy()
    df2_gender.rename(columns={gender2:"Count"}, inplace=True)
    df2_gender['Gender'] = gender2


    # Sort the values of the two dataframes.
    df1_gender.sort_values(by=['Age group (years)'], inplace=True)
    df2_gender.sort_values(by=['Age group (years)'], inplace=True)

    # Merge the two dataframes
    frames = [df1_gender, df2_gender]
    result = pd.concat(frames)
    print(result)
    # Create 
    fig = px.bar(result, x="Age group (years)", y="Count", color="Gender")
    graphJSON = json.dumps(fig, cls=plt.utils.PlotlyJSONEncoder)
    description = 'People of gender ' + str(gender1) + ' in ' + str(state1) + ' in the year ' + str(year1) + ' compared to People of gender ' + str(gender2) + ' in ' + str(state2) + ' in the year ' + str(year2)
    header = str(gender1) + ' ' + str(state1) + ' ' + str (year1) + ' compared to ' + str(gender2) + ' ' + str(state2) + ' ' + str (year2)
    # Return the graph to our barchart template for rendering.
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