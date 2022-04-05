# 2226. Maximum Candies Allocated to K Children
# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies, k):
        left,right=0,sum(candies)//k
        while left<right:
            mid=(left+right+1)//2
            count=0
            for i in candies:
                count+=(i//mid)
            if k>count:
                right=mid-1
            else:
                left=mid
        return left