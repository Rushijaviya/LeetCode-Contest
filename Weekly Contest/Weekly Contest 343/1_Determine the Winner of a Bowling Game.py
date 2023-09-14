# 2660. Determine the Winner of a Bowling Game
# https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

class Solution:
    def isWinner(self, player1, player2):
        score1,score2=player1[0],player2[0]
        for i in range(1,len(player1)):
            if player1[i-1]==10 or (i>1 and player1[i-2]==10):
                score1+=2*player1[i]
            else:
                score1+=player1[i]
            if player2[i-1]==10 or (i>1 and player2[i-2]==10):
                score2+=2*player2[i]                
            else:
                score2+=player2[i]
        if score1==score2:
            return 0
        return 1 if score1>score2 else 2