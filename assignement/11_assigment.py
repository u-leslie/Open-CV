import cv2  # Import OpenCV library

# Read the image 'assignment-001-given.jpg'
image = cv2.imread('assignment-001-given.jpg')

# Draw a green rectangle on the image
# Rectangle coordinates: top-left (750, 750), bottom-right (1500, 1500)
# Color: Green (BGR format: (0, 255, 0)), Thickness: 8 pixels

cv2.rectangle(image, (255, 190), (980, 920), (0, 255, 0), 8)

# Add text to the image
# Text: 'RAH972U', Location (x,y): (100, 200)
# Font: FONT_HERSHEY_SIMPLEX, Scale: 1, Color: Green (BGR: (0, 255, 0)), Thickness: 14
cv2.putText(image, 'RAH972U', (780, 160), cv2.FONT_HERSHEY_PLAIN, 6, (0, 255, 0), 10)
cv2.addWeighted(cv2.rectangle(image.copy(), (750, 85), (1230, 175), (0, 0, 0), -1), 0.5, image, 1 - 0.5, 0, dst=image)

# Display the image in a new window named 'Image'
cv2.imshow('Image', image)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Save the grayscale image to a new file
cv2.imwrite('assignment-my-result.jpg', image)

# Close all OpenCV windows to release resources
cv2.destroyAllWindows()