# 2606. Find the Substring With Maximum Cost
# https://leetcode.com/problems/find-the-substring-with-maximum-cost/

class Solution:
    def maximumCostSubstring(self, s, chars, vals):
        '''
        d={}
        for idx in range(26):
            d[chr(idx+97)]=idx+1
        for idx in range(len(chars)):
            d[chars[idx]]=vals[idx]
        s=list(map(lambda char:d[char],s))
        ans=0
        sum=0
        for i in s:
            sum=max(sum+i,i)
            ans=max(ans,sum)
        return ans
        '''

        d=dict(zip(chars,vals))
        ans=sum=0
        for char in s:
            value=d.get(char,ord(char)-96)
            sum=max(sum+value,value)
            ans=max(ans,sum)
        return ans