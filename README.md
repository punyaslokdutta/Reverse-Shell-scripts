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
Today's cryptosystems (such as TLS, Secure Shell) use both symmetric encryption and asymmetric encryption, often by using asymmetric encryption to securely exchange a secret key which is then used for symmetric encryption.

Reverse shells have multiple advantages to bind shells, particularly with evading detection and bypassing certain rule sets. Plus, having a port listening on a host that is not normal will, for the most part, trigger more alerts to system/network administrators. Whereas a reverse shell will just show up as a connection to an outside IP address,which will get caught less, especially with certain obfuscation techniques.

## Preventing Reverse Shells ##
Unless you are deliberately using reverse shells for remote administration, any reverse shell connections are likely to be malicious. Unfortunately, there’s also no surefire way of blocking reverse shell connections on a networked system, especially a server. You can mitigate the risk by selectively hardening your system:

1. To limit exploitation, you can lock down outgoing connectivity to allow only specific remote IP addresses and ports for the required services. This might be achieved by sandboxing or running the server in a minimal container. Another way could be to set up a proxy server with tightly controlled destination restrictions. However, considering that reverse shells can be created even over DNS, such hardening can only limit the risk of reverse shell connections, not eliminate it. 
2. To make attacks a little more difficult, you can remove all unnecessary tools and interpreters to prevent the execution of at least some reverse shell codes. However, this is usually not a practical option except for the most hardened and specialized servers, and a determined attacker will eventually find a working shell script anyway.
3. Regardless of the technicalities, once an attacker has a way of executing OS commands, the system should be considered compromised – so the best protection from reverse shells is to prevent exploitation in the first place. Shell scripts are typically executed by exploiting a code injection vulnerability, often followed by privilege escalation to obtain root privileges. To avoid these and other vulnerabilities, it’s vital to regularly patch your servers and web applications, and test them using a proven vulnerability scanner.

## Reverse Proxy (Ngrok/Cloudfared ) vs Load Balancer ##

![Reverse-proxy](https://user-images.githubusercontent.com/13198518/139104316-d25645d5-df26-49f8-b040-b8b8a1248b83.png)

They are often the same thing. But not always. When you refer to a load balancer you are referring to a very specific thing - a server or device that balances inbound requests across two or more web servers to spread the load. A reverse proxy, however, typically has any number of features:

1. Load balancing
2. Caching: it can cache content from the web server(s) behind it and thereby reduce the load on the web server(s) and return some static content back to the requester without having to get the data from the web server(s)
3. Security: it can protect the web server(s) by preventing direct access from the internet; it might do this through simple means by just obfuscating the web server(s) or it may have some more active components that actually review inbound requests looking for malicious code.
4. SSL acceleration: when SSL is used; it may serve as a termination point for those SSL sessions so that the workload of dealing with the encryption is offloaded from the web server(s)
#### It often makes sense to deploy a reverse proxy even with just one web server or application server, You can think of the reverse proxy as a website’s “public face.” .On the other hand, deploying load balancer makes sense when there are multiple web servers involved. ####

## Reverse Proxy vs API Gateway (From Microservice architecture POV) ##

![reverseProxywithNginx](https://user-images.githubusercontent.com/13198518/139108513-abe61b7a-bec5-496f-9889-640ed9230df0.png)

Think of an API gateway as a specific type reverse proxy implementation.
In regards to your questions, it is not uncommon to see the both used in conjunction where the API gateway is treated as an application tier that sits behind a reverse proxy for load balancing and health checking. An example would be something like a WAF sandwich architecture in that your Web Application Firewall/API Gateway is sandwiched by reverse proxy tiers, one for the WAF itself and the other for the individual microservices it talks to.

Reverse proxies are a critical component of microservices applications. They provide an externally reachable endpoint for services along with performance enhancements as mentioned above; in a Kubernetes environment, they are called Ingress Controllers. In addition to primary request routing, reverse proxies can provide more advanced routing functions such as load balancing, circuit breakers, rate limiting, A/B deployment, and canary testing. Service Meshes, more about these in a later article, utilize the advanced capabilities of proxies to enable their functionality. Some of the proxy implementations additionally offer simple tracing support, producing Zipkin or Jaeger (OpenTracing compliant) spans for the requests they route.



