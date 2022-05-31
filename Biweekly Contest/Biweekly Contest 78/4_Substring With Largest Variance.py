# 2272. Substring With Largest Variance
# https://leetcode.com/problems/substring-with-largest-variance/

class Solution:
    def largestVariance(self, s):
        n=len(s)
        ans=0
        for i in range(n):
            d={}
            for j in range(i,n):
                d[s[j]]=d.get(s[j],0)+1
                temp=sorted(d.values(),key=lambda x:x)
                ans=max(ans,temp[-1]-temp[0])
        return ans