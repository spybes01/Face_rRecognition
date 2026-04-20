import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

cv.imshow('BLANK',blank)

# # 1 Paint all pixels Green
# blank[:] = 0,255,0
#
# cv.imshow('GREEN',blank)

# # 2 Draw a rectangle
# cv.rectangle(blank,(0,0),(250,250),(0,255,0), thickness=2)
# cv.imshow("RECTANGLE",blank)

# # 3 Draw a circle
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,255,0),thickness=4)
# cv.imshow('CIRCLE',blank)

# # 4 Draw a line
#
# cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=4)
# cv.imshow('LINE',blank)

# 5 Write text
cv.putText(blank,'TAKAROS',(blank.shape[1]//2,blank.shape[0]//2),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)
cv.imshow('TEXT',blank)
cv.waitKey(0)