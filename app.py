
import numpy as np


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
station = Base.classes.station


session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
last_date = '2016-08-23'
@app.route("/")
def Home_Page():
    """List all available api routes."""
    return (
        f"Welcome to Hawaii weather API<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    results = session.query(Measurement.date,func.avg(Measurement.prcp)).filter(Measurement.date >= last_date).group_by(Measurement.date).all()

    all_data = list(np.ravel(results))
    return jsonify(all_data)


@app.route("/api/v1.0/stations")
def station_list():
    station_results = session.query(station.name,station.station).all()
    
    all_station = list(np.ravel(station_results))
    return jsonify(all_station)

@app.route("/api/v1.0/tobs")
def temp_list():
    temp_results = session.query(Measurement.date,Measurement.station,Measurement.tobs).\
    filter(Measurement.date >= '2017-08-23').all()
    
    all_temp = list(np.ravel(temp_results))
    return jsonify(all_temp)


@app.route("/api/v1.0/start/end")
def start_date_list(start_date,end_date):
    date_results = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
    filter(Measurement.date >= start_date).\
    filter(Measurement.date <= end_date).all()

    all_date = list(np.ravel(date_results))
    return jsonify(all_date)

if __name__ == "__main__":
    app.run(debug=True)

