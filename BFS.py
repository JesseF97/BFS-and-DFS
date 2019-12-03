#!/usr/bin/env python
# coding: utf-8

# the sample graph is found in the repo (graphorder.png)

# In[17]:


#neigbours of each node
graph    = { 'A':['B','E','C'], 
            'B':['A','D','E'], 
            'C':['A','F','G'],
            'D':['B','E'],
            'E':['A','B','D'],
            'F':['C'],
            'G':['C'] }

# start is origin node
def search(graph, start):
    visited = []
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbor = graph[node]
            
            for x in neighbor:
                queue.append(x)
    return visited

#input the node you want to start from
search(graph, 'A')


# In[18]:


search(graph,'A')


# In[19]:

#input the node you want to start from and the node you are going to 
def bfs_shortest_path(graph, start, end):
    visited=[]
    queue = [[start]]
    if start == end:
        return 'start = end'
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in visited:
            neighbor = graph[node]
            for x in neighbor:
                new_path = list(path)
                new_path.append(x)
                queue.append(x)
                
                if x == end:
                    return new_path
                visited.append(node)
                
    
    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist"        


# In[20]:


bfs_shortest_path(graph,'B','G')


# In[ ]:




