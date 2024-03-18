# 2709. Greatest Common Divisor Traversal
# https://leetcode.com/problems/greatest-common-divisor-traversal/

from math import sqrt

class Disjoint:
    def __init__(self,n):
        self.rank=[0]*n
        self.parent=[i for i in range(n)]

    def findpar(self,node):
        if self.parent[node]!=node:
            self.parent[node]=self.findpar(self.parent[node])
        return self.parent[node]
    
    def union(self,u,v):
        u,v=self.findpar(u),self.findpar(v)
        if self.rank[u]>self.rank[v]:
            self.parent[v]=u
        elif self.rank[v]>self.rank[u]:
            self.parent[u]=v
        else:
            self.parent[v]=u
            self.rank[u]+=1

class Solution:
    def canTraverseAllPairs(self, nums):
        
        def getprimefactor(num):
            for i in range(2,int(sqrt(num))+1):
                if num%i==0:
                    while num%i==0:
                        num//=i
                    yield i
            if num!=1:
                yield num
        
        n=len(nums)
        if n==1:
            return True
        obj=Disjoint(n)
        seen={}
        for i in range(n):
            if nums[i] == 1:
                return False
            for num in getprimefactor(nums[i]):
                if num in seen:
                    obj.union(i,seen[num])
                else:
                    seen[num]=i
        s=set()
        for i in range(n):
            s.add(obj.findpar(i))
        return len(s)==1