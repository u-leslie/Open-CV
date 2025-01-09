import cv2  # Import OpenCV library

# Read the image 'lena.jpg'
image = cv2.imread('lena.jpg')

# Flip the image horizontally (1 = horizontal flip)
flipped_image = cv2.flip(image, 100)

# Display the flipped image in a window
cv2.imshow('Image', flipped_image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the flipped image to a new file
cv2.imwrite('lena_flipped.jpg', flipped_image)

# Close all OpenCV windows
cv2.destroyAllWindows()