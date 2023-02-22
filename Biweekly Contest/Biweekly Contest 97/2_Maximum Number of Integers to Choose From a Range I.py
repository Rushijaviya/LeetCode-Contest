# 2554. Maximum Number of Integers to Choose From a Range I
# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

class Solution:
    def maxCount(self, banned, n, maxSum):
        sum=0
        length=0
        banned=set(banned)
        for i in range(1,n+1):
            if i not in banned:
                sum+=i
                length+=1
                if sum==maxSum:
                    return length
                elif sum>maxSum:
                    return length-1
        return length
        
        '''
        l=[i for i in range(1,n+1)]
        for num in set(banned):
            if num<=n:
                l.remove(num)
        l=list(accumulate(l))
        return bisect_right(l,maxSum)
        '''