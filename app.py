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
#print(DATA['Zip_Code'].dtype) <-- this was int64

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
        working_zip = DATA.loc[DATA["Zip_Code"] == int(by_Zip)]
        zip_dict = working_zip.to_dict(orient="records")
        return jsonify(zip_dict)
    except Exception as error:
        print(error)
        return jsonify([f'WRONG'])
        #return jsonify([])

### some notes from AskBCS:
##  results = df.loc[df['zip'] == search_zip]

    # return jsonify({'error':"Something went horribly wrong, no one ever learned to drive a car in your area."})

  

# return the data according to city entry
@app.route("/api/v1.0/city/<by_City>")
def city(by_City = None):
    """Return the car insurance and weather data by Zip Code"""
    
    ## Need some method in here for .lower example in justice league 
            # for city in test:
    #     city_result = test['by_City'].replace(" ","").lower()

    #     if city_result == search_city:
    #         return jsonify(test)

    try:
        working_zip2 = DATA.loc[DATA["City"] == by_City]
        city_dict = working_zip2.to_dict(orient="records")
        return jsonify(city_dict)
    except Exception as error:
        print(error)
        return jsonify([])

    # return jsonify({'error':"Something went horribly wrong; Tesla overtook your city - autopilot only = no insurance necessary."})


# return the data according to state entry
@app.route("/api/v1.0/state/<by_State>")
def state(by_State = None):
    """Return the car insurance and weather data by State"""

    ## Need some method in here for .lower example in justice league 
            # for state in test:
    #     city_result = test['by_City'].replace(" ","").lower()

    #     if city_result == search_city:
    #         return jsonify(test)
    
    try:
        working_zip3 = DATA.loc[DATA["State"] == by_State]
        state_dict = working_zip3.to_dict(orient="records")
        return jsonify(state_dict)
    except Exception as error:
        print(error)
        return jsonify([])

    # return jsonify({'error':"Something went horribly wrong; your state has been taken over by murder hornets - no driving for you!"})

# return the data according to city entry
@app.route("/api/v1.0/all_data")
def all():
    """Return all the car insurance and weather data"""

## Don't know how we want to display this ...



    return(
    DATA.head()
    )


    # try:
    #     working_zip4 = DATA.loc[DATA[""] == by_State]
    #     state_dict = working_zip3.to_dict(orient="records")
    #     return jsonify(state_dict)
    # except Exception as error:
    #     print(error)
    #     return jsonify([])

    # return jsonify(DATA)


if __name__ == "__main__":
    app.run(debug=True)
