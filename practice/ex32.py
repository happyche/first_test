# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 20:13:15 2012

@author: che
"""

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
for fruit in fruits:
    print"a fruit of type: %s"%fruit
element=[]
for i in range(0,7):
    print"Adding %d to the list"%i
    element.append(i)
for i in element:
    print"element was: %d"%i