# 2220. Minimum Bit Flips to Convert Number
# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start, goal):
        start=bin(start)
        goal=bin(goal)
        start=list(start[2:])
        goal=list(goal[2:])
        while len(start)>len(goal):
            goal.insert(0,'0')
        while len(goal)>len(start):
            start.insert(0,'0')
        x=len(start)-1
        count=0
        while x>=0:
            if start[x]!=goal[x]:
                count+=1
            x-=1
        return count

        '''
        return bin(start^goal).count('1')
        '''