# -*- coding: utf-8 -*-
"""task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NN4LXk4Hj7kzYkRh2q-GyxyWc17NCkBk
"""

#2 -- BES

def readFile():

  in2 = open("/content/drive/MyDrive/Lab04/in2.txt","r")
  q = in2.readline()
  q = q.strip()
  q = q.split(" ")
  node=int(q[0])
  p=int(q[1])
  q=node
  grph=BGULOL(q,p,in2)
  return grph

def bgulol(q,p,in2):
  lstgraph=[[]]
  for i in range(q):
    lstgraph.append([])

  count = 0

  while int(count)<int(p):
    l = in2.readline()
    m,n = l.split(" ")
    m=int(m)
    n=int(n.strip())
    lstgraph[m].append(n)
    lstgraph[n].append(m)
    count+=1

  return(lstgraph)

def BFS(g,h):

  out2 = open("/content/drive/MyDrive/Lab04/out2.txt","w")

  ss = ""

  import queue
  adjcnt = [0]*len(g)
  que = queue.Queue()
  adjcnt[h]= 1
  que.put(h)

  while que.empty() is not True:
    a = que.get()
    ss+= str(a)
    ss+=(" ")

    for i in g[a]:

      if adjcnt[i]==0:
        adjcnt[i] = 1
        que.put(i)

  print(ss.strip(), file=out2)

grph = readfile()
h=1

BFS(grph,h)