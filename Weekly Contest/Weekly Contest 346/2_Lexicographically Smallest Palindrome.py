# 2697. Lexicographically Smallest Palindrome
# https://leetcode.com/problems/lexicographically-smallest-palindrome/

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        start,end=0,len(s)-1
        s=list(s)
        while start<end:
            if s[start]!=s[end]:
                if s[start]<s[end]:
                    s[end]=s[start]
                else:
                    s[start]=s[end]
            start+=1
            end-=1
        return "".join(s)