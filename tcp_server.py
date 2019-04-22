# -*- coding: utf-8 -*-
"""
tcp_server.py
Created on Sat Apr 20 11:19:17 2019

@author: madhu
python udp_server.py
python udp_client.py
"""

from datetime import datetime
import socket
address = ('localhost', 6789)
max_size = 1000
print('Starting the server at', datetime.now())
print('Waiting for a client to call.')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)
client, addr = server.accept()
data = client.recv(max_size)
print('At', datetime.now(), client, 'said', data)
client.sendall(b'Are you talking to me?')
client.close()
server.close()