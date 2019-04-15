# -*- coding: utf-8 -*-
"""
readXML.py
Created on Sat Apr 13 18:44:02 2019

@author: madhu
menu.xml:
<?xml version="1.0"?>
<menu>
	<breakfast hours="7-11">
		<item price="$6.00">breakfast burritos</item>
		<item price="$4.00">pancakes</item>
	</breakfast>
	<lunch hours="11-3">
		<item price="$5.00">hamburger</item>
	</lunch>
	<dinner hours="3-10">
		<item price="8.00">spaghetti</item>
	</dinner>
</menu>    
"""
import xml.etree.ElementTree as et
filename = 'menu.xml'
try:
    tree = et.ElementTree(file = filename)
    root = tree.getroot()
    for child in root:
        print('tag:', child.tag, '\tattributes:', child.attrib)
        for grandchild in child:
            print('\ttag:', grandchild.tag, '\tTEXT:', grandchild.text, '\tattributes:', grandchild.attrib)

except:
    print('Error accessing file %s ' % filename)


