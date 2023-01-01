#!/bin/python3

import sys
import socket
from datetime import datetime as Time

#Define Target

if len(sys.argv) == 4:
	target = socket.gethostbyname(sys.argv[1])	#translating the domain name to IPv4
else:
	print("Invalid amount of Argument")
	print("USAGE : python3 scanner.py <ip> <starting port> <end port>")
	
print("- - " * 17)

print("Scanning Target : " + target)
print("Time start : " + str(Time.now()))



try:
	for port in range(int(sys.argv[2]), int(sys.argv[3])):
		
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
	if result == 0:
		print(f"In Target {sys.argv[1]} port {port} is open")
		print("- - " * 17)
		s.close()
		

		
except KeyboardInterrupt:
	print("\n Exiting Program.")
	print("- - " * 17)
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	print("- - " * 17)
	sys.exit()

except socket.error:
	print("Could not connect to the server.")
	print("- - " * 17)
	sys.exit()
	
