# 2283. Check if Number Has Equal Digit Count and Digit Value
# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

from collections import defaultdict


class Solution:
    def digitCount(self, num: str) -> bool:
        '''
        return True if num in ["1210", "2020" , "21200", "3211000", "42101000", "521001000", "6210001000"] else False
        '''

        d=defaultdict(int)
        n=len(num)
        for i in num:
            d[i]+=1
        for i,j in enumerate(num):
            if d[str(i)]!=int(num[i]):
                return False
        return True
        
        '''
        n=len(num)
        for i in range(n):
            if str(num.count(str(i)))!=num[i]:
                return False
        return True
        '''