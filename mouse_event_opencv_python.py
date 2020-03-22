import numpy as np
import cv2

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img,points[-1],points[-2],(250,0,0),3)
        cv2.imshow('image',img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_COMPLEX
        print(red)
        strXY = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img,strXY,(x,y),font,0.5,(0,250,0),2)
        cv2.imshow('image',img)
#img = np.zeros((512 , 512, 3),np.uint8)
img = cv2.imread('lena.jpg',1)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
points = []
cv2.waitKey(0)
cv2.destroyAllWindows()

