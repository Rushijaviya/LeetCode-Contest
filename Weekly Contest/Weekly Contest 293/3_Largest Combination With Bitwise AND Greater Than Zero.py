# 2275. Largest Combination With Bitwise AND Greater Than Zero
# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

class Solution:
    def largestCombination(self, candidates):
        ans=0
        for idx in range(0,24):
            count=0
            for can in candidates:
                if (can>>idx & 1)==1:
                    count+=1
            ans=max(ans,count)
        return ans

        '''
        return max(sum(can&(1<<idx)>0 for can in candidates) for idx in range(0,24))
        '''