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

## Reverse Proxy (Ngrok/Cloudfared ) vs Load Balancer ##

![Reverse-proxy](https://user-images.githubusercontent.com/13198518/139104316-d25645d5-df26-49f8-b040-b8b8a1248b83.png)

They are often the same thing. But not always. When you refer to a load balancer you are referring to a very specific thing - a server or device that balances inbound requests across two or more web servers to spread the load. A reverse proxy, however, typically has any number of features:

1. Load balancing

2. Caching: it can cache content from the web server(s) behind it and thereby reduce the load on the web server(s) and return some static content back to the requester without having to get the data from the web server(s)

3. Security: it can protect the web server(s) by preventing direct access from the internet; it might do this through simple means by just obfuscating the web server(s) or it may have some more active components that actually review inbound requests looking for malicious code.
#### It often makes sense to deploy a reverse proxy even with just one web server or application server. You can think of the reverse proxy as a website’s “public face.” ####

4. SSL acceleration: when SSL is used; it may serve as a termination point for those SSL sessions so that the workload of dealing with the encryption is offloaded from the web server(s)
