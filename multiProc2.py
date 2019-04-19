# -*- coding: utf-8 -*-
"""
multiProc2.py
Run from command line: python multiProc2.py
Created on Thu Apr 18 17:28:37 2019

@author: madhu
"""
import os
import multiprocessing
import time

def whoami(what):
    print("Process %s says: %s" % (os.getpid(), what))

def loopy(name):
    whoami(name)
    start = 1
    stop = 1000000
    for num in range(start, stop):
        print("\tNumber %s of %s. Honk!" % (num, stop))
        time.sleep(1)


#%%
if __name__ == "__main__":
    whoami("main")
    p = multiprocessing.Process(target=loopy, args=("loopy",))
    p.start()
    time.sleep(5)
    p.terminate()
    whoami("Back in main")
    
#%%

