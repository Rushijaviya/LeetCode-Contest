# 2682. Find the Losers of the Circular Game
# https://leetcode.com/problems/find-the-losers-of-the-circular-game/

class Solution:
    def circularGameLosers(self, n, k):
        visited=set()
        start,step=1,1
        while start not in visited:
            visited.add(start)
            start+=(step*k)
            step+=1
            if start>n:
                if start%n==0:
                    start=n
                else:
                    start%=n
        return [i for i in range(1,n+1) if i not in visited]