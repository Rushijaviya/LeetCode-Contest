# 2588. Count the Number of Beautiful Subarrays
# https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/

from collections import defaultdict

class Solution:
    def beautifulSubarrays(self, nums):
        '''
        n=len(nums)
        ans=0
        for i in range(n):
            c=Counter()
            count=0
            for bit in range(21):
                if nums[i]&(1<<bit):
                    c[bit]+=1
                    count+=1
            if count==0:
                ans+=1
            for j in range(i+1,n):
                for bit in range(21):
                    if nums[j]&(1<<bit):
                        c[bit]+=1
                        if c[bit]%2:
                            count+=1
                        else:
                            count-=1
                if count==0:
                    ans+=1
        return ans
        '''

        d=defaultdict(int)
        d[0]=1
        ans=0
        total=0
        for num in nums:
            total^=num
            ans+=d[total]
            d[total]+=1
        return ans