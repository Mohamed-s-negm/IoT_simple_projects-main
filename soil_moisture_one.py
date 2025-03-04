from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5050)

import time
from counterfit_shims_grove.adc import ADC
from counterfit_shims_grove.grove_led import GroveLed
from counterfit_shims_grove.grove_relay import GroveRelay

adc = ADC()
led_red = GroveLed(13)
relay_blue = GroveRelay(14)
led_green = GroveLed(15)

while True:
    soil_moisture = adc.read(12)
    print("Soil moisture: ", soil_moisture)
    if soil_moisture > 600:
        led_red.on()
        time.sleep(1)
        print("Too much water!")
    elif soil_moisture < 400:
        relay_blue.on()
        time.sleep(1)
        print("Need more water!")
    else:
        led_green.on()
        time.sleep(1)
        print("Satisfiedddddddd!")
    
    led_red.off()
    relay_blue.off()
    led_green.off()
    time.sleep(1)