# -*- coding: utf-8 -*-
"""
Created on Wed Sep 05 19:46:06 2012

@author: che
"""

from sys import argv
script,user_name=argv
prompt='>'
print"hi is %s,i'm the %s script."%(user_name,script)
print"i'd like to ask you a few question."
print"do you like me %s "%user_name
like=raw_input(prompt)
print"where do you like live %s"%user_name
live=raw_input(prompt)
print"what kind of computer do you have?"
computer=raw_input(prompt)
print"""so you said %r about liking me.
you live in %r.
And you have a %r computer. nice.
"""%(like,live,computer)