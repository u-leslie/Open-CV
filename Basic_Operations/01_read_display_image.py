import cv2  # Import OpenCV library

# Read the image file 'lena.jpg'
# Ensure 'lena.jpg' is in the same directory as this script
image = cv2.imread('lena.jpg')

# Display the image in a new window named 'Image'
cv2.imshow('Image Window', image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Close all OpenCV windows to release resources
cv2.destroyAllWindows()
