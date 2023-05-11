import cv2

import numpy as np

img = cv2.imread("C:/Users/yaswa/Pictures/Screenshots/Screenshot (22).png" , cv2.IMREAD_GRAYSCALE)

sobel_kernel_y = np.array([[-1, -2, -1],
                           [0, 0, 0],
                           [1, 2, 1]])
img_sobel_y = cv2.filter2D(img, -1, sobel_kernel_y)
cv2.imshow('Sobel Edge Detection (Y-axis)', img_sobel_y)
cv2.waitKey(0)
cv2.destroyAllWindows()
