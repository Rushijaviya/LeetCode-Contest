# 2615. Sum of Distances
# https://leetcode.com/problems/sum-of-distances/

from itertools import accumulate

class Solution:
    def distance(self, nums):
        '''
        # TLE
        d={}
        for idx,value in enumerate(nums):
            if value not in d:
                d[value]=[]
            d[value].append(idx)
        ans=[0]*len(nums)
        for i in range(nums):
            if nums[i] in d:
                for idx in d[nums[i]]:
                    ans[i]+=abs(i-idx)
        return ans
        '''
        
        '''
        # TLE
        visited={}
        n=len(nums)
        ans=[0]*n
        visited[nums[-1]]=[n-1]
        for i in range(n-2,-1,-1):
            if nums[i] in visited:
                for idx in visited[nums[i]]:
                    temp=abs(idx-i)
                    ans[idx]+=temp
                    ans[i]+=temp
                visited[nums[i]].append(i)
            else:
                visited[nums[i]]=[i]
        return ans
        '''

        d={}
        for idx,val in enumerate(nums):
            if val not in d:
                d[val]=[]
            d[val].append(idx)
        n=len(nums)
        ans=[0]*n
        for value in d:
            idxs=d[value]
            pref=list(accumulate(idxs))
            for idx in range(len(idxs)):
                right=(pref[-1]-pref[idx])-(idxs[idx]*(len(pref)-1-idx))
                left=idxs[idx]*(idx+1)-pref[idx]
                ans[idxs[idx]]=left+right
        return ans