# 2242. Maximum Score of a Node Sequence
# https://leetcode.com/problems/maximum-score-of-a-node-sequence/

from heapq import nlargest


class Solution:
    def maximumScore(self, scores, edges):
        n=len(scores)
        adj_list=[[] for _ in range(n)]
        for i,j in edges:
            adj_list[i].append([scores[j],j])
            adj_list[j].append([scores[i],i])
        for i in range(n):
            adj_list[i]=nlargest(3,adj_list[i])
        ans=-1
        for node1,node2 in edges:
            for value3,node3 in adj_list[node1]:
                for value4,node4 in adj_list[node2]:
                    if node3!=node4 and node3!=node2 and node4!=node1:
                        ans=max(ans,value3+value4+scores[node1]+scores[node2])
        return ans