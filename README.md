# Reverse-Shell-scripts
A reverse shell is a shell session established on a connection that is initiated from a remote machine, not from the local host. Attackers who successfully exploit a remote command execution vulnerability can use a reverse shell to obtain an interactive shell session on the target machine and continue their execution.

![Architecture-2](https://user-images.githubusercontent.com/13198518/138933225-e9160bd6-5c99-476b-bcf0-36c705abbc38.png)

Reverse shell connection is usually established via TCP
protocol, but it has also been seen via ICMP protocol. The
connection can be made through any port, for example,
through port 80 and 443. This makes it difficulty for
firewall and other network parameter security solutions
to detect and block since they are usually allowed to be
open by default. When it uses port 443 (SSL), network
content cannot be inspected easily since it is encrypted. 

