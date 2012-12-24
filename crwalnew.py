# -*- coding: utf-8 -*-
import urllib
import urllib2
from urlparse import urljoin
from BeautifulSoup import BeautifulSoup
import re
import os

def crawl(webside,depth=2): #深度为两层
    value=0    #后面用来标记循环是否结束
    container=[]
    path=r'D:\newdata' #文件的根目录
    for d in range(depth): 
        value=0        #第一次执行时值为0
        newpages=set()
        urllist=[]     
        folderlist=[]
        for web in webside:
            print web
            if d == 1: #在第二层时执行
                filename=str(int(web.split('/')[-1][4:6])+1987) #从url中提取字符串作为文件夹名
                lastfile=web
                folderpath=str(path+'\\'+filename) #文件夹的路径
                lastfolder=folderpath
                urllist.append(lastfile) #将循环中每个网址加入该列表
                folderlist.append(lastfolder) #将循环中每个文件夹路径加入列表
                print filename
                print folderpath
                os.chdir(path) 
                print value
                if os.path.exists(folderpath): #判断该文件夹是否存在
                    if web==list(webside)[-1]: #如果是最后一个网址
                        pass
                    else:
                        continue #结束本次循环
                elif web==list(webside)[0]: #如果是第一个网址
                    pass
                else:
                    if value==1: #如果某次循环正确结束，即某个文件夹的文件已全部下完，需要下载下一个文件夹
                        pass
                    else:
                        os.chdir(folderlist[-2]) #取出该已创建但未下完的文件夹继续下载
                        c1=urllib2.urlopen(urllist[-2])
                        soup=BeautifulSoup(c1.read())
                        print soup
                        links=soup('a')
                        #print links
                        for link in links:
                            if ('href' in dict(link.attrs)):
                                url=urljoin(urllist[-2],link['href'])
                                if url.find("'")!=-1:
                                    continue
                                url=url.split('#')[0]
                                if url[0:4]=='http':
                                    if re.match("http://books.nips.cc/papers/files/nips../.+pdf$",url) and\
                                    'slide' not in url and 'spotlight' not in url:
                                        try:
                                            webFile = urllib.urlopen(url)
                                        except:
                                            continue
                                        if os.path.exists(folderlist[-2]+'\\'+url.split('/')[-1]): #判断该文件是否存在
                                            if os.path.getsize(folderlist[-2]+'\\'+url.split('/')[-1]) == 0: 
                                                #若该文件存在但未下载完成
                                                os.remove((folderlist[-2]+'\\'+url.split('/')[-1]))
                                                #删除该文件，从新下载
                                            else:
                                                continue
                                        localFile = open(url.split('/')[-1], 'wb')
                                        localFile.write(webFile.read())
                                        webFile.close()
                                        localFile.close()
                os.chdir(path)
                if os.path.exists(folderpath):
                    pass
                else:
                    os.mkdir(filename)
                os.chdir(filename)
            try:
                c=urllib2.urlopen(web)
                soup=BeautifulSoup(c.read())
                links=soup('a')
            except:
                continue
            for link in links:
                if ('href' in dict(link.attrs)):
                    url=urljoin(web,link['href'])
                    if url.find("'")!=-1:continue
                    url=url.split('#')[0]
                    if url[0:4]=='http' and re.match("http://books.nips.cc/nips.+html",url):
                        newpages.add(url)
                        
                    if d==1:
                        if re.match("http://books.nips.cc/papers/files/nips../.+pdf$",url) and\
                        'slide' not in url and 'spotlight' not in url:
                            if url not in container: #判断网址是否已存在
                                container.append(url)
                                try:
                                    webFile = urllib.urlopen(url)
                                except:
                                    continue
                                if os.path.exists(folderpath+'\\'+url.split('/')[-1]): #判断文件是否已存在
                                    if os.path.getsize(folderpath+'\\'+url.split('/')[-1]) == 0: 
                                        os.remove((folderpath+'\\'+url.split('/')[-1]))
                                    else:
                                        continue
                                localFile = open(url.split('/')[-1], 'wb')
                                localFile.write(webFile.read())
                                webFile.close()
                                localFile.close()
            value=1 #本次循环已完成
        webside=newpages #将第一层爬下来的网址作为参数传给第二层
        print webside
        print list(webside)
crawl(['http://books.nips.cc/'])

