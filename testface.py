import cv2
import os
import numpy as np
import faceRecognition as fr


#This module takes images  stored in diskand performs face recognition
test_img=cv2.imread('testimage.jpg')#test_img path
faces_detected,gray_img=fr.faceDetection(test_img)
print("faces_detected:",faces_detected)

#Below function draws bounding boxes around detected face in image
for(x,y,w,h) in faces_detectded:
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=5)

resized_img=cv2.resize(test_img,(1000,1000))
cv2.imshow("face detection",resized_img)
cv2.waitKey(0)#Waits indefinitely until a key is pressed
cv2.destroyAllWindows
