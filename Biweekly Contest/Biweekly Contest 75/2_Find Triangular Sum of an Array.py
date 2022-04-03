# 2221. Find Triangular Sum of an Array
# https://leetcode.com/problems/find-triangular-sum-of-an-array/

class Solution:
    def triangularSum(self, nums):
        while len(nums)!=1:
            l=[]
            for i in range(1,len(nums)):
                l.append((nums[i]+nums[i-1])%10)
            nums=l
        return nums[0]