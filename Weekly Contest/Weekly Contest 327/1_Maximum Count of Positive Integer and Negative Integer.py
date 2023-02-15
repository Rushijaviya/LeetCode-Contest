# 2529. Maximum Count of Positive Integer and Negative Integer
# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

from bisect import bisect_left, bisect_right

class Solution:
    def maximumCount(self, nums):
        '''
        pos=neg=0
        for i in nums:
            pos+=(i>0)
            neg+=(i<0)
        return max(pos,neg)
        '''

        return max(bisect_left(nums,0),len(nums)-bisect_right(nums,0))