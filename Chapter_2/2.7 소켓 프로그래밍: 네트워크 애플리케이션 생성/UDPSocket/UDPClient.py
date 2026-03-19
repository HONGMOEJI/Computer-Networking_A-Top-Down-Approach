# import socket module
from socket import socket, AF_INET, SOCK_DGRAM

# Server's IP address and port number
serverName = 'localhost'
serverPort = 12000

# Create a UDP socket. AF_INET is used for IPv4 protocol, SOCK_DGRAM is used for UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Get user's input
message = input('What to send to server?: ')


# Send the message to the server, the message must be encoded to bytes.
# Q: Why messages that are sent through the network must be encoded to bytes?
# A: The network can only transmit data in bytes, so any data that we want to send over the network must be converted as bytes.
# sendto() explicitly receives only the destination address. The client's source IP
# and source port are not passed here as arguments; the OS kernel fills them into
# the UDP/IP headers based on the local socket state and routing decision.
clientSocket.sendto(message.encode(), (serverName, serverPort))

# Receive the modified message from the server, the message is received as bytes and must be decoded to string.
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print('From Server: ', modifiedMessage.decode())

# Close the socket
clientSocket.close()