import cv2
"""
cv2 reads image as numpy array and python read image as array or matrix of numbers
"""
# 1: Read image in RGB, 0: Read image as a gray scale
# 1: 3D array, 0: 2D array
img = cv2.imread("C:\\Users\\faiqa\\Downloads\\Video Editing\\finger on lips.jpg", 0)
# print(img.shape)
# print(type(img))
"""
img: Image object/source | Name of windows where picture will be displayed
waitKey: wait until a user presses a key and 2000 shows 
after 2000 millisecond it will automatically disappear
"""
cv2.imshow("Girl with finger on lips", img)
cv2.waitKey(2000)
cv2.destroyAllWindows()
