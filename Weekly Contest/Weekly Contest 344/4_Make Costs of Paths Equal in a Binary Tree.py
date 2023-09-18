# 2673. Make Costs of Paths Equal in a Binary Tree
# https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/

class Solution:
    def minIncrements(self, n, cost):
        def dfs(idx):
            if idx>n:
                return 0
            left = dfs(2*idx)
            right = dfs(2*idx+1)
            nonlocal ans
            ans+=abs(left-right)
            return cost[idx-1]+max(left,right)

        ans=0
        dfs(1)
        return ans
        
        '''
        ans=0
        for i in range(n-1,1,-2):
            ans+=abs(cost[i-1]-cost[i])
            cost[i//2-1]+=max(cost[i],cost[i-1])
        return ans
        '''
        
        '''
        ans=0
        for i in range(n//2-1,-1,-1):
            left,right=2*i+1,2*i+2
            ans+=abs(cost[left]-cost[right])
            cost[i]+=max(cost[left],cost[right])
        return ans
        '''