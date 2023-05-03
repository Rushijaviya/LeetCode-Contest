# 2646. Minimize the Total Price of the Trips
# https://leetcode.com/problems/minimize-the-total-price-of-the-trips/

from functools import lru_cache

class Solution:
    def minimumTotalPrice(self, n, edges, price, trips):

        def findpath(node,parent,target,path):
            if node==target:
                return path
            for nei in adj_list[node]:
                if nei!=parent:
                    x=findpath(nei,node,target,path+[nei])
                    if x:
                        return x
            return []

        @lru_cache(None)
        def dp(idx,parent,flag):
            res=freq[idx]*price[idx]
            for nei in adj_list[idx]:
                if nei!=parent:
                    res+=dp(nei,idx,False)
            if not flag:
                temp=res
                res=freq[idx]*(price[idx]//2)
                for nei in adj_list[idx]:
                    if nei!=parent:
                        res+=dp(nei,idx,True)
                res=min(res,temp)
            return res

        adj_list=[[] for _ in range(n)]
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        freq=[0]*n
        for u,v in trips:
            path=findpath(u,-1,v,[u])
            for node in path:
                freq[node]+=1

        return dp(0,-1,False)