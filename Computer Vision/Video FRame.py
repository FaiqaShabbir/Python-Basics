import time

import cv2

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
check, frame = video.read()
time.sleep(5)

# imshow: used to capture the first image/frame of video
cv2.imshow("Capturing", frame)
cv2.waitKey(0)
# release: release camera in few millisecond
video.release()
cv2.destroyAllWindows()