# 2678. Number of Senior Citizens
# https://leetcode.com/problems/number-of-senior-citizens/

class Solution:
    def countSeniors(self, details):
        '''
        count=0
        for s in details:
            if int(s[11:13])>60:
                count+=1
        return count
        '''

        return sum(1 if int(s[11:13])>60 else 0 for s in details)