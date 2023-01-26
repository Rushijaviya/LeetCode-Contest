# 2460. Apply Operations to an Array
# https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums):
        '''
        n=len(nums)
        ans=[0]*n
        idx=0
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
            if nums[i]!=0:
                ans[idx]=nums[i]
                idx+=1
        if nums[-1]!=0:
            ans[idx]=nums[-1]
        return ans
        '''

        n=len(nums)
        idx=0
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
            if nums[i]!=0:
                nums[idx]=nums[i]
                idx+=1
        if nums[-1]!=0:
            nums[idx]=nums[-1]
            idx+=1
        return nums[:idx]+[0]*(n-idx)