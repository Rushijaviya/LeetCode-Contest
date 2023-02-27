# 2568. Minimum Impossible OR
# https://leetcode.com/problems/minimum-impossible-or/

class Solution:
    def minImpossibleOR(self, nums):
        nums=set(nums)
        return next(1<<i for i in range(32) if 1<<i not in nums)
        
        '''
        nums.sort()
        start=1
        for num in nums:
            if num>start:
                return start
            elif num==start:
                start*=2
        return start
        '''
        
        '''
        curr=0
        for num in nums:
            if num&(num-1)==0:
                curr|=num
        curr=~curr
        return curr&(-curr)
        '''