import socket
import cv2


cap= cv2.VideoCapture(0)

sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

perlength = int( (480 * 640 * 3) / 20)
reallength = perlength + 1

# bytes([i]) + str[i*perlength:(i+1)*perlength]


while cap.isOpened():
    ret , frame = cap.read()
    mat = cv2.resize(frame,(480,640))
    num = mat.flatten()
    str = num.tostring()
    for i in range(20):
        sender.sendto(bytes([i]) + str[i*perlength:(i+1)*perlength],('192.168.16.101',7778))
        pass
    pass



