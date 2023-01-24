# 2457. Minimum Addition to Make Integer Beautiful
# https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/

class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        '''
        def valid(x):
            sum=0
            while x:
                sum+=(x%10)
                x//=10
            return sum<=target
        
        start=0
        while True:
            if valid(n+start):
                return start
            start+=1
        '''
        
        '''
        s=list(map(int,str(n)))
        idx=len(s)-1
        while sum(s)>target:
            s[idx]=0
            if idx==0:
                s.insert(0,1)
                break
            idx-=1
            s[idx]+=1
            while idx>0 and s[idx]==10:
                s[idx]=0
                idx-=1
                s[idx]+=1
            if idx==0 and s[idx]==10:
                s[idx]=0
                s.insert(0,1)
        return int("".join(str(i) for i in s))-n
        '''
        
        '''
        original=n
        base=0
        while sum(list(map(int,str(n))))>target:
            n=n//10+1
            base+=1
        return n*(10**base)-original
        '''

        diff=0
        base=10
        while sum(list(map(int,str(n+diff))))>target:
            diff=base-n%base
            base*=10
        return diff