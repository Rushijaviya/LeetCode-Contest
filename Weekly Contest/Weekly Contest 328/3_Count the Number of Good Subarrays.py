# 2537. Count the Number of Good Subarrays
# https://leetcode.com/problems/count-the-number-of-good-subarrays/

from collections import defaultdict

class Solution:
    def countGood(self, nums, k):
        d=defaultdict(int)
        ans=0
        pairs=0
        n=len(nums)
        left=0
        for right in range(n):
            pairs+=d[nums[right]]
            d[nums[right]]+=1
            temp=left
            while pairs>=k:
                d[nums[left]]-=1
                pairs-=d[nums[left]]
                left+=1
            ans+=((left-temp)*(n-right))
        return ans
        
        '''
        count=0
        left=0
        pairs=0
        d=defaultdict(int)
        for right in range(len(nums)):
            pairs+=d[nums[right]]
            d[nums[right]]+=1
            while left<=right and pairs>=k:
                d[nums[left]]-=1
                pairs-=d[nums[left]]
                left+=1
            count+=(right-left+1)
        return (len(nums)*(len(nums)+1))//2-count
        '''