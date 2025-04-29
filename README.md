# 🔌 Remote Relay Control System

A smart system to control a physical relay remotely using MQTT and WebSocket communication. The system lets users schedule ON/OFF times through a web interface, and executes those commands via an Arduino-controlled relay.

---

## 🎯 Project Overview

This project integrates multiple technologies to create a complete remote relay control solution:

- ✅ **Web UI** for setting relay ON/OFF schedules  
- ✅ **WebSocket Server** that forwards the schedule to MQTT  
- ✅ **Python MQTT Subscriber** that listens and sends data to Arduino  
- 🤖 **Arduino** that physically controls the relay (LOW = ON, HIGH = OFF)  

---

### ⚙️ Setup Instructions

#### 1. Start the MQTT Broker
```bash
sudo systemctl start mosquitto  # or use 'mosquitto' command if not using systemd
```

#### 2. Launch the WebSocket Server
```bash
cd backend
python3 websocket_server.py
```

#### 3. Open the Web UI
Open `frontend/index.html` in your browser (use Live Server extension or Python's HTTP server).

#### 4. Start the MQTT Subscriber Script
```bash
cd subscriber
python3 mqtt_to_serial.py
```

Ensure the Arduino is connected and listening on the specified serial port.

---

### 💡 Arduino Behavior
The Arduino listens for messages in the format `HH:MM,HH:MM\n` (ON and OFF times) and activates a relay accordingly.

---

## 📸 Screenshots

**Web Dashboard**
![Web UI](/scheduler/screenshots/ui.png)
