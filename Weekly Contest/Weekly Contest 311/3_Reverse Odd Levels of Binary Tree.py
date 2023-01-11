# 2415. Reverse Odd Levels of Binary Tree
# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root):
        idx=0
        level=[root]
        while root and level:
            if idx%2:
                x=[node for node in level]
                temp=[node.val for node in x[::-1]]
                for i in range(len(x)):
                    x[i].val=temp[i]
            temp=[[node.left,node.right] for  node in level]
            level=[side for node in temp for side in node if side]
            idx+=1
        return root