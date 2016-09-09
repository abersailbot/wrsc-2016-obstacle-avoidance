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

	mask = cv2.inRange(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV), np.array((0,125,125)), np.array((50,255,255)))
	kernel = np.ones((5,5),np.uint8)
	mask = cv2.erode(mask,kernel,iterations=1)
	mask = cv2.dilate(mask,kernel, iterations=5)
	detector = cv2.SimpleBlobDetector()
	keypoints = detector.detect(255-mask)
	im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (255,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	cv2.imshow("Keypoints", im_with_keypoints)
	cv2.waitKey(0)
	


if __name__ == '__main__':
    detector = obstacle_detector()
    detector.check_for_obstacle()
