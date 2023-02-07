# 2501. Longest Square Streak in an Array
# https://leetcode.com/problems/longest-square-streak-in-an-array/

from math import sqrt

class Solution:
    def longestSquareStreak(self, nums):
        nums=set(nums)
        ans=-1
        for i in nums:
            if sqrt(i) not in nums:
                j=i*i
                curr=0
                while j in nums:
                    j=j*j
                    curr+=1
                if curr:
                    ans=max(ans,curr+1)
        return ans
        
        '''
        memo={}
        nums.sort()
        ans=-1
        for i in nums:
            j=sqrt(i)
            if j*j==i and j in memo:
                memo[i]=memo[j]+1
                ans=max(ans,memo[i])
            else:
                memo[i]=1
        return ans
        '''