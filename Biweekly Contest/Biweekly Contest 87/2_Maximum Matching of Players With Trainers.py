# 2410. Maximum Matching of Players With Trainers
# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players, trainers):
        '''
        trainers.sort(reverse=True)
        players.sort()
        ans=0
        for i in trainers:
            idx=bisect_left(players,i)
            if 0<=idx<=len(players):
                if idx<len(players) and players[idx]==i:
                    players.pop(idx)
                    ans+=1
                elif idx-1>=0:
                    players.pop(idx-1)
                    ans+=1
        return ans
        '''
        
        '''
        trainers.sort(reverse=True)
        players.sort()
        idx=len(players)-1
        ans=0
        for i in trainers:
            while idx>=0 and players[idx]>i:
                idx-=1
            if idx==-1:
                break
            ans+=1
            idx-=1
        return ans
        '''
        
        trainers.sort()
        players.sort()
        n=len(players)
        idx=0
        for i in trainers:
            if players[idx]<=i:
                idx+=1
                if idx==n:
                    break
        return idx