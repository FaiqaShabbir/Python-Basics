import time

import cv2

# in place of 0 we can also pass video url but in this case laptop camera will be used
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
"""
frame: NumPy Array represents first image that video 
captures
check: bool dat type will show is python able to read 
video capture object
"""
check, frame = video.read()
print(check)
print(frame)
time.sleep(5)
video.release()
