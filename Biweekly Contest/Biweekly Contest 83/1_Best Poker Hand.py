# 2347. Best Poker Hand
# https://leetcode.com/problems/best-poker-hand/

from collections import Counter

class Solution:
    def bestHand(self, ranks, suits):
        '''
        if len(set(suits))==1:
            return "Flush"
        d=defaultdict(int)
        flag=0
        for i in ranks:
            d[i]+=1
            if d[i]==3:
                return "Three of a Kind"
            if d[i]==2:
                flag=1
        if flag:
            return "Pair"
        return "High Card"
        '''

        if max(suits)==min(suits):
            return "Flush"
        x=max(Counter(ranks).values())
        if x>=3:
            return "Three of a Kind"
        if x==2:
            return "Pair"
        return "High Card"