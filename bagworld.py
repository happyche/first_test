# -*- coding: utf-8 -*-
"""
Created on Fri Nov 09 21:13:10 2012

@author: che

"""

from gensim import corpora
import  cPickle as pickle
import os
filelist=os.listdir("G:\\pdf\\lastest\\WTT")
stoppath="G:\\pdf\\停用词.txt".decode('utf8')  
contentlist=[]

while(len(filelist)>0):
    name=filelist.pop()
    path="G:\\pdf\\lastest\\WTT"+"\\"+name
    contents=open(path,'r')
    contentlist.append(contents.read())
    contents.close()

words=open(stoppath,'r')
stoplist=(words.read().split())
text=[[word for word in content.lower().split() if word not in stoplist]for content in contentlist]
#print text
####移去只出现一次的词
#all_tokens = sum(text, [])
#tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
#text = [[word for word in texts if word not in tokens_once]
#        for texts in text]

dictionary=corpora.Dictionary(text)
#print '{' + ', '.join(map(lambda kv_pair: "'%s': %s" % kv_pair, dictionary.token2id.iteritems())) + '}'
corpus = [dictionary.doc2bow(texts) for texts in text]
#print corpus
       ###########dump到一个文件中
pickle.dump(corpus,open('G:\\pdf\\test\\ENV.dump','w')) 
     #### 输出dump的内容 
doc=pickle.load(open('G:\\pdf\\test\\ENV.dump','r'))
print doc 
