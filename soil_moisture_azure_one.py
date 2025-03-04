from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5050)

import time
from counterfit_shims_grove.adc import ADC
from counterfit_shims_grove.grove_relay import GroveRelay
from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse
import json

connection_string = "HostName=soil-moisture-sensor-msen-project-1.azure-devices.net;DeviceId=soil-moisture-sensor;SharedAccessKey=ANcbIYnpJDREkXK/Fad+8+K0kPxZkQgwKqyxtTHXKVE="
device_client = IoTHubDeviceClient.create_from_connection_string(connection_string)

print('Connecting')
device_client.connect()
print('Connected')

adc = ADC()
relay = GroveRelay(14)

def handle_method_request(request):
    print("Direct method received - ", request.name)

    if request.name == "relay_on":
        relay.on()
    elif request.name == "relay_off":
        relay.off()    
    
    method_response = MethodResponse.create_from_method_request(request, 200)
    device_client.send_method_response(method_response)

device_client.on_method_request_received = handle_method_request



while True:
    soil_moisture = adc.read(12)
    print("soil_moisture: ", soil_moisture)
    telemetry = json.dumps({'soil_moisture' : soil_moisture})
    print("Sending telemetry ", telemetry)

    message = Message(json.dumps({ 'soil_moisture': soil_moisture }))
    device_client.send_message(message)
    time.sleep(5)
