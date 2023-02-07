# 2498. Frog Jump II
# https://leetcode.com/problems/frog-jump-ii/

from bisect import bisect_left

class Solution:
    def maxJump(self, stones):
        '''
        # TLE
        @lru_cache(None)
        def dp2(idx,visited,res):
            if idx==0:
                return res
            temp=float('inf')
            for j in range(idx-1,-1,-1):
                if j not in visited:
                    temp=min(temp,dp2(j,tuple(set(visited)|set([j])),max(res,stones[idx]-stones[j])))
            return temp
        
        @lru_cache(None)
        def dp(idx,visited,res):
            if idx==n-1:
                return max(res,dp2(n-1,visited,0))
            temp=float('inf')
            for j in range(idx+1,n):
                temp=min(temp,dp(j,tuple(set(visited)|set([j])),max(res,stones[j]-stones[idx])))
            return temp
        
        n=len(stones)
        return dp(0,tuple(),0)
        '''

        '''
        # TLE
        def dp2(idx,res):
            if idx==0:
                return res
            temp=float('inf')
            for j in range(idx-1,-1,-1):
                if not visited[j]:
                    visited[j]=True
                    temp=min(temp,dp2(j,max(res,stones[idx]-stones[j])))
                    visited[j]=False
            return temp
        
        def dp(idx,res):
            if idx==n-1:
                return max(res,dp2(n-1,0))
            temp=float('inf')
            for j in range(idx+1,n):
                visited[j]=True
                temp=min(temp,dp(j,max(res,stones[j]-stones[idx])))
                visited[j]=False
            return temp
        
        n=len(stones)
        visited=[False]*n
        return dp(0,0)
        '''
        
        '''
        def valid(gap):
            curr_idx=0
            visited=set()
            while curr_idx<len(stones)-1:
                next_idx=bisect_left(stones,min(stones[-1],stones[curr_idx]+gap))
                while stones[next_idx]>min(stones[-1],stones[curr_idx]+gap):
                    next_idx-=1
                if next_idx==curr_idx:
                    return False
                curr_idx=next_idx
                visited.add(curr_idx)
            while curr_idx>0:
                next_idx=bisect_left(stones,stones[curr_idx]-gap)
                while next_idx<curr_idx and next_idx in visited:
                    next_idx+=1
                if next_idx==curr_idx:
                    return False
                curr_idx=next_idx
                visited.add(curr_idx)
            return True

        start=0
        end=stones[-1]-stones[0]
        while start<=end:
            mid=(start+end)//2
            if valid(mid):
                end=mid-1
            else:
                start=mid+1
        return start
        '''

        ans=stones[1]-stones[0]
        for i in range(2,len(stones),2):
            ans=max(ans,stones[i]-stones[i-2])
        for i in range(3,len(stones),2):
            ans=max(ans,stones[i]-stones[i-2])
        return ans

        # return max((stones[i]-stones[i-2] for i in range(2,len(stones))),default=stones[1])