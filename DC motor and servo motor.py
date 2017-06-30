#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 17:40:07 2017

@author: rocheparadox
"""
import RPi.GPIO as GPIO
import time

left_wheels_enable=1
right_wheels_enable=2
left_wheels_forward=3
right_wheels_forward=4
right_wheels_backward=5
left_wheels_backward=6
sprayer_enable=7
sprayer_activate=8
hand_servo_pin=9
bucket_servo_pin=10
seed_servo_pin=11


def Init_gpio():
    global hand_servo,seed_servo,bucket_servo
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(left_wheels_enable,GPIO.OUT)
    GPIO.setup(right_wheels_enable,GPIO.OUT)
    GPIO.setup(right_wheels_forward,GPIO.OUT)
    GPIO.setup(left_wheels_forward,GPIO.OUT)
    GPIO.setup(right_wheels_backward,GPIO.OUT)
    GPIO.setup(left_wheels_backward,GPIO.OUT)
    GPIO.setup(sprayer_enable,GPIO.OUT)
    GPIO.setup(sprayer_activate,GPIO.OUT)
    GPIO.setup(hand_servo_pin,GPIO.OUT)
    GPIO.setup(bucket_servo_pin,GPIO.OUT)
    GPIO.setup(seed_servo_pin,GPIO.OUT)
    hand_servo=hand_servo_pin.pwm(50)
    seed_servo=seed_servo_pin.pwm(50)
    bucket_servo=bucket_servo.pwm(50)

def servo_position():
    global hand_servo,seed_servo,bucket_servo
    hand_servo.start(7.5)
    seed_servo.start(7.5)
    bucket_servo.start(7.5)
    
    
def bot_forward():
    GPIO.output(left_wheels_enable,True)
    GPIO.output(right_wheels_enable,True)
    GPIO.output(right_wheels_forward,True)
    GPIO.output(left_wheels_forward,True)
    GPIO.output(right_wheels_backward,False)
    GPIO.output(left_wheels_backward,False)
    
def bot_backward():
    GPIO.output(left_wheels_enable,True)
    GPIO.output(right_wheels_enable,True)
    GPIO.output(right_wheels_forward,False)
    GPIO.output(left_wheels_forward,False)
    GPIO.output(right_wheels_backward,True)
    GPIO.output(left_wheels_backward,True)
    
def bot_stop():
    GPIO.output(left_wheels_enable,False)
    GPIO.output(right_wheels_enable,False)
    
def sprayer_start():
    GPIO.output(sprayer_enable,True)
    GPIO.output(sprayer_activate,True)    

def sprayer_stop():
    GPIO.output(sprayer_enable,False)
    GPIO.output(sprayer_activate,False)
    
def seeding_process():
    servo_position()
    bot_forward()
    time.sleep(10)
    bot_stop()
    hand_servo.ChangeDutyCycle(2.5)
    time.sleep(.25)
    bucket_servo.ChangeDutyCycle(2.5)
    time.sleep(.25)
    hand_servo.ChangeDutyCycle(12.5)
    time.sleep(.25)
    seed_servo.ChangeDutyCycle(2.5)
    time.sleep(.25)
    seed_servo.ChangeDutyCycle(7.5)
    time.sleep(1)
    bucket_servo.ChangeDutyCycle(2.5)
    time.sleep(.25)
    hand_servo.ChangeDutyCycle(2.5)

def sprayer_process():
    bot_forward()
    time.sleep(10)
    bot_stop()
    time.sleep(0.10)
    sprayer_start()
    time.sleep(5)
    sprayer_()
    
Init_gpio()
servo_position()
while(True):
    seeding_process()
    
    
