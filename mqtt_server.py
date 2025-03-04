import json
import time

import paho.mqtt.client as mqtt

id = 'cbb34c1d-fc8a-4a66-9072-88b93ab9b5b4'

client_telemetry_topic = id + '/telemetry'
server_command_topic = id + '/commands'
client_name = id + 'nightlight_server'

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_name)
mqtt_client.connect('test.mosquitto.org')

mqtt_client.loop_start()

def handle_telemetry(client, userdata, message, reason_code=None):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)
    
    command = { 'led_on' : payload['light'] < 500}
    print("Sending message:", command)
    
    client.publish(server_command_topic, json.dumps(command))

mqtt_client.subscribe(client_telemetry_topic)
mqtt_client.on_message = handle_telemetry

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(client_telemetry_topic)

mqtt_client.on_connect = on_connect

mqtt_client.loop_start()

while True:
    time.sleep(2)