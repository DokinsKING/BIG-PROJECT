import re
import cv2
from cv2 import CAP_PROP_FPS
import numpy as np

class LaserTracker:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(CAP_PROP_FPS, 30)
        # self.cap.set(3, 1920)	 
        # self.cap.set(4, 1080)


    def cycle_laser(self, img):        
        gaus = cv2.GaussianBlur(img, (5, 5), 0)
        hsv = cv2.cvtColor(gaus, cv2.COLOR_BGR2HSV)



        min_green = np.array((40, 60, 70))
        max_green = np.array((60, 255, 255))
        res_mask = cv2.inRange(hsv, min_green, max_green)

        
        # cv2.imshow('rg', res_mask)
        # cv2.imshow('fgn', img)
        moments = cv2.moments(res_mask, 1)
        dm01 = moments['m01']
        dm10 = moments['m10']
        dArea = moments['m00']


        if dArea > 30:
            x = int(dm10/dArea) 
            y = int(dm01/dArea) 
            return [x, y]

        return [0, 0]

    
    def tracking_rect(self):
        hsv_min = ((90, 0, 0))
        hsv_max = ((150, 255, 255))

        # hsv_min = ((130, 30, 25))
        # hsv_max = ((165, 110, 55))


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
                cv2.imshow('rect', img)
                return[box.tolist(), True]


    def transform_rect(self, box):
        _, img = self.cap.read()
        pts1 = np.float32([box[1], box[0], box[2], box[3]])
        
        pts2 = np.float32([[0, 0], [0, 1234], [2194, 0], [2194, 1234]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        result = cv2.warpPerspective(img, matrix, (2194, 1234))

        # cv2.imshow('result', result)

        return result
        
            
       

       
        

    
    def cameraoff(self):
        cap.release()
        cv2.destroyAllWindows()

# contours, hiar = cv2.findContours(res_mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

