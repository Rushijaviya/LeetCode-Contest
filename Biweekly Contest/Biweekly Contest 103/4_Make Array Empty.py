# 2659. Make Array Empty
# https://leetcode.com/problems/make-array-empty/

class Solution:
    def countOperationsToEmptyArray(self, nums):
        '''
        pos = {val:idx for idx,val in enumerate(nums)}
        n=len(nums)
        ans=n
        nums.sort()
        for i in range(1,n):
            if pos[nums[i]]<pos[nums[i-1]]:
                ans+=(n-i)
        return ans
        '''

        n=len(nums)
        ans=n
        pos = sorted(range(n),key=lambda x:nums[x])
        for i in range(1,n):
            if pos[i]<pos[i-1]:
                ans+=(n-i)
        return ans