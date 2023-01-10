# 2413. Smallest Even Multiple
# https://leetcode.com/problems/smallest-even-multiple/

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return 2*n if n%2 else n

        # return n*(n%2+1)

        # return n<<(n%2)