import paho.mqtt.client as mqtt
import serial
import json
import threading
import time
from datetime import datetime

SERIAL_PORT = "/dev/ttyUSB0"  # Change if needed, e.g. "COM3" on Windows
BAUD_RATE = 9600
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "light/schedule"

# Initialize serial communication with Arduino
try:
    arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to Arduino on {SERIAL_PORT}")
except Exception as e:
    print(f"Failed to connect to Arduino: {e}")
    exit(1)

scheduled_on = None
scheduled_off = None

def time_loop():
    global scheduled_on, scheduled_off
    while True:
        now = datetime.now().strftime("%H:%M")
        if scheduled_on == now:
            print("Turning light ON")
            arduino.write(b'1')
        elif scheduled_off == now:
            print("Turning light OFF")
            arduino.write(b'0')
        time.sleep(30)  # Check every 30 seconds

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code", rc)
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    global scheduled_on, scheduled_off
    try:
        payload = json.loads(msg.payload.decode())
        scheduled_on = payload.get("on")
        scheduled_off = payload.get("off")
        print(f"Schedule received - ON: {scheduled_on}, OFF: {scheduled_off}")
    except Exception as e:
        print("Failed to process message:", e)

# Start time-checking thread
threading.Thread(target=time_loop, daemon=True).start()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()
