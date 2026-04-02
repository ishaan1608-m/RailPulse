import requests
import time
import random
import math

URL = "http://localhost:5000/api/esp32/data"

i = 0
lat = 17.3850
lng = 78.4867

print("Starting test data sender... Press Ctrl+C to stop.")
print(f"Sending to: {URL}\n")

while True:
    combined = random.uniform(0.05, 0.95)

    if combined > 0.70:
        verdict = "CRITICAL"
    elif combined > 0.35:
        verdict = "MODERATE"
    else:
        verdict = "HEALTHY"

    lat += random.uniform(-0.002, 0.002)
    lng += random.uniform(-0.002, 0.002)

    fft = [round(abs(math.sin(j * 0.3 + i * 0.1)) * random.uniform(0.3, 1.8), 4) for j in range(64)]

    payload = {
        "verdict": verdict,
        "features": {
            "combined": round(combined, 4)
        },
        "gps": {
            "latitude":  round(lat, 6),
            "longitude": round(lng, 6),
            "satellites": random.randint(5, 12)
        },
        "fftMagnitudes": fft,
        "deviceId": "TEST-BOT-01",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }

    try:
        r = requests.post(URL, json=payload, timeout=3)
        score = round(combined * 100)
        print(f"[#{i+1}] {verdict:<10} | score={score:<3} | lat={round(lat,5)} lng={round(lng,5)} | HTTP {r.status_code}")
    except requests.exceptions.ConnectionError:
        print(f"[#{i+1}] ERROR — Cannot connect. Is Flask running? (python app.py)")
    except Exception as e:
        print(f"[#{i+1}] ERROR — {e}")

    i += 1
    time.sleep(2)