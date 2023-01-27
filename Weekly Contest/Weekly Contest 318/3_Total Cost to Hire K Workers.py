# 2462. Total Cost to Hire K Workers
# https://leetcode.com/problems/total-cost-to-hire-k-workers/

import heapq

class Solution:
    def totalCost(self, costs, k, candidates):
        queue=[]
        left=0
        while left<candidates:
            heapq.heappush(queue,(costs[left],0))
            left+=1
        count=0
        right=len(costs)-1
        while left<=right and count!=candidates:
            heapq.heappush(queue,(costs[right],1))
            right-=1
            count+=1
        ans=0
        while k:
            k-=1
            cost,side=heapq.heappop(queue)
            ans+=cost
            if left<=right:
                if side:
                    heapq.heappush(queue,(costs[right],1))
                    right-=1
                else:
                    heapq.heappush(queue,(costs[left],0))
                    left+=1
        return ans
        
        '''
        left=costs[:candidates]
        right=costs[max(len(costs)-candidates,candidates):]
        heapq.heapify(left)
        heapq.heapify(right)
        start=candidates
        end=len(costs)-candidates-1
        ans=0
        for _ in range(k):
            if not right or left and left[0]<=right[0]:    
                ans+=heapq.heappop(left)
                if start<=end:
                    heapq.heappush(left,costs[start])
                    start+=1
            else:
                ans+=heapq.heappop(right)
                if start<=end:
                    heapq.heappush(right,costs[end])
                    end-=1
        return ans
        '''