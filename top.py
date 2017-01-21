
import cv2
import numpy as np
import copy

def nothing(x):
    pass


def hsvFilter(img,lowerHSV,upperHSV,returnMask=True):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array(lowerHSV)
    upper = np.array(upperHSV)
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    if returnMask:
        return mask
    else:
        return res

    
cv2.namedWindow('settings')
cap = cv2.VideoCapture(0)

cv2.createTrackbar('lower_H','settings',0,180,nothing)
cv2.createTrackbar('lower_S','settings',0,255,nothing)
cv2.createTrackbar('lower_V','settings',0,255,nothing)
cv2.createTrackbar('upper_H','settings',0,180,nothing)
cv2.createTrackbar('upper_S','settings',0,255,nothing)
cv2.createTrackbar('upper_V','settings',0,255,nothing)

cv2.setTrackbarPos('lower_H','settings',68)
cv2.setTrackbarPos('lower_S','settings',27)
cv2.setTrackbarPos('lower_V','settings',50)
cv2.setTrackbarPos('upper_H','settings',103)
cv2.setTrackbarPos('upper_S','settings',255)
cv2.setTrackbarPos('upper_V','settings',180)

switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'settings',0,1,nothing)
   
while(1):
    _, frame = cap.read()
    
    lowH = cv2.getTrackbarPos('lower_H','settings')
    lowS = cv2.getTrackbarPos('lower_S','settings')
    lowV = cv2.getTrackbarPos('lower_V','settings')
    upH = cv2.getTrackbarPos('upper_H','settings')
    upS = cv2.getTrackbarPos('upper_S','settings')
    upV = cv2.getTrackbarPos('upper_V','settings')
    
    mask = hsvFilter(frame,[lowH,lowS,lowV],[upH,upS,upV],True)
    eroded = cv2.erode(mask,None,iterations=3)
    dilated = cv2.dilate(eroded,None,iterations=3)

    final = copy.copy(dilated)
    
    im2, contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    contourAreas = []
    for contour in contours:
        contourAreas.append((contour,cv2.contourArea(contour)))
    contourAreas.sort(key=lambda tup: tup[1])
    if len(contourAreas)>1:
        print(contourAreas[-1][1])
        print(contourAreas[-2][1])

    cv2.imshow('frame',frame)
    cv2.imshow('mask',final)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()



