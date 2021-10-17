import cv2
import numpy as np

# face_detection=cv2.CascadeClassifier("./XML_Data/haarcascade_frontalface_default.xml")  
face_detection=cv2.CascadeClassifier("ENTER THE .XML PATH")


# img = cv2.imread('./snowden.jpg')
img = cv2.imread('IMAGE PATH')
cv2.imshow("Original Image", cv2.resize(img, (650, 500)))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_detection.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),3)

cv2.imshow("Face Detection", cv2.resize(img, (650, 500)))

if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()
