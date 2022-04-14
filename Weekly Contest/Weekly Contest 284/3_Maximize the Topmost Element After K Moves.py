# 2202. Maximize the Topmost Element After K Moves
# https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/

class Solution:
    def maximumTop(self, nums, k):
        if len(nums)==1:
            return nums[0] if k%2==0 else -1
        if len(nums)>=k:
            if k==0:
                return nums[0]
            if k==1:
                return nums[1]
            return max(max(nums[:k-1]),nums[k] if k!=len(nums) else -1)
        return max(nums)