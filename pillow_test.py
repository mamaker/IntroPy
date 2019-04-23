# -*- coding: utf-8 -*-
"""
pillow_test.py
Created on Sat Apr 20 11:19:17 2019

@author: madhu

"""


from PIL import Image

#file_name = 'oreilly.png'
file_name = 'BruceLee101.jpg'
#%%
img = Image.open(file_name)
print('File', file_name,'is a type', img.format, 'file,')
print('of size:',img.size, ', mode:',img.mode)
img.show()
print('-'*30)
#%%

#%%
crop = (185, 0, 575, 430)
img2 = img.crop(crop)
fil2_name = 'BruceLee25.gif'
save_format = 'GIF'
img2.save(fil2_name, save_format)
img2.show()
print('-'*30)
#%%

#%%
img3 = Image.open(fil2_name)
print('File', fil2_name,'is a type', img3.format, 'file,')
print('of size:',img3.size, ', mode:',img3.mode)
print('-'*30)
#%%

#%%
print('opening mustache file:')
fil4_name = 'moustache2.png'
mustache = Image.open(fil4_name)
mustache.show()
print('-'*30)
#%%

#%%
print('Pasting mustache on BruceLee image:')
img.paste(mustache, (250, 270) )
img.show()
print('-'*30)
#%%
