# 2592. Maximize Greatness of an Array
# https://leetcode.com/problems/maximize-greatness-of-an-array/

class Solution:
    def maximizeGreatness(self, nums):
        '''
        # TLE
        nums.sort()
        l=nums.copy()
        ans=0
        for i in l:
            for j in range(len(nums)):
                if nums[j]>i:
                    nums.pop(j)
                    ans+=1
                    break
        return ans
        '''

        '''
        nums.sort()
        l=nums.copy()
        ans=0
        idx=0
        for i in l:
            while idx<len(nums):
                if nums[idx]>i:
                    ans+=1
                    idx+=1
                    break
                idx+=1
        return ans
        '''

        nums.sort()
        idx=0
        for num in nums:
            if num>nums[idx]:
                idx+=1
        return idx
        
        '''
        return len(nums)-max(Counter(nums).values())
        '''