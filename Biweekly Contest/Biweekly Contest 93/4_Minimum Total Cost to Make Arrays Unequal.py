# 2499. Minimum Total Cost to Make Arrays Unequal
# https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/

from collections import defaultdict

class Solution:
    def minimumTotalCost(self, nums1, nums2):
        d=defaultdict(int)
        n=len(nums1)
        swap=0
        max_freq=0
        max_ele=0
        ans=0
        for i in range(n):
            if nums1[i]==nums2[i]:
                d[nums1[i]]+=1
                if max_freq<d[nums1[i]]:
                    max_freq=d[nums1[i]]
                    max_ele=nums1[i]
                swap+=1
                ans+=i
        for i in range(n):
            if max_freq>(swap//2) and nums1[i]!=nums2[i] and nums1[i]!=max_ele and nums2[i]!=max_ele:
                swap+=1
                ans+=i
        if max_freq>(swap//2):
            return -1
        return ans