# -*- coding: utf-8 -*-
"""task1a.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NN4LXk4Hj7kzYkRh2q-GyxyWc17NCkBk
"""

in1a=open("/content/drive/MyDrive/Lab04/in1a.txt","r")
out1a=open("/content/drive/MyDrive/Lab04/out1a.txt","w")

node=in1a.readline()
xn,xe=node.split()

mtrx=[[0 for x in range(int(xn)+1)]for y in range(int(xn)+1)]


for n in range(int(xe)):
    r=in1a.readline().strip()
    node,eg,weight=r.split()
    mtrx[int(node)][int(eg)]=int(weight)

for n2 in range(len(mtrx)):
    out1a.write(f"{mtrx[n2]}\n")