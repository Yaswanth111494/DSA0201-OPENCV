import cv2
import numpy as np
img = cv2.imread("C:/Users/yaswa/Pictures/Screenshots/Screenshot (22).png", cv2.IMREAD_GRAYSCALE)
sobel_kernel_x = np.array([[-1, 0, 1],
                           [-1, 0, 1],
                           [-1, 0, 1]])
img_sobel_x = cv2.filter2D(img, -1, sobel_kernel_x)
cv2.imshow('Sobel Edge Detection (X-axis)', img_sobel_x)
cv2.waitKey(0)
cv2.destroyAllWindows()
