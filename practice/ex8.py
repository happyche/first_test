# -*- coding: utf-8 -*-
"""
Created on Tue Sep 04 19:29:34 2012

@author: che
"""

formatter ="%r,%r,%r,%r"
print formatter %(1,2,3,4)
print formatter %("1","2","3","4")
print formatter %('1','2','3','4')
print formatter %("I had this thing.","That you could type up right.","But it didn't sing.","So I said goodnight.")