# 2572. Count the Number of Square-Free Subsets
# https://leetcode.com/problems/count-the-number-of-square-free-subsets/

from collections import defaultdict
from functools import lru_cache

class Solution:
    def squareFreeSubsets(self, nums):
        '''
        # TLE
        @lru_cache(None)
        def valid(x):
            if x==0:
                return False
            if x==1:
                return True
            if sqrt(x)%1==0:
                return False
            idx=2
            while (idx*idx)<x:
                if x%(idx*idx)==0:
                    return False
                idx+=1
            return True
        
        @lru_cache(None)
        def dp(idx,product):
            if idx==n:
                return product!=0
            x=dp(idx+1,product)%(10**9+7)
            y=0
            if nums[idx]==1 or ((sqrt(nums[idx])%1)!=0 and valid(product*nums[idx] if product!=0 else nums[idx])):
                y=dp(idx+1,product*nums[idx] if product!=0 else nums[idx])%(10**9+7)
            return (x+y)%(10**9+7)
            
        n=len(nums)
        return dp(0,0)%(10**9+7)
        '''

        mask={1:0, 2:1, 3:2, 5:4, 6:3, 7:8, 10:5, 11:16, 13:32, 14:9, 15:6, 17:64, 19:128, 21:10, 22:17, 23:256, 26:33, 29:512, 30:7}
        count=defaultdict(int)
        for num in nums:
            if num in mask:
                for k in count.copy():
                    if mask[num]&k==0:
                        count[mask[num]|k]+=count[k]
                count[mask[num]]+=1
        return sum(count.values())%(10**9+7)