# 2289. Steps to Make Array Non-decreasing
# https://leetcode.com/problems/steps-to-make-array-non-decreasing/

class Solution:
    def totalSteps(self, nums):
        stack=[]
        ans=0
        for i in range(len(nums)-1,-1,-1):
            count=0
            while stack and stack[-1][1]<nums[i]:
                count=max(count+1,stack[-1][0])
                stack.pop()
            ans=max(ans,count)
            stack.append((count,nums[i]))
        return ans