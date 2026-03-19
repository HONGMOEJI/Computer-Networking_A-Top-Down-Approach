# In this example, comments are added to explain differences between TCP and UDP protocols.
from socket import socket, AF_INET, SOCK_STREAM

serverName = 'localhost'
serverPort = 12000

# Q: What SOCK_STREAM and SOCK_DGRAM mean?
# A: SOCK_STREAM is used for TCP socket, which provides a reliable, connection-oriented communication.
clientSocket = socket(AF_INET, SOCK_STREAM)

# A TCP connection must be established before any data are sent
# TCP connection is established by calling connect() method, and 3-way handshake is performed between client and server.
print('Client: starting TCP connection setup')
print('Client: connect() asks the OS to begin the TCP 3-way handshake')
clientSocket.connect((serverName, serverPort))
print('Client: TCP 3-way handshake completed, connection established')

message = input('What to send to server?: ')

clientSocket.send(message.encode())

modifiedMessage = clientSocket.recv(1024).decode()
print('From Server: ', modifiedMessage)

clientSocket.close()
