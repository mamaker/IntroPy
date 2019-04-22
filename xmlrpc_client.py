# -*- coding: utf-8 -*-
"""
xmlrpc_client.py
Created on Sat Apr 20 11:19:17 2019

@author: madhu
start /b python xmlrpc_server.py
python xmlrpc_client.py
"""
import xmlrpc.client

host_name = "localhost"
port_num = 6789
proxy_server = 'http://'+host_name+':'+str(port_num)+'/'

#proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")
proxy = xmlrpc.client.ServerProxy(proxy_server)
num = 7
result = proxy.double(num)
print("Double %s is %s" % (num, result))
