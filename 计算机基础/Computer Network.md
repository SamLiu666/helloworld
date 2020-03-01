# Network
- [概述](计算机网络%20-%20概述.md)
- [物理层](计算机网络%20-%20物理层.md)
- [链路层](计算机网络%20-%20链路层.md)
- [网络层](计算机网络%20-%20网络层.md)
- [传输层](计算机网络%20-%20传输层.md)
- [应用层](计算机网络%20-%20应用层.md)
- 
__Internet__: connect the network of the world
__ISP__:Internet Service Provider
__Communication__: C/S-client and server    P2P--peer to peer
Application layer:DNS(port 53), FTP(20), DHCP, TELNET,SMTP
transport layer:communicate, UDP TCP,3-connect 4 -disconnect
network layer: IP contract, ARP, ICMP:ping, traceroute, VPN, NAT, Route-RIP_OSPF_BGP
data link layer:frame, local network, MAC address
physical layer: byte

[Summary of knowledge](https://github.com/Snailclimb/JavaGuide/blob/master/docs/network/%E5%B9%B2%E8%B4%A7%EF%BC%9A%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C%E7%9F%A5%E8%AF%86%E6%80%BB%E7%BB%93.md#%E4%B8%80%E8%AE%A1%E7%AE%97%E6%9C%BA%E6%A6%82%E8%BF%B0)
应用	应用层协议	端口号	传输层协议	备注
域名解析	DNS	53	UDP/TCP	长度超过 512 字节时使用 TCP
动态主机配置协议	DHCP	67/68	UDP	
简单网络管理协议	SNMP	161/162	UDP	
文件传送协议	FTP	20/21	TCP	控制连接 21，数据连接 20
远程终端协议	TELNET	23	TCP	 
超文本传送协议	HTTP	80	TCP	
简单邮件传送协议	SMTP	25	TCP	
邮件读取协议	POP3	110	TCP	
网际报文存取协议	IMAP	143	TCP	