from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route("/update", methods=["GET"])
def update():
    data1 = request.args.get("data1", default="0")
    data2 = request.args.get("data2", default="0")

    # Wuaze (000Webhost) adresine yönlendirme (kendi URL'ine göre değiştir)
    wuaze_url = f"http://sayac-takip.wuaze.com/update.php?data1={data1}&data2={data2}&i=1"

    try:
        # Tarayıcı gibi davranması için User-Agent başlığı eklendi
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(wuaze_url, headers=headers, timeout=5)
        response.raise_for_status()  # HTTP hatalarını yakalar
    except Exception as e:
        return f"Wuaze aktarım hatası: {e}"

    return f"Render veri alındı ve wuaze'e yönlendirildi: {data1}, {data2}"

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
    return "Render sunucu çalışıyor."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
