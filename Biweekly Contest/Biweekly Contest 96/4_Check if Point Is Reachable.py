# 2543. Check if Point Is Reachable
# https://leetcode.com/problems/check-if-point-is-reachable/

from math import gcd

class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        '''
        while True:
            if targetX==1 and targetY==1:
                return True
            if targetX%2==0:
                targetX//=2
            elif targetY%2==0:
                targetY//=2
            elif targetX>targetY:
                targetX-=targetY
            elif targetY>targetX:
                targetY-=targetX
            else:
                return False
        '''
        
        '''
        x=gcd(targetX,targetY)
        return x&(x-1)==0
        '''
        
        return gcd(targetX,targetY).bit_count()==1