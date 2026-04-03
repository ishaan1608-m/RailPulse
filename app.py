from flask import Flask, request, jsonify, send_file, Response
from flask_cors import CORS
import urllib.request

app = Flask(__name__)
CORS(app)

# ── Pi camera stream URL (the separate Pi stream server) ──────
PI_STREAM_URL = "http://10.154.32.188:5000/"

# ── ESP32 data store ──────────────────────────────────────────
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

# ── Proxy the Raspberry Pi MJPEG camera stream ────────────────
# The browser fetches /video_feed from this Flask server.
# Flask opens a connection to the Pi stream and forwards the
# raw MJPEG bytes, avoiding any cross-origin or mixed-content
# issues in the browser.
@app.route("/video_feed")
def video_feed():
    def generate():
        try:
            req = urllib.request.urlopen(PI_STREAM_URL, timeout=10)
            while True:
                chunk = req.read(4096)
                if not chunk:
                    break
                yield chunk
        except Exception as e:
            print(f"Camera proxy error: {e}")
            return

    # Pass the multipart content-type through from the Pi stream
    content_type = "multipart/x-mixed-replace; boundary=frame"
    try:
        upstream = urllib.request.urlopen(PI_STREAM_URL, timeout=5)
        ct = upstream.headers.get("Content-Type", content_type)
        upstream.close()
    except Exception:
        ct = content_type

    return Response(generate(), mimetype=ct)

# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
