import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('Cascades/facevalues.xml')

cap = cv2.VideoCapture(0) #fetch videostream from index zero
cap.set(3,640) #set Width
cap.set(4,480) #set Height

while(True):
	ret, img = cap.read() #read camera

    faces = faceCascade.detectMultiScale( #facedetection
        img,
        scaleFactor=1.5,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_color = img[y:y+h, x:x+w] #Rectangle around face
        
    cv2.imshow('video',img) #show image
    
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()