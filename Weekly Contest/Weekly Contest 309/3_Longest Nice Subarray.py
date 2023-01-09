# 2401. Longest Nice Subarray
# https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums):
        '''
        n=len(nums)
        ans=1
        start=0
        for end in range(1,n):
            for j in range(end-1,start-1,-1):
                if nums[end]&nums[j]:
                    start=j+1
                    break
            ans=max(ans,end-start+1)
        return ans
        '''

        ans=1
        start=0
        value=nums[0]
        for end in range(1,len(nums)):
            while value&nums[end]:
                value^=nums[start]
                start+=1
            ans=max(ans,end-start+1)
            value|=nums[end]
        return ans