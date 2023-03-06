# 2580. Count Ways to Group Overlapping Ranges
# https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

class Solution:
    def countWays(self, ranges):
        ranges.sort()
        count=0
        start,end=ranges[0][0],ranges[0][1]
        for i,j in ranges[1:]:
            if i<=end:
                end=max(end,j)
            else:
                count+=1
                start,end=i,j
        return (2**(count+1))%(10**9+7)
        
        '''
        ranges.sort()
        count=0
        end=ranges[0][1]
        for i,j in ranges[1:]:
            if i>end:
                count+=1
            end=max(end,j)
        return (2**(count+1))%(10**9+7)
        '''