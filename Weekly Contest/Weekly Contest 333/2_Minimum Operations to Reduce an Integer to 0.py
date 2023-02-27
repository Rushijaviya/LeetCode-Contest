# 2571. Minimum Operations to Reduce an Integer to 0
# https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/

class Solution:
    def minOperations(self, n: int) -> int:
        l=[1<<i for i in range(32)]
        ans=0
        while n:
            closest=min(l,key=lambda x:abs(x-n))
            n=abs(n-closest)
            ans+=1
        return ans
        
        '''
        ans=0
        for i in range(14):
            if (n+(1<<i)).bit_count()<n.bit_count():
                n+=(1<<i)
                ans+=1
        return ans+n.bit_count()
        '''

        # return (n^(n*3)).bit_count()