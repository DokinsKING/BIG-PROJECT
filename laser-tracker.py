import cv2
import numpy as np
import pygame


cap = cv2.VideoCapture(0)
size = 500, 500
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
while True:
    _, img = cap.read()
    gaus = cv2.GaussianBlur(img, (5, 5), 0)
    hsv = cv2.cvtColor(gaus, cv2.COLOR_BGR2HSV)


    min_red1 = np.array((40, 70, 100))
    max_red1 = np.array((80, 255, 255))
    res_mask = cv2.inRange(hsv, min_red1, max_red1)

    contours, hiar = cv2.findContours(res_mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    moments = cv2.moments(res_mask, 1)
    dm01 = moments['m01']
    dm10 = moments['m10']
    dArea = moments['m00']


    if dArea > 20:
        x = int(dm10/dArea)
        y = int(dm01/dArea)
        pygame.draw.circle(screen, 'red', (x, y), 10)
        pygame.display.flip()
        
    cv2.drawContours(img, contours, -1, (0, 255, 0), 3)


    cv2.imshow('result', res_mask)
    # cv2.imshow('img', img)

    ch = cv2.waitKey(5)
    if ch == 27:
        break

cap.release()
cv2.destroyAllWindows()

