import cv2

img = cv2.imread('Suraj.png')

gaussianimg = cv2.GaussianBlur(img, (21,21),50)

cv2.imshow('Original Image',img)

cv2.imshow('Gaussian Blur', gaussianimg)

# Wait for a key press to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()