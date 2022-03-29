# 2211. Count Collisions on a Road
# https://leetcode.com/problems/count-collisions-on-a-road/

class Solution:
    def countCollisions(self, directions):
        left,right=0,len(directions)-1
        while left<len(directions) and directions[left]=='L':
            left+=1
        while right>=0 and directions[right]=='R':
            right-=1
        count=0
        for i in range(left,right+1):
            if directions[i]!='S':
                count+=1
        return count