import cv2
import numpy as np

# Read the image
path = "C:/Users/yaswa/Pictures/Screenshots/Screenshot (30).png"
image = cv2.imread(path)  # 0 flag reads the image as grayscale

# Create a kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)  # 5x5 kernel with all ones

# Perform the black hat operation
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

# Display the result
cv2.imshow('Black Hat', blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()
