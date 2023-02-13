# 2516. Take K of Each Character From Left and Right
# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

from collections import Counter

class Solution:
    def takeCharacters(self, s, k):
        '''
        @lru_cache(None)
        def dp(left,right,ka,kb,kc):
            if ka<=0 and kb<=0 and kc<=0:
                return 0
            if left>right:
                return float('inf')
            return 1+min(dp(left+1,right,ka-(s[left]=='a'),kb-(s[left]=='b'),kc-(s[left]=='c')),dp(left,right-1,ka-(s[right]=='a'),kb-(s[right]=='b'),kc-(s[right]=='c')))
            
        n=len(s)
        x=dp(0,n-1,k,k,k)
        return x if x!=float('inf') else -1
        '''
        
        limit=Counter(s)
        for char in 'abc':
            limit[char]-=k
            if limit[char]<0:
                return -1
        left,ans=0,0
        curr=Counter()
        for right,char in enumerate(s):
            curr[char]+=1
            while curr[char]>limit[char]:
                curr[s[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return len(s)-ans
        
        '''
        ka,kb,kc=0,0,0
        for char in s:
            ka+=(char=='a')
            kb+=(char=='b')
            kc+=(char=='c')
        if ka<k or kb<k or kc<k:
            return -1
        left,right=len(s)-1,len(s)-1
        ans=len(s)
        while left>=0:
            ka-=(s[left]=='a')
            kb-=(s[left]=='b')
            kc-=(s[left]=='c')
            while ka<k or kb<k or kc<k:
                ka+=(s[right]=='a')
                kb+=(s[right]=='b')
                kc+=(s[right]=='c')
                right-=1
            ans=min(ans,left+len(s)-right-1)
            left-=1
        return ans
        '''