# -*- coding: utf-8 -*-
"""
Created on Thu Sep 06 19:29:51 2012

@author: che
"""

from sys import argv
script,input_file=argv
def print_all(f):
    print f.read()
def rewind(f):
    f.seek(0)
def print_a_line(line_count,f):
    print line_count,f.readline()
current_file=open(input_file)
print_all(current_file)
rewind(current_file)
line_count2= raw_input("input the line:")

print_a_line(line_count2,current_file)
line_count2= raw_input("input the line:")

print_a_line(line_count2,current_file)
line_count2= raw_input("input the line:")

print_a_line(line_count2,current_file)
