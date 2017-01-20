#!/usr/bin/env python
#coding: utf-8

import requests as rq
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import networkx as nx
import matplotlib.pylab as plt
import community

global loooong

loooong=1

G=nx.Graph()




def getinurl(url):
	htmin=rq.get(url)
	htmin.encoding="utf-8"
	naiyou=BeautifulSoup(htmin.text,"lxml")
	atag=naiyou.find_all("a")
	link=[a.get("href") for a in atag]
	sinurl=[urljoin(url,path) for path in link]

	for i in sinurl:
		G.add_edge(url,i,weight=loooong)

	return sinurl

def getif(turl):
	#This URL is alive?
	tans=None
	try:
		tans=getinurl(turl)
	except:
		print("none")
	return tans

def flatlist(lis):
	#This list is mountain [[[],[]],[[],[]],[[],[]]] -> [,,,,,,,,]
	#return [e for inlis in lis for e in inlis]
	flatlist=[]
	for e in lis:
		flatlist.extend(e)
	return flatlist

def listandlist(alllist,nowlist):
	alllistset=set(alllist)
	nowlistset=set(nowlist)
	match=list(alllistset & nowlistset)
	return match



kaisuu=int(input("How dive? ->"))

urlno=input("1:leo 2:nit 3:Hahiuralab   other:inputmode  ->")
if(urlno=="1"):
	url=("http://leo.nit.ac.jp/~ss/lecture/wip/page_list.html")
elif(urlno=="2"):
	url=("http://www.nit.ac.jp/")
elif(urlno=="3"):
	url=("http://kbse.nit.ac.jp")
else:
	url=input("come on -> ")



print("----Attack URL----")
print(url)
alllist=[url]
G.add_node(url)


print("---- 1 ----")
one=getinurl(url)
xone=listandlist(alllist,one)
zone=list(filter(lambda x:x not in xone,one))
alllist=alllist+zone
alllist=list(set(alllist))
print(alllist)

for i in alllist:
	G.add_node(i)


def rooper(zenkai,alial):
	raw=[getif(i) for i in zenkai]
	none=filter(None,raw)
	num=flatlist(none)
	xnum=listandlist(alial,num)
	znum=list(filter(lambda x:x not in xnum,num))
	alial=alial+znum
	alial=list(set(alial))
	return(znum,alial)


nget=int(2)
kaisuu=kaisuu-1
if(kaisuu<=0):
	exit()


znum=zone

for x in range(0,kaisuu):
	print("----",nget,"----")
	znum,alllist=rooper(znum,alllist)
	print(alllist)
	nget=nget+1

	loooong=loooong+1

	for i in alllist:
		G.add_node(i)


partition=community.best_partition(G)
cm=["blue","red","lime","yellow","pink","green","black","grey","darkred","tan","cyan","purple","violet","seagreen","coral","firebrick","skyblue","indigo","orchid","midnightblue","sage","rosybrown","navy","olive","peachpuff","lemonchiffon","gold","palegoldenrod","sienna","thistle"]

pos = nx.spring_layout(G)

for com in set(partition.values()):
	list_nodes=[nodes for nodes in partition.keys() if partition[nodes]==com]
	nx.draw_networkx_nodes(G,pos,list_nodes,node_size=60,node_color=cm[com])

nx.draw_networkx_edges(G,pos)
plt.show()


