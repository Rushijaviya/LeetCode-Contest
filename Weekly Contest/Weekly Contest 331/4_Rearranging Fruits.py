# 2561. Rearranging Fruits
# https://leetcode.com/problems/rearranging-fruits/

from collections import Counter

class Solution:
    def minCost(self, basket1, basket2):
        c=Counter(basket1)
        for x in basket2:
            c[x]-=1
        exchange=[]
        for i,j in c.items():
            if j%2:
                return -1
            exchange+=([i]*abs(j//2))
        m=min(basket1+basket2)
        ans=0
        exchange.sort()
        for i in exchange[:len(exchange)//2]:
            ans+=min(2*m,i)
        return ans