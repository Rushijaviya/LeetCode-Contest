# 2458. Height of Binary Tree After Subtree Removal Queries
# https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def treeQueries(self, root, queries):
        '''
        # TLE
        @lru_cache(None)
        def findheight(node,target):
            if not node:
                return 0
            left=0
            right=0
            if node.left and node.left.val!=target:
                left=findheight(node.left,target)
            if node.right and node.right.val!=target:
                right=findheight(node.right,target)
            return 1+max(left,right)
        
        ans=[]
        for q in queries:
            ans.append(findheight(root,q)-1)
        return ans  
        '''
        
        depth,height={},{}

        def dfs(node,dep):
            if not node:
                return -1
            depth[node.val]=dep
            curr=max(dfs(node.left,dep+1),dfs(node.right,dep+1))+1
            height[node.val]=curr
            return curr

        dfs(root,0)
        cousin=defaultdict(list)
        for i in depth:
            cousin[depth[i]].append([-height[i],i])
            cousin[depth[i]].sort()
            if len(cousin[depth[i]])>2:
                cousin[depth[i]].pop()
        
        ans=[]
        for q in queries:
            dep=depth[q]
            if len(cousin[dep])==1:
                ans.append(dep-1)
            elif cousin[dep][0][1]==q:
                ans.append(dep-cousin[dep][1][0])
            else:
                ans.append(dep-cousin[dep][0][0])
        return ans
        
        '''
        @lru_cache(None)
        def height(node):
            if not node:
                return -1
            return max(height(node.left),height(node.right))+1
        
        def rec(node,depth,mx):
            if not node:
                return
            ans[node.val]=mx
            rec(node.left,depth+1,max(mx,depth+height(node.right)))
            rec(node.right,depth+1,max(mx,depth+height(node.left)))

        ans={}
        rec(root,1,0)
        return [ans[q] for q in queries]
        '''