# 2271. Maximum White Tiles Covered by a Carpet
# https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

from bisect import bisect_right
from itertools import accumulate

class Solution:
    def maximumWhiteTiles(self, tiles, carpetLen):
        tiles.sort()
        pref=[0]+list(accumulate(r-l+1 for l,r in tiles))
        end=[r for _,r in tiles]
        ans=j=0
        n=len(tiles)
        
        for i in range(n):
            left=tiles[i][0]
            right=min(end[-1],left+carpetLen-1)

            while j<n and end[j]<right:
                j+=1
            
            if right<tiles[j][0]:
                ans=max(ans,pref[j]-pref[i])
            else:
                ans=max(ans,pref[j+1]-pref[i]-end[j]+right)
        return ans
        
        '''
        n=len(tiles)
        tiles.sort()
        start=[l for l,_ in tiles]
        pref=[0]
        for i in range(n):
            pref.append(pref[-1]+tiles[i][1]-tiles[i][0]+1)
        ans=0
        for i in range(n):
            left,right=tiles[i]
            if right>=left+carpetLen-1:
                return carpetLen
            j=bisect_right(start,left+carpetLen-1)-1
            compensate=0
            if tiles[j][1]>left+carpetLen-1:
                compensate=tiles[j][1]-(left+carpetLen-1)
            ans=max(ans,pref[j+1]-pref[i]-compensate)
        return ans
        '''