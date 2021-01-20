#!/usr/bin/env python3

"""
AUTHOR: ShuyaTanaka
DESCRIPTION: Operate the LED
LICENSE: GPL v3.0

"""
import RPi.GPIO as GPIO
import time

led_one = 23
led_two = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_one, GPIO.OUT)
GPIO.setup(led_two, GPIO.OUT)

for i in range(20):
        GPIO.output(led_one, GPIO.HIGH)
        time.sleep(0.15)
        GPIO.output(led_one, GPIO.LOW)
        time.sleep(0.15)

for i in range(50):
        GPIO.output(led_two, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(led_two, GPIO.LOW)
        time.sleep(0.05)


GPIO.cleanup()
