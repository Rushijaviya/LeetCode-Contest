# 2407. Longest Increasing Subsequence II
# https://leetcode.com/problems/longest-increasing-subsequence-ii/

class SEG:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * 2 * self.n
       
    def query(self, l, r):
        l += self.n
        r += self.n
        ans = 0
        while l < r:
            if l & 1:
                ans = max(ans, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                ans = max(ans, self.tree[r])
            l >>= 1
            r >>= 1
        return ans
    
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1])

class Solution:
    def lengthOfLIS(self, nums, k):
        '''
        # TLE
        n=len(nums)
        dp=[1]*n
        for i in range(1,n):
            for j in range(i):
                if 0<nums[i]-nums[j]<=k:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
        '''
        
        '''
        # TLE
        arr=[0]*(100001)
        ans=0
        for i in nums:
            arr[i]=1+max(arr[max(0,i-k):i])
            ans=max(ans,arr[i])
        return ans
        '''

        n, ans = max(nums), 1
        seg = SEG(n)
        for a in nums:
            a -= 1
            premax = seg.query(max(0, a - k), a)
            ans = max(ans, premax + 1)
            seg.update(a, premax + 1)
        return ans