# 2542. Maximum Subsequence Score
# https://leetcode.com/problems/maximum-subsequence-score/

import heapq

class Solution:
    def maxScore(self, nums1, nums2, k):
        sum=0
        l=list(zip(nums1,nums2))
        l.sort(key=lambda x:-x[1])
        queue=[]
        ans=0
        for i,j in l:
            heapq.heappush(queue,i)
            sum+=i
            if len(queue)>k:
                sum-=heapq.heappop(queue)
            if len(queue)==k:
                ans=max(ans,sum*j)
        return ans