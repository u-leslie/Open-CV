import cv2  # Import OpenCV library

# Read the image 'lena.jpg'
image = cv2.imread('lena.jpg')

# Draw a green rectangle on the image
# Rectangle coordinates: top-left (750, 750), bottom-right (1500, 1500)
# Color: Green (BGR format: (0, 255, 0)), Thickness: 8 pixels

cv2.rectangle(image, (750, 750), (1500, 1500), (0, 255, 0), 8)

# Draw a red circle on the image
# Center coordinates: (1125, 1125), Radius: 375
# Color: Red (BGR format: (0, 255, 0)), Thickness: 8 pixels
cv2.circle(image, (1125, 1125), 375, (0, 0, 255), 8)

# Display the image in a new window named 'Image'
cv2.imshow('Image', image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the grayscale image to a new file
cv2.imwrite('lena_shapes.jpg', image)

# Close all OpenCV windows to release resources
cv2.destroyAllWindows()