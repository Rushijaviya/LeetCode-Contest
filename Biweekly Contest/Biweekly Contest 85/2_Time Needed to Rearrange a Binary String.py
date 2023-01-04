# 2380. Time Needed to Rearrange a Binary String
# https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/

class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        '''
        n=len(s)
        time=0
        s=list(s)
        while True:
            flag=0
            idx=0
            while idx<n-1:
                if s[idx]=='0' and s[idx+1]=='1':
                    s[idx],s[idx+1]=s[idx+1],s[idx]
                    idx+=1
                    flag=1
                idx+=1
            if not flag:
                return time
            time+=1
        '''
        
        '''
        ans=0
        while '01' in s:
            s=s.replace('01','10')
            ans+=1
        return ans
        '''

        zeros=0
        seconds=0
        for i in s:
            if i=='0':
                zeros+=1
            if i=='1' and zeros:
                seconds=max(seconds+1,zeros)
        return seconds