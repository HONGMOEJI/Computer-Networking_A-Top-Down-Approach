from socket import socket, AF_INET, SOCK_DGRAM

# Server port number
serverPort = 12000

# Create a UDP socket. AF_INET is used for IPv4 protocol, SOCK_DGRAM is used for UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the socket to the server address and server port
# Q: Why do we need to bind the socket to an address and port?
# A: Binding the socket to an address and port allows the server to listen for incoming messages
# Q2: What binding means?
# A2: Binding is the process of associating a socket with a specific local IP address and port number. 
#     This allows the server to listen for incoming messages on that address and port.
serverSocket.bind(('', serverPort))

while True:
    # Wait for a client to send a message, the message is received as bytes and must be decoded to string.
    message, clientAddress = serverSocket.recvfrom(2048)

    # Convert the message from bytes to string and convert it to uppercase
    modifiedMessage = message.decode().upper()

    # Send the modified message back to the client, the message must be encoded to bytes.
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)