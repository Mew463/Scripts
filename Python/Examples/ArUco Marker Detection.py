import cv2
from cv2 import aruco
import time
# Use this website to generate the markers https://chev.me/arucogen/

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)
parameters =  cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(dictionary, parameters)


cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        corners, ids, rejectedImgPoints = detector.detectMarkers(frame)
        # cv2.aruco.detectMarkers(gray, dictionary, parameters=parameters)

        frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)
        target_id = 27
        if ids is not None:
            XLeft = corners[0][0][0][0]
            XRight = corners[0][0][2][0]
            YTop = corners[0][0][0][1]
            YBottom = corners[0][0][2][1]
            print(((XRight + XLeft)/ 2, (YTop + YBottom)/2))
            
        cv2.imshow('frame', frame_markers)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyWindow('frame')
    cap.release()
except KeyboardInterrupt:
    cv2.destroyWindow('frame')
    cap.release()