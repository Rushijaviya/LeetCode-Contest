# 2193. Minimum Number of Moves to Make Palindrome
# https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/

class Solution:
    def minMovesToMakePalindrome(self, s):
        s=list(s)
        count=0
        while s:
            idx=s.index(s[-1])
            if idx==len(s)-1:
                count+=(idx//2)
            else:
                count+=idx
                s.pop(idx)
            s.pop()
        return count