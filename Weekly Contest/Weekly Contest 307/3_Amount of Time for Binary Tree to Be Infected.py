# 2385. Amount of Time for Binary Tree to Be Infected
# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root, start: int) -> int:
        '''
        # BFS + Graph
        adj_list=defaultdict(list)
        queue=[(root,None)]
        while queue:
            node,per=queue.pop(0)
            if per:
                adj_list[per].append(node.val)
                adj_list[node.val].append(per)
            if node.left:
                queue.append((node.left,node.val))
            if node.right:
                queue.append((node.right,node.val))
        ans=0
        queue=[(0,start)]
        visited=set()
        visited.add(start)
        while queue:
            cost,node=queue.pop(0)
            ans=max(ans,cost)
            for u in adj_list[node]:
                if u not in visited:
                    visited.add(u)
                    queue.append((cost+1,u))
        return ans
        '''

        def dfs(node):
            if not node:
                return False,0
            left,ld=dfs(node.left)
            right,rd=dfs(node.right)
            nonlocal ans
            if node.val==start:
                ans=max(ans,ld,rd)
                return True,0
            if left:
                sum=1+ld+rd
                ans=max(ans,sum)
                return True,1+ld
            if right:
                sum=1+ld+rd
                ans=max(ans,sum)
                return True,1+rd
            sum=1+max(ld,rd)
            return False,sum

        ans=0
        dfs(root)
        return ans