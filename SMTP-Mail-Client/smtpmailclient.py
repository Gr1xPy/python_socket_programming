#---------------------------------------------------------#
# Name: SMTP Mail Client
# Purpose: simple mail client that sends email recipients
#	the client connects to mail server, talk with it using
#	SMTP protocol and send email message to mail server
#
# Author: Konstantin Polyashenko
#
# Created: 12/01/2014
#---------------------------------------------------------#

from socket import*
msg="\r\n I love computer networks!"
endmsg="\r\n.\r\n"

#choose a mail server and call it mailserver
mailserver = 'gaia.ecs.csus.edu'

#create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver,25))#establish TCP connection with mail server

recv=clientSocket.recv(1024)

print recv

if recv[:3]!='220':
    print '220 reply not received from server.'

#send HELO command and print server response.
heloCommand='HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1=clientSocket.recv(1024)
print recv1
if recv1[:3]!='250':
    print '250 reply not received from server.'

#send MAIL FROM command and print server response.
clientSocket.send('MAIL FROM: <kman239@gmail.com>\r\n')
recv2 = clientSocket.recv(1024)
print recv2

#send RCPT TO command and print server response.
clientSocket.send('RCPT TO: <kman239@gmail.com>\r\n')
recv2 = clientSocket.recv(1024)
print recv2

clientSocket.send('RCPT TO: <kman239@gmail.com>\r\n')
recv2 = clientSocket.recv(1024)
print recv2

#Send DATA command and print server response.
clientSocket.send('DATA\r\n')
recv2 = clientSocket.recv(1024)
print recv2

#send message data
clientSocket.send(msg)

#message ends with a single period.
clientSocket.send(endmsg)

#send QUIT command and get server response.
clientSocket.send('QUIT\r\n')
recv2 = clientSocket.recv(1024)
print recv2