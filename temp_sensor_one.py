from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5050)

from counterfit_shims_seeed_python_dht import DHT
import time

sensor = DHT('11', 5)

while True:
    
    _,temp = sensor.read()
    print(f'Temp is {temp}C')
    time.sleep(1)