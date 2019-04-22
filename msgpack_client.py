# -*- coding: utf-8 -*-
"""
msgpack_client.py
Created on Sat Apr 20 11:19:17 2019

@author: madhu
start /b python msgpack_server.py
python xmlrpc_client.py
"""
from msgpackrpc import Client, Address

host_name = 'localhost'
port_num = 6789

client = Client(Address(host_name, port_num))
num = 8
result = client.call('double', num)
print("Double %s is %s" % (num, result))

