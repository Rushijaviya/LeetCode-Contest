# 2342. Max Sum of a Pair With Equal Sum of Digits
# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

class Solution:
    def maximumSum(self, nums):
        '''
        d=defaultdict(list)
        for i in nums:
            s=reduce(lambda x,y:(int(x)+int(y)),list(str(i)))
            d[int(s)].append(i)
        ans=-1
        for i in d:
            if len(d[i])>1:
                d[i].sort()
                ans=max(ans,d[i][-1]+d[i][-2])
        return ans
        '''

        def digitsum(i):
            res=0
            while i>0:
                res+=i%10
                i//=10
            return res
        
        d={}
        ans=-1
        for i in nums:
            s=digitsum(i)
            if s not in d:
                d[s]=i
            else:
                ans=max(ans,d[s]+i)
                d[s]=max(d[s],i)
        return ans