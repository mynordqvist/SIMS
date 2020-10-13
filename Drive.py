from adafruit_motorkit import MotorKit
import time
import RPi.GPIO as GPIO

#Drive forwards
def Start():
    
    kit = MotorKit()
    kit.motor1.throttle = 0.8
    kit.motor2.throttle = 0.8
    kit.motor3.throttle = 0.8
    kit.motor4.throttle = 0.8

#Stop
def Stop():
    kit = MotorKit()
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0
    time.sleep(2)
    
#Turn right    
def Turn():
    kit = MotorKit()
    kit.motor1.throttle = 0.8
    kit.motor3.throttle = 0.8
    kit.motor2.throttle = -0.8
    kit.motor4.throttle = -0.8
    time.sleep(0.5)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0
    
def Sensor_init():
    GPIO.setwarnings(False) #Disable warnings

    #Set ports
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.IN)
    GPIO.setup(24, GPIO.IN)
    GPIO.setup(25, GPIO.IN)