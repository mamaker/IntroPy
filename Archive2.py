# -*- coding: utf-8 -*-
"""
Archive2.py
input: lolcats.com
       20190412 
Created on Sat Apr 13 10:57:36 2019

@author: madhu
"""

import webbrowser
import requests

print("Let's find an old website.")
site = input("Type a website URL: ")
era = input("Type a year, month, and day, like 20150613: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = requests.get(url)
data = response.json()
try :
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Found this copy: ", old_site)
    print("It should appear in your browser now.")
    webbrowser.open(old_site)
except :
    print("Sorry, no luck finding", site)