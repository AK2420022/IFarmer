import RPi.GPIO as GPIO
import time
pin_dude=15
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_dude,GPIO.OUT)
#GPIO.setup(11,GPIO.OUT)
servo=GPIO.PWM(pin_dude,50)
#servo1=GPIO.PWM(11,50)
#servo1.start(4)
while (True):
    mama=float(input("Enter the duty cycle: "))
    servo.start(mama)
    time.sleep(2)

    
