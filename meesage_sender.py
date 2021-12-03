import socket

sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

sender.sendto(str.encode('hello kj'),('192.168.16.34',7778))
