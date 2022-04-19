# 2244. Minimum Rounds to Complete All Tasks
# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

class Solution:
    def minimumRounds(self, tasks):
        d={}
        for i in tasks:
            d[i]=d.get(i,0)+1
        ans=0
        for k in d.keys():
            x=d[k]
            if x==1:
                return -1
            if x==2:
                ans+=1
            if x==3:
                ans+=1
            if x>=4:
                div=x//3
                rem=x%3
                if rem==0:
                    ans+=div
                if rem==2:
                    ans+=(div+1)
                if rem==1:
                    ans+=(div-1+2)  
        return ans