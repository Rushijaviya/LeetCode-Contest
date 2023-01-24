# 2456. Most Popular Video Creator
# https://leetcode.com/problems/most-popular-video-creator/

from collections import defaultdict

class Node:
    def __init__(self) -> None:
        self.total_views=0
        self.max_views=0
        self.ids=chr(97+26)

class Solution:
    def mostPopularCreator(self, creators, ids, views):
        '''
        total_views={}
        d={}
        max_views=float('-inf')
        for i in range(len(creators)):
            if creators[i] not in total_views:
                total_views[creators[i]]=0
            total_views[creators[i]]+=views[i]
            max_views=max(max_views,total_views[creators[i]])
            if creators[i] not in d:
                d[creators[i]]=[chr(97+27),0]
            if d[creators[i]][1]<views[i]:
                d[creators[i]]=[ids[i],views[i]]
            elif d[creators[i]][1]==views[i]:
                d[creators[i]][0]=min(d[creators[i]][0],ids[i])
        ans=[]
        for i in total_views:
            if total_views[i]==max_views:
                ans.append([i,d[i][0]])
        return ans
        '''

        d=defaultdict(Node)
        count=float('-inf')
        for i in range(len(creators)):
            d[creators[i]].total_views+=views[i]
            count=max(count,d[creators[i]].total_views)
            if d[creators[i]].max_views<views[i]:
                d[creators[i]].max_views=views[i]
                d[creators[i]].ids=ids[i]
            elif d[creators[i]].max_views==views[i]:
                d[creators[i]].ids=min(d[creators[i]].ids,ids[i])
        ans=[]
        for i in d:
            if d[i].total_views==count:
                ans.append([i,d[i].ids])
        return ans