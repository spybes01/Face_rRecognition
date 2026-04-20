import cv2 as cv


# Reading a photo
#
# img = cv.imread(r"C:\Users\spybe\Pictures\me_test.jpg")
#
# cv.imshow("TAKHS",img)
#


# Reading a video

capture = cv.VideoCapture(r"C:\Users\spybe\Pictures\Camera Roll\WIN_20250301_19_43_37_Pro.mp4")
# capture = cv.VideoCapture(0)

while True:
    isTrue, frame= capture.read()

    cv.imshow("LIVE", frame)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)