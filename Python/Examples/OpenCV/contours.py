import cv2 as cv 
import numpy as np 

img = cv.imread('Examples\OpenCV\Data\cat.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape, dtype = 'uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175) #canny edge detection
cv.imshow('Canny Edges', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours were found')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours drawn', blank)

if cv.waitKey(20) & 0xFF == ord('d'): #press d to stop video read
    cv.destroyAllWindows()

cv.waitKey(0)