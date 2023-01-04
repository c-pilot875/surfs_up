# import core dependencies
import datetime as dt
import numpy as np
import pandas as pd

#import SQLAlchemy dependencies
import sqlalchemy 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# import flask dependencies
from flask import Flask, jsonify

# set up databse engine for Flask application
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database into classes
Base = automap_base()

Base.prepare(engine, reflect=True)

# Save refrences to each table using new variable name
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session link from Python to database
session = Session(engine)

# Define app fro Flask
app = Flask(__name__)

#import app 

print("example __name__ = %s", __name__)

if __name__ == "__main__":
    print("example is being run directly")

else:
    print("example is being imported")

# Create app routes, define welcome route - do not separate.

@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temps/start/end
    ''')

if __name__ == '__main__':
    app.run()
#@app.route("/api/v1.0/precipitation")
#def precipitation():
    #prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #precipitation = session.query(Measurement.date, Measurement.prcp).\
        #filter(Measurement.date >= prev_year).all()
    #precip = {date: prcp for date, prcp in precipitation}
    #return jsonify(precip)




    