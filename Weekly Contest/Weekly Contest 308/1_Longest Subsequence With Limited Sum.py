# 2389. Longest Subsequence With Limited Sum
# https://leetcode.com/problems/longest-subsequence-with-limited-sum/

from bisect import bisect_right
from itertools import accumulate

class Solution:
    def answerQueries(self, nums, queries):
        '''
        nums.sort()
        ans=[]
        for i in queries:
            sum=0
            length=0
            for num in nums:
                if sum+num>i:
                    break
                sum+=num
                length+=1
            ans.append(length)
        return ans
        '''
        
        nums.sort()
        nums=list(accumulate(nums))
        ans=[]
        for maxsum in queries:
            idx=bisect_right(nums,maxsum)
            ans.append(idx)
        return ans