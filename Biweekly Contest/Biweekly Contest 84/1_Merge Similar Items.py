# 2363. Merge Similar Items
# https://leetcode.com/problems/merge-similar-items/

from collections import Counter, defaultdict

class Solution:
    def mergeSimilarItems(self, items1, items2):
        '''
        d=defaultdict(int)
        for i,j in items1:
            d[i]+=j
        for i,j in items2:
            d[i]+=j
        ans=[[i,j] for i,j in d.items()]
        ans.sort()
        return ans
        '''

        return sorted((Counter(dict(items1))+Counter(dict(items2))).items())