# 2587. Rearrange Array to Maximize Prefix Score
# https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/

class Solution:
    def maxScore(self, nums):
        '''
        nums.sort(reverse=True)
        nums=list(accumulate(nums))
        count=0
        for i in nums:
            if i<=0:
                break
            count+=1
        return count
        '''

        nums.sort(reverse=True)
        sum=0
        count=0
        for num in nums:
            sum+=num
            if sum<=0:
                break
            count+=1
        return count