# 2302. Count Subarrays With Score Less Than K
# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

from itertools import accumulate

class Solution:
    def countSubarrays(self, nums, k):
        # Sliding Windows
        ans=0
        n=len(nums)
        start=sum=score=0
        for end in range(n):
            sum+=nums[end]
            score=sum*(end-start+1)
            while start<=end and score>=k:
                sum-=nums[start]
                start+=1
                score=sum*(end-start+1)
            ans+=(end-start+1)
        return ans
        
        '''
        # Prefix sum + Binary Search
        ans=0
        pref=[0]+list(accumulate(nums))
        n=len(nums)
        for i in range(1,n+1):
            start,end=i,n
            sum=score=0
            temp=-1
            while start<=end:
                mid=(start+end)//2
                sum=pref[mid]-pref[i-1]
                score=sum*(mid-i+1)
                if score>=k:
                    end=mid-1
                else:
                    temp=mid
                    start=mid+1
            if temp!=-1:
                ans+=(temp-i+1)
        return ans
        '''

        '''
        # TLE
        ans=0
        n=len(nums)
        pref=[0]*n
        pref[0]=nums[0]
        for i in range(1,n):
            pref[i]+=(nums[i]+pref[i-1])
        pref=[0]+pref
        for i in range(n):
            for j in range(i,n):
                if (pref[j+1]-pref[i])*(j+1-i)<k:
                    ans+=1
                else:
                    break
        return ans
        '''