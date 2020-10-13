import numpy as np
import cv2

#Find faces 
def FaceDetect():
    faceCascade = cv2.CascadeClassifier('Cascades/facevalues.xml')
    cap = cv2.VideoCapture(0) #Fetch videostream from index zero
    cap.set(3,640) #Set Width
    cap.set(4,480) #Set Height
    
    ret, img = cap.read() #Read camera
    face_found = False 

    #Facedetection
    faces = faceCascade.detectMultiScale( 
            img,
            scaleFactor=1.5,
            minNeighbors=5,
            minSize=(20, 20)
            )
        
    #When a face is found
    for (x,y,w,h) in faces:
        face_found = True
        
    return face_found