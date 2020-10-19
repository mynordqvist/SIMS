import time
import board
import busio
import adafruit_adxl34x

def Crash():
    
    i2c = busio.I2C(board.SCL, board.SDA)
    accelerometer = adafruit_adxl34x.ADXL345(i2c)
    accelerometer.enable_tap_detection(tap_count=1,threshold=65, duration=50)

    while True:
        if accelerometer.events["tap"] == True :
            print("Crash")
            return True

