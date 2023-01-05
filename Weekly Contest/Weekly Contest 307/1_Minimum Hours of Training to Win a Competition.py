# 2383. Minimum Hours of Training to Win a Competition
# https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy, experience):
        count=max(sum(energy)+1-initialEnergy,0)
        n=len(energy)
        for i in range(n):
            if initialExperience>experience[i]:
                initialExperience+=experience[i]
            else:
                diff=experience[i]-initialExperience
                count+=(diff+1)
                initialExperience+=(diff+1+experience[i])
        return count