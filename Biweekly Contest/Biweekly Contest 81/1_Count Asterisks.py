# 2315. Count Asterisks
# https://leetcode.com/problems/count-asterisks/

class Solution:
    def countAsterisks(self, s):
        '''
        count=0
        words=s.split('|')
        for i in range(0,len(words),2):
            count+=words[i].count('*')
        return count
        '''

        flag=1
        count=0
        for i in s:
            if i=='|':
                flag=1-flag
            elif flag and i=='*':
                count+=1
        return count