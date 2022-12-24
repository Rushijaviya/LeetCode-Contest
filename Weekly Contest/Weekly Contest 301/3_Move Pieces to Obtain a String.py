# 2337. Move Pieces to Obtain a String
# https://leetcode.com/problems/move-pieces-to-obtain-a-string/

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        '''
        curr_left=[]
        curr_right=[]
        req_left=[]
        req_right=[]
        n=len(start)
        for i in range(n):
            if (not req_left) and (not req_right) and (not curr_right) and (not curr_left) and start[i]==target[i]:
                continue
            if start[i]=='L':
                curr_left.append(i)
            elif start[i]=='R':
                curr_right.append(i)
            if target[i]=='L':
                req_left.append(i)
            elif target[i]=='R':
                req_right.append(i)
        if len(req_left)!=len(curr_left) or len(req_right)!=len(curr_right):
            return False
        for i in range(len(req_left)):
            if req_left[i]>curr_left[i] or (len(req_right)>i and curr_left[i]>=req_right[i] and req_right[i]>req_left[i]) or (len(curr_right)>i and curr_right[i]<=curr_left[i] and req_right[i]>req_left[i]):
                return False
        for i in range(len(req_right)):
            if req_right[i]<curr_right[i] or (len(req_left)>i and curr_right[i]<=req_left[i] and req_left[i]<req_right[i]) or (len(curr_left)>i and curr_left[i]>=curr_right[i] and req_left[i]<req_right[i]):
                return False
        return True
        '''

        i=0
        j=0
        n=len(start)
        while i<n or j<n:
            while i<n and start[i]=='_':
                i+=1
            while j<n and target[j]=='_':
                j+=1
            if i==n or j==n or start[i]!=target[j] or (start[i]=='L' and j>i) or (start[i]=='R' and j<i):
                break
            i+=1
            j+=1
        return i==n and j==n