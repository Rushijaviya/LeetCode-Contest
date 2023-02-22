# 2549. Count Distinct Numbers on Board
# https://leetcode.com/problems/count-distinct-numbers-on-board/

class Solution:
    def distinctIntegers(self, n: int) -> int:
        if n==1:
            return 1
        return n-1

        # return max(n-1,1)