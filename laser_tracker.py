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


        min_green = np.array((40, 70, 100))
        max_green = np.array((80, 255, 255))
        res_mask = cv2.inRange(hsv, min_green, max_green)

        

        moments = cv2.moments(res_mask, 1)
        dm01 = moments['m01']
        dm10 = moments['m10']
        dArea = moments['m00']


        if dArea > 20:
            x = int(dm10/dArea)
            y = int(dm01/dArea)
            return (x, y)

        return (0, 0)

    
    def tracking_cycle(self):
        _, img = self.cap.read()
        gaus = cv2.GaussianBlur(img, (5, 5), 0)
        hsv = cv2.cvtColor(gaus, cv2.COLOR_BGR2HSV)

        min_white = ((0, 0, 240))
        max_white = ((255, 15, 255))
        res_white = cv2.inRange(hsv, min_white, max_white)

        min_blue = ((90, 68, 70))
        max_blue = ((137, 255, 255))
        res_blue = cv2.inRange(hsv, min_blue, max_blue)

        cv2.imshow('wrg', res_blue)
        cv2.imshow('cam', img)

        moments_white = cv2.moments(res_white, 1)
        dm01_white = moments_white['m01']
        dm10_white = moments_white['m10']
        dArea_white = moments_white['m00']

        moments_blue = cv2.moments(res_blue, 1)
        dm01_blue = moments_blue['m01']
        dm10_blue = moments_blue['m10']
        dArea_blue = moments_blue['m00']
        

      
        if dArea_white > 40:
            x_white = int(dm10_white/dArea_white)
            y_white = int(dm01_white/dArea_white)

        if dArea_blue > 30:
            x_blue = int(dm10_blue/dArea_blue)
            y_blue = int(dm01_blue/dArea_blue)
            return([x_blue, y_blue])
        else: return([0, 0])


            

        

    
    def cameraoff(self):
        cap.release()
        cv2.destroyAllWindows()

# contours, hiar = cv2.findContours(res_mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)