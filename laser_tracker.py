import re
import cv2
from cv2 import CAP_PROP_FPS
import numpy as np

class LaserTracker:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(CAP_PROP_FPS, 30)

    def cycle_laser(self):
        _, img = self.cap.read()



        
        gaus = cv2.GaussianBlur(img, (5, 5), 0)
        hsv = cv2.cvtColor(gaus, cv2.COLOR_BGR2HSV)



        min_green = np.array((50, 50, 60))
        max_green = np.array((100, 255, 255))
        res_mask = cv2.inRange(hsv, min_green, max_green)

        
        cv2.imshow('rg', res_mask)
        cv2.imshow('fgn', img)
        moments = cv2.moments(res_mask, 1)
        dm01 = moments['m01']
        dm10 = moments['m10']
        dArea = moments['m00']


        if dArea > 50:
            x = int(dm10/dArea) 
            y = int(dm01/dArea) 
            return [x, y]

        return [0, 0]

    
    def tracking_rect(self):
        hsv_min = ((90, 70, 50))
        hsv_max = ((150, 255, 255))


        _, img = self.cap.read()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, hsv_min, hsv_max)
        contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.round(np.int0(box))
            area = int(rect[1][0]*rect[1][1])
            if area > 30000:
                cv2.drawContours(img, [box], 0, (255, 0, 0), 2)
                # cv2.imshow('contours', img)
                return[box[0].tolist(), True]
            
       

       
        

    
    def cameraoff(self):
        cap.release()
        cv2.destroyAllWindows()

# contours, hiar = cv2.findContours(res_mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

