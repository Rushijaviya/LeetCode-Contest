# 2357. Make Array Zero by Subtracting Equal Amounts
# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

class Solution:
    def minimumOperations(self, nums):
        '''
        nums=set(nums)
        if 0 in nums:
            nums.remove(0)
        nums=list(nums)
        nums.sort()
        if len(nums)<=2:
            return len(nums)
        prev=nums[0]
        count=1
        for i in nums[1:]:
            if prev<i:
                count+=1
                prev=i
        return count
        '''

        return len(set(nums))-(0 in nums)