# 2492. Minimum Score of a Path Between Two Cities
# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

class disjoint:
    def __init__(self,n) -> None:
        self.rank=[0]*n
        self.parent=[i for i in range(n)]

    def findpar(self,u):
        if u==self.parent[u]:
            return u
        self.parent[u]=self.findpar(self.parent[u])
        return self.parent[u]

    def union(self,u,v):
        u,v=self.findpar(u),self.findpar(v)
        if self.rank[u]<self.rank[v]:
            self.parent[u]=v
        elif self.rank[v]<self.rank[u]:
            self.parent[v]=u
        else:
            self.parent[v]=u
            self.rank[u]+=1

class Solution:
    def minScore(self, n, roads):
        '''
        def dfs(node,visited,path):
            visited.add(node)
            path.append(node)
            for nei,_ in adj_list[node]:
                if nei not in visited:
                    dfs(nei,visited,path)
            return path
        
        adj_list=[[] for _ in range(n)]
        for u,v,cost in roads:
            adj_list[u-1].append([v-1,cost])
            adj_list[v-1].append([u-1,cost])
        ans=set(dfs(0,set(),[]))
        res=float('inf')
        for u,v,cost in roads:
            if res>cost and u-1 in ans:
                res=cost
        return res
        '''
        
        '''
        def bfs():
            queue=[0]
            ans=float('inf')
            visited=set()
            while queue:
                node=queue.pop(0)
                for nei,cost in adj_list[node]:
                    ans=min(ans,cost)
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            return ans

        adj_list=[[] for _ in range(n)]
        for u,v,cost in roads:
            adj_list[u-1].append([v-1,cost])
            adj_list[v-1].append([u-1,cost])
        return bfs()
        '''

        obj=disjoint(n)
        for u,v,cost in roads:
            obj.union(u-1,v-1)
        ans=float('inf')
        for u,v,cost in roads:
            if ans>cost and obj.findpar(0)==obj.findpar(u-1):
                ans=cost
        return ans