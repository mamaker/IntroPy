# -*- coding: utf-8 -*-
"""
dishes.py
Errors out
Spyder Editor

This is a temporary script file.
"""
import multiprocessing as mp

def washer(dishes, output):
    for dish in dishes:
        print('Washing', dish, 'dish')
        output.put(dish)

def dryer(input):
    while True:
        dish = input.get()
        print('Drying', dish, 'dish')
        input.task_done()

dish_queue = mp.JoinableQueue()
dryer_proc = mp.Process(target=dryer, args=(dish_queue,))

dishes = ['salad', 'bread', 'entree', 'dessert']
washer(dishes, dish_queue)
dryer_proc.start()
dish_queue.join()
