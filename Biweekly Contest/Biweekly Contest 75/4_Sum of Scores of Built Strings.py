# 2223. Sum of Scores of Built Strings
# https://leetcode.com/problems/sum-of-scores-of-built-strings/

class Solution:
    def sumScores(self, s):
        '''
        # TLE
        def check(l):
            ans=0
            start=0
            while start<len(l) and start<len(s) and s[start]==l[start]:
                start+=1
                ans+=1
            return ans
        
        count=0
        s=list(s)
        for i in range(len(s)):
            count+=check(s[len(s)-(i+1):])
        return count
        '''

        # Z-function
        s=list(s)
        n=len(s)
        z=[0]*n
        left=right=0
        for i in range(1,n):
            if i<=right:
                z[i]=min(z[i-left],right-i+1)
            while i+z[i]<n and s[z[i]]==s[i+z[i]]:
                z[i]+=1
            if i+z[i]-1>right:
                right=i+z[i]-1
                left=i
        return sum(z)+n