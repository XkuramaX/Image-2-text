import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd='D:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img=cv2.imread('img1.jpg')
img=cv2.resize(img,(10000,8000))
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur=cv2.GaussianBlur(img_gray,(7,7),1)
img_canny=cv2.Canny(img_blur,25,25)
#threshold=cv2.threshold(img_blur,70,255,cv2.THRESH_BINARY)[1]
#print(pytesseract.image_to_data(img_canny))
#cv2.imshow('THRESHOLD',threshold)
cv2.imshow('Blur',img_blur)
cv2.imshow('result',img)
cv2.imshow('Canny',cv2.resize(img_canny,(800,500)))
cv2.waitKey(0)