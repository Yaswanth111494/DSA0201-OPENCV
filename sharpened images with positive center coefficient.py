import cv2
import numpy as np

# Load the image
image = cv2.imread("C:/Users/yaswa/Pictures/Screenshots/Screenshot (22).png")
# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the grayscale image
blurred = cv2.GaussianBlur(gray, (3, 3), 0)

# Create the Laplacian kernel with a positive center coefficient
kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

# Apply the Laplacian filter to the blurred image
sharpened = cv2.filter2D(blurred, -1, kernel)

# Adjust the contrast of the sharpened image
sharpened = cv2.convertScaleAbs(sharpened, alpha=2.5, beta=0)

# Display the sharpened image
cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)

# Save the sharpened image
cv2.imwrite('sharpened_image.jpg', sharpened)
