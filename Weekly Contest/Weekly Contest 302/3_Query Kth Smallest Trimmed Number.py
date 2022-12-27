# 2343. Query Kth Smallest Trimmed Number
# https://leetcode.com/problems/query-kth-smallest-trimmed-number/

class Solution:
    def smallestTrimmedNumbers(self, nums, queries):
        ans=[]
        n=len(nums)
        length=len(nums[0])
        for k,trim in queries:
            l=[]
            for idx in range(n):
                l.append([nums[idx][length-trim:],idx])
            l.sort()
            ans.append(l[k-1][1])
        return ans