# 2563. Count the Number of Fair Pairs
# https://leetcode.com/problems/count-the-number-of-fair-pairs/

from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums, lower, upper):
        '''
        # TLE
        nums.sort()
        count=0
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if lower<=nums[i]+nums[j]<=upper:
                    count+=1
                elif nums[i]+nums[j]>upper:
                    break
        return count
        '''
        
        '''
        # TLE
        l=[(i,j) for i,j in Counter(nums).items()]
        l.sort(key=lambda x:(x[0],-x[1]))
        ans=0
        n=len(l)
        for idx in range(n):
            if lower<=2*l[idx][0]<=upper:
                ans+=((l[idx][1]*(l[idx][1]-1))//2)
            for j in range(idx+1,n):
                if lower<=l[idx][0]+l[j][0]<=upper:
                    ans+=(l[idx][1]*l[j][1])
                elif l[idx][0]+l[j][0]>upper:
                    break
        return ans
        '''
        
        '''
        nums.sort()
        n=len(nums)
        ans=0
        for i in range(n):
            left=bisect_left(nums,lower-nums[i])
            right=bisect_right(nums,upper-nums[i])
            if right>left:
                if lower<=nums[left]+nums[i]<=upper:
                    ans+=max(0,min(right,i)-left)
                elif lower<=nums[left+1]+nums[i]<=upper:
                    ans+=max(0,min(i,right)-left-1)
        return ans
        '''
        
        '''
        nums.sort()
        n=len(nums)
        ans=0
        for i in range(n):
            left_idx=bisect_left(nums,lower-nums[i])
            right_idx=bisect_right(nums,upper-nums[i])
            ans+=max(0,min(i,right_idx)-left_idx)
        return ans
        '''

        def count(limit):
            start=0
            end=len(nums)-1
            ans=0
            while start<end:
                if nums[start]+nums[end]>limit:
                    end-=1
                else:
                    ans+=(end-start)
                    start+=1
            return ans

        nums.sort()
        return count(upper)-count(lower-1)