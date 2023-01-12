# 2425. Bitwise XOR of All Pairings
# https://leetcode.com/problems/bitwise-xor-of-all-pairings/

class Solution:
    def xorAllNums(self, nums1, nums2):
        '''
        ans=0
        for i in nums1:
            for j in nums2:
                ans^=(i^j)
        return ans
        '''
        
        '''
        temp=0
        for i in nums2:
            temp^=i
        ans=0
        n=len(nums2)
        for i in nums1:
            if n%2==0:
                ans^=(temp)
            else:
                ans^=(temp^i)
        return ans
        '''

        ans=0
        if len(nums1)%2:
            for i in nums2:
                ans^=i
        if len(nums2)%2:
            for i in nums1:
                ans^=i
        return ans