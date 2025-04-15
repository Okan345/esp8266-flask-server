from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/update")
def update():
    data1 = request.args.get("data1", "0")
    data2 = request.args.get("data2", "0")
    with open("sensor_data.txt", "w") as f:
        f.write(f"{data1},{data2}")
    return f"Veri alındı: {data1}, {data2}"

@app.route("/sensor_data.txt")
def data():
    try:
        with open("sensor_data.txt", "r") as f:
            return f.read()
    except:
        return "0,0"

@app.route("/")
def home():
    return "ESP8266 Render Sunucusu"
