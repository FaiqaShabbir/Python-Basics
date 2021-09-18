import cv2

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

a = 1

while True:
    a = a + 1
    check, frame = video.read()
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", gray)

    # Generate the new frame after each millisecond
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

# Will print the number of frame that it has captured during
# the video capturing
print("Number of frame captured: ", a)
video.release()
cv2.destroyAllWindows()
