import socket
import RPi.GPIO as g
import time

g.setmode(g.BOARD)
g.setup(12,g.OUT)

udp_ip="192.168.43.249"
udp_port=5007
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((udp_ip,udp_port))

while True:
	data,addr = sock.recvfrom(1024)
d=int(data)
if d ==1:
	g.output(12,g.HIGH)
elif d==0:
	g.output(12,g.LOW)

print "Received Message:",data