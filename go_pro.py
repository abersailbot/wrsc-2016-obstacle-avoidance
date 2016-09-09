#!/usr/bin/env python

import cv2
import socket
import urllib2

GoProIP = "10.5.5.9"
GoProPort = 8554
Message = "_GPHD_:0:0:2:0\n"

urllib2.urlopen("http://{0}/gp/gpControl/execute?p1=gpStream&a1=proto_v2&c1=restart".format(GoProIP)).read()

capture = cv2.VideoCapture("udp://@{0}:{1}".format(GoProIP, GoProPort))

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(Message, (GoProIP, GoProPort))
    ret, img = capture.read()
    cv2.imshow('stream', img)
    cv2.waitKey(1)

cv2.destroyAllWindows()
