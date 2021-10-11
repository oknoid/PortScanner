
import socket

def tryPort():
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

def tryPortRange():
	PORTSTART = int(input("Target Start Port: "))
	PORTEND = int(input("Target End Port:"))

	portdata = []
	#Input information about IP and Port which is going to be used to try to connect to target
	SERVER = input("Target IP: ")

	#Creating a client which requests services 
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	for port in range(PORTSTART,PORTEND):
		ADDR = (SERVER,int(port))
		try: 
			#Try to connect to the Server at the given port
			client.connect(ADDR)
			portdata.append(port)
		except:
			None
	print("Found Ports: ")
	for i in portdata:
		print(i)

def main():
	multipleports = input("Portrange? Y/N: ")
	if multipleports == "N":
		tryPort()

	if multipleports == "Y":
		tryPortRange()

if __name__ == "__main__":
    main()
