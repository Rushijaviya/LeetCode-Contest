# 2607. Make K-Subarray Sums Equal
# https://leetcode.com/problems/make-k-subarray-sums-equal/

from math import gcd

class Solution:
    def makeSubKSumEqual(self, arr, k):
        '''
        def rec(l):
            median=l[len(l)//2]
            return sum(abs(val-median) for val in l)

        temp=gcd(len(arr),k)
        ans=0
        for i in range(temp):
            ans+=rec(sorted(arr[i::temp]))
        return ans
        '''

        def rec(l):
            return sum(l[len(l)-1-idx]-l[idx] for idx in range(len(l)//2))

        temp=gcd(len(arr),k)
        ans=0
        for i in range(temp):
            ans+=rec(sorted(arr[i::temp]))
        return ans