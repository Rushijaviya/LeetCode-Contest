# 2441. Largest Positive Integer That Exists With Its Negative
# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

class Solution:
    def findMaxK(self, nums):
        '''
        nums.sort()
        for i in nums:
            if i>0:
                return -1
            if -i in nums:
                return -i
        return -1
        '''

        arr=[0]*2001
        for i in nums:
            arr[i+1000]=1
        for i in range(1000,-1,-1):
            if arr[1000+i] and arr[1000-i]:
                return i
        return -1

        '''
        s=set(nums)
        check=list(filter(lambda x:x<0,list(s)))
        ans=-1
        for i in check:
            if -i in s:
                ans=max(ans,-i)
        return ans
        '''