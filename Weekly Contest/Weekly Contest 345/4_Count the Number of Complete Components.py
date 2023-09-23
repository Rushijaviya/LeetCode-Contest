# 2685. Count the Number of Complete Components
# https://leetcode.com/problems/count-the-number-of-complete-components/

from collections import defaultdict

class disjoint:
    def __init__(self,n):
        self.par=[i for i in range(n)]
        self.rank=[0]*n
    
    def findpar(self,node):
        if self.par[node]==node:
            return node
        self.par[node]=self.findpar(self.par[node])
        return self.par[node]
    
    def union(self,u,v):
        u,v=self.findpar(u),self.findpar(v)
        if self.rank[u]>self.rank[v]:
            self.par[v]=u
        elif self.rank[u]<self.rank[v]:
            self.par[u]=v
        else:
            self.par[v]=u
            self.rank[u]+=1

class Solution:
    def countCompleteComponents(self, n, edges):
        '''
        def dfs(node,res):
            visited[node]=True
            res.append(node)
            for nei in adj_list[node]:
                if not visited[nei]:
                    dfs(nei,res)

        adj_list=[[] for _ in range(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        ans=0
        visited=[False]*n
        for i in range(n):
            if not visited[i]:
                res=[]
                dfs(i,res)
                vertex=len(res)
                edge=0
                for node in res:
                    edge+=len(adj_list[node])
                if vertex==1 or (vertex*(vertex-1)) == edge:
                    ans+=1
        return ans
        '''

        edge = [0]*n
        obj = disjoint(n)
        for i,j in edges:
            obj.union(i,j)
            edge[i]+=1
            edge[j]+=1

        group=defaultdict(list)
        for i in range(n):
            temp=obj.findpar(i)
            group[temp].append(i)
        ans=0
        for i in group:
            if len(group[i])==1:
                ans+=1
            else:
                total_edge=0
                for x in group[i]:
                    total_edge+=(edge[x])
                if len(group[i])*(len(group[i])-1)==total_edge:
                    ans+=1
        return ans