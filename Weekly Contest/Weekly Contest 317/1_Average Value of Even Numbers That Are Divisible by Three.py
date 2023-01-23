# 2455. Average Value of Even Numbers That Are Divisible by Three
# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

class Solution:
    def averageValue(self, nums):
        '''
        poss=[]
        for num in nums:
            if num%2==0 and num%3==0:
                poss.append(num)
        if not poss:
            return 0
        return sum(poss)//len(poss)
        '''

        sum,length=0,0
        for num in nums:
            if num%6==0:
                sum+=num
                length+=1
        if length==0:
            return 0
        return sum//length