import cv2
from pyzbar.pyzbar import decode

# Read the image
image = cv2.imread("image05.png")

# Check if the image is loaded correctly
if image is None:
    print("Error: Image not loaded correctly.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect and decode barcodes (including Aztec codes)
decoded_objects = decode(gray)

if decoded_objects:
    for obj in decoded_objects:
        print(f"Detected Aztec Code: {obj.data.decode('utf-8')}")
        
        # Draw a rectangle around the detected code
        points = obj.polygon
        if len(points) == 4:
            pts = [(point.x, point.y) for point in points]
            pts = [tuple(map(int, pt)) for pt in pts]
            cv2.polylines(image, [pts], isClosed=True, color=(0, 255, 0), thickness=2)
else:
    print("No Aztec code detected.")

# Show the image
cv2.imshow("Aztec Code", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
