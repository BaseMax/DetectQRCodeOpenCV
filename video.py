import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture('test6.mkv')
# cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

myDataList = [
	"111111"
]

while True:
	success, img = cap.read()
	if not success:
		break
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

	cv2.imshow("Result", img)
	cv2.waitKey(1)


