# 2382. Maximum Segment Sum After Removals
# https://leetcode.com/problems/maximum-segment-sum-after-removals/

from itertools import accumulate
from sortedcontainers import SortedList

class Solution:
    def maximumSegmentSum(self, nums, removeQueries):
        '''
        # TLE
        n=len(nums)
        ans=[]
        for i in range(n):
            nums[removeQueries[i]]=0
            s=0
            idx=0
            while idx<n:
                if nums[idx]==0:
                    idx+=1
                    continue
                count=0
                while idx<n and nums[idx]!=0:
                    count+=nums[idx]
                    idx+=1
                s=max(s,count)
            ans.append(s)
        return ans
        '''
        
        '''
        # TLE
        n=len(nums)
        nums=list(accumulate(nums))
        ans=[]
        for i in range(n):
            idx=removeQueries[i]
            value=nums[idx]
            nums[idx]=0
            idx+=1
            while idx<n:
                if nums[idx]<value:
                    break
                nums[idx]-=value
                idx+=1
            ans.append(max(nums))
        return ans
        '''
        
        '''
        n=len(nums)
        pref=[0]+list(accumulate(nums))
        segments=SortedList([(0,n-1)])
        sums=SortedList([0,pref[-1]])
        ans=[]
        for i in removeQueries:
            idx=segments.bisect_left((i+1,-1))-1
            left,right=segments[idx]
            segments.remove((left,right))
            sums.remove(pref[right+1]-pref[left])
            if left<=i-1:
                segments.add((left,i-1))
                sums.add(pref[i]-pref[left])
            if right>=i+1:
                segments.add((i+1,right))
                sums.add(pref[right+1]-pref[i+1])
            ans.append(sums[-1])
        return ans
        '''

        d={}
        ans=[]
        curr=0
        for i in removeQueries[::-1][:-1]:
            d[i]=(nums[i],1)
            rval,rlen=d.get(i+1,(0,0))
            lval,llen=d.get(i-1,(0,0))
            total=nums[i]+rval+lval
            d[i+rlen]=(total,llen+rlen+1)
            d[i-llen]=(total,llen+rlen+1)
            curr=max(curr,total)
            ans.append(curr)
        return ans[::-1]+[0]