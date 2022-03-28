# 2206. Divide Array Into Equal Pairs
# https://leetcode.com/problems/divide-array-into-equal-pairs/

class Solution:
    def divideArray(self, nums):
        if len(nums)%2:
            return False
        l=list(set(nums))
        for i in l:
            if nums.count(i)%2:
                return False
        return True