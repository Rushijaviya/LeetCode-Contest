# 2681. Power of Heroes
# https://leetcode.com/problems/power-of-heroes/

class Solution:
    def sumOfPower(self, nums):
        nums.sort()
        ans,prev=0,0
        for num in nums:
            res= num*num*num+num*num*prev
            prev=2*prev+num
            ans+=res
        return ans%(10**9+7)