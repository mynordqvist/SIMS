from Speech import *
from Drive import *
from FaceDetection import *
from Accelerometer import *
import threading
import globals

import qwiic_ccs811


#Drive around and avoid crashes, find faces and start conversations 
def Run():
    
    #Initialization of GPIO pins for sensors
    Sensor_init()
    
    #Threds for face detection and crash detection
    faceThread = threading.Thread(target=FaceDetect)
    crashThred = threading.Thread(target=Crash)
    heyThread = threading.Thread(target=Hey)
    faceThread.start()
    crashThred.start()
    heyThread.start()

    while True:
        
        i = GPIO.input(23) 
        k = GPIO.input(24)
        j = GPIO.input(25)
        
        #If any sensor detect an object, stop and reverse then turn random left or right  
        if (i == 0 or j == 0 or k == 0):
            Stop()
            Reverse()
            random_functions=[TurnLeft, TurnRight]
            random.choice(random_functions)()
            
        #Otherwise continue driving 
        else:
            Start()
        
        #If a crash is detected, stop and reverse then turn random left or right 
        if globals.crash == True:
            print("Crash")
            Stop()
            Reverse()
            random_functions=[TurnLeft, TurnRight]
            random.choice(random_functions)()
            globals.crash = False #Reset global variable for crash is detected

        #If a face is found then stop and start a conversation
        if globals.face_found == True:
            globals.hey_found = True
            print('hej')
            Stop()
            Conversation()
            globals.face_found = False #Reset global variable for face is found
            globals.hey_found = False
            
        
        if globals.hey_found == True:
            Stop()
            Conversation()
            globals.hey_found = False
        
    GPIO.cleanup() # Clean up the ports