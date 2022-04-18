# 2240. Number of Ways to Buy Pens and Pencils
# https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

class Solution:
    def waysToBuyPensPencils(self, total, cost1, cost2):
        cost1,cost2=max(cost1,cost2),min(cost1,cost2)
        ans=0
        for i in range(1+total//cost1):
            left=max(0,total-cost1*i)
            ans+=(1+left//cost2)
        return ans
        
        '''
        if cost1>total and cost2>total:
            return 1
        upper=total//cost1
        start=0
        ans=0
        while start<=upper:
            temp=total-(cost1*start)
            if temp<0:
                break
            ans+=(1+temp//cost2)
            start+=1
        return ans
        '''