# 2487. Remove Nodes From Linked List
# https://leetcode.com/problems/remove-nodes-from-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head):
        '''
        stack=[]
        curr=head
        while curr:
            while stack and stack[-1].val<curr.val:
                stack.pop()
            stack.append(curr)
            curr=curr.next
        ans=stack[0]
        curr=ans
        for i in stack[1:]:
            curr.next=i
            curr=curr.next 
        return ans
        '''
        
        '''
        def rec(node):
            if not node:
                return 
            node.next=rec(node.next)
            if node.next and node.val<node.next.val:
                return node.next
            return node

        return rec(head)
        '''

        def reverse(curr):
            prev=None
            while curr:
                next=curr.next
                curr.next=prev
                prev=curr
                curr=next
            return prev

        head=reverse(head)
        curr=head
        max_val=curr.val
        while curr.next:
            if curr.next.val<max_val:
                curr.next=curr.next.next
            else:
                curr=curr.next
                max_val=curr.val
        return reverse(head)