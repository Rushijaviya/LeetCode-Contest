# 2233. Maximum Product After K Increments
# https://leetcode.com/problems/maximum-product-after-k-increments/

from functools import reduce
import heapq


class Solution:
    def maximumProduct(self, nums, k):
        heapq.heapify(nums)
        while k:
            k-=1
            x=heapq.heappop(nums)
            heapq.heappush(nums,x+1)
        return reduce(lambda a,b:(a*b)%(10**9+7),nums)