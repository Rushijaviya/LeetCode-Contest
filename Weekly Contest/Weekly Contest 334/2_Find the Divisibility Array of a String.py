# 2575. Find the Divisibility Array of a String
# https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

class Solution:
    def divisibilityArray(self, word, m):
        num=0
        ans=[]
        for char in word:
            num*=10
            num+=int(char)
            if num%m:
                ans.append(0)
            else:
                ans.append(1)
            num%=m
        return ans