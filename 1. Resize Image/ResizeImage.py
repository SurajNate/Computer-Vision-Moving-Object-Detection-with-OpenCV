import cv2  # OpenCV
import imutils  # For resizing

# Read the image
img = cv2.imread('Suraj.png')

# Resize the image
resized_img = imutils.resize(img, width=200)

# Display the Original image
cv2.imshow('Original Image', img)

# Display the resized image
cv2.imshow('Resized Image', resized_img)

# Wait for a key press to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()