from Speech import *
from Drive import *
from FaceDetection import *
import keyboard
import sys

#Drive around and avoid crashes, find faces and start conversations 
def Run():
    
    #Initialization of GPIO pins for sensors
    Sensor_init()

    while True:
        
        i = GPIO.input(23) 
        k = GPIO.input(24)
        j = GPIO.input(25)
        
        #If any sensor detect an object, stop and turn  
        if (i == 0 or j == 0 or k == 0):
            Stop()
            Turn()
            
        #Otherwise continue driving 
        else:
            Start()
            
        face_found = FaceDetect() #Search for face
        
        #If a face is found then stop and start a conversation
        if face_found == True:
            print('hej')
            Stop()
            Conversation()
            face_found = False
        
    GPIO.cleanup() # Clean up the ports