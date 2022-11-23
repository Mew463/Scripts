import cv2 as cv 

img = cv.imread('Examples\OpenCV\Data\cat.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT) #blur an image
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175) #canny edge detection
cv.imshow('Canny Edges', canny)

(h, w) = img.shape[:2]
(cX, cY) = (w/2, h/2)
m = cv.getRotationMatrix2D((cX, cY), 45, 1.0)
rotate = cv.warpAffine(img, m, (w, h))
cv.imshow('Rotated image', rotate)

if cv.waitKey(20) & 0xFF == ord('d'): #press d to stop video read
    cv.destroyAllWindows()

cv.waitKey(0)