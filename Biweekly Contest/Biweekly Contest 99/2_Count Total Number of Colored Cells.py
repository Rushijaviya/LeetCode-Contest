# 2579. Count Total Number of Colored Cells
# https://leetcode.com/problems/count-total-number-of-colored-cells/

class Solution:
    def coloredCells(self, n):
        '''
        ans=0
        start=1
        while n>1:
            ans+=(2*start)
            start+=2
            n-=1
        return ans+start
        '''

        return n*n+((n-1)*(n-1))