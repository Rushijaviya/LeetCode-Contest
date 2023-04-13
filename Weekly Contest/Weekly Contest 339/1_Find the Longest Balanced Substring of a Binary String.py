# 2609. Find the Longest Balanced Substring of a Binary String
# https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/

class Solution:
    def findTheLongestBalancedSubstring(self, s):
        ans=0
        n=len(s)
        for i in range(n):
            if s[i]=='1':
                left=i-1
                right=i
                while left>=0 and right<n  and s[left]=='0' and s[right]=='1':
                    left-=1
                    right+=1
                ans=max(ans,right-left-1)
        return ans