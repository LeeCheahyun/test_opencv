import socket

sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

sender.sendto(str.encode('hello god boy'),('192.168.16.101',7778))
