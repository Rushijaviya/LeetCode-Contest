# 2369. Check if There is a Valid Partition For The Array
# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

from functools import lru_cache

class Solution:
    def validPartition(self, nums):
        '''
        # TLE
        def rec(idx,path):
            if idx==n:
                return (len(path)==3 or (len(path)==2 and path[0]==path[1]))
            if len(path)<2:
                if len(path)==0 or (len(path)==1 and ((path[0]==nums[idx]) or (path[0]+1==nums[idx]))):
                    return rec(idx+1,path+[nums[idx]])
                return False
            if len(path)==2:
                temp=False
                if path[0]==path[1]:
                    if nums[idx]==path[0]:
                        temp|=rec(idx+1,path+[nums[idx]])
                    temp|=rec(idx+1,[nums[idx]])
                else:
                    if nums[idx]==1+path[1]:
                        temp|=rec(idx+1,path+[nums[idx]])
                return temp
            return rec(idx+1,[nums[idx]])
            
        n=len(nums)
        return rec(0,[])
        '''
        
        @lru_cache(None)
        def rec(idx,prev,length,flag):
            if idx==n:
                return length==3 or (length==2 and flag)
            if length<2:
                if length==0:
                    return rec(idx+1,nums[idx],length+1,0)
                elif prev==nums[idx]:
                    return rec(idx+1,prev,length+1,1)
                elif prev+1==nums[idx]:
                    return rec(idx+1,nums[idx],length+1,0)
                return False
            elif length==2:
                temp=False
                if flag:
                    if prev==nums[idx]:
                        temp|=rec(idx+1,prev,length+1,1)
                    temp|=rec(idx+1,nums[idx],1,0)
                else:
                    if prev+1==nums[idx]:
                        temp|=rec(idx+1,nums[idx],length+1,0)
                return temp
            else:
                return rec(idx+1,nums[idx],1,0)

        n=len(nums)
        return rec(0,-1,0,0)
        
        '''
        n=len(nums)
        dp=[0]*n
        if nums[0]==nums[1]:
            dp[1]=1
        if n>2 and nums[0]==nums[1]==nums[2]:
            dp[2]=1
        if n>2 and nums[0]+1==nums[1] and nums[1]+1==nums[2]:
            dp[2]=1
        for i in range(3,n):
            if nums[i]==nums[i-1]:
                dp[i]|=dp[i-2]
            if nums[i]==nums[i-1]==nums[i-2]:
                dp[i]|=dp[i-3]
            if nums[i]==nums[i-1]+1 and nums[i-1]==nums[i-2]+1:
                dp[i]|=dp[i-3]
        return dp[-1]
        '''
        
        '''
        n=len(nums)
        dp=[0,0,0,0]
        if nums[0]==nums[1]:
            dp[1]=1
        if n>2 and nums[0]==nums[1]==nums[2]:
            dp[2]=1
        if n>2 and nums[0]+1==nums[1] and nums[1]+1==nums[2]:
            dp[2]=1
        for i in range(3,n):
            dp[i%4]=0
            if nums[i]==nums[i-1]:
                dp[i%4]|=dp[(i-2)%4]
            if nums[i]==nums[i-1]==nums[i-2]:
                dp[i%4]|=dp[(i-3)%4]
            if nums[i]==nums[i-1]+1 and nums[i-1]==nums[i-2]+1:
                dp[i%4]|=dp[(i-3)%4]
        return dp[(n-1)%4]
        '''