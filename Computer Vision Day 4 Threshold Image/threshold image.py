import cv2

# Load the image
img = cv2.imread(r"C:\Users\SHREERAM SUNDAR T\Pictures\Saved Pictures\Shreeram Sundar.jpg")

# Convert the image to grayscale
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, thresholdImg = cv2.threshold(grayImg, 20, 255, cv2.THRESH_BINARY)#adjust the value depends upon image

# Display the original and thresholded images
cv2.imshow("Original Image", img)
cv2.imshow("Thresholded Image", thresholdImg)

# Save the images
cv2.imwrite("Original_Image.jpg", img)
cv2.imwrite("Threshold_Image.jpg", thresholdImg)

