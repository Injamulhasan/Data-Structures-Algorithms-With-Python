# -*- coding: utf-8 -*-
"""task1b.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NN4LXk4Hj7kzYkRh2q-GyxyWc17NCkBk
"""

#1b
def readfile():

  in1b = open("/content/drive/MyDrive/Lab04/in1b.txt","r") 
  out1b=open("/content/drive/MyDrive/Lab04/out1b.txt", "w")

  q=in1b.readline()
  q = q.strip()
  q = q.split(" ")
  node=int(q[0]) 
  p=int(q[1]) 
  q=node

  BGULOL(q,p,in1b,out1b)

def BGULOL(q,p,in1b,out1b):

  lstgraph=[[]]
  count = 0

  while int(count) <int(p):
    line = in1b.readline() 
    m,n,l = line.split(" ") 
    l = l.strip() 
    m=int(m)
    n=int(n)
    l=int(l)

    if(m in range(len(lstgraph))):
      a=(n,l)
      lstgraph[m].append(a)

    else:

      for i in range(q): 
        lstgraph.append([])
      a=(n,l)
      lstgraph[m].append(a)

    count+=1


  PGAL(None,lstgraph,out1b)

  return

def PGAL(graph, lstgraph,out1b):

  k =""

  if lstgraph is not None:
    lpq =lstgraph

    for i in range(len(lpq)):
      k+=str(i)
      k+= str(" : ");
      
      for j in range(len(lpq[i])): 

        if j==len(lpq[i])-1:
          k+=str(lpq[i][j])

        else:
          k+=str(lpq[i][j])
          k+=str(" ")

    k+= str("\n")

  print (k.strip(), file=out1b)

readfile()