import cv2 as cv
import matplotlib.pyplot as plt


# Reading a photo

img = cv.imread(r"C:\Users\spybe\Pictures\me_test.jpg")

cv.imshow("TAKHS",img)

# plt.imshow(img)
# plt.show()


#BGR to Grayscale
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("gray",gray)

#BGR to HSV

hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)

cv.imshow("hsv",hsv)

# BGR to L*a*b

lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('lab',lab)

#BGR to RGB

rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("rgb",rgb)




cv.waitKey(0)