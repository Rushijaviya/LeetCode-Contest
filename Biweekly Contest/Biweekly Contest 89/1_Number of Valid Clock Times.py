# 2437. Number of Valid Clock Times
# https://leetcode.com/problems/number-of-valid-clock-times/

class Solution:
    def countTime(self, time: str) -> int:
        ans=1
        for i in range(len(time)):
            if time[i]!='?':
                continue
            if i==0:
                if time[i+1]>'3':
                    ans=2
                else:
                    ans=3
            if i==1:
                if time[i-1]=='?':
                    ans=24
                elif time[i-1]=='2':
                    ans=4
                else:
                    ans=10
            if i==3:
                ans*=6
            if i==4:
                ans*=10
        return ans
        
        '''
        def vaild(s):
            try:
                a=int("".join(s[:2]))
                b=int("".join(s[3:]))
            except:
                return 0
            return 0<=a<24 and 0<=b<60

        def rec(idx):
            if idx==5:
                return vaild(time)
            count=0
            if time[idx]=='?':
                for j in range(10):
                    time[idx]=str(j)
                    count+=rec(idx+1)
                time[idx]='?'
            count+=rec(idx+1)
            return count
        
        time=list(time)
        return rec(0)
        '''