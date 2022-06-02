# 2278. Percentage of Letter in String
# https://leetcode.com/problems/percentage-of-letter-in-string/

class Solution:
    def percentageLetter(self, s, letter):
        count=0
        for i in s:
            if i==letter:
                count+=1
        return count*100//len(s)
        
        '''
        return (s.count(letter)*100)//len(s)
        '''