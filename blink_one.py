from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5050)

from counterfit_shims_grove.grove_led import GroveLed
import time

led = GroveLed(13)

while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)