# 2654. Minimum Number of Operations to Make All Array Elements Equal to 1
# https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

from math import gcd

class Solution:
    def minOperations(self, nums):
        count=nums.count(1)
        if count:
            return len(nums)-count
        diff=float('inf')
        for i in range(len(nums)):
            curr=nums[i]
            for j in range(i+1,len(nums)):
                curr=gcd(curr,nums[j])
                if curr==1:
                    diff=min(diff,j-i)
                    break
        return len(nums)+diff-1 if diff!=float('inf') else -1