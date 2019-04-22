# -*- coding: utf-8 -*-
"""
udp_client.py
Created on Sat Apr 20 11:19:17 2019

@author: madhu
python udp_server.py
python udp_client.py
"""

import socket
from datetime import datetime
server_address = ('localhost', 6789)
max_size = 4096
print('Starting the client at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b'Hey!', server_address)
data, server = client.recvfrom(max_size)
print('At', datetime.now(), server, 'said', data)
client.close()
