# 2527. Find Xor-Beauty of Array
# https://leetcode.com/problems/find-xor-beauty-of-array/

class Solution:
    def xorBeauty(self, nums):
        ans=0
        for i in nums:
            ans^=i
        return ans

        # return reduce(lambda x,y:x^y,nums)