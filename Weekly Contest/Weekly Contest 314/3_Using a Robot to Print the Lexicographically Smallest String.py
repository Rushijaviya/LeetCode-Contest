# 2434. Using a Robot to Print the Lexicographically Smallest String
# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        '''
        def lowest(c):
            for i in range(26):
                if c.get(chr(i+97),0)>0:
                    return chr(i+97)
            return 'z'

        stack=[]
        ans=""
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        for i in s:
            d[i]-=1
            stack.append(i)
            while stack and stack[-1]<=lowest(d):
                ans+=stack.pop()
        while stack:
            ans+=stack.pop()
        return ans
        '''

        c=Counter(s)
        ans=""
        stack=[]
        lowest='a'
        for i in s:
            stack.append(i)
            c[i]-=1
            while lowest<'z' and c[lowest]==0:
                lowest=chr(ord(lowest)+1)
            while stack and stack[-1]<=lowest:
                ans+=stack.pop()
        return ans