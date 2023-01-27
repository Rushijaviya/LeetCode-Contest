# 2465. Number of Distinct Averages
# https://leetcode.com/problems/number-of-distinct-averages/

class Solution:
    def distinctAverages(self, nums):
        '''
        s=set()
        while nums:
            x=min(nums)
            y=max(nums)
            s.add((x+y)/2)
            nums.remove(x)
            nums.remove(y)
        return len(s)
        '''
        
        '''
        nums.sort()
        s=set()
        while nums:
            s.add((nums[0]+nums[-1])/2)
            nums.pop()
            nums.pop(0)
        return len(s)
        '''

        nums.sort()
        s=set()
        for i in range(len(nums)//2+1):
            s.add((nums[i]+nums[len(nums)-i-1])/2)
        return len(s)