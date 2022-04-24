# 2249. Count Lattice Points Inside a Circle
# https://leetcode.com/problems/count-lattice-points-inside-a-circle/

import math

class Solution:
    def countLatticePoints(self, circles):
        s=set()

        def countLattice(x,y,r,s):    
            for cenx in range(x+1, x+r+1):
                for ceny in range(y+1,y+r+1):
                    if math.sqrt((cenx-x)**2+(ceny-y)**2)<=r:
                        s.add((cenx,ceny))
                        s.add((2*x-cenx,ceny))
                        s.add((2*x-cenx,2*y-ceny))
                        s.add((cenx,2*y-ceny))
            for ceny in range(y-r,y+r+1):
                s.add((x,ceny))
            for cenx in range(x-r,x+r+1):
                s.add((cenx,y))
    
        for cir in circles:
            countLattice(cir[0],cir[1],cir[2],s)
        
        return len(s)

        '''
        # TLE
        s=set()
        def countLattice(cenx,ceny,r,s): 
            if (r <= 0):
                return 0 

            for x in range(0, 201):
                for y in range(0,201):
                    i=(x-cenx)*(x-cenx)
                    j=(y-ceny)*(y-ceny)
                    if i+j<=r*r:
                        s.add((x,y))
        
        for cir in circles:
            countLattice(cir[0],cir[1],cir[2],s)
        return len(s)
        '''