# 2200. Find All K-Distant Indices in an Array
# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

class Solution:
    def findKDistantIndices(self, nums, key, k):
        ans=[]
        for i in range(len(nums)):
            if key in nums[max(0,i-k):min(len(nums),i+k+1)]:
                ans.append(i)
        return ans