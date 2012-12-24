# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 16:42:32 2012

@author: che
"""


import os

def listfile(path):
    name = ""
    temppath = path
    filelist = os.listdir(temppath)

    while(len(filelist)>0):
        name = filelist.pop()
        subpath = temppath + "\\" +name
        try:
            sublist = os.listdir(subpath)
        except:
            continue
        
        to_write = open(name+'.txt','w')
        for f in sublist:
            to_read=open(subpath+"\\"+str(f),'r')
            to_write.write(to_read.read()+'\n')
            to_read.close()
     
        to_write.close()
   
listfile("G:\\pdf\\test")


