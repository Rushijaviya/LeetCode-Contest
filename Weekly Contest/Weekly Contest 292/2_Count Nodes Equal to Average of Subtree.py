# 2265. Count Nodes Equal to Average of Subtree
# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root):
        '''
        def preorder(node):
            if not node:
                return []
            return [node.val]+preorder(node.left)+preorder(node.right)

        queue=[root]
        ans=0
        while queue:
            curr=queue.pop(0)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            l=preorder(curr)
            if curr.val == sum(l)//len(l):
                ans+=1
        return ans
        '''

        def postorder(node):
            if not node:
                return 0,0
            left_sum,left_count=postorder(node.left)
            right_sum,right_count=postorder(node.right)
            total_sum=left_sum+right_sum+node.val
            total_count=left_count+right_count+1
            if node.val == total_sum//total_count:
                self.ans+=1
            return total_sum,total_count

        self.ans=0
        postorder(root)
        return self.ans