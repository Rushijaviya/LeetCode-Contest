# 2552. Count Increasing Quadruplets
# https://leetcode.com/problems/count-increasing-quadruplets/

class Solution:
    def countQuadruplets(self, nums):
        n = len(nums)
        dp = [0] * n
        ans = 0
        for j in range(n):
            prev_small = 0
            for i in range(j):
                if nums[j] > nums[i]:
                    prev_small += 1
                    ans += dp[i]
                elif nums[j] < nums[i]:
                    dp[i] += prev_small
        return ans