from adafruit_motorkit import MotorKit
import time

def Start():
    
    kit = MotorKit()
    kit.motor1.throttle = 0.5
    kit.motor2.throttle = 0.5
    kit.motor3.throttle = 0.5
    kit.motor4.throttle = 0.5

def Stop():
    kit = MotorKit()
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0
    time.sleep(2)
    
def Turn():
    kit = MotorKit()
    kit.motor1.throttle = 0.8
    kit.motor3.throttle = 0.8
    kit.motor2.throttle = -0.8
    kit.motor4.throttle = -0.8
    time.sleep(3)
    kit.motor1.throttle = 0
    kit.motor4.throttle = 0
    kit.motor2.throttle = 0
    kit.motor4.throttle = 0


    


    
