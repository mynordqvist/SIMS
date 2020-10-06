from adafruit_motorkit import MotorKit
import time
import RPi.GPIO as GPIO

def Start(): #drive forwards
    
    kit = MotorKit()
    kit.motor1.throttle = 0.5
    kit.motor2.throttle = 0.5
    kit.motor3.throttle = 0.5
    kit.motor4.throttle = 0.5

def Stop(): #stop 

    kit = MotorKit()
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0
    time.sleep(2)
    
def Turn(): #turn right

    kit = MotorKit()
    kit.motor1.throttle = 0.8
    kit.motor3.throttle = 0.8
    kit.motor2.throttle = -0.8
    kit.motor4.throttle = -0.8

def Drive():
    
    GPIO.setwarnings(False) #disable warnings

    #set ports
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.IN)
    GPIO.setup(24, GPIO.IN)
    GPIO.setup(25, GPIO.IN)

    while True:
        
        i = GPIO.input(23) 
        k = GPIO.input(24)
        j = GPIO.input(25)

        #if any sensor detect an object 
        if (i == 0 or j == 0 or k == 0):
            Stop()
            Turn()
        
        #if none of the sensors detects an object    
        elif (i == 1 and j == 1 and k == 1):
            Start()
            
    GPIO.cleanup() # clean up the ports   

    


    
