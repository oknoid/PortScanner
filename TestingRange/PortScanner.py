#!/usr/bin/env/python3
import socket
import re

ip_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535
open_ports = []
close_filtered_ports = []

while True:
    ip_input = input("\nPlease enter the IP adress that you want to scan:")
    if ip_pattern.search(ip_input):
        print(f"{ip_input} is accepted")
        break
    else:
        print(f"{ip_input} is not accepted, please reenter")

while True:
    print("Please enter the range of ports you which to scan in format <int>-<int> (ex: 100-200)")
    port_input = input("Enter a range:")
    port_input_valid = port_pattern.search(port_input.replace(" ", ""))
    if port_input_valid:
        port_min = int (port_input_valid.group(1))
        port_max = int (port_input_valid.group(2))
        print("Please wait")
        break

for port in range(port_min, port_max+1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ip_input, port))
            open_ports.append(port)
    except:
        close_filtered_ports.append(port)
        

if close_filtered_ports:
    print("##########################\nRESULTS:")
    print(f"There are {len(close_filtered_ports)} closed ports.")
if open_ports:
    print(f"The open ports on {ip_input} are:")
    for port in open_ports:
        print(f"port {port} is open on {ip_input}")        


    