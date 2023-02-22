# 2553. Separate the Digits in an Array
# https://leetcode.com/problems/separate-the-digits-in-an-array/

class Solution:
    def separateDigits(self, nums):
        '''
        ans=[]
        for num in nums:
            for char in str(num):
                ans.append(int(char))
        return ans
        '''

        return list(map(int,list(''.join(map(str,nums)))))