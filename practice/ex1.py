# -*- coding: gbk -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\che\.spyder2\.temp.py
"""


############ÿ���ʶ���������ƪ�ĵ���#######
from collections import defaultdict

import cPickle as pickle
import os
dic=defaultdict(str)
filelist=os.listdir('G:\\pdf\\test\\ENV')
while(len(filelist)>0):
    filename=filelist.pop()
    to_read=open('G:\\pdf\\test\ENV\\'+filename,'r')
    
    for i in to_read.read().split():
        
        dic[i]+= filename+','

#print dic
pickle.dump(dic,open('G:\\pdf\\test\\ENV.dump','w')) 
     ### ���dump������ 
doc=pickle.load(open('G:\\pdf\\test\\ENV.dump','r'))
print set(doc['����'].split(','))