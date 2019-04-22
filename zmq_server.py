# -*- coding: utf-8 -*-
"""
zmq_server.py
Created on Sat Apr 20 11:19:17 2019

@author: madhu

>start /b python zmq_server.py
>python zmq_client.py
"""
import zmq

host = '127.0.0.1'
port = 6789
context = zmq.Context()
server = context.socket(zmq.REP)
server.bind("tcp://%s:%s" % (host, port))
print('ZMQ Server: Ready, Waiting for request from client')
while True:
    # Wait for next request from client
    request_bytes = server.recv()
    request_str = request_bytes.decode('utf-8')
    print("That voice in my head says: %s" % request_str)
    reply_str = "Stop saying: %s" % request_str
    reply_bytes = bytes(reply_str, 'utf-8')
    server.send(reply_bytes)