# 2419. Longest Subarray With Maximum Bitwise AND
# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums):
        '''
        ans=0
        curr=0
        target=max(nums)
        for i in nums:
            if i==target:
                curr+=1
            else:
                ans=max(ans,curr)
                curr=0
        return max(ans,curr)
        '''
        
        ans=curr=target=0
        for i in nums:
            if i>target:
                target=i
                curr=0
                ans=0
            curr=curr+1 if i==target else 0
            ans=max(ans,curr)
        return ans
        
        '''
        target=max(nums)
        return max(len(list(l)) for val,l in groupby(nums) if val==target)
        '''