# 2391. Minimum Amount of Time to Collect Garbage
# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

from itertools import accumulate

class Solution:
    def garbageCollection(self, garbage, travel):
        '''
        def fun(char,lastidx):
            if lastidx==0:
                return garbage[0].count(char)
            count=garbage[0].count(char)
            idx=1
            while idx<=lastidx:
                count+=travel[idx-1]
                count+=garbage[idx].count(char)
                idx+=1
            return count

        midx,pidx,gidx=0,0,0
        for i in range(len(garbage)-1,-1,-1):
            if (not midx) and 'M' in garbage[i]:
                midx=i
            if (not pidx) and 'P' in garbage[i]:
                pidx=i
            if (not gidx) and 'G' in garbage[i]:
                gidx=i
            if midx and pidx and gidx:
                break
        
        ans=0
        ans+=fun('M',midx)
        ans+=fun('G',gidx)
        ans+=fun('P',pidx)
        return ans
        '''
        
        midx,pidx,gidx=0,0,0
        ans=0
        for i,word in enumerate(garbage):
            if ('M' in word):midx=i 
            if ('P' in word):pidx=i 
            if ('G' in word):gidx=i 
            ans+=len(word)
        
        travel=list(accumulate(travel))
        ans+=travel[midx-1] if midx>0 else 0
        ans+=travel[gidx-1] if gidx>0 else 0
        ans+=travel[pidx-1] if pidx>0 else 0
        return ans