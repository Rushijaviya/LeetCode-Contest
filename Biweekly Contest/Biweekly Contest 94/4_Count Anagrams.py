# 2514. Count Anagrams
# https://leetcode.com/problems/count-anagrams/

from collections import Counter
from math import factorial

class Solution:
    def countAnagrams(self, s: str) -> int:
        words=s.split()
        ans=1
        for word in words:
            temp=1
            c=Counter(word)
            for i in c:
                temp*=factorial(c[i])
            ans*=(factorial(len(word))//temp)
        return ans%(10**9+7)