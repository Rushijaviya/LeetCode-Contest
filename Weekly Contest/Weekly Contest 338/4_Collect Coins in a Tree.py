# 2603. Collect Coins in a Tree
# https://leetcode.com/problems/collect-coins-in-a-tree/

from collections import defaultdict

class Solution:
    def collectTheCoins(self, coins, edges):
        adj_list=defaultdict(list)
        n=len(coins)
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        leaves=[i for i in range(n) if len(adj_list[i])==1 and coins[i]==0]
        for node in leaves:
            while len(adj_list[node])==1 and coins[node]==0:
                nei=adj_list[node][0]
                del adj_list[node]
                adj_list[nei].remove(node)
                node=nei
        for _ in range(2):
            leaves=[i for i in range(n) if len(adj_list[i])==1]
            for node in leaves:
                for nei in adj_list[node]:
                    adj_list[nei].remove(node)
                del adj_list[node]
        count=0
        for i in adj_list:
            if adj_list[i]:
                count+=1
        return max(0,(count-1)*2)