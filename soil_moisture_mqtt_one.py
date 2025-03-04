from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5050)

import time
from counterfit_shims_grove.adc import ADC
from counterfit_shims_grove.grove_relay import GroveRelay
import json
import paho.mqtt.client as mqtt

adc = ADC()
relay = GroveRelay(5)

id = 'wwwwaaaaattttteeeeerrrrr123456'

client_telemetry_topic = id + '/telemetry'
server_command_topic = id + '/commands'
client_name = id + 'soilmoisturesensor_client'

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_name)
mqtt_client.connect('test.mosquitto.org')

mqtt_client.loop_start()

def handle_command(client, userdata, message, rc=None):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)

    if payload['relay_on']:
        relay.on()
    else:
        relay.off()

mqtt_client.subscribe(server_command_topic)
mqtt_client.on_message = handle_command

while True:
    soil_moisture = adc.read(10)
    print("Soil moisture:", soil_moisture)

    mqtt_client.publish(client_telemetry_topic, json.dumps({'soil_moisture' : soil_moisture}))

    time.sleep(10)