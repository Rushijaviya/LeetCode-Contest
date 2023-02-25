# 2564. Substring XOR Queries
# https://leetcode.com/problems/substring-xor-queries/

from collections import defaultdict

class Solution:
    def substringXorQueries(self, s, queries):
        '''
        ans=[]
        n=len(s)
        d={}
        for first,second in queries:
            target=first^second
            if target in d:
                ans.append(d[target])
                continue
            value=0
            left=0
            for right in range(n):
                value<<=1
                if s[right]=='1':
                    value+=1
                while left<right and (value>target or s[left]=='0'):
                    if s[left]=='1':
                        value-=2**(right-left)
                    left+=1
                if value==target:
                    d[target]=[left,right]
                    ans.append([left,right])
                    break
            else:
                d[target]=[-1,-1]
                ans.append([-1,-1])
        return ans
        '''
        
        '''
        ans=[]
        n=len(s)
        d={}
        for first,second in queries:
            target=bin(first^second)[2:]
            if target in d:
                ans.append(d[target])
                continue
            idx=s.find(target)
            if idx==-1:
                ans.append([-1,-1])
            else:
                ans.append([idx,len(target)+idx-1])
            d[target]=ans[-1]
        return ans
        '''

        d=defaultdict(lambda:[-1,-1])
        n=len(s)
        for i in range(n-1,-1,-1):
            if s[i]=='0':
                d[0]=[i,i]
                continue
            value=0
            for j in range(i,n):
                value=value*2+int(s[j])
                if value>2**32:
                    break
                d[value]=[i,j]
        return [d[first^second] for first,second in queries]