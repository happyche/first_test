# -*- coding: utf-8 -*-
"""
Created on Thu Nov 08 11:09:36 2012

@author: che
"""
####### 结巴分词功能 ###########

import jieba, os
def cutword(path):
    
    name=""
    filelist=os.listdir(path)
    while(len(filelist)>0):
        name=filelist.pop()
        subpath=path+"\\"+name
        subfilelist=os.listdir(subpath)
        
        for f in subfilelist:
            to_read=open(subpath+"\\"+str(f),'r')
            content=jieba.cut(to_read.read(),cut_all=False)   #默认模式
            to_write=open(subpath+"\\"+str(f),'w')
            newcontent=" ".join(content)
            to_write.write(newcontent)
            to_read.close()
            to_write.close()

cutword("G:\\pdf\\lastest")
