# 2334. Subarray With Elements Greater Than Varying Threshold
# https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/

class Solution:
    def validSubarraySize(self, nums, threshold):
        
        '''
        def vaildSubArray(length,min_value):
            prev=-1
            for i in range(len(nums)):
                if nums[i]<=min_value:
                    if i-prev-1>=length:
                        return True
                    prev=i
            return len(nums)-prev-1>=length

        if len(nums)>threshold:
            return len(nums)
        if max(nums)>threshold:
            return 1
        for i in range(len(nums),0,-1):
            if vaildSubArray(i,threshold//i):
                return i
        return -1
        '''
        
        '''
        # monotonic stack 
        if len(nums)>threshold:
            return len(nums)
        if max(nums)>threshold:
            return 1
        n=len(nums)
        nexts=[n]*n
        stack=[0]
        for i in range(1,n):
            while stack and nums[stack[-1]]>nums[i]:
                x=stack.pop()
                nexts[x]=i
            stack.append(i)
        prevs=[-1]*n
        stack=[n-1]
        for i in range(n-2,-1,-1):
            while stack and nums[stack[-1]]>nums[i]:
                x=stack.pop()
                prevs[x]=i
            stack.append(i)
        for i in range(n):
            length=nexts[i]-prevs[i]-1
            if nums[i]>threshold//length:
                return length
        return -1
        '''
        
        nums=[0]+nums+[0]
        stack=[0]
        for i in range(1,len(nums)):
            while nums[i]<nums[stack[-1]]:
                idx=stack.pop()
                length=i-stack[-1]-1
                if nums[idx]>threshold//length:
                    return length
            stack.append(i)
        return -1

        '''
        class Disjoint:
            def __init__(self) -> None:
                self.parent={}
                self.size={}

            def insert(self,x):
                if x not in self.parent:
                    self.parent[x]=x
                    self.size[x]=1
            
            def findpar(self,x):
                if self.parent[x]!=x:
                    self.parent[x]=self.findpar(self.parent[x])
                return self.parent[x]
            
            def union(self,x,y):
                x,y=self.findpar(x),self.findpar(y)
                if x==y:
                    return
                if self.size[x]>self.size[y]:
                    self.parent[y]=x
                    self.size[x]+=self.size[y]
                else:
                    self.parent[x]=y
                    self.size[y]+=self.size[x]

        n=len(nums)
        ks=[]
        for i in range(n):
            ks.append((threshold//nums[i] + 1,i))
        ks.sort()

        obj=Disjoint()
        for k,idx in ks:
            obj.insert(idx)
            if idx-1 in obj.parent:
                obj.union(idx,idx-1)
            if idx+1 in obj.parent:
                obj.union(idx,idx+1)
            if obj.size[obj.findpar(idx)]>=k:
                return k
        return -1
        '''