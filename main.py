from flask import Flask, request, render_template
from validators.pulse_data_validator import pulse_data_validator
from ml.knn import KNN
import pandas as pd
import pymongo
import time

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://aditya:aditya@cluster0.jnyunbc.mongodb.net/?retryWrites=true&w=majority")
db = client['device_data']

@app.route('/')
def home():
    return """
    <div>
        <h1>PR1101: Health Insight Monitor</h1>
        <p>This is the API used by our IoT enabled health insight monitor</p>
        <p>Endpoint</p>
        <ul>
            <li>GET: /</li>
            <li>POST: /heart_pulse_data</li>
            <li>GET: /get_insights</li>
        </ul>
    </div>
    """

@app.route('/data')
def data():
    data = db.get_collection('pulse_rate').find().limit(10).sort({"timestamp": 1})
    return render_template('data.html', data=data)
    

@app.route("/heart_pulse_data", methods = ['POST'])
def heart_pulse_data():
    body = request.json
    
    heart_pulse = body['heart_pulse']
    time = body['timestamp']

    if heart_pulse <= 35 or heart_pulse >= 160:
        return 'OUTLIER'

    db.get_collection('pulse_rate').insert_one({'heart_pulse': heart_pulse, 'timestamp': time})
    return 'OK'

@app.route("/ml")
def ML():
    pass

if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=3005)
