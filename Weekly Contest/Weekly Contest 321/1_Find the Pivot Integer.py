# 2485. Find the Pivot Integer
# https://leetcode.com/problems/find-the-pivot-integer/

from math import sqrt

class Solution:
    def pivotInteger(self, n: int) -> int:
        '''
        total=(n*(n+1))//2
        for i in range(n+1):
            s=(i*(i+1))//2
            remain=total-s+i
            if remain==s:
                return i
        return -1
        '''

        x=sqrt((n*(n+1))//2)
        return -1 if x%1 else int(x)