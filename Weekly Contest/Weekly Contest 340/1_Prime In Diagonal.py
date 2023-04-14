# 2614. Prime In Diagonal
# https://leetcode.com/problems/prime-in-diagonal/

from math import sqrt

class Solution:
    def diagonalPrime(self, nums):

        def is_prime(num):
            if num==1:
                return False
            for i in range(2,int(sqrt(num))+1):
                if num%i==0:
                    return False
            return True

        ans=0
        n=len(nums)
        for i in range(n):
            if is_prime(nums[i][i]):
                ans=max(ans,nums[i][i])
            if is_prime(nums[i][n-1-i]):
                ans=max(ans,nums[i][n-1-i])
        return ans