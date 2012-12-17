# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 17:36:00 2012

@author: che
"""

print "you enter a dark room with two doors.do you go through door #1 or door #2"
door=raw_input(">")
if door=="1":
    print"there's a giant bear here eating a cheese cake. what do you do?"
    print"1.take the cake"
    print"2.scream at the bear"
    bear=raw_input(">")
    if bear=="1":
        print"the bear eats your face off"
    elif bear=="2":
        print"the bear eats your legs off"
    else:
        print"well doing %s is probably better"%bear
elif door=="2":
    print"you stare into the endless abyss ..."
    print"1.bluederries"
    print"2.yellow jacket clothespins"
    print"3.uderstanding revolvers yelling melodies"
    insanity = raw_input("> ")
    if insanity=="1" or insanity=="2":
        print"your body surives powered by a mind of jello"
    else:
        print"...........good job"
else:
    print "You stumble around and fall on a knife and die.  Good job!"