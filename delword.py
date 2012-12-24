# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 14:32:09 2012

@author: che
"""
######################删除文本里的字母数字等符号#####
import re, os
filelist=os.listdir('G:\\pdf\\lastest\\WTT')
while(len(filelist)>0):
    
    name=filelist.pop()
    path='G:\\pdf\\lastest\\WTT'+'\\'+name
    path2='G:\\pdf\\lastest\\WTT2'+'\\'+name
    content=open(path,'r')
    r = re.sub("[A-Za-z0-9\[\`\~\!\@\#\$\^\?\+\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%]", "", content.read())
    content2=open(path2,'w')
    content2.write(r)
    content.close()
    content2.close()

