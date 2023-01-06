# 2396. Strictly Palindromic Number
# https://leetcode.com/problems/strictly-palindromic-number/

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        '''
        def numToBase(n,i):
            res=""
            while n:
                res+=str(n%i)
                n//=i
            return res[::-1]

        for i in range(2,n-1):
            x=numToBase(n,i)
            if x!=x[::-1]:
                return False
        return True
        '''

        return False