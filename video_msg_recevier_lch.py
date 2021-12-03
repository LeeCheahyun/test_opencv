import socket
import numpy as np
import cv2 as cv

reciver = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
reciver.bind(('192.168.16.27',7778))

# 480 * 640 * 3 / 20 = 46080
perlength = int( (480 * 640 * 3) / 20)
reallength = perlength + 1

array = list()
while True:
    message, address = reciver.recvfrom(1024)
    # message = bytepair[0]
    # address = bytepair[1]

    array[message[0]] = message[1:46081]
    num_array = b''
    if message[0] == 19:
        for i in range(20):
            num_array += array[i]
        frame = np.fromstring(num_array, dtype =np.uint8)
        frame = frame.reshape(480,640,3)
        cv.imshow('video reciver', frame)
        pass
pass
    # print(message, ', ', address)

    # arr = message