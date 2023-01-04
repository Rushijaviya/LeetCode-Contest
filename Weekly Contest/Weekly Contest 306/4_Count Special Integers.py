# 2376. Count Special Integers
# https://leetcode.com/problems/count-special-integers/

class Solution:
    def countSpecialNumbers(self, n):
        '''
        # TLE
        def vaild(i):
            l=list(str(i))
            return len(l)==len(set(l))

        count=0
        for i in range(1,n+1):
            if vaild(i):
                count+=1
        return count
        '''

        s=str(n)
        length=len(s)
        ans=0
        for i in range(length-1):
            idx=9
            count=1
            for _ in range(i):
                count*=idx
                idx-=1
            ans+=(9*count)
        visited=set()
        for i in range(length):
            smaller=0
            for j in range(int(s[i])):
                if j not in visited:
                    smaller+=1
            if i==0 and smaller>0:
                smaller-=1
            idx=9
            count=1
            for k in range(i+1,length):
                count*=(idx-len(visited))
                idx-=1
            ans+=(smaller*count)
            if int(s[i]) in visited:
                return ans
            else:
                visited.add(int(s[i]))
        return ans+1