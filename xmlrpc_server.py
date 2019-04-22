# -*- coding: utf-8 -*-
"""
xmlrpc_server.py
Created on Sat Apr 20 11:19:17 2019

@author: madhu
start /b python xmlrpc_server.py
python xmlrpc_client.py
"""
from xmlrpc.server import SimpleXMLRPCServer

def double(num):
    return num * 2

host_name = "localhost"
port_num = 6789
server = SimpleXMLRPCServer((host_name, port_num))
server.register_function(double, "double")
server.serve_forever()

print('xmlrpc_server: Ready and Waiting to serve function...')
