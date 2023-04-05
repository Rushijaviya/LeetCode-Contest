# 2593. Find Score of an Array After Marking All Elements
# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

class Solution:
    def findScore(self, nums):
        arr=[(val,idx) for idx,val in enumerate(nums)]
        arr.sort()
        ans=0
        n=len(nums)
        visited=[0]*n
        for val,idx in arr:
            if not visited[idx]:
                ans+=val
                if idx>0:
                    visited[idx-1]=1
                visited[idx]=1
                if idx+1<n:
                    visited[idx+1]=1
        return ans