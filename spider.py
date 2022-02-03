# This Python file uses the following encoding: utf-8
from asyncio.windows_events import NULL
from email.quoprimime import unquote
import threading
from bs4 import BeautifulSoup
import requests
import re
import os
import threading
import time
class spider():
    url_add=[]
    song_name=[]
    song_type=[]
    url8song=[]
    def __init__(self,url,format,pathname,):
        if pathname==None:
            self.pathname='./'
        self.url=url
        self.format=format
        self.pathname=pathname    
    def getContent(self):                                                 #A GET request of the album site
        try:
            res=requests.get(self.url)
            return res.content
        except:
            print("failed to connect")
            
    def getUrls(self):                                                    #TO get urls and names of songs
        bs=BeautifulSoup(self.getContent().decode("utf-8"),'lxml')      
        for item in bs.find_all("a"):
            a=item.get('href')
            s=item.string
            a=str(a)
            if re.search(r"/game-soundtracks/album/(.*).mp3",a):
                self.url_add.append('https://vgmsite.com/soundtracks'+a.replace('/game-soundtracks/album','').replace('.mp3','')+'.{}'.format(self.format))
        self.url_add=set(self.url_add)
    def getName8Type(self):
        for url in self.url_add:
            temp=url.split('/')          
            name=temp[5]
            name8type=name.split('.')  
            # self.song_name.append(unquote(name8type[0]))             #if fuction unquote is used here,it won't work.i don' know why
            self.song_name.append(re.sub(r'%\d{4}','',name8type[0].replace('-','_')))
            self.url8song=list(zip(self.url_add,self.song_name))
    def Dnowload(self,url8song):
        print("DOWN")
        mes2=QMessageBox.critical(self,'download',"dowloading")
        for song in url8song:
            res=requests.get(url8song)
                 
            
            file=open(self.pathname+url8song[1]+'.'+self.format,'wb')
        # file.write(res.content)
            file.write(res)
        mes1=QMessageBox.critical(self,'finish',"download finished")
# url="https://downloads.khinsider.com/game-soundtracks/album/g.c.best-i-ve-girls-compilation-best"
# format='FLAC'
# pathname='./'
#test=spider(url,format,pathname)
#test.getUrls()
#test.getName8Type()
#test.Dnowload(test.url8song[2])
#for text in test.song_name:
#    print(text)
