import cv2
import numpy as np

# Read the image 'lena.jpg'
image = cv2.imread('lena.jpg')

# Split the image into its B, G, and R color channels
b, g, r = cv2.split(image)

# Create colorized versions of each channel
blue_channel = cv2.merge((b, np.zeros_like(b), np.zeros_like(b)))  # Only Blue
green_channel = cv2.merge((np.zeros_like(g), g, np.zeros_like(g)))  # Only Green
red_channel = cv2.merge((np.zeros_like(r), np.zeros_like(r), r))  # Only Red

# Prepare images and titles for the slideshow
slides = [
    ("Blue Channel (Colorized)", blue_channel),
    ("Green Channel (Colorized)", green_channel),
    ("Red Channel (Colorized)", red_channel)
]

# Duration (milliseconds) for each slide
slide_duration = 2000  # 2000 ms = 2 seconds

# Show each slide
for title, img in slides:
    cv2.imshow(title, img)  # Display the current slide
    cv2.waitKey(slide_duration)  # Wait for the duration before showing the next

# Merge the channels back together (optional)
merged_image = cv2.merge((r, g, b))
cv2.imshow('Merged Image (Swapped)', merged_image)

# Display the merged image for the same duration
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()