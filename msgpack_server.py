# -*- coding: utf-8 -*-
"""
msgpack_server.py
Created on Sat Apr 20 11:19:17 2019

@author: madhu
start /b python msgpack_server.py
python xmlrpc_client.py
"""
from msgpackrpc import Server, Address

class Services():
    def double(self, num):
        return num * 2

host_name = 'localhost'
port_num = 6789

server = Server(Services())
server.listen(Address(host_name, port_num))
server.start()
