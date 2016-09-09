#!/usr/bin/env python

import cv2
import numpy as np

class obstacle_detector:
    def __init__(self):
	
	self.camera = cv2.VideoCapture(0)

    def check_for_obstacle(self):
	(_,frame) = self.camera.read()
	(_,frame) = self.camera.read()
	(_,frame) = self.camera.read()
	
	frame = cv2.imread("puc.png")
	mask = cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV), np.array((150,25,25)), np.array((255,200,200))) \
        + cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV), np.array((0,100,75)), np.array((40,250,255)))
	kernel = np.ones((5,5),np.uint8)
	mask = cv2.erode(mask,kernel,iterations=1)
	mask = cv2.dilate(mask,kernel, iterations=1)
	(cnts, _) = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(frame, cnts, -1, (0,255,0), 3)
	cv2.imshow("Keypoints", frame)
	cv2.waitKey(0)
	


if __name__ == '__main__':
    detector = obstacle_detector()
    detector.check_for_obstacle()
