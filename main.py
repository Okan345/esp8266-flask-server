from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/update", methods=["GET"])
def update():
    data1 = request.args.get("data1", default="0")
    data2 = request.args.get("data2", default="0")
    
    # Wuaze/000webhost siteye yönlendirme (kendi URL’ine göre değiştir)
    wuaze_url = f"http://sayac-takip.wuaze.com/update.php?data1={data1}&data2={data2}&i=1"
    try:
        requests.get(wuaze_url)
    except Exception as e:
        return f"Wuaze aktarım hatası: {e}"

    return f"Render veri alındı ve yönlendirildi: {data1}, {data2}"

@app.route("/sensor_data.txt")
def get_data():
    try:
        with open("sensor_data.txt", "r") as f:
            return f.read()
    except:
        return "0,0"

@app.route("/status")
def status():
    return "OK", 200

@app.route("/")
def home():
    return "Render sunucu çalışıyor"
