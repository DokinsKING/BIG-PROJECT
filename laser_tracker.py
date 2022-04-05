import cv2
import numpy as np
import pygame

class LaserTracker:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.x = 0
        self.y = 0
        

    def cycle_laser(self):
        
        _, img = self.cap.read()
        gaus = cv2.GaussianBlur(img, (5, 5), 0)
        hsv = cv2.cvtColor(gaus, cv2.COLOR_BGR2HSV)


        min_green = np.array((40, 70, 100))
        max_green = np.array((80, 255, 255))
        res_mask = cv2.inRange(hsv, min_green, max_green)

        # contours, hiar = cv2.findContours(res_mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        moments = cv2.moments(res_mask, 1)
        dm01 = moments['m01']
        dm10 = moments['m10']
        dArea = moments['m00']


        if dArea > 20:
            self.x = int(dm10/dArea)
            self.y = int(dm01/dArea)
            return (self.x, self.y)

        return (0, 0)
    
    def cameraoff(self):
        cap.release()
        cv2.destroyAllWindows()