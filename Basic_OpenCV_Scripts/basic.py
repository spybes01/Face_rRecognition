import cv2 as cv


img = cv.imread(r"C:\Users\spybe\Pictures\me_test.jpg")

cv.imshow("TAKHS",img)

# Converting to grayscale

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("GRAY",gray)

# Blur an image

blur= cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)  # the higher the ksize the higher the blur

cv.imshow("BLUR",blur)

# Edge Cascade

canny=cv.Canny(img,125,175)
# IF I WANT TO REDUCE THE AMOUNT OF EDGES FOUND I CAN USE BLURED IMAGES INSTEAD OF THE NORMAL ONE
cv.imshow("EDGES",canny)

# Dialating the image
dilated= cv.dilate(canny,(3,3),iterations=1)
cv.imshow("DILATED",dilated)


# Eroding

eroded= cv.erode(dilated,(3,3),iterations=1)
cv.imshow("ERODED",eroded)


#Resize

resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("RESIZED",resized)


#Cropping

cropped=img[50:200,200:400]

cv.imshow("CROPPED",cropped)

cv.waitKey(0)