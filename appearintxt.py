# -*- coding: utf-8 -*-
"""
Created on Thu Nov 08 11:09:36 2012

@author: che
"""

############每个词都出现在哪篇文档中#######
from collections import defaultdict

import cPickle as pickle
import os
dic=defaultdict(str)
filelist=os.listdir('G:\\pdf\\lastest\\LAW')
while(len(filelist)>0):
    filename=filelist.pop()
    to_read=open('G:\\pdf\\lastest\\LAW\\'+filename,'r')
    
    for i in to_read.read().split():
        
        dic[i]+= filename+','

#print dic
pickle.dump(dic,open('G:\\pdf\\lastest\\appearintxt\\LAW2.dump','w')) 
     #### 输出dump的内容 
#doc=pickle.load(open('G:\\pdf\\test\\ENV.dump','r'))
#print doc