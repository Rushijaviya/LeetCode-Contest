# 2405. Optimal Partition of String
# https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s):
        '''
        ans=0
        idx=0
        n=len(s)
        while idx<n:
            visited=set()
            visited.add(s[idx])
            idx+=1
            while idx<n and s[idx] not in visited:
                visited.add(s[idx])
                idx+=1
            ans+=1
        return ans
        '''
        
        '''
        visited=set()
        ans=0
        for i in s:
            if i in visited:
                visited=set()
                ans+=1
            visited.add(i)
        return 1+ans
        '''

        flag=0
        ans=0
        for i in s:
            idx=ord(i)-ord('a')
            if (flag>>idx)&1:
                ans+=1
                flag=0
            flag|=(1<<idx)
        return 1+ans