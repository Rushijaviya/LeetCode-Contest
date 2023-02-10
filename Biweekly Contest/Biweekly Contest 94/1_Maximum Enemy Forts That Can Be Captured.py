# 2511. Maximum Enemy Forts That Can Be Captured
# https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

class Solution:
    def captureForts(self, forts):
        '''
        ans=0
        n=len(forts)
        for idx in range(n):
            if forts[idx]==-1:
                left=idx-1
                right=idx+1
                while left>=0 and forts[left]==0:
                    left-=1
                if left==-1 or forts[left]==-1:
                    left=idx-1
                while right<n and forts[right]==0:
                    right+=1
                if right==n or forts[right]==-1:
                    right=idx+1
                ans=max(ans,right-idx-1,idx-left-1)
        return ans
        '''

        left=0
        ans=0
        for right in range(len(forts)):
            if forts[right]!=0:
                if forts[right]==-forts[left]:
                    ans=max(ans,right-left-1)
                left=right
        return ans