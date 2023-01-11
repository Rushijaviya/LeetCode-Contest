# 2421. Number of Good Paths
# https://leetcode.com/problems/number-of-good-paths/

class disjoint:
    def __init__(self,n):
        self.ranks=[0]*n
        self.par=[i for i in range(n)]
    
    def findpar(self,node):
        if self.par[node]==node:
            return node
        self.par[node]=self.findpar(self.par[node])
        return self.par[node]
    
    def union(self,u,v):
        u,v=self.findpar(u),self.findpar(v)
        if self.ranks[u]<self.ranks[v]:
            self.par[u]=v
        elif self.ranks[v]<self.ranks[u]:
            self.par[v]=u
        else:
            self.par[v]=u
            self.ranks[u]+=1

class Solution:
    def numberOfGoodPaths(self, vals, edges):
        '''
        # TLE
        def rec(node,visited,tar,start):
            if vals[node]==tar:
                if (start,node) not in s:
                    s.add((node,start))
                    
            visited.add(node)
            for i in adj_list[node]:
                if i not in visited and vals[i]<=tar:
                    rec(i,visited,tar,start)
        
        if len(vals)==len(set(vals)):
            return len(vals)
        n=len(vals)
        adj_list=[[] for _ in range(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        s=set()
        for i in range(n):
            rec(i,set(),vals[i],i)
        return len(s)
        '''

        n=len(vals)
        valtoidx={}
        for i in range(n):
            if vals[i] not in valtoidx:
                valtoidx[vals[i]]=[]
            valtoidx[vals[i]].append(i)
        adj_list=[[] for _ in range(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        obj=disjoint(n)
        temp=[[i,j] for i,j in valtoidx.items()]
        temp.sort()
        ans=0
        for value,idx_list in temp:
            for idx in idx_list:
                for node in adj_list[idx]:
                    if vals[node]<=vals[idx]:
                        obj.union(idx,node)
            d={}
            for idx in idx_list:
                parent=obj.findpar(idx)
                d[parent]=d.get(parent,0)+1
            for i in d:
                ans+=((d[i]*(d[i]+1))//2)
        return ans