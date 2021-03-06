#!/usr/bin/env python

import cv2
import numpy as np
import socket
import urllib2

GoProIP = "10.5.5.9"
GoProPort = 8554
Message = "_GPHD_:0:0:2:0\n"

print 'sending message to gopro'
urllib2.urlopen("http://{0}/gp/gpControl/execute?p1=gpStream&a1=proto_v2&c1=restart".format(GoProIP)).read()

print 'opening capture'
capture = cv2.VideoCapture("udp://@{0}:{1}".format(GoProIP, GoProPort))

def _process_image(img):
    print 'processing image'
    mask = cv2.inRange(cv2.cvtColor(img, cv2.COLOR_BGR2HSV), np.array((150,25,25)), np.array((255,200,200))) \
    + cv2.inRange(cv2.cvtColor(img, cv2.COLOR_BGR2HSV), np.array((0,100,75)), np.array((40,250,255)))
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.erode(mask,kernel,iterations=1)
    mask = cv2.dilate(mask,kernel, iterations=1)
    (cnts, _) = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, cnts, -1, (0,255,0), 3)
    cv2.imshow("Keypoints", img)
    cv2.waitKey(1)


def is_obstacle_detected():
    print 'opening socket to gopro'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(Message, (GoProIP, GoProPort))
    print 'reading from gopro'
    for i in range(30):
        ret, img = capture.read()
    return _process_image(img)
