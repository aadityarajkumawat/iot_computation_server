from flask import Flask, request
from validators.pulse_data_validator import pulse_data_validator
from ml.knn import KNN
import pandas as pd

app = Flask(__name__)

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

@app.route("/heart_pulse_data")
def heart_pulse_data():
    response_type = {"data": {}, "error": None}

    body = request.json

    df = pd.read_csv('./train.csv')

    a = (df.iloc[[-1]])
    last_idx = (a['sno'].sum()) + 1

    f = open('./train.csv', 'a')
    f.write(str(last_idx) + ',' + str(body['heart_pulse']) + ',0,6\n')
    f.close()

    return 'OK'

@app.route("/ml")
def ML():
    pass

if __name__ == "__main__":
    from waitress import serve
    # serve(app, host='0.0.0.0', port=3000)
    app.run()
