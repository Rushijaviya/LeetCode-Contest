# 2411. Smallest Subarrays With Maximum Bitwise OR
# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

class Solution:
    def smallestSubarrays(self, nums):
        '''
        # TLE
        tar=0
        for i in nums:
            tar|=i
        ans=[]
        n=len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                ans.append(max(1,ans[-1]-1))
                continue
            val=nums[i]
            j=i+1
            temp=[val]
            while j<n and val<tar:
                val|=nums[j]
                j+=1
                temp.append(val)
            ans.append(temp.index(max(temp))+1)
        return ans
        '''

        bits=[0]*32
        n=len(nums)
        ans=[0]*n
        for i in range(n-1,-1,-1):
            for j in range(32):
                if nums[i]&(1<<j):
                    bits[j]=i
            ans[i]=max(1,max(bits)-i+1)
        return ans