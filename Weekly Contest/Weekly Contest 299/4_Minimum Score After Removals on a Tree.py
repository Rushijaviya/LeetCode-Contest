# 2322. Minimum Score After Removals on a Tree
# https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

from collections import defaultdict
from functools import reduce

class Solution:
    def minimumScore(self, nums, edges):
        n=len(nums)
        m=len(edges)
        adj_list=[[] for _ in range(n)]
        value=nums[:]
        degree=[0]*n
        visited=[0]*n
        children=defaultdict(set)
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
            degree[i]+=1
            degree[j]+=1
        
        queue=[]
        total=0
        for i in range(n):
            total^=nums[i]
            if degree[i]==1:
                queue.append(i)
                visited[i]=1
        
        while queue:
            node=queue.pop(0)
            for j in adj_list[node]:
                if not visited[j]:
                    children[j].add(node)
                    children[j]|=children[node]
                    value[j]^=value[node]
                degree[j]-=1
                if degree[j]==1:
                    queue.append(j)
                    visited[j]=1
        
        ans=float('inf')
        for i in range(m-1):
            for j in range(i+1,m):
                a,b=edges[i]
                c,d=edges[j]
                if b in children[a]:
                    a,b=b,a
                if d in children[c]:
                    c,d=d,c
                
                if c in children[a]:
                    x,y,z=value[c],value[a]^value[c],total^value[a]
                elif a in children[c]:
                    x,y,z=value[a],value[c]^value[a],total^value[c]
                else:
                    x,y,z=value[a],value[c],total^value[a]^value[c]
                ans=min(ans,max(x,y,z)-min(x,y,z))
        return ans
        
        '''  
        n=len(nums)
        m=len(edges)
        adj_list=[[] for _ in range(n)]
        value=nums[:]
        degree=[0]*n
        visited=[0]*n
        children=defaultdict(set)
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
            degree[i]+=1
            degree[j]+=1
        
        def dfs(node):
            visited[node]=1
            for j in adj_list[node]:
                if not visited[j]:
                    dfs(j)
                    value[node]^=value[j]
                    children[node].add(j)
                    children[node]|=children[j]

        dfs(0)

        total=reduce(lambda x, y: x^y, nums)
        ans=float('inf')
        for i in range(m-1):
            for j in range(i+1,m):
                a,b=edges[i]
                c,d=edges[j]
                if b in children[a]:
                    a,b=b,a
                if d in children[c]:
                    c,d=d,c
                
                if c in children[a]:
                    x,y,z=value[c],value[a]^value[c],total^value[a]
                elif a in children[c]:
                    x,y,z=value[a],value[c]^value[a],total^value[c]
                else:
                    x,y,z=value[a],value[c],total^value[a]^value[c]
                ans=min(ans,max(x,y,z)-min(x,y,z))
        return ans
        '''