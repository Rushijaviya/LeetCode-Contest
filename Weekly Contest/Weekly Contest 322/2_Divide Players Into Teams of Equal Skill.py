# 2491. Divide Players Into Teams of Equal Skill
# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

from collections import Counter

class Solution:
    def dividePlayers(self, skill):
        '''
        skill.sort()
        value=skill[0]+skill[-1]
        chem=skill[0]*skill[-1]
        left,right=1,len(skill)-2
        while left<right:
            if skill[left]+skill[right]!=value:
                return -1
            chem+=(skill[left]*skill[right])
            left+=1
            right-=1
        return chem
        '''

        value=(2*sum(skill))//len(skill)
        ans=0
        c=Counter(skill)
        for i in c:
            if c[i]!=c[value-i]:
                return -1
            ans+=(i*(value-i)*c[i])
        return ans//2