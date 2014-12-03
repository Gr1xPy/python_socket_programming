#---------------------------------------------------------#
# Name: UDP Server
#
# Author: Konstantin Polyashenko
#
# Created: 11/12/2014
#---------------------------------------------------------#

import random
import socket
from socket import *
#create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM) #notice the use of SOCK_DGRAM for UDP packets 

serverSocket.bind(('', 12000)) #assign IP address and port number to socket 
while True:
	rand = random.randint(0, 10) #make random number from 1 to 10

	message, address = serverSocket.recvfrom(1024) #get client packet along with address its coming from
	# Capitalize the message from the client
	message = message.upper()

	#if rand is less is than 4, we consider the packet lost and do not respond 
	if rand < 4:
		continue
   #otherwise, the server responds
   serverSocket.sendto(message, address)