import cv2

# Read the image
img = cv2.imread('Suraj.png')

# Define rectangle coordinates (x, y) and width, height (w, h)
x, y, w, h = 120, 60, 120, 120  # Example values

# Draw the rectangle
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show the image with the rectangle
cv2.imshow('Image with Rectangle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()