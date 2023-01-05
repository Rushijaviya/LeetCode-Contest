# 2384. Largest Palindromic Number
# https://leetcode.com/problems/largest-palindromic-number/

from collections import Counter

class Solution:
    def largestPalindromic(self, num: str) -> str:
        c=Counter(num)
        idx=9
        middle=-1
        ans=""
        while idx>0:
            if c[str(idx)]:
                ans+=(str(idx)*(c[str(idx)]//2))
                if c[str(idx)]%2:
                    middle=max(middle,idx)
            idx-=1
        if ans and c['0']:
            ans+=('0'*(c['0']//2))
            if c['0']%2:
                middle=max(middle,0)
        if middle!=-1:
            ans+=str(middle)+ans[::-1]
        else:
            ans+=ans[::-1]
        if not ans and c['0']:
            return '0'
        return ans