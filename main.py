from flask import Flask, request

from validators.pulse_data_validator import pulse_data_validator

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

    body: dict = request.json

    if not pulse_data_validator(body):
        response_type["error"] = "Invalid Data, try again!"
        return response_type

    return body

if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=3000)
