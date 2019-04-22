# -*- coding: utf-8 -*-
"""
cap_doctst.py
>python cap_doctst.py -v
Created on Sat Apr 20 11:19:17 2019

@author: madhu

"""


def just_do_it(text):
    """
    >>> just_do_it('duck')
    'Duck'
    >>> just_do_it('a veritable flock of ducks')
    'A Veritable Flock Of Ducks'
    >>> just_do_it("I'm fresh out of ideas")
    "I'm Fresh Out Of Ideas"
    """
    from string import capwords

    return capwords(text)
#    return text.capitalize()
#    return text.title()

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
    text = "\"You're despicable,\" said Daffy Duck"
    result = just_do_it(text)
    print('text:', text)
    print('result:', result)
    print('-'*30)
#%%


if __name__ == '__main__':
    import doctest
    doctest.testmod()