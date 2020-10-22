import time
import board
import busio
import adafruit_adxl34x
import globals

#Detects crashes
def Crash():
    
    #Initialization of accelerometer
    i2c = busio.I2C(board.SCL, board.SDA)
    accelerometer = adafruit_adxl34x.ADXL345(i2c)
    accelerometer.enable_tap_detection(tap_count=1,threshold=100, duration=150)
    
    while True:
        
        #If accelerometer detects a crash, then set a global variable to True
        if accelerometer.events["tap"] == True: 
            globals.crash = True

