import cv2 as cv
from numpy import empty

path = r'Examples\OpenCV\classifier\cascade.xml' #path to cascade classifier
cameraNo = 1
objectName = 'Target'
frameWidth = 1920
frameHeight = 1080
color = (0, 0 , 255)

cap = cv.VideoCapture(cameraNo)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

#Trackbars
cv.namedWindow("Result")
cv.resizeWindow("Result", 10, 10)
cv.createTrackbar("Scale", "Result", 400, 1000, empty)
cv.createTrackbar("Neighbor", "Result", 8, 20,empty)
cv.createTrackbar("Min Area", "Result", 0, 200,empty)
cv.createTrackbar("Max Area", "Result", 100, 200,empty)
cv.createTrackbar("Brightness", "Result", 180, 255,empty)


cascade = cv.CascadeClassifier(path)

while True:
    cameraBrightness = cv.getTrackbarPos("Brightness", "Result")
    cap.set(10, cameraBrightness)
    success, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (7,7), cv.BORDER_DEFAULT)
    scaleVal = 2 + (cv.getTrackbarPos("Scale", "Result") / 1000)
    neighbor = cv.getTrackbarPos("Neighbor", "Result")
    minArea = cv.getTrackbarPos("Min Area", "Result")
    maxArea = cv.getTrackbarPos("Max Area", "Result")
    objects = cascade.detectMultiScale(blur, scaleVal, neighbor,0,(minArea,minArea), (maxArea,maxArea))
    for (x,y,w,h) in objects:
        cv.rectangle(img,(x,y),(x+w,y+h), color, 2)
        cv.putText(img, objectName, (x,y-5), cv.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
        roi_color = img[y:y+h, x:x+w]
            

    cv.imshow("Result", img)

    if cv.waitKey(1) & 0xFF == ord('d'): #press d to stop video read
        break
