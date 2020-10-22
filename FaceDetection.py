import numpy as np
import cv2
import globals

#Find faces 
def FaceDetect():
    
    faceCascade = cv2.CascadeClassifier('Cascades/facevalues.xml')
    cap = cv2.VideoCapture(0) #Fetch videostream from index zero
    cap.set(3,640) #Set Width
    cap.set(4,480) #Set Height    
    
    while True:
        
        #Facedetection
        ret, img = cap.read() #Read camera  
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,     
            scaleFactor=1.4,
            minNeighbors=5,     
            minSize=(20, 20)
        )
            
        #When a face is found, set global variable to True
        for (x,y,w,h) in faces:
            globals.face_found = True