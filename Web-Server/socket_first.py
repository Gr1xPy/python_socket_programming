#---------------------------------------------------------#
# Name: Web-Server
# Purpose: Code creates a socket and defines a port number
#   then associates the port with the socket and tells 
#   server to listen to incoming requests. After a bit
#   of time it prints statenment declaring itself ready.
#
# Author: Konstantin Polyashenko
#
# Created: 10/20/2014
#---------------------------------------------------------#

#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM) #Prepare a sever socket

serverPort = 6789 #sets the port
serverSocket.bind(('', serverPort)) #associates the socket this port
serverSocket.listen(1)

while True:
    #Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept() #makes socket for this client
    
    try:
        message = connectionSocket.recv(1024) #receives message from client
        print message
        filename = message.split()[1]
        f = open(filename[1:]) #opens file and reads content
        outputdata = f.read()

        connectionSocket.send('\nHTTP/1.x 200 OK\n')

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i]) #outputs all the data in file
        connectionSocket.close() #closes the socket for this client
        print 'File Received'

    except IOError:
        #Send response message for file not found
        #sends error message to be printed on the page
        connectionSocket.send('\n404 File Not Found\n')

        #Close client socket
        connectionSocket.close() #closes the socket for the client
serverSocket.close() #closes the server socket
