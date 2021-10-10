#This code is used as fundation, and was found on https://realpython.com/python-sockets/ go check them out! They also explain the code very good!

import socket

#Starting a server on the IP you provide. You can use 127.0.0.1, or provide your IPV4 address. 
HOST = input("Provide IP of which server should start on (Don't use your public IP if you don't know what you are doing!): ")  # Standard loopback interface address (localhost)
PORT = int(input("Starting server on this port (Recommending that you use the port 65432): "))        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #Binding the Host to the port
    s.bind((HOST, PORT))
    #Listen for clients to connect
    s.listen()
    #The server accepts the connection (conn) from the address (addr)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            #If you want to send a message to the server from the client
            data = conn.recv(1024)
            #If there is no message
            if not data:
                break
            conn.sendall(data)
