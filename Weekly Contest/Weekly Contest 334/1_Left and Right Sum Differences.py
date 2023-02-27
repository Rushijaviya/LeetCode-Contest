# 2574. Left and Right Sum Differences
# https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRigthDifference(self, nums):
        '''
        ans=[]
        for i in range(len(nums)):
            ans.append(abs(sum(nums[:i])-sum(nums[i+1:])))
        return ans
        '''
        
        '''
        ans=[]
        pref=list(accumulate(nums))
        for i in range(len(nums)):
            ans.append(abs(pref[-1]-pref[i]-(pref[i-1] if i>0 else 0)))
        return ans
        '''

        ans=[]
        left,right=0,sum(nums)
        for num in nums:
            left+=num
            ans.append(abs(left-right))
            right-=num
        return ans