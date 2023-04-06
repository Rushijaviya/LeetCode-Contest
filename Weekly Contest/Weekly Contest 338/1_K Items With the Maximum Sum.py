# 2600. K Items With the Maximum Sum
# https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        '''
        if numOnes>=k:
            return k
        elif numOnes+numZeros>=k:
            return numOnes
        else:
            return numOnes-(k-numOnes-numZeros)
        '''

        return k if k<= numOnes else numOnes - max(0, k-numOnes-numZeros)