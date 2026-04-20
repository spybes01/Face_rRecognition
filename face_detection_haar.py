import cv2 as cv



#=========================IMAGE FACE DETECTION==========================================================
# img = cv.imread(r"C:\Users\spybe\Pictures\me_test.jpg")
#
# cv.imshow("TAKHS",img)
#
# gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#
# cv.imshow("gray",gray)
#
#
# haar_cascade= cv.CascadeClassifier('haar_face.xml')
#
# faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=3)
#
# print(f'number of faces found={len(faces_rect)}')
#
# for (x,y,w,h) in faces_rect:
#     cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
#
# cv.imshow("detected face",img)

#====================================VIDEO FACE DETECTION===================================================
# capture = cv.VideoCapture(r"C:\Users\spybe\Pictures\Camera Roll\WIN_20250301_19_43_37_Pro.mp4")
capture = cv.VideoCapture(0)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
while True:
    isTrue, frame= capture.read()

    # cv.imshow("LIVE", frame)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # cv.imshow("gray", gray)


    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)

    print(f'number of faces found={len(faces_rect)}')

    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
    cv.rectangle(frame, (40, 40), (80,80), (0, 0, 255), thickness=2)
    cv.imshow("detected face", cv.flip(frame,1))


    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)

cv.waitKey(0)

