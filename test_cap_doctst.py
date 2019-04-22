# -*- coding: utf-8 -*-
"""
test_cap_doctst.py
>python test_cap_doctst.py -v
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


if __name__ == '__main__':
    import doctest
    doctest.testmod()