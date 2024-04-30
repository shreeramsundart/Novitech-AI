import cv2

# Path to the Haar cascade XML file
alg = "haar_cascade_frontface_detect.xml"

# Load the Haar cascade classifier
haar_cascade = cv2.CascadeClassifier(alg)

# Open the camera
cam = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    _, img = cam.read()


    

    # Convert the frame to grayscale
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = haar_cascade.detectMultiScale(grayImg, 1.3, 4)

    # Draw rectangles around detected faces and add text
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Face Detected"
        cv2.putText(img, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the image
    cv2.imshow("Face Detection", img)

    # Check for key press
    key = cv2.waitKey(1)
    if key == ord("q"):  # Quit if 'q' is pressed
        break

# Release the camera and close all windows
cam.release()
cv2.destroyAllWindows()
