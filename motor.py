import time
import wiringpi
wiringpi.wiringPiSetupGpio()

#wiringpi.pinMode(2, wiringpi.GPIO.PWM_OUTPUT) 
#wiringpi.digitalWrite(2, 1)
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)
delay_period= .1
while True:

    for pulse in range(50, 250, 1):
            wiringpi.pwmWrite(18, pulse)
            time.sleep(delay_period)
    for pulse in range(250, 50, -1):
            wiringpi.pwmWrite(18, pulse)
            time.sleep(delay_period)

