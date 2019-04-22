# -*- coding: utf-8 -*-
"""
cap.py
Created on Sat Apr 20 11:19:17 2019

@author: madhu

"""


def just_do_it(text):
    from string import capwords

    return capwords(text)
#    return text.capitalize()
#    return text.title()

def just_do_it_main():
    print('Doing just_do_it_main()')
    print('-'*30)

#%%
    text = 'duck'
    result = just_do_it(text)
    print('text:', text)
    print('result:', result)
    print('-'*30)
#%%

#%%
    text = 'a veritable flock of ducks'
    result = just_do_it(text)
    print('text:', text)
    print('result:', result)
    print('-'*30)
#%%
    
#%%
    text = "I'm fresh out of ideas"
    result = just_do_it(text)
    print('text:', text)
    print('result:', result)
    print('-'*30)
#%%

#%%
    text = '''"You're despicable," said Daffy Duck'''
    result = just_do_it(text)
    print('text:', text)
    print('result:', result)
    print('-'*30)
#%%


if __name__ == '__main__':
    just_do_it_main()