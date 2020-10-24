## GROUP 1 Flask App

import numpy as np
import os
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
        f"Enter a Zip@          /api/v1.0/<by_ZIP><br/>"
        f"Enter a City@         /api/v1.0/<by_city><br/>"
        f"Enter a State@        /api/v1.0/<by_state><br/>"
        f"Or, return all data@  /api/v1.0/all_data<br/>"
    )

# return the data according to zip entry
@app.route("/api/v1.0/<by_Zip>")
def zip(by_Zip = None):
    """Return the car insurance and weather data by zip code"""
        
    search_zip = test.replace(" ","").lower()

    for zip in test:
        search_zip = character['real_name'].replace(" ","").lower()

        if real_name_lowered == search_zip:
            return jsonify(by_zip)

    return jsonify({'error':"Something went horribly wrong, no one must drive a car in your area"})


    #################
        if end:

        init_query = session.query(func.min(measurement.tobs).label('min'), func.max(measurement.tobs).label('max'), func.avg(measurement.tobs).label('avg'))
        results_end = init_query.filter(measurement.date >= start).filter(measurement.date <= end).all()

        else:

        init_query = session.query(func.min(measurement.tobs).label('min'), func.max(measurement.tobs).label('max'), func.avg(measurement.tobs).label('avg'))
        results_end = init_query.filter(measurement.date >= start).all()

        return jsonify(hawaii_measurements_dates) 
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


# return the data according to city entry
@app.route("/api/v1.0/<by_State>")
def state(by_State = None):
    """Return the car insurance and weather data by State"""


# return the data according to city entry
@app.route("/api/v1.0/all_data")
def all():
    """Return all the car insurance and weather data"""

    return(test)



if __name__ == "__main__":
    app.run(debug=True)
