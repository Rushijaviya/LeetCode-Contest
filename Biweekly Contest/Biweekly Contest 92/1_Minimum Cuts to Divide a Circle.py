# 2481. Minimum Cuts to Divide a Circle
# https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/

class Solution:
    def numberOfCuts(self, n):
        '''
        if n==1:
            return 0
        if n%2:
            return n
        return n//2
        '''

        return n if n%2 and n!=1 else n//2