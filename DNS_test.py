# -*- coding: utf-8 -*-
"""
DNS_test.py
Created on Sat Apr 20 11:19:17 2019

@author: madhu

"""
import socket

#%%
print('-'*30)
web_site = 'www.crappytaxidermy.com'
ip_num = socket.gethostbyname(web_site)
print('web_site:', web_site, 'ip_num:', ip_num) 
#%%

#%%
print('-'*30)
web_site = 'www.crappytaxidermy.com'
hostbyname = socket.gethostbyname_ex(web_site)
print('web_site:', web_site, '\nhostbyname:', hostbyname) 
#%%

#%%
print('-'*30)
web_site = 'www.crappytaxidermy.com'
port_num = 80
addrinfo = socket.getaddrinfo(web_site, port_num)
print('web_site:', web_site, '\naddrinfo:', addrinfo) 
#%%
        
#%%
print('-'*30)
server = 'http'
port_num = socket.getservbyname(server)
print('server:', server, '\nport_num:', port_num) 
#%%

#%%
print('-'*30)
port_num = 80        
server = socket.getservbyport(port_num)
print('port_num:', port_num, '\nserver:', server) 
#%%
