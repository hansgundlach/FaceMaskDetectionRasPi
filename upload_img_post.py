import os
import requests
import json
import wiringpi
from io import BytesIO
from time import sleep
from picamera import PiCamera
url = 'http://192.168.0.31:8000'
#data = open('0.jpg', 'rb').read()
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)
delay_period= .001


stream = BytesIO()
camera = PiCamera()
camera.start_preview()
sleep(2)
for i in list(range(2)):
    camera.capture(stream, 'jpeg')
    stream.seek(0)
    data = stream.read()
    r = requests.post(url,data=data)
    lst_str = r.content.decode('utf-8')
    lst = json.loads(lst_str)
    #print(lst)
    all_masked  = sum([x[0] for x in lst])
    if (all_masked == 0):
        for pulse in range(50, 250, 1):
            wiringpi.pwmWrite(18, pulse)
            sleep(delay_period)
        sleep(3)
        for pulse in range(250, 50, -1):
            wiringpi.pwmWrite(18, pulse)
            sleep(delay_period)

    stream = BytesIO()
    sleep(5)

