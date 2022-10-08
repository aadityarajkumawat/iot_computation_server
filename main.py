from flask import Flask, request

from validators.pulse_data_validator import pulse_data_validator

app = Flask(__name__)

@app.route("/heart_pulse_data")
def heart_pulse_data():
    response_type = {"data": {}, "error": None}

    body: dict = request.json

    if not pulse_data_validator(body):
        response_type["error"] = "Invalid Data, try again!"
        return response_type

    return body
