# 2379. Minimum Recolors to Get K Consecutive Black Blocks
# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        '''
        ans=float('inf')
        for i in range(len(blocks)-k+1):
            s=blocks[i:i+k]
            ans=min(ans,s.count('W'))
        return ans
        '''

        start=0
        white=0
        ans=float('inf')
        for end in range(len(blocks)):
            if blocks[end]=='W':
                white+=1
            if end-start+1==k:
                ans=min(ans,white)
                white-=(blocks[start]=='W')
                start+=1
        return ans