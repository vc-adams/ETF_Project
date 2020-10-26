## GROUP 1 Flask App

import numpy as np
import pandas as pd
import os
import csv
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#...if we pull from a database....
#################################################
# Database Setup
#################################################
# engine = create_engine("sqlite:///Resources/... .sqlite")

# reflect an existing database into a new model
# Base = automap_base()
# Base.prepare(engine, reflect=True)

# Save reference to the table
# TABLE = Base.classes.WHATEVERWECALLTHIS

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

file_path = os.path.join("Resources", "Temp_Average_Auto_Insurance_Data.csv")
DATA = pd.read_csv(file_path)
print(DATA['Zip_Code'].dtype)

#################################################
# Flask Routes
#################################################
# List all available api routes for the user
@app.route("/")
def welcome():
    """Return all routes/display options available"""
    return (
        f"Welcome! Utilize this API to find Car Insurance Data by Area<br/>"
        f"Available searches are as follows:<br/>"
        f"Enter a Zip@          /api/v1.0/by_zip<br/>"
        f"Enter a City@         /api/v1.0/by_city<br/>"
        f"Enter a State@        /api/v1.0/by_state<br/>"
        f"Or, return all data@  /api/v1.0/all_data<br/>"
    )

# return the data according to zip entry
@app.route("/api/v1.0/zipcode/<by_Zip>")
def zip(by_Zip = None):
    """Return the car insurance and weather data by zip code"""
    try:
        new_df = DATA.loc[DATA["Zip_Code"] == int(by_Zip)]
        new_dict = new_df.to_dict(orient="records")
        return jsonify(new_dict)
    except Exception as e:
        print(e)
        return jsonify([])

### some notes from AskBCS:
##  results = df.loc[df['zip'] == search_zip]







    # search_zip = by_Zip
    # zip_search_list = []

    # for zip in test:
    #     zipcode_result = test['by_Zip...or whatever we call the zip column']
    #         #.replace(" ","").lower()
    #     zip_test_dict = {}

    #     if zipcode_result == search_zip:
    #         #return jsonify(zip)

    #         zip_test_dict['min temp']= zip.min
    #         zip_test_dict['max temp']= zip.max
    #         zip_test_dict['average temp']= zip.avg
    #         zip_search_list.append(zip_test_dict)

    #         return jsonify(zip_search_list)

    # return jsonify({'error':"Something went horribly wrong, no one ever learned to drive a car in your area."})




    #################
        # if end:

        # init_query = session.query(func.min(measurement.tobs).label('min'), func.max(measurement.tobs).label('max'), func.avg(measurement.tobs).label('avg'))
        # results_end = init_query.filter(measurement.date >= start).filter(measurement.date <= end).all()

        # else:

        # init_query = session.query(func.min(measurement.tobs).label('min'), func.max(measurement.tobs).label('max'), func.avg(measurement.tobs).label('avg'))
        # results_end = init_query.filter(measurement.date >= start).all()

        # return jsonify(hawaii_measurements_dates) 
    #################



### if we wanted to combine all available data within the flask app... we could utilize he Hawaii example..
    # hawaii_measurements_dates = []
    # for row in results_end:
    #     measurements = {}
    # # here, utlizing my orig earlier idea from the Titanic example
    #     measurements['min temp']= row.min
    #     measurements['max temp']= row.max
    #     measurements['average temp']= row.avg
    #     hawaii_measurements_dates.append(measurements) 

    # return jsonify(hawaii_measurements_dates)   



# return the data according to city entry
@app.route("/api/v1.0/<by_City>")
def city(by_City = None):
    """Return the car insurance and weather data by Zip Code"""

    file_path = os.path.join("Resources", "Temp_Average_Auto_Insurance_Data.csv")
    data = pd.read_csv(file_path)

    # with open("..", "Resources", "Temp_Average_Auto_Insurance_Data.csv") as csv_file:
    #     data = csv.reader(csv_file, delimiter=',')
    #     #first_line = True
    search_city = by_City
    city_list = []
    for row in data:
        if data['City'] == search_city:
            city_list.append({
            "State": row[0],
            "Zip_Code": row[1],
            "City": row[2],
            "Avg Rate":row[3]
            })
            print(city_list)
        else:
            print('No match for this City')
        #return render_template("index.html", places=places)
    return zip_list
    # search_city = by_City

    # for city in test:
    #     city_result = test['by_City']
    #         #.replace(" ","").lower()

    #     if city_result == search_city:
    #         return jsonify(test)

    # return jsonify({'error':"Something went horribly wrong; Tesla overtook your city - autopilot only = no insurance necessary."})

# return the data according to city entry
@app.route("/api/v1.0/<by_State>")
def state(by_State = None):
    """Return the car insurance and weather data by State"""

    search_State = by_State

    for state in test:
        state_result = test['by_State']
            #.replace(" ","").lower()

        if state_result == search_state:
            return jsonify(test)

    return jsonify({'error':"Something went horribly wrong; your state has been taken over by murder hornets - no driving for you!"})

# return the data according to city entry
@app.route("/api/v1.0/all_data")
def all():
    """Return all the car insurance and weather data"""

    file_path = os.path.join("Resources", "Temp_Average_Auto_Insurance_Data.csv")
    data = pd.read_csv(file_path)

    return jsonify(data)



if __name__ == "__main__":
    app.run(debug=True)
