# 2331. Evaluate Boolean Binary Tree
# https://leetcode.com/problems/evaluate-boolean-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root):
        '''
        def postorder(node):
            if not node:
                return []
            return postorder(node.left)+postorder(node.right)+[node.val]

        l=postorder(root)
        stack=[]
        for i in l:
            if i in [0,1]:
                stack.append(i)
            elif i==2:
                x=stack.pop()
                y=stack.pop()
                stack.append(y or x)
            else:
                x=stack.pop()
                y=stack.pop()
                stack.append(y and x)
        return stack[0]
        '''

        def postorder(node):
            if node.val in [0,1]:
                return node.val
            return (postorder(node.left) or postorder(node.right)) if node.val==2 else (postorder(node.left) and postorder(node.right))

        return postorder(root)