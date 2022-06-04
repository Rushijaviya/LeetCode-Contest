# 2287. Rearrange Characters to Make Target String
# https://leetcode.com/problems/rearrange-characters-to-make-target-string/

from collections import defaultdict

class Solution:
    def rearrangeCharacters(self, s, target):
        d=defaultdict(int)
        t=defaultdict(int)
        for i in target:
            d[i]+=1
        for i in s:
            t[i]+=1
        ans=float('inf')
        for i in d:
            ans=min(ans,t[i]//d[i])
        return ans
        
        '''
        d={}
        for i in target:
            d[i]=s.count(i)
        ans=0
        while True:
            for i in target:
                if i in d and d[i]!=0:
                    d[i]-=1
                else:
                    return ans
            ans+=1
        '''

        '''
        d, t = map(Counter, (s, target))
        return min(d[c] // t[c] for c in t)
        '''
        