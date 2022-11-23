import cv2 as cv
import os 
import time 
from numpy import empty

myPath = 'Examples\OpenCV\Data'
cameraNo = 1
cameraBrightness = 150
moduleVal = 10 #save every ith frame to avoid repetition
grayImage = False #save images as color or gray 
blurImage = True
rotateImage = True
saveData = True
showImage = True
imgWidth = 180
imgHeight = 120

#Trackbars
cv.namedWindow("Result")
cv.resizeWindow("Result", 500, 100)
cv.createTrackbar("minBlur", "Result", 50, 1000, empty)

global countFolder
cap = cv.VideoCapture(cameraNo)
cap.set(3, 480)
cap.set(4, 480)
cap.set(10, cameraBrightness)

def saveDataFunc(): 
    global countFolder
    countFolder = 0
    while os.path.exists(myPath+ str(countFolder)):
        countFolder = countFolder + 1
    os.makedirs(myPath + str(countFolder))

if saveData:saveDataFunc()
count = 0
countSave = 0



while True:
    success, orgimg = cap.read()
    img = cv.resize(orgimg,(imgWidth, imgHeight))
    if grayImage:img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    if rotateImage: 
        (h, w) = orgimg.shape[:2]
        (cX, cY) = (w/2, h/2)
        m = cv.getRotationMatrix2D((cX, cY), 45, 1.0)
        rotate = cv.warpAffine(orgimg, m, (w, h))
        rotateresizedimg = cv.resize(rotate,(imgWidth, imgHeight))
    if blurImage:
        blur = cv.GaussianBlur(orgimg, (7,7), cv.BORDER_DEFAULT) #blur an image
        blurresizedimg = cv.resize(blur,(imgWidth, imgHeight))
    if saveData:
        blur = cv.Laplacian(img, cv.CV_64F).var()
        if count % moduleVal == 0 and blur > cv.getTrackbarPos("minBlur", "Result"):
            cv.imwrite(myPath + str(countFolder) + '/' + str(countSave) + '.jpg',img)
            countSave+=1
            if rotateImage:
                cv.imwrite(myPath + str(countFolder) + '/' + str(countSave) + '.jpg',rotateresizedimg) 
                countSave+=1
            if blurImage:
                cv.imwrite(myPath + str(countFolder) + '/' + str(countSave) + '.jpg',blurresizedimg) 
                countSave+=1
        count+=1
    if showImage:
        cv.imshow("Image", img)
    if cv.waitKey(1) & 0xFF == ord('d'):
        break
cap.release()
cv.destroyAllWindows
