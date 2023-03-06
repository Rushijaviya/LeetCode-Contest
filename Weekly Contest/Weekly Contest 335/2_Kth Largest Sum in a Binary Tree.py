# 2583. Kth Largest Sum in a Binary Tree
# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root, k):
        ans=[]
        level=[root]
        while level and root:
            ans.append(sum(node.val for node in level))
            temp=[[node.left,node.right] for node in level]
            level=[side for node in temp for side in node if side]
        ans.sort(reverse=True)
        return ans[k-1] if (k-1)<len(ans) else -1