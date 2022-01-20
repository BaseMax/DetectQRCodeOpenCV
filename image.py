import cv2
import numpy as np
from pyzbar.pyzbar import decode

# img = cv2.imread("test1.jpg")
# img = cv2.imread("test2.jpg")
# img = cv2.imread("test3.jpg")
# img = cv2.imread("test4.jpg")
# img = cv2.imread("test5.webp")
img = cv2.imread("test7.jpg")

myDataList = [
	"111114"
]

for barcode in decode(img):
	myData = barcode.data.decode("utf-8")
	print(myData)

	if myData in myDataList:
		color = (0, 255, 0)
	else:
		color = (0, 0, 255)
	# (255, 0, 255)

	pts = np.array([barcode.polygon], np.int32)
	pts = pts.reshape((-1, 1, 2))
	cv2.polylines(img, [pts], True, color, 5)
	pts2 = barcode.rect
	cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

while True:
	cv2.imshow("Result", img)
	cv2.waitKey(1)
