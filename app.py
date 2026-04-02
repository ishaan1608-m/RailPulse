from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

latest_data = {}

@app.route("/")
def home():
    return send_file('index.html')

@app.route("/api/esp32/data", methods=["POST"])
def receive_data():
    global latest_data
    latest_data = request.json
    print("Received:", latest_data)
    return jsonify({"message": "Data received"})

@app.route("/api/esp32/data", methods=["GET"])
def send_data():
    return jsonify(latest_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)