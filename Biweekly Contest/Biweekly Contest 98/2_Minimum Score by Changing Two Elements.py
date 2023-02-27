# 2567. Minimum Score by Changing Two Elements
# https://leetcode.com/problems/minimum-score-by-changing-two-elements/

class Solution:
    def minimizeSum(self, nums):
        '''
        nums.sort()
        return min(nums[-1]-nums[2],nums[-3]-nums[0],nums[-2]-nums[1])
        '''

        first_max_val,second_max_val,third_max_val=float('-inf'),float('-inf'),float('-inf')
        first_min_val,second_min_val,third_min_val=float('inf'),float('inf'),float('inf')
        for num in nums:
            if num>=first_max_val:
                first_max_val,second_max_val,third_max_val=num,first_max_val,second_max_val
            elif num>=second_max_val:
                second_max_val,third_max_val=num,second_max_val
            elif num>=third_max_val:
                third_max_val=num
            if num<=first_min_val:
                first_min_val,second_min_val,third_min_val=num,first_min_val,second_min_val
            elif num<=second_min_val:
                second_min_val,third_min_val=num,second_min_val
            elif num<=third_min_val:
                third_min_val=num
        return min(first_max_val-third_min_val,third_max_val-first_min_val,second_max_val-second_min_val)