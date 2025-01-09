import cv2  # Import OpenCV library

# Read the image 'lena.jpg'
image = cv2.imread('lena.jpg')

# Resize the image to quarter of its original width and height
# (image.shape[1] is width, image.shape[0] is height)
resized_image = cv2.resize(image, (image.shape[1] // 4, image.shape[0] // 4))

#show resized image
cv2.imshow("Resized", resized_image);

#display the image until any key is pressed
cv2.waitKey(0);

# Save the resized image to a new file
cv2.imwrite('lena_resized.jpg', resized_image)

#Distroy all the open windows before exiting
cv2.destroyAllWindows();