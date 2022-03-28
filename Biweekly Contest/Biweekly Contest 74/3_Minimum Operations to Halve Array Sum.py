# 2208. Minimum Operations to Halve Array Sum
# https://leetcode.com/problems/minimum-operations-to-halve-array-sum/

from heapq import heapify, heappop, heappush


class Solution:
    def halveArray(self, nums):
        half=sum(nums)/2
        count=0
        heap=[-i for i in nums]
        heapify(heap)
        while half>0:
            temp=heappop(heap)
            temp/=2
            half+=temp
            heappush(heap,temp)
            count+=1
        return count