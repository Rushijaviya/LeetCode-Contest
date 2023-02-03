# 2497. Maximum Star Sum of a Graph
# https://leetcode.com/problems/maximum-star-sum-of-a-graph/

import heapq

class Solution:
    def maxStarSum(self, vals, edges, k):
        '''
        n=len(vals)
        adj_list=[[] for _ in range(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        ans=float('-inf')
        for i in range(n):
            l=list(sorted(map(lambda x:vals[x],adj_list[i]),reverse=True))
            value=vals[i]
            ans=max(ans,value)
            for j in l[:k]:
                value+=j
                ans=max(ans,value)
        return ans
        '''

        n=len(vals)
        adj_list=[[] for _ in range(n)]
        for i,j in edges:
            if vals[j]>0:
                adj_list[i].append(vals[j])
            if vals[i]>0:
                adj_list[j].append(vals[i])
        ans=float('-inf')
        for i in range(n):
            value=vals[i]
            if len(adj_list[i])<k:
                value+=sum(adj_list[i])
            else:
                value+=sum(heapq.nlargest(k,adj_list[i]))
            ans=max(ans,value)
        return ans