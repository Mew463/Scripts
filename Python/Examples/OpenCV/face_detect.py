import cv2 as cv 

img = cv.imread('Examples\OpenCV\Data\groupofpeople.jpg')
cv.imshow('Person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('Examples\OpenCV\Data\haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 2.1,  minNeighbors = 5)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness = 2)
cv.imshow('Detected faces', img)

if cv.waitKey(20) & 0xFF == ord('d'): #press d to stop video read
    cv.destroyAllWindows()

cv.waitKey(0)