import numpy as np
import matplotlib.pyplot as plt
import cv2


foto = cv2.imread("gri fındık.png", cv2.IMREAD_GRAYSCALE )

histogram = [0] * 256

for row in foto:
    for pixel_value in row:
        histogram[pixel_value] += 1


for i, count in enumerate(histogram):
    print(f'Gri Seviye {i}: {count} piksel')


plt.bar(range(256), histogram)
plt.title('Fotoğrafın Histogramı')
plt.xlabel('Gri Değer')
plt.ylabel('Piksel Sayısı')
plt.show()
