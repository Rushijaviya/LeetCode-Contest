# 2295. Replace Elements in an Array
# https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums, operations):
        d={}
        n=len(nums)
        for i in range(n):
            d[nums[i]]=i
        for i,j in operations:
            idx=d[i]
            del d[i]
            d[j]=idx
        for i,j in d.items():
            nums[j]=i
        return nums
        
        '''
        d={}
        for i in range(len(nums)):
            d[nums[i]]=i
        for i,j in operations:
            d[j]=d[i]
            nums[d[j]]=j
        return nums
        '''