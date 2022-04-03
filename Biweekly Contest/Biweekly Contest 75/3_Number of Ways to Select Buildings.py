# 2222. Number of Ways to Select Buildings
# https://leetcode.com/problems/number-of-ways-to-select-buildings/

class Solution:
    def numberOfWays(self, s):
        '''
        # TLE
        def count(s1,s2,m,n):
            if m==0 and n==0:
                return 1
            if n==0:
                return 1
            if m==0:
                return 0
            if (m,n) in memo:
                return memo[(m,n)]
            if s1[m-1]==s2[n-1]:
                memo[(m,n)]=count(s1,s2,m-1,n-1)+count(s1,s2,m-1,n)
                return memo[(m,n)]
            memo[(m,n)]=count(s1,s2,m-1,n)
            return memo[(m,n)]

        memo={}
        count1=count(s,"010",len(s),3)
        memo={}
        count2=count(s,"101",len(s),3)
        return count1+count2
        '''

        '''
        count0=count1=0
        for i in s:
            if i=='1':
                count1+=1
            else:
                count0+=1
        current0=current1=ans=0
        for i in s:
            if i=='1':
                ans+=(count0*current0)
                count1-=1
                current1+=1
            else:
                ans+=(count1*current1)
                count0-=1
                current0+=1
        return ans
        '''

        dp={"0":0,"1":0,"01":0,"010":0,"10":0,"101":0}
        for i in s:
            if i=='0':
                dp["0"]+=1
                dp["10"]+=dp["1"]
                dp["101"]+=dp["01"]
            else:
                dp["1"]+=1
                dp["01"]+=dp["0"]
                dp["010"]+=dp["10"]
        return dp["101"]+dp["010"]