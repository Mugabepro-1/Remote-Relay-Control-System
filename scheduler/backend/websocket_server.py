import asyncio
import websockets
import json
import subprocess

MQTT_TOPIC = "light/schedule"
BROKER = "localhost"
PORT = 1883

async def handle_connection(websocket):
    async for message in websocket:
        print("Received from frontend:", message)
        data = json.loads(message)
        on_time = data.get("on")
        off_time = data.get("off")

        mqtt_payload = json.dumps({"on": on_time, "off": off_time})

        subprocess.run([
            "mosquitto_pub",
            "-h", BROKER,
            "-p", str(PORT),
            "-t", MQTT_TOPIC,
            "-m", mqtt_payload
        ])

        print(f"Published to MQTT topic '{MQTT_TOPIC}': {mqtt_payload}")

async def main():
    async with websockets.serve(handle_connection, "0.0.0.0", 8765):
        print("WebSocket server listening on ws://0.0.0.0:8765")
        await asyncio.Future()  

if __name__ == "__main__":
    asyncio.run(main())