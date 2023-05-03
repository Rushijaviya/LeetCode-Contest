# 2644. Find the Maximum Divisibility Score
# https://leetcode.com/problems/find-the-maximum-divisibility-score/

class Solution:
    def maxDivScore(self, nums, divisors):
        score,ans=0,divisors[0]
        for div in divisors:
            count=0
            for num in nums:
                if num%div==0:
                    count+=1
            if count>score:
                score,ans=count,div
            elif count==score:
                ans=min(ans,div)
        return ans