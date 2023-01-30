# 2471. Minimum Number of Operations to Sort a Binary Tree by Level
# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root) -> int:
        '''
        # TLE
        def makesorted(l):
            res=0
            for idx in range(len(l)):
                minidx=idx
                for j in range(idx+1,len(l)):
                    if l[j]<l[minidx]:
                        minidx=j
                if minidx!=idx:
                    l[minidx],l[idx]=l[idx],l[minidx]
                    res+=1
            return res
        
        level=[root]
        count=0
        while level and root:
            count+=makesorted([node.val for node in level])
            temp=[[node.left,node.right] for node in level]
            level=[side for node in temp for side in node if side]
        return count
        '''    
        
        def makesorted(l):
            temp=sorted(l)
            res=0
            d={}
            for i in range(len(l)):
                d[l[i]]=i
            for i in range(len(l)):
                if temp[i]!=l[i]:
                    idx=d[temp[i]]
                    d[temp[i]]=i
                    d[l[i]]=idx
                    l[i],l[idx]=l[idx],l[i]
                    res+=1
            return res
        
        level=[root]
        count=0
        while level and root:
            count+=makesorted([node.val for node in level])
            temp=[[node.left,node.right] for node in level]
            level=[side for node in temp for side in node if side]
        return count
        
        '''
        def cyclesort(l):
            res=0
            d={}
            for idx,val in enumerate(sorted(l)):
                d[val]=idx
            visited=[0]*len(l)
            for i in range(len(l)):
                if visited[i] or l[i]==d[l[i]]:
                    continue
                c=0
                while not visited[i] and d[l[i]]!=i:
                    visited[i]=1
                    i=d[l[i]]
                    c+=1
                res+=max(0,c-1)
            return res
        
        level=[root]
        count=0
        while level and root:
            count+=cyclesort([node.val for node in level])
            temp=[[node.left,node.right] for node in level]
            level=[side for node in temp for side in node if side]
        return count
        '''