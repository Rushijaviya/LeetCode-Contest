# 2562. Find the Array Concatenation Value
# https://leetcode.com/problems/find-the-array-concatenation-value/

class Solution:
    def findTheArrayConcVal(self, nums):
        '''
        ans=0
        while len(nums)>1:
            left=nums.pop(0)
            right=nums.pop()
            ans+=int(str(left)+str(right))
        if nums:
            ans+=nums[0]
        return ans
        '''

        ans=0
        left,right=0,len(nums)-1
        while left<right:
            ans+=int(str(nums[left])+str(nums[right]))
            left+=1
            right-=1
        if left==right:
            ans+=nums[left]
        return ans