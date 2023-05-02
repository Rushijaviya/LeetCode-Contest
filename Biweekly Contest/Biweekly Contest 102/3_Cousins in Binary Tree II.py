# 2641. Cousins in Binary Tree II
# https://leetcode.com/problems/cousins-in-binary-tree-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def replaceValueInTree(self, root):
        level=defaultdict(int)

        def dfs(node,lev):
            level[lev]+=node.val
            if node.left:
                dfs(node.left,lev+1)
            if node.right:
                dfs(node.right,lev+1)
        
        def dfs2(node,lev):
            prev_left=0
            if node.left:
                prev_left=node.left.val
                node.left.val=level[lev+1]-(node.left.val+(node.right.val if node.right else 0))
                dfs2(node.left,lev+1)
            if node.right:
                node.right.val=level[lev+1]-(node.right.val+prev_left)
                dfs2(node.right,lev+1)

        dfs(root,0)
        dfs2(root,0)
        root.val=0
        return root