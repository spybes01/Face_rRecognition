import cv2 as cv

 # Reading a photo

# img = cv.imread(r"C:\Users\spybe\Pictures\me_test.jpg")
#
# cv.imshow("TAKHS",img)

def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# capture = cv.VideoCapture(r"C:\Users\spybe\Pictures\Camera Roll\WIN_20250301_19_43_37_Pro.mp4")
capture = cv.VideoCapture(0)

while True:
    isTrue, frame= capture.read()

    frame_resize = rescaleFrame(frame,scale=0.2)
    cv.imshow("LIVE", frame)
    cv.imshow("live",frame_resize)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
