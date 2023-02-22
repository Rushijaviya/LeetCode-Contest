# 2550. Count Collisions of Monkeys on a Polygon
# https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

class Solution:
    def monkeyMove(self, n: int) -> int:
        '''
        mod=10**9+7
        return (pow(2,n,mod)-2)%mod
        '''
        
        def powerTLE(a,b):
            if b==0:
                return 1
            ans=powerTLE(a,b//2)
            if b%2:
                return ans*ans*a
            return ans*ans
        
        def power2TLE(a,b):
            ans=1
            while b:
                if b%2:
                    ans*=a
                a*=a
                b//=2
            return ans
                
        def power(a,b):
            if b==0:
                return 1
            ans=power(a,b//2)%(10**9+7)
            if b%2:
                return ans*ans*a
            return ans*ans
        
        def power2(a,b):
            ans=1
            while b:
                if b%2:
                    ans*=a
                a*=a
                a%=(10**9+7)
                b//=2
            return ans
        
        return (power(2,n)-2)%(10**9+7)