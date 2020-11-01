from adafruit_motorkit import MotorKit
import time
import RPi.GPIO as GPIO
import globals

#Drive forwards
def Start():
    
    kit = MotorKit()
    kit.motor1.throttle = 0.6
    kit.motor2.throttle = 0.6
    kit.motor3.throttle = 0.6
    kit.motor4.throttle = 0.6

#Stop
def Stop():
    kit = MotorKit()
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0
    time.sleep(1)

#Reverse
def Reverse():
    kit = MotorKit()
    kit.motor1.throttle = -0.6
    kit.motor2.throttle = -0.6
    kit.motor3.throttle = -0.6
    kit.motor4.throttle = -0.6
    time.sleep(0.5)
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0
    
#Turn right    
def TurnRight():
    kit = MotorKit()
    kit.motor1.throttle = 0.8
    kit.motor3.throttle = 0.8
    kit.motor2.throttle = -0.8
    kit.motor4.throttle = -0.8
    time.sleep(0.5)

#Turn left
def TurnLeft():
    kit = MotorKit()
    kit.motor1.throttle = -0.8
    kit.motor3.throttle = -0.8
    kit.motor2.throttle = 0.8
    kit.motor4.throttle = 0.8
    time.sleep(0.5)
    
#Time for driving forward    
def ForwardClock():
    while True:
        time.sleep(1)
        globals.time = globals.time + 1

#Initialization of GPIO pins for sensors
def Sensor_init():
    GPIO.setwarnings(False) #Disable warnings

    #Set ports
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.IN)
    GPIO.setup(24, GPIO.IN)
    GPIO.setup(25, GPIO.IN)
