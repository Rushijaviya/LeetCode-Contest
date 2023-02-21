# 2541. Minimum Operations to Make Array Equal II
# https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/

class Solution:
    def minOperations(self, nums1, nums2, k):
        pos=0
        neg=0
        if nums1==nums2:
            return 0
        if k==0:
            return -1
        for i in range(len(nums2)):
            if nums1[i]>nums2[i]:
                if (nums1[i]-nums2[i])%k!=0:
                    return -1
                pos+=(nums1[i]-nums2[i])
            else:
                if (nums2[i]-nums1[i])%k!=0:
                    return -1
                neg+=(nums2[i]-nums1[i])
        if pos==neg:
            return pos//k
        return -1