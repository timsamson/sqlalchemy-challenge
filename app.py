
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()
measurement = Base.classes.measurement
station = Base.classes.station

app = Flask(__name__)


#@app.route("/")
#def home():

@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)
    output = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date > '2016-08-22').all()
    session.close()

    prcp = []
    for row in output:
        new_dict = {}
        new_dict[row[0]]= row[1]
        prcp.append(new_dict)
    return jsonify(prcp)

@app.route('/api/v1.0/<start>')
def app_start(start):
    session = Session(engine)
    output = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
        filter(measurement.date > start).all()
    session.close

    temp = []
    for row in output:
        new_dict = {}
        new_dict['tmin']= row[0]
        new_dict['tmax']= row[1]
        new_dict['tavg']= row[2]
        temp.append(new_dict)
    return jsonify(temp)

@app.route('/api/v1.0/<start>/<end>')
def app_start_end(start,end):
    session = Session(engine)
    output = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
        filter(measurement.date > start).filter(measurement.date < end).all()
    session.close

    temp = []
    for row in output:
        new_dict = {}
        new_dict['tmin']= row[0]
        new_dict['tmax']= row[1]
        new_dict['tavg']= row[2]
        temp.append(new_dict)
    return jsonify(temp)










if __name__ == "__main__":
    app.run(debug=True)