import cv2

img=cv2.imread(r"C:\Users\SHREERAM SUNDAR T\Pictures\Saved Pictures\InShot_20220621_222327842-01.jpeg")

cv2.imshow ('show',img)
cv2.imwrite('Pink.jpg',img)

grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


cv2.imshow('orginal',img)
cv2.imshow('Gray',grayimg)

cv2.imwrite('graynew.jpg',grayimg)

