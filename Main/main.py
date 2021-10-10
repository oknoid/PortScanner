
import socket

#Input information about IP and Port which is going to be used to try to connect to target
SERVER = input("Target IP: ")
PORT = int(input("Target Port: "))
ADDR= (SERVER,PORT)

#Creating a client which requests services 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try: 
	#Try to connect to the Server at the given port
	client.connect(ADDR)
	print("Successfully detected open port!")
except:
	print("Failed to connect to server...")
