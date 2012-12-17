# -*- coding: utf-8 -*-
"""
Created on Wed Sep 05 21:16:54 2012

@author: che
"""

txt=raw_input("input the file")
target=open(txt,"w")           #打开文件执行读命令
print"truncating the file"
target.truncate()
print"now i will input some sentence"
line1=raw_input("the first line")
line2=raw_input("the second line")
line3=raw_input("the third line")
print"i will write to the file"
target.write(line1+"\n"+line2+"\n"+line3)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.close()
target=open(txt)               #必须从新打开文件才能读
print target.read()