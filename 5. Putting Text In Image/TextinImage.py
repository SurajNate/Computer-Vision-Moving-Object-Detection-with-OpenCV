import cv2
# Read the image
img = cv2.imread('Suraj.png')

# Define the text to be added
text = "Suraj Nate"
text2 = "Kyu Hila Dala na ☻"

# Put text on the image
cv2.putText(img, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

cv2.putText(img, text2, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 255), 1)

# Display the image
cv2.imshow('Image with Text', img)
# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()