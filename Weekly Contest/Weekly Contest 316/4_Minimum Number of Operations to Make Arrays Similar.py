# 2449. Minimum Number of Operations to Make Arrays Similar
# https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

class Solution:
    def makeSimilar(self, nums, target):
        '''
        nums.sort()
        target.sort()
        odd_nums,even_nums=[],[]
        odd_target,even_target=[],[]
        for i in range(len(nums)):
            if nums[i]%2:
                odd_nums.append(nums[i])
            else:
                even_nums.append(nums[i])
            if target[i]%2:
                odd_target.append(target[i])
            else:
                even_target.append(target[i])
        cost=0
        for i,j in zip(odd_nums,odd_target):
            cost+=max(0,i-j)
        for i,j in zip(even_nums,even_target):
            cost+=max(0,i-j)
        return cost//2
        '''

        nums.sort(key=lambda x:(x%2,x))
        target.sort(key=lambda x:(x%2,x))
        return sum(i-j for i,j in zip(nums,target) if i-j>0)//2