# 2395. Find Subarrays With Equal Sum
# https://leetcode.com/problems/find-subarrays-with-equal-sum/

class Solution:
    def findSubarrays(self, nums):
        '''
        s=set()
        s.add(nums[0]+nums[1])
        for i in range(2,len(nums)):
            if nums[i]+nums[i-1] in s:
                return True
            s.add(nums[i]+nums[i-1])
        return False
        '''

        s=set()
        for i in range(1,len(nums)):
            s.add(nums[i]+nums[i-1])
        return len(s)!=len(nums)-1