# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\che\.spyder2\.temp.py
"""

import os

def merge(path):

    x = [ item for item in os.walk(path)  ]
    for path, dirs, files in x:
        for file in files:
            print(path )
            
       
            file_to_write = open(path+'.txt','a')
            
        
            file_to_read=open(path+os.sep+str(file),'r')
            
            file_to_write.write(file_to_read.read()+'\n')
            
            
            file_to_read.close()
            file_to_write.close()
            
merge("G:\\pdf\\test123123123")

