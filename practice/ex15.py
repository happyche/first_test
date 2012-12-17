# -*- coding: utf-8 -*-
"""
Created on Wed Sep 05 20:14:45 2012

@author: che
"""

filename=raw_input("input your file name:")
txt=open(filename)
print txt.read()
txt.close()