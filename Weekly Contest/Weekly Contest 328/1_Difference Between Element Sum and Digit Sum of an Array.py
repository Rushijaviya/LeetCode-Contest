# 2535. Difference Between Element Sum and Digit Sum of an Array
# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

class Solution:
    def differenceOfSum(self, nums):
        '''
        def digitsum(x):
            ans=0
            while x:
                ans+=(x%10)
                x//=10
            return ans
        
        ele_sum=0
        dig_sum=0
        for num in nums:
            dig_sum+=digitsum(num)
            ele_sum+=num
        return abs(ele_sum-dig_sum)
        '''

        return sum(nums)-sum(map(int,list("".join(map(str,nums)))))