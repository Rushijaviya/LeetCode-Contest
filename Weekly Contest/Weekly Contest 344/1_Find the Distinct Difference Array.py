# 2670. Find the Distinct Difference Array
# https://leetcode.com/problems/find-the-distinct-difference-array/

class Solution:
    def distinctDifferenceArray(self, nums):
        '''
        ans=[]
        for idx in range(len(nums)):
            ans.append(len(set(nums[:idx+1]))-len(set(nums[idx+1:])))
        return ans
        '''
        
        '''
        prefix=defaultdict(int)
        suffix=Counter(nums)
        ans=[]
        for val in nums:
            suffix[val]-=1
            if suffix[val]==0:
                del suffix[val]
            prefix[val]+=1
            ans.append(len(prefix)-len(suffix))
        return ans
        '''

        visited=set()
        ans=[]
        for num in nums:
            ans.append((ans[-1] if ans else 0)+(1 if num not in visited else 0))
            visited.add(num)
        visited=set()
        dist = 0
        for idx in range(len(nums)-1,0,-1):
            dist += 1 if nums[idx] not in visited else 0
            visited.add(nums[idx])
            ans[idx-1]-=dist
        return ans