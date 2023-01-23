# 2454. Next Greater Element IV
# https://leetcode.com/problems/next-greater-element-iv/

class Solution:
    def secondGreaterElement(self, nums):
        stack1,stack2=[],[]
        n=len(nums)
        ans=[-1]*n
        for i in range(n):
            while stack2 and nums[stack2[-1]]<nums[i]:
                ans[stack2.pop()]=nums[i]
            temp=[]
            while stack1 and nums[stack1[-1]]<nums[i]:
                temp.append(stack1.pop())
            stack2+=temp[::-1]
            stack1.append(i)
        return ans