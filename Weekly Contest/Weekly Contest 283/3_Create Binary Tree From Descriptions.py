# 2196. Create Binary Tree From Descriptions
# https://leetcode.com/problems/create-binary-tree-from-descriptions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions):
        '''
        d={}
        child=set()
        for i in descriptions:
            node=d.get(i[0],TreeNode(i[0]))
            child.add(i[1])
            if i[2]:
                node.left=d.get(i[1],TreeNode(i[1]))
                d[i[1]]=node.left
            else:
                node.right=d.get(i[1],TreeNode(i[1]))
                d[i[1]]=node.right
            d[i[0]]=node
        root=None
        for i in descriptions:
            if i[0] not in child:
                root=d[i[0]]
                break
        return root
        '''

        d={}
        child=set()
        for p,c,l in descriptions:
            node=d.setdefault(p,TreeNode(p))
            ch=d.setdefault(c,TreeNode(c))
            if l:
                node.left=ch
            else:
                node.right=ch
            child.add(c)
        root=(set(d)-set(child)).pop()
        return d[root]