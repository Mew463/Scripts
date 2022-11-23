import cv2 as cv
import numpy as np 

blank = np.zeros((500,500,3), dtype = 'uint8') #make a blank image, data type is uint8
cv.imshow('Blank', blank)

cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness = 2)
cv.imshow('Rectangle', blank)
# image, text, origin, font, fontscale, color, thickness, linetype
blank = cv.putText(blank, "hello",(100,100), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv.LINE_AA)

cv.imshow('Text', blank)
cv.waitKey(0)