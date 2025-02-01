import cv2
import numpy as np

# Load the image
image = cv2.imread("qr2.jpg")

if image is None:
    print("Error: Image not loaded correctly.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding
gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Initialize QR code detector
detector = cv2.QRCodeDetector()

# Detect and decode the QR code
data, points, _ = detector.detectAndDecode(gray)

print(f"Points detected: {points}")

if data:
    print(f"QR Code Data: {data}")
    if points is not None:
        points = points.astype(int)
        cv2.polylines(image, [points], True, (0, 255, 0), 2)
else:
    print("No QR code detected.")

# Display the result
cv2.imshow("QR Code", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
