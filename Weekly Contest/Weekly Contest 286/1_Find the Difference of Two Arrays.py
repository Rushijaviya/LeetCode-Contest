# 2215. Find the Difference of Two Arrays
# https://leetcode.com/problems/find-the-difference-of-two-arrays/

class Solution:
    def findDifference(self, nums1, nums2):
        '''
        # Method 1
        l1=[]
        l2=[]
        for i in nums1:
            if i not in nums2 and i not in l1:
                l1.append(i)
        for i in nums2:
            if i not in nums1 and i not in l2:
                l2.append(i)
        return [l1,l2]
        '''

        # Method 2
        s1=set(nums1)
        s2=set(nums2)
        return [list(s1-s2),list(s2-s1)]