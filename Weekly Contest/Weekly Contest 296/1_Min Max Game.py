# 2293. Min Max Game
# https://leetcode.com/problems/min-max-game/

class Solution:
    def minMaxGame(self, nums):
        '''
        while len(nums)>1:
            temp=[]
            c=1
            for i in range(0,len(nums),2):
                if c:
                    temp.append(min(nums[i],nums[i+1]))
                else:
                    temp.append(max(nums[i],nums[i+1]))
                c=1-c
            nums=temp
        return nums[0]
        '''
        
        n=len(nums)
        while n>1:
            n-=(n//2)
            c=1
            for i in range(len(nums)//2):
                nums[i]=min(nums[2*i],nums[2*i+1]) if c else max(nums[2*i],nums[2*i+1])
                c=1-c
        return nums[0]