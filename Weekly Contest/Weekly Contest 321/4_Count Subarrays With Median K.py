# 2488. Count Subarrays With Median K
# https://leetcode.com/problems/count-subarrays-with-median-k/

from collections import defaultdict

class Solution:
    def countSubarrays(self, nums, k):
        '''
        d=defaultdict(int)
        balance=0
        idx=nums.index(k)
        for i in range(idx,len(nums)):
            if nums[i]>k:
                balance+=1
            elif nums[i]<k:
                balance-=1
            d[balance]+=1
        ans=0
        balance=0
        for i in range(idx,-1,-1):
            if nums[i]>k:
                balance+=1
            elif nums[i]<k:
                balance-=1
            ans+=(d[-balance]+d[-balance+1])
        return ans
        '''

        d=defaultdict(int)
        d[0]=1
        found=False
        ans=0
        balance=0
        for i in nums:
            if i>k:
                balance+=1
            elif i<k:
                balance-=1
            else:
                found=True
            if found:
                ans+=(d[balance]+d[balance-1])
            else:
                d[balance]+=1
        return ans