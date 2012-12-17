# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 17:38:02 2012

@author: che
"""

class TheThing(object):
    
    def __init__     (self):
        self.number = 0
        
    def some_function(self):
        print"I got called."
    
    def add_me_up(self,more):
        self.number += more
        return self.number
a=TheThing()
b=TheThing()
a.some_function()
b.some_function()
#a._init_()
#b._init_()
print a.add_me_up(20)
#print a.add_me_up(20)
print b.add_me_up(30)
#print b.add_me_up(30)
print a.number
print b.number

#class TheThing(object):
#
#    def __init__(self):
#        self.number = 0
#
#    def some_function(self):
#        print "I got called."
#
#    def add_me_up(self, more):
#        self.number += more
#        return self.number
#
## two different things
#a = TheThing()
#b = TheThing()
#
#a.some_function()
#b.some_function()
#
#print a.add_me_up(20)
#print b.add_me_up(30)
#
#print a.number
#print b.number