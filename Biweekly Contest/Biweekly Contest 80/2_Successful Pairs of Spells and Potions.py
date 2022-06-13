# 2300. Successful Pairs of Spells and Potions
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells, potions, success):
        def binsearch(l,target):
            start=0
            end=len(l)-1
            while start<=end:
                mid=(start+end)//2
                if l[mid]>target:
                    end=mid-1
                else:
                    start=mid+1
            return start
        
        potions=list(map(lambda x:success/x,potions))
        potions.sort()
        ans=[]
        for i in spells:
            ans.append(binsearch(potions,i))
        return ans
        
        '''
        potions.sort()
        return [len(potions) - bisect_left(potions, (success+s-1) // s) for s in spells]
        '''