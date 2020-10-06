import numpy as np
import cv2
from Speech import tts

def Face_Detect():
    faceCascade = cv2.CascadeClassifier('Cascades/facevalues.xml')
    cap = cv2.VideoCapture(0) #fetch videostream from index zero
    cap.set(3,640) # set Width
    cap.set(4,480) # set Height

    while True:
        ret, img = cap.read() #read camera
        face_found = False #variable to check if a face is found

        #facedetection
        faces = faceCascade.detectMultiScale( 
            img,
            scaleFactor=1.5,
            minNeighbors=5,
            minSize=(20, 20)
        )
      	
      	#when a face is found
        for (x,y,w,h) in faces:
            face_found = True
       
        if face_found == True:
            break

    cap.release()
    cv2.destroyAllWindows()

    return face_found

if __name__ == "__main__":
    face_recognizing()
    tts("hej, hur mår du")