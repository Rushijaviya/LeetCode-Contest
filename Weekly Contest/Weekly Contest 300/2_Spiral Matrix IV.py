# 2326. Spiral Matrix IV
# https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head):
        def traversal(startRow,endRow,startCol,endCol,head):
            for i in range(startCol,endCol):
                if not head:
                    return None
                ans[startRow][i]=head.val
                head=head.next
            for i in range(startRow+1,endRow):
                if not head:
                    return None
                ans[i][endCol-1]=head.val
                head=head.next
            if endCol-startCol>1:
                for i in range(endCol-2,startCol-1,-1):
                    if not head:
                        return None
                    ans[endRow-1][i]=head.val
                    head=head.next
            if endRow-startRow>1:
                for i in range(endRow-2,startRow,-1):
                    if not head:
                        return None
                    ans[i][startCol]=head.val
                    head=head.next
            return head

        ans=[[-1]*n for _ in range(m)]
        startRow,startCol=0,0
        endRow,endCol=m,n
        while startRow<endRow and startCol<endCol and head:
            head=traversal(startRow,endRow,startCol,endCol,head)
            startRow+=1
            startCol+=1
            endRow-=1
            endCol-=1
        return ans
        
        '''
        ans=[[-1]*n for _ in range(m)]
        startRow,startCol=0,0
        endRow,endCol=m,n
        while startRow<endRow and startCol<endCol and head:
            for i in range(startCol,endCol):
                if not head:
                    return ans
                ans[startRow][i]=head.val
                head=head.next
            startRow+=1
            for i in range(startRow,endRow):
                if not head:
                    return ans
                ans[i][endCol-1]=head.val
                head=head.next
            endCol-=1
            for i in range(endCol-1,startCol-1,-1):
                if not head:
                    return ans
                ans[endRow-1][i]=head.val
                head=head.next
            endRow-=1
            for i in range(endRow-1,startRow-1,-1):
                if not head:
                    return ans
                ans[i][startCol]=head.val
                head=head.next
            startCol+=1
        return ans
        '''