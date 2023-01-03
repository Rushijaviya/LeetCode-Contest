# 2375. Construct Smallest Number From DI String
# https://leetcode.com/problems/construct-smallest-number-from-di-string/

class Solution:
    def smallestNumber(self, pattern):
        '''
        n=len(pattern)
        ans=[n+1]
        value=n
        for i in range(n-1,-1,-1):
            ans.insert(0,value)
            value-=1
            idx=0
            for j in range(i,n):
                if pattern[j]=='D' and ans[idx]<ans[idx+1]:
                    ans[idx],ans[idx+1]=ans[idx+1],ans[idx]
                    idx+=1
                elif pattern[j]=='I' and ans[idx]>ans[idx+1]:
                    ans[idx],ans[idx+1]=ans[idx+1],ans[idx]
                    idx+=1
                else:
                    break
        return "".join(str(i) for i in ans)
        '''

        n=len(pattern)
        ans=""
        stack=[]
        for i in range(n+1):
            stack.append(i+1)
            if i==n or pattern[i]=='I':
                while stack:
                    ans+=str(stack.pop())
        return ans