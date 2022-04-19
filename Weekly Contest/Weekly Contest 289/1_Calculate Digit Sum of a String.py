# 2243. Calculate Digit Sum of a String
# https://leetcode.com/problems/calculate-digit-sum-of-a-string/

from functools import reduce
import math

class Solution:
    def digitSum(self, s, k):
        while len(s)>k:
            x=math.ceil(len(s)/k)
            l=[]
            for i in range(x):
                l.append(s[i*k:min(i*k+k,len(s))])
            for i in range(len(l)):
                sum=reduce(lambda x,y:int(x)+int(y),l[i])
                l[i]=str(sum)
            s="".join(l)
        return s