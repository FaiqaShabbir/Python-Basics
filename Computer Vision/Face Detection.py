"""
For face detection cascade classifier will be created that contains the feature
of face.
1st OpenCv will read the image an d convert it into numpy array which will search for
rows and columns values of face numpy ndarray
"""

import cv2

face_cascade = cv2.CascadeClassifier("C:\\Users\\faiqa\\Downloads\\opencv-master\\data\\haarcascades\\haarcascade_frontalface_default.xml")

img = cv2.imread("C:\\Users\\faiqa\\OneDrive\\Desktop\\Python\\awesome-whatsapp-dp-for-girls.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# detectMultiScale: Method to search for the face rectangle co-ordinates
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05,
                                      minNeighbors=5)
# We define the method to create a rectangle using cv2.rectangle by passing parameters such as the image object,
# RGB values of the box outline and the width of the rectangle.
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

# commented the resize because we don't want
# resized = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))

cv2.imshow("Gray", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
