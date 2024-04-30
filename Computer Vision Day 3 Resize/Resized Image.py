import cv2

import imutils

img=cv2.imread(r"C:\Users\SHREERAM SUNDAR T\Pictures\Saved Pictures\Shreeram Sundar.jpg")

resizedImg=imutils.resize(img,width=200)

cv2.imshow('Orginal',img)
cv2.imshow('resizedImg',resizedImg)

cv2.imwrite('Orginal_Shree_Ram.jpg',img)
cv2.imwrite('Resized_Shree_Ram.jpg',resizedImg)



