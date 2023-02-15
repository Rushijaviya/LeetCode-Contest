# 2530. Maximal Score After Applying K Operations
# https://leetcode.com/problems/maximal-score-after-applying-k-operations/

from heapq import heapify, heappop, heappush
from math import ceil
from sortedcontainers import SortedList

class Solution:
    def maxKelements(self, nums, k):
        '''
        nums=SortedList(nums)
        ans=0
        for _ in range(k):
            x=nums.pop()    
            ans+=x
            nums.add(ceil(x/3))
        return ans
        '''

        nums=[-i for i in nums]
        heapify(nums)
        ans=0
        for _ in range(k):
            x=-heappop(nums)
            ans+=x
            heappush(nums,-ceil(x/3))
        return ans