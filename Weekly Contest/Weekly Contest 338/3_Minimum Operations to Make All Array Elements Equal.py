# 2602. Minimum Operations to Make All Array Elements Equal
# https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

from bisect import bisect_left
from itertools import accumulate

class Solution:
    def minOperations(self, nums, queries):
        '''
        # TLE
        n=len(queries)
        ans=[0]*n
        for num in nums:
            for i in range(n):
                ans[i]+=abs(queries[i]-num)
        return ans
        '''

        nums.sort()
        pref=[0]+list(accumulate(nums))
        ans=[]
        for qur in queries:
            idx=bisect_left(nums,qur)
            temp=qur*(idx)-pref[idx]+(pref[-1]-pref[idx])-qur*(len(nums)-(idx))
            ans.append(temp)
        return ans