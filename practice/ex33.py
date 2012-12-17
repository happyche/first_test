# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 18:30:52 2012

@author: che
"""

i=0
number=[]
while i<6:
    print"the top i is %d" %i
    number.append(i)
    i=i+1
    print"numbers now:",number
    print"at the bottom is %d"%i
print"the number:"
for num in number:
        print num