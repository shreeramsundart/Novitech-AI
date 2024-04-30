import cv2

img=cv2.imread(r"C:\Users\SHREERAM SUNDAR T\Pictures\Saved Pictures\Shreeram Sundar.jpg")

GaussianBlur=cv2.GaussianBlur(img,(41,41),50)

cv2.imshow("OrginalImg",img)
cv2.imshow("GaussianBlur",GaussianBlur)

cv2.imwrite("Orginal_Image.jpg",img)
cv2.imwrite("Gaussian_Blur.jpg",GaussianBlur)
