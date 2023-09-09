# 2656. Maximum Sum With Exactly K Elements
# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

class Solution:
    def maximizeSum(self, nums, k):
        '''
        res=max(nums)
        ans=0
        for _ in range(k):
            ans+=res
            res+=1
        return ans
        '''
        
        ans=max(nums)
        return k*ans+(k*(k-1))//2