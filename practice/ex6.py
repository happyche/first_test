# -*- coding: gbk -*-
"""
Created on Tue Sep 04 18:52:56 2012

@author: che
"""

#x="there are %d types of people" %10
#binary="binary"
#do_not="don't"
#y="those who know %s and those who %s."%(binary,do_not)
#print x+y
#a='flase'
#b="this is true? %r"
#print b %a
#dic={}
#data = [['01', '����'], ['02', '����'], ['03', 'None']]
#dic = dict(data)
#print dic
#from collections import defaultdict
##import fileinput
import cPickle as pickle
#import os
#dic=defaultdict(str)
#filelist=os.listdir('G:\\pdf\\test\\ENV')
#while(len(filelist)>0):
#    filename=filelist.pop()
#    to_read=open('G:\\pdf\\test\ENV\\'+filename,'r')
#    for i in to_read.read().split():
#        
#        dic[i]+="," +filename.encode('gbk')
#
#print dic['��ѧ']
##pickle.dump(dic,open('G:\\pdf\\test\\test.dump','w')) 
#     #### ���dump������ 
doc=pickle.load(open('G:\\pdf\\test\\test.dump','r'))
print doc['��ѧ']