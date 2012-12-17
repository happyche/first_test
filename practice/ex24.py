# -*- coding: utf-8 -*-
"""
Created on Fri Sep 07 19:36:42 2012

@author: che
"""
print "Let's practice everything."
print"you'd need to konw......"
poem="""
aaaaaaaaaaaaaaaaaaaaaa
sssssssssssssssssssssss
ddddddddddddddddddddd
"""
print"------------------------"
print poem
print"------------------------"
five=10-2+3-6
print"this should be five:%s" %five
def secret_formulate(started):
    jelly_beans=started*500
    jars=jelly_beans/1000
    crates=jars/100
    return jelly_beans,jars,crates
start_point=10000
beans,jars,crates=secret_formulate(start_point)
print"with s starting point of:%d"%start_point
print"we'd have %d beans,%d jars,and %d crates."%(beans,jars,crates)
start_point=start_point/10
print"we can also do that this way:"
print"we'd have %d beans,%djars,and%d crates."%secret_formulate(start_point)