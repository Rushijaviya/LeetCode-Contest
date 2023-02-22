# 2551. Put Marbles in Bags
# https://leetcode.com/problems/put-marbles-in-bags/

class Solution:
    def putMarbles(self, weights, k):
        '''
        @lru_cache(None)
        def dp(idx,start,bages,cost):
            if bages>k:
                return
            if bages==k and idx!=n:
                return
            if k-bages>n-idx:
                return
            nonlocal max_val,min_val
            if idx<n and bages==k-1:
                value=weights[start]+weights[-1]
                max_val=max(max_val,cost+value)
                min_val=min(min_val,cost+value)
                return
            if idx==n:
                if bages==k and start==idx:
                    print(cost)
                    max_val=max(max_val,cost)
                    min_val=min(min_val,cost)
                return
            dp(idx+1,start,bages,cost)
            dp(idx+1,idx+1,bages+1,cost+weights[idx]+weights[start])
            
            
        max_val=float('-inf')
        min_val=float('inf')
        n=len(weights)
        dp(0,0,0,0)
        return max_val-min_val
        '''
        
        '''
        if k==1 or len(weights)==k:
            return 0
        n=len(weights)
        l=[]
        for i in range(n-1):
            l.append(weights[i]+weights[i+1])
        l.sort()
        min_sum,max_sum=0,0
        for i in range(k-1):
            min_sum+=l[i]
            max_sum+=l[len(l)-i-1]
        return max_sum-min_sum
        '''

        if k==1 or len(weights)==k:
            return 0
        l=[weights[i+1]+weights[i] for i in range(len(weights)-1)]
        l.sort()
        return sum(l[-(k-1):])-sum(l[:k-1])
        
        '''
        if k==1 or len(weights)==k:
            return 0
        l=[weights[i+1]+weights[i] for i in range(len(weights)-1)]
        return sum(nlargest(k-1,l))-sum(nsmallest(k-1,l))
        '''