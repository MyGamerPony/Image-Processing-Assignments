import cv2
from matplotlib import pyplot as plt
import numpy as np

camera = cv2.VideoCapture(0)

while camera.isOpened():
    _, ekran = camera.read()

    hsv = cv2.cvtColor(ekran, cv2.COLOR_BGR2HSV)

    lower = np.array([0,130,90])
    upper = np.array([326,359,359])

    mask = cv2.inRange(hsv,lower,upper)

    res = cv2.bitwise_and(ekran,ekran,mask=mask)

    cv2.namedWindow("ekran", cv2.WINDOW_NORMAL)
    cv2.imshow("ekran",ekran)
    cv2.namedWindow("res", cv2.WINDOW_NORMAL)
    cv2.imshow("res", res)

    if cv2.waitKey(1) == ord("q"):
        print("GÖRÜNTÜ SONLANDIRILDI")
        break

camera.release()
cv2.destroyAllWindows()
