# 2358. Maximum Number of Groups Entering a Competition
# https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/

class Solution:
    def maximumGroups(self, grades):
        '''
        grades.sort()
        length=1
        ans=0
        idx=0
        n=len(grades)
        while idx+length<=n:
            ans+=1
            idx+=length
            length+=1
        return ans
        '''
        
        '''
        ans=1
        n=len(grades)
        while ans*(ans+1)<=2*n:
            ans+=1
        return ans-1
        '''
        
        start=1
        end=447
        n=len(grades)
        while start<end:
            mid=(start+end)//2
            if mid*(mid+1)<=2*n:
                start=mid+1
            else:
                end=mid
        return start-1
        
        '''
        return int((math.sqrt(1+8*len(grades))-1)//2)
        '''