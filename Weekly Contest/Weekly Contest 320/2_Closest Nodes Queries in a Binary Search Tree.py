# 2476. Closest Nodes Queries in a Binary Search Tree
# https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from bisect import bisect_left, bisect_right


class Solution:
    def closestNodes(self, root, queries):
        '''
        def inorder(node):
            if not node:
                return []
            return inorder(node.left)+[node.val]+inorder(node.right)
        
        l=inorder(root)
        ans=[]
        for q in queries:
            res=[-1,-1]
            for i in l:
                if i<q:
                    res[0]=i
                elif i>q:
                    res[1]=i
                    break
                else:
                    res=[i,i]
                    break
            ans.append(res)
        return ans
        '''
        
        '''
        # TLE
        def inorder(node):
            if not node:
                return []
            return inorder(node.left)+[node.val]+inorder(node.right)
        
        l=inorder(root)
        ans=[]
        for q in queries:
            idx=bisect_left(l,q)
            if idx<len(l):
                if l[idx]==q:
                    temp=[q,q]
                elif idx>0:
                    temp=[l[idx-1],l[idx]]
                elif idx==0:
                    temp=[-1,l[idx]]
            else:
                temp=[l[-1],-1]
            ans.append(temp)
        return ans
        '''
        
        def inorder(node,l):
            if node:
                inorder(node.left,l)
                l.append(node.val)
                inorder(node.right,l)
        
        l=[]
        inorder(root,l)
        ans=[]
        for q in queries:
            idx=bisect_left(l,q)
            if idx<len(l):
                if l[idx]==q:
                    temp=[q,q]
                elif idx>0:
                    temp=[l[idx-1],l[idx]]
                elif idx==0:
                    temp=[-1,l[idx]]
            else:
                temp=[l[-1],-1]
            ans.append(temp)
        return ans
        
        '''
        # TLE
        def dfs(node,target,min_val,max_Val):
            if not node:
                return min_val,max_Val                
            if node.val<target:
                return dfs(node.right,target,node.val,max_Val)
            elif node.val>target:
                return dfs(node.left,target,min_val,node.val)
            else:
                min_val=node.val
                max_Val=node.val
                return min_val,max_Val

        ans=[]
        for q in queries:
            min_val,max_val=float('inf'),float('-inf')
            min_val,max_val=dfs(root,q,min_val,max_val)
            ans.append([min_val if min_val!=float('inf') else -1,max_val if max_val!=float('-inf') else -1])
        return ans
        '''