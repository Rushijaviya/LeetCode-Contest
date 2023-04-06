# 2597. The Number of Beautiful Subsets
# https://leetcode.com/problems/the-number-of-beautiful-subsets/

class Solution:
    def beautifulSubsets(self, nums, k):
        def dp(idx,path):
            if idx==n:
                return 1 if path else 0
            x=0
            for num in path:
                if nums[idx]-num==k:
                    break
            else:
                x+=dp(idx+1,path+[nums[idx]])
            return dp(idx+1,path)+x
            
        n=len(nums)
        nums.sort()
        return dp(0,[])