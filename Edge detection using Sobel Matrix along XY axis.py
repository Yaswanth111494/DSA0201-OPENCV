import cv2

import matplotlib.pyplot as plt

imgpath = "C:/Users/yaswa/Pictures/Screenshots/Screenshot (22).png"

img = cv2.imread(imgpath, 1)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

edgesx = cv2.Sobel(img, -1, dx=1, dy=0, ksize=1)

edgesy = cv2.Sobel(img, -1, dx=0, dy=1, ksize=1)

edges = edgesx + edgesy

output = [img, edgesx, edgesy, edges]
titles = ['Original', 'x', 'y', 'Edges']

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(output[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
