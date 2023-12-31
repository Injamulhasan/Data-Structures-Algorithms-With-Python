# -*- coding: utf-8 -*-
"""221 lab-5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a-RcmMlJl1jK4fHoy4oO3HJ5HkhY2t0F
"""

# Task 1 


def buildGraphUsingDictionary(f,lines): #c= no of connections/ lines, f=inputfile
    # creating a dictionary


    
    graph = {}
    counter = 0
    while (counter<lines):
        line = f.readline().strip() # reading each line
        a,b,c = line.split(" ") # splitting the vertex and edge nodes
        c=int(c)

        global pq
        if a not in pq:
          pq.append(a)
        if b not in pq:
          pq.append(b)

        # we first search if the vertex exists in the dictionary or not
        if(a not in graph):
            t=(b,c)
            # create a new list in graph with a as the key and b as the list of its value
            graph[a] = [t]
            
        else:
            t=(b,c)
            # append() the value in b(edge) to key a(vertex) 
            graph[a].append(t)

        #As it is an undirected graph, We also make the reverse connections
        # we first search if the value inside variable a exists in the dictionary or not
        if(b in graph):
            t=(a,c)
            # if yes, then append() the value in b to a
            graph[b].append(t)
        else:
            t=(a,c)
            # create a new list in graph with a as the key and b as the value
            graph[b] = [t]
        

        counter+=1

     
    
    return graph





i1=open("input1.txt","r")
line1=i1.readline().split()
lines=int(line1[0]) #number of lines

destination=(line1[1]) #destination

source="Motijheel"




# Start #

pq=[] 
g=buildGraphUsingDictionary(i1,lines) #also appending all nodes in pq
 

import math
pqw=[math.inf]*len(pq) #pq min current weights
pqd=["no"]*len(pq) #pq done
pi=[None]*len(pq)

pqw[pq.index(source)]=0 #initializing distence of source to be 0


# print(g)
# print("pq=",pq)
# print("pqw=",pqw)
# print("pqd=",pqd)
# print("parent=",pi)

# print()
# print("################### initialization done ###############")
# print()




while "no" in pqd: #till work on all nodes are complete
  minimum=math.inf # find node with min weight whos work s not yet complete  
  minimumindex=math.inf
  for i in range(len(pqw)):
    if pqd[i]=="no" and (pqw[i])<minimum: #"no" means work of node is not complete
      minimum=pqw[i]
      minimumindex=i
  
  # print(minimum,"minimum")
  # print(minimumindex,"minimumindex")

  u=pq[minimumindex]
  # print(u)

  if u in g.keys():
    for v in g[u]:
      if int(pqw[minimumindex])+v[1]<(pqw[pq.index(v[0])]): #if current chost < existing chost
        pqw[pq.index(v[0])]=int(pqw[minimumindex])+v[1] #updating minimum chost of node form source
        pi[pq.index(v[0])]=u #updating parent
      #   print(v,"update")
      # else:
      #   print(v,"unchanged")

  pqd[pq.index(u)]="yes"  #work of node is complete

  
  # print(pq)
  # print(pqw)
  # print(pqd)
  # print(pi)
  # print()





# print("Final reasult #########################################################")
# print("pq=",pq)
# print("pqw=",pqw)
# print("pqd=",pqd)
# print(pi)
# print()

o1=open("output1.txt","w")


print(pqw[pq.index(destination)],"is the","minimum chost to reach destination", destination,"from source",source,file=o1)

# print(g)




# 2
def buildGraphUsingDictionary(f): #c= no of connections/ lines, f=inputfile

    line1=i2.readline().strip()
    line1=line1.split(" ")
    N=int(line1[0])  #destination and number of nodes
    M=int(line1[1])  #number of connections / lines in current test case

    graph = {}
    counter = 0
    while (counter<M):
        line = f.readline().strip() # reading each line
        a,b,c = line.split(" ") # splitting the vertex and edge nodes
        c=int(c)

        global pq
        if a not in pq:
          pq.append(a)
        if b not in pq:
          pq.append(b)

        # we first search if the vertex exists in the dictionary or not
        if(a not in graph):
            t=(b,c)
            # create a new list in graph with a as the key and b as the list of its value
            graph[a] = [t]
            
        else:
            t=(b,c)
            # append() the value in b(edge) to key a(vertex) 
            graph[a].append(t)

        #As it is an undirected graph, We also make the reverse connections
        # we first search if the value inside variable a exists in the dictionary or not
        if(b in graph):
            t=(a,c)
            # if yes, then append() the value in b to a
            graph[b].append(t)
        else:
            t=(a,c)
            # create a new list in graph with a as the key and b as the value
            graph[b] = [t]
        

        counter+=1
    
    def f(g,pq,destination):

      if len(pq)<1:
        return 0


      
      else:
        source="1"

        import math
        pqw=[math.inf]*len(pq) #pq min current weights
        pqd=["no"]*len(pq) #pq done
        pi=[None]*len(pq)

        pqw[pq.index(source)]=0 #initializing distence of source to be 0

        while "no" in pqd: #till work on all nodes are complete
          minimum=math.inf # find node with min weight whos work s not yet complete  
          minimumindex=math.inf
          for i in range(len(pqw)):
            if pqd[i]=="no" and (pqw[i])<minimum: #"no" means work of node is not complete
              minimum=pqw[i]
              minimumindex=i


          u=pq[minimumindex]

          if u in g.keys():
            for v in g[u]:
              if int(pqw[minimumindex])+v[1]<(pqw[pq.index(v[0])]): #if current chost < existing chost
                pqw[pq.index(v[0])]=int(pqw[minimumindex])+v[1] #updating minimum chost of node form source
                pi[pq.index(v[0])]=u #updating parent


          pqd[pq.index(u)]="yes"  #work of node is complete


        return pqw[pq.index(str(destination))]


     
    
    return f(graph,pq,N)






i2=open("input2.txt","r")
o2=open("output2.txt","w")


t=i2.readline()
t=int(t)


for i in range(t):
  pq=[]
  min_titans=buildGraphUsingDictionary(i2)
  print(min_titans,file=o2)

#3
def buildGraphUsingDictionary(f): #c= no of connections/ lines, f=inputfile

    line1=f.readline().strip()
    line1=line1.split(" ")
    N=int(line1[0])  #destination and number of nodes
    M=int(line1[1])  #number of connections / lines in current test case

    graph = {}
    counter = 0
    while (counter<M):
        line = f.readline().strip() # reading each line
        a,b,c = line.split(" ") # splitting the vertex and edge nodes
        c=int(c)

        global pq
        if a not in pq:
          pq.append(a)
        if b not in pq:
          pq.append(b)

        # we first search if the vertex exists in the dictionary or not
        if(a not in graph):
            t=(b,c)
            # create a new list in graph with a as the key and b as the list of its value
            graph[a] = [t]
            
        else:
            t=(b,c)
            # append() the value in b(edge) to key a(vertex) 
            graph[a].append(t)

        #As it is an undirected graph, We also make the reverse connections
        # we first search if the value inside variable a exists in the dictionary or not
        if(b in graph):
            t=(a,c)
            # if yes, then append() the value in b to a
            graph[b].append(t)
        else:
            t=(a,c)
            # create a new list in graph with a as the key and b as the value
            graph[b] = [t]
        

        counter+=1
        
    def f(g,pq,destination):

      if len(pq)<1:
        path=[]
        path.append(str(destination))
        return path
        
      else:
        source="1"

        import math
        pqw=[math.inf]*len(pq) #pq min current weights
        pqd=["no"]*len(pq) #pq done
        pi=[None]*len(pq)

        pqw[pq.index(source)]=0 #initializing distence of source to be 0

        while "no" in pqd: #till work on all nodes are complete
          minimum=math.inf # find node with min weight whos work s not yet complete  
          minimumindex=math.inf
          for i in range(len(pqw)):
            if pqd[i]=="no" and (pqw[i])<minimum: #"no" means work of node is not complete
              minimum=pqw[i]
              minimumindex=i


          u=pq[minimumindex]

          if u in g.keys():
            for v in g[u]:
              if int(pqw[minimumindex])+v[1]<(pqw[pq.index(v[0])]): #if current chost < existing chost
                pqw[pq.index(v[0])]=int(pqw[minimumindex])+v[1] #updating minimum chost of node form source
                pi[pq.index(v[0])]=u #updating parent


          pqd[pq.index(u)]="yes"  #work of node is complete

        
        # print("pq=",pq)  # pq= ['3', '5', '1', '2', '4']
        # print("pi=",pi)  # pi= ['4', '3', None, '1', '1']

        destination=str(destination) # = "5"
        path=[]
        path.append(destination) #[5]

        f=0
        while f==0:
          if pi[pq.index( path[len(path)-1] )]!=source:
            path.append(pi[pq.index( path[len(path)-1] )]) #[5,3]
          else:
            path.append(pi[pq.index( path[len(path)-1] )])
            f=1
        return path

    
    return f(graph,pq,N)









i3=open("input3.txt","r")
o3=open("output3.txt","w")


t=i3.readline()
t=int(t)

s=""
for i in range(t):
  pq=[]
  path=buildGraphUsingDictionary(i3)
  
  for i in range(len(path)-1,-1,-1):  #    for i in (path[::-1]): 
      s+=path[i]                      #         s+=i
      s+=" "
  s+="\n"

print(s,file=o3)

#5
def buildGraphUsingDictionary(f): #c= no of connections/ lines, f=inputfile

    line1=f.readline().strip()
    line1=line1.split(" ")
    N=int(line1[0])  #destination and number of nodes
    M=int(line1[1])  #number of connections / lines in current test case

    
    if M>=1:

      graph = {}
      counter = 0
      while (counter<M):
          line = f.readline().strip() # reading each line
          a,b,c = line.split(" ") # splitting the vertex and edge nodes
          c=int(c)

          global pq
          if a not in pq:
            pq.append(a)
          if b not in pq:
            pq.append(b)

          # we first search if the vertex exists in the dictionary or not
          if(a not in graph):
              t=(b,c)
              # create a new list in graph with a as the key and b as the list of its value
              graph[a] = [t]
              
          else:
              t=(b,c)
              # append() the value in b(edge) to key a(vertex) 
              graph[a].append(t)

          #As it is an undirected graph, We also make the reverse connections
          # we first search if the value inside variable a exists in the dictionary or not
          if(b in graph):
              t=(a,c,"r")
              # if yes, then append() the value in b to a
              graph[b].append(t)
          else:
              t=(a,c,"r")
              # create a new list in graph with a as the key and b as the value
              graph[b] = [t]
          

          counter+=1

      source=f.readline().strip()




  #        
      def function(source,g,pq,destination):
        import math
        pqw=[-math.inf]*len(pq) #pq min current weights
        pqwr=[-math.inf]*len(pq)
        pqd=["no"]*len(pq) #pq done


        pq.sort()
        pqw[pq.index(source)]=0 #initializing distence of source to be 0
        pqwr[pq.index(source)]=0

        while "no" in pqd: #till work on all nodes are complete

          max=-math.inf # find node with min weight whos work s not yet complete  
          maximindex=-math.inf
          for i in range(len(pqw)):
            if pqd[i]=="no" and (pqw[i])>=max: #"no" means work of node is not complete
              max=pqw[i]
              maximumindex=i


          u=pq[maximumindex]
          if u in g.keys():
            for v in g[u]:
              if len(v)!=3: #As this is directed graph,
                if v[1] >pqw[pq.index(v[0])]: #'''pqw[maximumindex]''' #if current chost < existing chost
                  pqw[pq.index(v[0])]= v[1] #'''pqw[maximumindex]''' #updating minimum chost of node form source
                  if pqw[maximumindex]<pqw[pq.index(v[0])] and pqw[maximumindex]>0:
                    pqw[pq.index(v[0])]=pqw[maximumindex]
              elif len(v)==3: #backward connections
                if v[1]>pqwr[pq.index(v[0])]:
                  pqwr[pq.index(v[0])]=-v[1]


          pqd[pq.index(u)]="yes"  #work of node is complete

        s=""
        if -math.inf in pqw:
         for i in range(len(pqwr)):
            s+=str(int(pqwr[i])-int(pqwr[pq.index(source)]) )
            s+=" "
        else:
          for i in range(len(pqw)):
            s+=str(int(pqw[i])-int(pqw[pq.index(source)]) )
            s+=" "
        

        return s
        
#

      return function(source,graph,pq,N)



    else:
      source=f.readline()
      return "0"
################################## Driver ###########################

i5=open("input5.txt","r")
o5=open("output5.txt","w")


t=i5.readline()
t=int(t)

o=""
for i in range(t):
  pq=[]
  path=buildGraphUsingDictionary(i5)
  o+=path
  o+="\n"

print(o,file=o5)