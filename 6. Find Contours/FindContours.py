import cv2

# Read the image
img = cv2.imread('Suraj.png')
# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Apply thresholding to get a binary image
_, threshimg = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# Find contours
contours, hierarchy = cv2.findContours(threshimg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Draw contours on the original image
cv2.drawContours(img, contours, -1, (0, 255, 0), 1)

# Show the image with contours
cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
