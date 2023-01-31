# 2477. Minimum Fuel Cost to Report to the Capital
# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

import math

class Solution:
    def minimumFuelCost(self, roads, seats):
        def dfs(node,parent):
            res=1
            for nei in adj_list[node]:
                if nei!=parent:
                    res+=dfs(nei,node)
            if node!=0:
                self.ans+=math.ceil(res/seats)
            return res

        n=len(roads)+1
        adj_list=[[] for _ in range(n)]
        for i,j in roads:
            adj_list[i].append(j)
            adj_list[j].append(i)
        self.ans=0
        dfs(0,-1)
        return self.ans
        
        '''
        def bfs():
            queue=[]
            for i in range(1,n):
                if degree[i]==1:
                    queue.append(i)
            res=[1]*n
            while queue:
                node=queue.pop(0)
                self.ans+=math.ceil(res[node]/seats)
                for nei in adj_list[node]:
                    degree[nei]-=1
                    res[nei]+=res[node]
                    if degree[nei]==1 and nei!=0:
                        queue.append(nei)

        n=len(roads)+1
        adj_list=[[] for _ in range(n)]
        degree=[0]*n
        for i,j in roads:
            adj_list[i].append(j)
            adj_list[j].append(i)
            degree[i]+=1
            degree[j]+=1
        self.ans=0
        bfs()
        return self.ans
        '''