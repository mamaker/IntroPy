# -*- coding: utf-8 -*-
"""
tcp_client.py
Created on Sat Apr 20 11:19:17 2019

@author: madhu
python udp_server.py
python udp_client.py
"""

import socket
from datetime import datetime
address = ('localhost', 6789)
max_size = 1000
print('Starting the client at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.sendall(b'Hey!')
data = client.recv(max_size)
print('At', datetime.now(), 'someone replied', data)
client.close()
