# -*- coding: utf-8 -*-
"""task5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ytHzZzW5Rs91avEU8I-knBfk8fS0fe4t
"""

#5

input5= open("/content/sample_data/input5.txt","r")
output5= open("/content/sample_data/output5.txt","w")

xy=int(input5.readline())
larr=[]
for i in range(xy):
  larr.append(xy)
for j in range(1,len(larr)):
  k=larr[i]

  b=""
  for k in range(len(larr[i])):
    if larr[i][k]==" ":
      break
    else:
      b+=larr[i][k]
  p=i-1
  for j in range(i-1,0-1,-1):
    d=""
    for i in range(len(larr[j])):
      if larr[j][i]==" ":
        break
      else:
        d+=larr[j][i]
    if b>d:
      break
    elif b<d:
      larr[j+1]=larr[j]
      p-=1
    elif b==d:
      c=k[-6:].split(":")
      e=larr[j][-6:].split(":")
      if c[0]>e[0]:
        larr[j+1]=larr[j]
        p-=1
      elif c[0]==e[0] and c[1][:2]>e[1][:2]:
        p-=1
  larr[p+1]=k
for y in range(xy):
  print(larr[y],end="",file=output5)