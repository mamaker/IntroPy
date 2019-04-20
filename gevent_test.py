# -*- coding: utf-8 -*-
"""
gevent_test.py

Created on Sat Apr 20 09:17:11 2019

@author: madhu
"""
import gevent
from gevent import socket

hosts = ['www.crappytaxidermy.com', 'www.walterpottertaxidermy.com',
         'www.antique-taxidermy.com', 'www.google.com']
jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=20)
for job in jobs:
    print(job.value)
    