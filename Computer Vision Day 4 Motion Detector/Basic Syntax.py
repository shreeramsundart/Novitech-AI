#Display Rectangle

import cv2

img=(r"C:\Users\SHREERAM SUNDAR T\Pictures\Saved Pictures\Shreeram Sundar.jpg")

cv2.rectange(img,(x,y),(x+w,y+h),(0,255,0),2)


cv2.imshow("Rectengle Img",img)


cv2.write("Rectangle_Image",img)




#Putting Text in Image

import cv2

img=(r"C:\Users\SHREERAM SUNDAR T\Pictures\Saved Pictures\Shreeram Sundar.jpg")

cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)



#Detect Countors

cnts=cv2,findcontours(threshImg.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
