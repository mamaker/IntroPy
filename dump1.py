# -*- coding: utf-8 -*-
"""
dump_test.py
Created on Sat Apr 20 11:19:17 2019

@author: madhu

"""


def dump(func):
    "Print input arguments and output value(s)"

    def wrapped(*args, **kwargs):
        print("Function name: %s" % func.__name__)
        print("Input arguments: %s" % ' '.join(map(str, args)))
        print("Input keyword arguments: %s" % kwargs.items())
        output = func(*args, **kwargs)
        print("Output:", output)
        return output
    return wrapped

