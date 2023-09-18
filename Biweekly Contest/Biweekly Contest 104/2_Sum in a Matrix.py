# 2679. Sum in a Matrix
# https://leetcode.com/problems/sum-in-a-matrix/

class Solution:
    def matrixSum(self, nums):
        for row in nums:
            row.sort()
        ans=0
        for col in zip(*nums):
            ans+=max(col)
        return ans

        # return sum(max(col) for col in zip(*(sorted(row) for row in nums)))