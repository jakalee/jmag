# -*- coding: utf-8 -*-
"""
Created on Wed Oct 01 13:45:14 2014
@author: jakal
"""
import numpy as np
import console as cn
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen,Request
from requests.utils import quote   #주소창에 한글을 유니코드8로 변환시켜준다.
import urllib
from collections import Counter
cn.clear()

test=0 #test할려면 1
#from urllib.urlparse import quote
#로또검색어로부터 최종횟수를 가져온다.
url=u'https://search.naver.com/search.naver?sm=tab_drt&where=nexearch&query='+quote('로또')
#print(url)
#403금지를 막는다. 봇(bot)으로 인식할수 있으므로 헤더를 가져다 붙인다.
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
web_byte = urlopen(req).read()
webpage = web_byte.decode('utf-8')  #
soup=bs(webpage,'html.parser')
a=soup.find('a',class_='_lotto-btn-current') #class="_lotto-btn-current"
last=int(a.find('em').contents[0][:-1])
#print(last)
#last=1
#lott_box=np.zeros((last,7))   #로또번호를 담을 변수
jj=1
for num in range(last-7,last+1):
    url=u'https://search.naver.com/search.naver?sm=tab_drt&where=nexearch&query='+quote('%d회로또'% num)
    #print(url)
    #403금지를 막는다. 봇(bot)으로 인식할수 있으므로 헤더를 가져다 붙인다.
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')  #
    soup=bs(webpage,'html.parser')
    #print(soup.prettify())
    a=soup.find('div',class_='num_box')
    #print(a)
    b=a.find_all('span')
    #c=np.zeros(45)   #당첨번호를 45 비트화 시킨다.
    lott_box=[]
    for i in range(len(b)):
        if i!=6:
            #print(b[i].contents)    #리스트로 나온다.
            #c[int(b[i].contents[0])-1]=1
            lott_box.append(b[i].contents[0])
    if jj==1:
        v=np.array(lott_box)
        jj=jj+1
    else:
        v=np.vstack((v,np.array(lott_box)))
        jj=jj+1      
    #print(lott_box)
#lott_box
print(v)
c=v[:-1]
ssort=c.astype('int')
cnt=Counter(ssort.ravel())
ssort_elem=np.array(list(cnt.elements()))
ssort_val=np.array(list(cnt.values()))

lucknum = np.unique(ssort)
#print(lucknum)


cc=lucknum #np.array([11,12,15,17,18,19,24,25,29	,32,34,41,43,44])
cc=np.setdiff1d(np.arange(1,46),lucknum)
cc=np.sort(np.unique(np.append(cc,v[-1])).astype('int'))
print(cc)
#np.random.shuffle(coldn)
coldn=[]#coldn[:6]

print('cold bumber: ' , np.sort(coldn))
cnt=0
a=np.arange(1,46)
n=0
cc=np.array(cc)
gg=v[-1][:6].astype('int')  #np.array([11,12,29,33,38,42])
print('하느님 행운의 번호 좀 주세요.')
print('행운의 1등 로또번호가 되기를 바랍니다.')
n3=0
n4=0
n5=0
n6=0
trynum=100 #몇장 살꺼지
sun=np.array([0,1,2,2,1])
selectn=[]
for i in range(5000000):
	
	np.random.shuffle(a)
	np.random.shuffle(sun)
	b=a[:6];b.sort()
	if len(set(b).intersection(set(cc)))>=5 and len(set(b).intersection(set(coldn)))==0 and len(set(b).intersection(set(gg)))>=1:
		if bool(set(b).intersection(set(b+1))) |bool(set(b).intersection(set(b-1))):
			
			if sum(b)>np.sum(cc)/np.size(cc)*6-20 and sum(b)<np.sum(cc)/np.size(cc)*6+20:
				if np.size(b[(b>0)&(b<10)])==sun[0] and \
				np.size(b[(b>9)&(b<19)])==sun[1] and \
				np.size(b[(b>18)&(b<28)])==sun[2] and \
				np.size(b[(b>27)&(b<37)])==sun[3] and \
				np.size(b[(b>36)&(b<46)])==sun[4]:
					n=n+1
					panda=len(set(b).intersection(set(gg)))
					#print(n,u'번째',b,sum(b),panda)
					if n>trynum-1:
						n=trynum
						break
					if panda==2:
						selectn.append(list(b))
						#pass
					if panda==3:
						n3=n3+1
					if panda==4:
						n4=n4+1
					if panda==5:
						n5=n5+1
					if panda==6:
						n6=n6+1
						
#set(a).symmetric_difference(set(b))

print('총 투입금액 %10s원' % "{0:,d}".format(n*1000))	
print('5등 %s개'% "{0:,d}".format(n3))
print('4등 %s개'% "{0:,d}".format(n4))
print('3등 %s개'% "{0:,d}".format(n5))
print('1등 %s개'% "{0:,d}".format(n6))

good= n3*5000+n4*50000+n5*1400000+n6*1000000000
print('총 당첨금액 %10s원' % "{0:,d}".format(good))
if n6==1: print('=====bingo===')

nn=0
mesu=10
for i in range(len(selectn)):
	if mesu>nn:
		print('%d번째'%(i+1),selectn[i])
		nn=nn+1
	else:
		break
