# -*- coding: utf-8 -*-
"""
zmq_client.py
Created on Sat Apr 20 11:19:17 2019

@author: madhu

>start /b python zmq_server.py
>python zmq_client.py
"""
import zmq
host = '127.0.0.1'
port = 6789
context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect("tcp://%s:%s" % (host, port))
for num in range(1, 6):
    request_str = "message #%s" % num
    request_bytes = request_str.encode('utf-8')
    client.send(request_bytes)
    reply_bytes = client.recv()
    reply_str = reply_bytes.decode('utf-8')
    print("Sent %s, received %s" % (request_str, reply_str))

print('ZMQ Client: Finished sending all requests to server.')
    