import cv2 as cv

img = cv.imread('Examples\OpenCV\Data\cat.jpg') #read an image

cv.imshow('Cat', img) #show an image

capture = cv.VideoCapture(0) #read a video

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'): #press d to stop video read
        break

capture.release()
cv.destroyAllWindows()
