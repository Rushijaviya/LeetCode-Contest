# 2335. Minimum Amount of Time to Fill Cups
# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

class Solution:
    def fillCups(self, amount):
        count=0
        amount.sort()
        while amount[1] and amount[2]:
            amount[1]-=1
            amount[2]-=1
            count+=1
            amount.sort()
        return count+amount[2]
        
        '''
        return max(max(amount),(sum(amount)+1)//2)
        '''