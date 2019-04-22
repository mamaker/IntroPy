# -*- coding: utf-8 -*-
"""
zmq_sub.py
Created on Sat Apr 20 11:19:17 2019

@author: madhu
python zmq_sub.py
python zmq_pub.py
"""
import zmq

host = '127.0.0.1'
port = 6789
ctx = zmq.Context()
sub = ctx.socket(zmq.SUB)
sub.connect('tcp://%s:%s' % (host, port))
#topics = ['maine coon', 'persian']
topics = ['']
for topic in topics:
    sub.setsockopt(zmq.SUBSCRIBE, topic.encode('utf-8'))
print('Subscriber: Ready and listening, waiting...')
while True:
    cat_bytes, hat_bytes = sub.recv_multipart()
    cat = cat_bytes.decode('utf-8')
    hat = hat_bytes.decode('utf-8')
    print('Subscribe: %s wears a %s' % (cat, hat))

