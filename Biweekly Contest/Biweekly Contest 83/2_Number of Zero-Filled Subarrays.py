# 2348. Number of Zero-Filled Subarrays
# https://leetcode.com/problems/number-of-zero-filled-subarrays/

class Solution:
    def zeroFilledSubarray(self, nums):
        '''
        count=0
        ans=0
        for i in nums:
            if i==0:
                count+=1
            else:
                ans+=((count*(count+1))//2)
                count=0
        return ans+((count*(count+1))//2)
        '''

        ans=0
        count=0
        for i in nums:
            if i==0:
                count+=1
            else:
                count=0
            ans+=count
        return ans

        '''
        ans=0
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                j=i+1
            ans+=(i-j+1)
        return ans
        '''