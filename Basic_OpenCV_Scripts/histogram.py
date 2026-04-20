import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img = cv.imread(r"C:\Users\spybe\Pictures\me_test.jpg")

cv.imshow("TAKHS",img)

#Change to gray
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("gray", gray)

#Create a mask
blank = np.zeros(img.shape[:2],dtype='uint8')
circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2-70),5,255,-1)
cv.imshow('Mask location', circle)

mask = cv.bitwise_and(gray,gray,mask=circle)

cv.imshow('Masked takhs',mask)

#Grayscale histogram

gray_hist= cv.calcHist([gray],[0],circle,[256],[0,256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

#Coloured histogram
#
# mask = cv.bitwise_and(img,img,mask=circle)
#
# cv.imshow('Masked takhs',mask)
#
#
# plt.figure()
# plt.title('Colored Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# colors =('b','g','r')
# for i,col in enumerate(colors):
#     hist=cv.calcHist([img],[i],None,[256],[0,256])
#     plt.plot(hist,color=col)
#     plt.xlim([0,256])
# plt.show()


cv.waitKey(0)