import sys
import threading
import time
import socket

usage = "python3 port_scan.py TARGET START_PORT END_PORT"

if (len(sys.argv) != 4):
	print(usage)
	sys.exit()

try:
	target = socket.gethostbyname(sys.argv[1])
except socket.guierror:
	print("Name resolution error")
	sys.exit()

print("Scanning target: ", target)

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

def scan_port(port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(5)
	conn = s.connect_ex((target, port))
	if(not conn):
		print("Port is {} open".format(port))
	s.close()

for port in range(start_port, end_port+1):
	thread = threading.Thread(target = scan_port, args = (port,))
	thread.daemon = True
	thread.start()