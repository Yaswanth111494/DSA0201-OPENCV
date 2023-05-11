import cv2

# Load the image
image = cv2.imread("C:/Users/yaswa/Pictures/Screenshots/Screenshot (22).png")

# Define the watermark text
watermark_text = 'SAMPLE WATERMARK'

# Choose a font and font size
font = cv2.FONT_HERSHEY_SIMPLEX
font_size = 1

# Determine the size of the text watermark
text_size, _ = cv2.getTextSize(watermark_text, font, font_size, thickness=1)

# Choose a location for the watermark (in this case, bottom-right corner)
x = image.shape[1] - text_size[0] - 10
y = image.shape[0] - text_size[1] - 10

# Draw the text watermark onto the image
cv2.putText(image, watermark_text, (x, y), font, font_size, (255, 255, 255), thickness=1, lineType=cv2.LINE_AA)

# Display the watermarked image
cv2.imshow('Watermarked Image', image)
cv2.waitKey(0)

# Save the watermarked image
cv2.imwrite('watermarked_image.jpg', image)
