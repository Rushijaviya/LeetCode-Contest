# 2576. Find the Maximum Number of Marked Indices
# https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/

class Solution:
    def maxNumOfMarkedIndices(self, nums):
        '''
        nums.sort()
        n=len(nums)
        i,j=0,n//2
        count=0
        while i<(n//2) and j<n:
            if 2*nums[i]<=nums[j]:
                j+=1
                i+=1
                count+=2
            else:
                j+=1
        return count
        '''

        nums.sort()
        n=len(nums)
        left=0
        for right in range(n-n//2,n):
            left+=(2*nums[left]<=nums[right])
        return 2*left