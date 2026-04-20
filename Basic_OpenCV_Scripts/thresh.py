import cv2 as cv


img = cv.imread(r"C:\Users\spybe\Pictures\me_test.jpg")

cv.imshow("TAKHS",img)



gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("gray", gray)

#SIMPLE THRESHOLDING
threshold, thresh= cv.threshold(gray,100,255,cv.THRESH_BINARY)

cv.imshow('simple threshold',thresh)


threshold, thresh_inv= cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)

cv.imshow('simple threshold inverted',thresh_inv)


#ADAPTIVE THRESHOLDING
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,1)

cv.imshow("adaptive threshold",adaptive_thresh)

cv.waitKey(0)