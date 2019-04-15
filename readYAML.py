# -*- coding: utf-8 -*-
"""
readYAML.py
Created on Sat Apr 13 18:44:02 2019

@author: madhu
mcintyre.yaml (NO TABS PLEASE):
name:
    first: James
    last: McIntyre
dates:
    birth: 1828-05-25
    death: 1906-03-31
details:
    bearded: true
    themes: [cheese, Canada]
books:
    url: http://www.gutenberg.org/files/36068/36068-h/36068-h.htm
poems:
    - title: 'Motto'
      text: |
        Politeness, perseverance and pluck,
        To their possessor will bring good luck.
    - title: 'Canadian Charms'
      text: |
        Here industry is not in vain,
        For we have bounteous crops of grain,
        And you behold on every field
        Of grass and roots abundant yield,
        But after all the greatest charm
        Is the snug home upon the farm,
        And stone walls now keep cattle warm.

"""
import yaml
filename = 'mcintyre.yaml'
readmode = 'r'
textfile = 't'
modes = readmode+textfile
try:
    with open(filename, modes) as fin:
        text = fin.read()
    data = yaml.load(text)
    print('details:', data['details'])
    print('No. of poems:', len(data['poems']))
    print('Title of poem# 2:', data['poems'][1]['title'])
    print('Content of poem# 1:\n'+data['poems'][0]['text'])
    

except:
    print('Error accessing file %s ' % filename)
    

