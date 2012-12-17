# -*- coding: utf-8 -*-
"""
Created on Mon Sep 03 20:20:50 2012

@author: che
"""

x = [ item for item in os.walk(path)  ] #os.walk递归地遍历所有子文件夹

#返回的是一个list，list中每一个元素由3个部分：(path, dirs, files)
    for path, dirs, files in x:
        for file in files:
                                    file_to_write = open(path+'.txt','a')
            print(path+'.txt')
        
            file_to_read=open(path+os.sep+str(file),'r')
                       file_to_write.write(file_to_read.read()+'\n')
           
            
            file_to_read.close()
            file_to_write.close()