# 2279. Maximum Bags With Full Capacity of Rocks
# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

class Solution:
    def maximumBags(self, capacity, rocks, additionalRocks):
        diff=[]
        n=len(capacity)
        for i in range(n):
            diff.append(capacity[i]-rocks[i])
        diff.sort()
        ans=0
        idx=0
        while additionalRocks and idx<n:
            if additionalRocks<diff[idx]:
                break
            additionalRocks-=diff[idx]
            ans+=1
            idx+=1
        return ans