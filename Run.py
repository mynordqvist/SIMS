from Speech import *
from Drive import *
from FaceDetection import *
from Accelerometer import *
from Environment import *
import threading
import globals


#Drive around and avoid crashes, find faces and start conversations 
def Run():  
    
    #Threds for face detection, crash detection, "hej doris" detection,
    #co2 measure, sensor detection and time of driving forward
    faceThread = threading.Thread(target=FaceDetect)
    crashThread = threading.Thread(target=Crash)
    heyThread = threading.Thread(target=Hey)
    co2Thread = threading.Thread(target=Co2Variable)
    forwardThread = threading.Thread(target=ForwardClock)
    
    faceThread.start()
    crashThread.start()
    heyThread.start()
    co2Thread.start()
    forwardThread.start()
    
    #Initialization of GPIO pins for sensors
    Sensor_init()

    while True:
                      
        i = GPIO.input(23) 
        k = GPIO.input(24)
        j = GPIO.input(25)
        
        #If any sensor detect an object, a crash is detected or driving forward 10 seconds,
        #Stop and turn left or right 
        if (i == 0 or j == 0 or k == 0) or globals.crash == True or globals.time >= 10:
            Stop()
            random_reverse=[Reverse, Stop]
            random.choice(random_reverse)()
            random_functions=[TurnLeft, TurnRight]
            random.choice(random_functions)()
            globals.crash = False #Reset global variable for crash is detected
            globals.time = 0 #Reset global variable for time
            
        else:
            Start()

        #If a face is found or "Hej Doris" is detected, stop and start a conversation
        if globals.hey_found == True:
            Stop()
            Conversation()
            globals.hey_found = False #Reset global variable 
            globals.time = 0 #Reset global variable
        
    GPIO.cleanup() # Clean up the ports