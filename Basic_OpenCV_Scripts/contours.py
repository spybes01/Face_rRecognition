import cv2 as cv
import numpy as np


# Reading a photo

img = cv.imread(r"C:\Users\spybe\Pictures\me_test.jpg")

cv.imshow("TAKHS",img)

blank= np.zeros(img.shape,dtype='uint8')
cv.imshow('BLANK',blank)


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("GRAY",gray)

blur= cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow("BLURED",blur)

canny= cv.Canny(blur, 125,175)
cv.imshow("CANNY TAKHS",canny)

# ret, thresh = cv.threshold(gray, 125,255,cv.THRESH_BINARY)
#
# cv.imshow("THRESH",thresh)
#GET CONTOURS

contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} countour(s) found!')

cv.drawContours(blank, contours,-1,(0,0,255),1)
cv.imshow("DRAW",blank)


cv.waitKey(0)