# 2598. Smallest Missing Non-negative Integer After Operations
# https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

from collections import Counter

class Solution:
    def findSmallestInteger(self, nums, value):
        '''
        # TLE
        start=0
        while True:
            if start not in nums:
                for idx in range(len(nums)):
                    diff=abs(nums[idx]-start)
                    if diff%value==0:
                        nums[idx]=start
                        break
                else:
                    return start
            nums.remove(start)
            start+=1
        '''

        c=Counter([num%value for num in nums])
        for i in range(len(nums)):
            if c[i%value]==0:
                return i
            c[i%value]-=1
        return len(nums)