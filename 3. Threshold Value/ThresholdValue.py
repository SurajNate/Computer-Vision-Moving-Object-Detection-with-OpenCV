import cv2
img = cv2.imread('Suraj.png')
grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresholdimg = cv2.threshold(grayimg, 120,255,cv2.THRESH_BINARY)[1]

# Display the Original image
cv2.imshow('Original Image', img)
# Display the Threshold Image
cv2.imshow('Sketched Image', thresholdimg)

cv2.waitKey(0)
cv2.destroyAllWindows()
