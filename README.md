# 🚆 RailPulse — Intelligent Railway Track Monitoring System

RailPulse is a **real-time smart railway monitoring system** that combines **acoustic sensing, vibration analysis, computer vision, and IoT** to detect track faults and obstacles.

It uses an **ESP32 + Raspberry Pi 4 hybrid architecture** to identify:

* 🔊 Internal cracks (via vibration & acoustic analysis)
* 👁️ Visible cracks (via camera + computer vision)
* 🐄 Animal intrusion on tracks (via AI detection)

---

## 🔥 Key Features

* 🎯 **Internal Crack Detection**

  * Uses vibration data from IMU sensors
  * Detects hollow sections & structural weakness

* 📸 **Visual Fault Detection**

  * Raspberry Pi Camera scans tracks
  * Detects visible cracks using computer vision

* 🐾 **Animal Detection System**

  * AI-based detection of animals on railway tracks
  * Prevents accidents proactively

* 📡 **Real-Time Alerts**

  * Sends alerts via Telegram
  * Includes:

    * 📍 GPS location
    * 🖼️ Captured image
    * ⚠️ Fault type

* 📊 **Live Dashboard**

  * Real-time monitoring UI
  * Includes:

    * Track map 📍
    * Health profile 📈
    * FFT analysis 📊
    * Event logs 📋

---

## 🧠 System Architecture

```
ESP32 (Sensors) ──► WiFi ──► Flask Backend (Laptop / Pi)
        │                          │
        │                          ▼
   IMU + Vibration         Web Dashboard (Live UI)
        │
        ▼
Raspberry Pi 4 (Camera + AI)
        │
        ▼
Telegram Alerts (Image + GPS + Fault)
```

---

## 🛠️ Tech Stack

### 🔌 Hardware

* ESP32
* Raspberry Pi 4
* MPU6050 (IMU Sensor)
* SW-420 Vibration Sensor
* NEO-6M GPS Module
* Raspberry Pi Camera Module

### 💻 Software

* Python (Flask Backend)
* JavaScript (Dashboard UI)
* OpenCV (Computer Vision)
* Chart.js (Graphs)
* Leaflet.js (Map Visualization)

---

## 🚀 How It Works

### 1. Data Collection

* ESP32 reads:

  * Vibration data (IMU + SW420)
  * GPS location

### 2. Processing

* Vibration patterns analyzed for internal cracks
* Raspberry Pi processes camera feed for:

  * Animal detection
  * Surface cracks

### 3. Transmission

* Data sent to backend via WiFi

### 4. Visualization

* Dashboard updates in real-time:

  * Graphs
  * Map
  * Alerts

### 5. Alert System

* If fault detected:

  * Telegram bot sends:

    * 📍 Location
    * 📸 Image
    * ⚠️ Alert message

---

## 📸 Screenshots

> Add your dashboard screenshots here

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/railpulse.git
cd railpulse
```

---

### 2. Install Backend Dependencies

```bash
pip install flask flask-cors
```

---

### 3. Run Backend

```bash
python app.py
```

---

### 4. Open Dashboard

```bash
http://localhost:8000/index.html
```

---

### 5. Configure ESP32

Update your ESP32 code:

```cpp
const char* serverURL = "http://YOUR_IP:5000/api/esp32/data";
```

---

## 🧪 Testing

You can simulate ESP32 data:

```bash
curl -X POST http://localhost:5000/api/esp32/data ^
-H "Content-Type: application/json" ^
-d "{\"verdict\":\"CRITICAL\",\"features\":{\"mpu\":0.3,\"sw420\":0.2,\"combined\":0.35}}"
```

---

## 📡 Telegram Alert Example

```
⚠️ RAILWAY ALERT

Type: Animal Detected
Location: 28.6139, 77.2090
Status: CRITICAL

📸 Image Attached
```

---

## 🎯 Future Improvements

* 🤖 AI-based predictive maintenance
* ☁️ Cloud dashboard deployment
* 📱 Mobile app integration
* 🔋 Solar-powered rover
* 🛰️ GSM-based alert system

---

## 👨‍💻 Contributors

* Ishaan Maheshwari
* sidhu kumar
* Team RailPulse

---

## 🏆 Inspiration

RailPulse aims to solve **real-world railway safety challenges** by combining:

* Embedded Systems
* AI
* IoT
* Robotics

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 💡 Tagline

> *"Listening to rails before they break."*
