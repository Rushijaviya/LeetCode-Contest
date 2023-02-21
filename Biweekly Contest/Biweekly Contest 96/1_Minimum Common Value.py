# 2540. Minimum Common Value
# https://leetcode.com/problems/minimum-common-value/

class Solution:
    def getCommon(self, nums1, nums2):
        return min(set(nums1).intersection(set(nums2)),default=-1)
            
        '''
        s=list(set(nums1).intersection(set(nums2)))
        if not s:
            return -1
        return sorted(s)[0]
        '''
    
        '''
        m,n=len(nums1),len(nums2)
        i,j=0,0
        while i<m and j<n:
            if nums1[i]==nums2[j]:
                return nums1[i]
            if nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return -1
        '''