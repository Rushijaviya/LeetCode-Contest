# 2414. Length of the Longest Alphabetical Continuous Substring
# https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        '''
        prev=s[0]
        curr=1
        ans=0
        for i in s[1:]:
            if ord(i)==1+ord(prev):
                curr+=1
                prev=i
            else:
                ans=max(ans,curr)
                curr=1
                prev=i
        return max(ans,curr)
        '''

        curr=1
        ans=0
        for i in range(1,len(s)):
            if ord(s[i-1])+1==ord(s[i]):
                curr+=1
            else:
                ans=max(ans,curr)
                curr=1
        return max(ans,curr)