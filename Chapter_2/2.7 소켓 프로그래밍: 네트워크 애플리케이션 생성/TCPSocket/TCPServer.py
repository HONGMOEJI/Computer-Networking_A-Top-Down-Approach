# In this example, comments are added to explain differences between TCP and UDP protocols.
from socket import socket, AF_INET, SOCK_STREAM

serverPort = 12000

# Create a TCP socket, AF_INET is used for IPv4 protocol, SOCK_STREAM is used for TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))

# Listen for incoming connections, the argument specifies the maximum number of queued connections
serverSocket.listen(1)
print('The server is ready to receive')
print('Server: listening on port 12000 and waiting for a TCP handshake')

while True:
    # Accept a connection, the server will block and wait until a client connects to it.
    print('Server: waiting in accept() until the client finishes the TCP handshake')
    connectionSocket, addr = serverSocket.accept()
    print('Server: TCP 3-way handshake completed')
    print('Connected by', addr)

    # Receive the message from the client, the message is received as bytes and must be decoded to string.
    message = connectionSocket.recv(1024).decode()
    print('Received from client: ', message)

    # Modify the message and send it back to the client, the message must be encoded to bytes.
    modifiedMessage = message.upper()
    connectionSocket.send(modifiedMessage.encode())

    # Close the connection socket
    connectionSocket.close()
