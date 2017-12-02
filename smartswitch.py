import time
import urllib2
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(02,GPIO.OUT)
GPIO.setup(03,GPIO.OUT)

light = GPIO.input(02)
fan = GPIO.input(03)
while True:
    response = urllib2.urlopen('https://listenuswitch.eu-gb.mybluemix.net/status?light='+str(light)+'&fan='+str(fan)).read()
    light = GPIO.input(02)
    fan = GPIO.input(03)
    print response
    print 'light='+str(light)
    print 'fan  ='+str(fan)
    
    if (response== '1'):
        GPIO.output(02,GPIO.HIGH)
        GPIO.output(03,GPIO.HIGH)
    elif (response== '2'):
        GPIO.output(02,GPIO.LOW)
        GPIO.output(03,GPIO.LOW)
    elif (response== '3'):
        GPIO.output(02,GPIO.HIGH)
    elif (response== '4'):
        GPIO.output(02,GPIO.LOW)
    elif (response== '5'):
        GPIO.output(03,GPIO.HIGH)
    elif (response== '6'):
        GPIO.output(03,GPIO.LOW)
