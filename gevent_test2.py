# -*- coding: utf-8 -*-
"""
gevent_test.py

Created on Sat Apr 20 09:17:11 2019

@author: madhu
"""
import gevent
from gevent import monkey; monkey.patch_all()
import socket

hosts = ['www.crappytaxidermy.com', 'www.walterpottertaxidermy.com',
         'www.antique-taxidermy.com', 'www.cnn.com', 'www.gmail.com']
jobs = [gevent.spawn(socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5000)
for job in jobs:
    print(job.value)
    