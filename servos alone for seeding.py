import RPi.GPIO as GPIO
import time
bucket_servo_pin=13
arm_servo_pin=11
seed_servo_pin=15
GPIO.setmode(GPIO.BOARD)
GPIO.setup(bucket_servo_pin,GPIO.OUT)
GPIO.setup(arm_servo_pin,GPIO.OUT)
GPIO.setup(seed_servo_pin,GPIO.OUT)
arm_servo=GPIO.PWM(arm_servo_pin,50)
bucket_servo=GPIO.PWM(bucket_servo_pin,50)
seed_servo=GPIO.PWM(seed_servo_pin,50)

arm_servo.start(12.5)
bucket_servo.start(5)
seed_servo.start(7)
while(True):
    time.sleep(1.5)
    arm_servo.ChangeDutyCycle(8)
    time.sleep(1.5)
    bucket_servo.ChangeDutyCycle(9)
    time.sleep(1.5)
    arm_servo.ChangeDutyCycle(4)
    time.sleep(0.1)
    bucket_servo.ChangeDutyCycle(6)
    time.sleep(1.5)
    seed_servo.ChangeDutyCycle(9)
    time.sleep(0.5)
    seed_servo.ChangeDutyCycle(7)
    time.sleep(1.5)
    arm_servo.ChangeDutyCycle(8)
    time.sleep(.01)
    bucket_servo.ChangeDutyCycle(2)
    time.sleep(1.5)
    arm_servo.ChangeDutyCycle(12.5)
    #time.sleep(1)
    bucket_servo.ChangeDutyCycle(5)
    time.sleep(2)
