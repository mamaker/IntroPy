# -*- coding: utf-8 -*-
"""
fab1.py
Needs further  configuring
Created on Sat Apr 20 11:19:17 2019

@author: madhu
fab -f fab1.py -H localhost iso
fab -c fab1.py -H localhost iso
"""


def iso():
    from datetime import date
    print(date.today().isoformat())
