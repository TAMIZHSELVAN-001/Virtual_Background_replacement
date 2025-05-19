import cv2
import numpy as np
background = cv2.imread('BackgroundImg.jpg')
background = cv2.resize(background, (640, 480))
cap = cv2.VideoCapture(0)
cap.set(3, 640)  
cap.set(4, 480) 
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([35, 40, 40])
    upper = np.array([85, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    mask_inv = cv2.bitwise_not(mask)
    person = cv2.bitwise_and(frame, frame, mask=mask_inv)
    bg_part = cv2.bitwise_and(background, background, mask=mask)
    combined = cv2.add(person, bg_part)
    cv2.imshow('Virtual Background', combined)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()