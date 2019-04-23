# -*- coding: utf-8 -*-
"""
tkinter_test.py
Errors out!
Created on Sat Apr 20 11:19:17 2019

@author: madhu

"""


import tkinter
from PIL import Image, ImageTk

#file_name = 'oreilly.png'
file_name = 'moustache2.png'

#%%
main = tkinter.Tk()
img = Image.open(file_name)
tkimg = ImageTk.PhotoImage(img)
tkinter.Label(main, image=tkimg).pack()
main.mainloop()
print('-'*30)
#%%
