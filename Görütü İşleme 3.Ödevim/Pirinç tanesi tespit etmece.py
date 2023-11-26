import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("gohan2.png")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# treshold islemi
_, mask = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY) # 100 pikselin uzerindekileri 255 yap

# Morfolojik işlemler
iyilestirme_boyutu = np.ones((5, 5), np.uint8)
mask1 = cv2.morphologyEx(mask, cv2.MORPH_OPEN, iyilestirme_boyutu, iterations=2)

mask1_copy = cv2.morphologyEx(mask, cv2.MORPH_OPEN, iyilestirme_boyutu, iterations=2)

# Sınırları bulma islemi
contours, _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

pirinc_Sayisi = len(contours)
print(pirinc_Sayisi)


cv2.namedWindow("original image",cv2.WINDOW_NORMAL)
cv2.imshow("original image",img)
cv2.namedWindow("gri", cv2.WINDOW_NORMAL)
cv2.imshow("gri", img_gray)
cv2.namedWindow("mask1", cv2.WINDOW_NORMAL)
cv2.imshow("mask1", mask1)
cv2.namedWindow("mask1_copy", cv2.WINDOW_NORMAL)
cv2.imshow("mask1_copy", mask1_copy)

k = cv2.waitKey(0)
cv2.destroyAllWindows()

if k == ord("s"):
    print("s ye basıldı resim kaydedildi")
    cv2.imwrite("tespit edilmiş prinçler.png",mask1)
elif k == ord("a"):
    print("a ya basıldı resimler kapatıldı")
