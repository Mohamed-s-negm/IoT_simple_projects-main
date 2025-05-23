from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5050)

from counterfit_shims_picamera.camera import PiCamera
import io

camera = PiCamera()
camera.resolution = (640, 480)
camera.rotation = 0

image = io.BytesIO()
camera.capture(image, 'jpeg')
image.seek(0)

with open('image.jpg', 'wb') as image_file:
    image_file.write(image.read())