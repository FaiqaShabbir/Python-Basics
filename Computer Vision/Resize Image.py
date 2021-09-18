import cv2

img = cv2.imread("C:\\Users\\faiqa\\Downloads\\Video Editing\\finger on lips.jpg", 1)

# resized_img = cv2.resize(img, (700, 500))
# [1]/2 and [0]/2 shows image size half of the old img
# We can also do this [1]*2 and [0]*2 to increase size
resize_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Girl", resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
