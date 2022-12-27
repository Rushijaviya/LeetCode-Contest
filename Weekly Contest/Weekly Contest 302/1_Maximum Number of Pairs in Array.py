# 2341. Maximum Number of Pairs in Array
# https://leetcode.com/problems/maximum-number-of-pairs-in-array/

from collections import Counter

class Solution:
    def numberOfPairs(self, nums):
        '''
        even_count=0
        odd_count=0
        l=list(set(nums))
        for i in l:
            x=nums.count(i)
            if x%2!=0:
                odd_count+=1
            even_count+=(x//2)
        return [even_count,odd_count]
        '''

        c=Counter(nums)
        left=sum(c[i]%2 for i in c)
        return [(len(nums)-left)//2,left]