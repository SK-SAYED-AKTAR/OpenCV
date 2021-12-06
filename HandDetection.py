from cv2 import cv2
# Also use import cv2 if you facing error, like ModuleNotFound
from cvzone.HandTrackingModule import HandDetector

# cap = cv2.VideoCapture(-1)
cap = cv2.VideoCapture("http://192.168.43.6:8080/video")

detector = HandDetector(detectionCon=0.8)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (800, 600))
    hands, frame = detector.findHands(frame)
    cv2.imshow("Live Video", frame)

    cv2.waitKey(1)
