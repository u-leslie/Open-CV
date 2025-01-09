import cv2  # Import OpenCV library

# Read the image 'lena.jpg'
image = cv2.imread('lena.jpg')

# Display the original image in a window
cv2.imshow('Image', image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the image in PNG format
cv2.imwrite('lena_image.png', image)

# Save the image in BMP format
cv2.imwrite('lena_image.bmp', image)

# Close all OpenCV windows
cv2.destroyAllWindows()