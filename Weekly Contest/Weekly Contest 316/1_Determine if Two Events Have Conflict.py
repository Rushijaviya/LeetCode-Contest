# 2446. Determine if Two Events Have Conflict
# https://leetcode.com/problems/determine-if-two-events-have-conflict/

class Solution:
    def haveConflict(self, event1, event2):
        '''
        def transfer(s):
            return int(s[:2])*60+int(s[3:])

        event1[0]=transfer(event1[0])
        event1[1]=transfer(event1[1])
        event2[0]=transfer(event2[0])
        event2[1]=transfer(event2[1])

        return event2[0]<=event1[0]<=event2[1] or event1[0]<=event2[0]<=event1[1]
        '''
        
        '''
        return event2[0]<=event1[0]<=event2[1] or event1[0]<=event2[0]<=event1[1]
        '''
        
        '''
        return max(event1[0],event2[0])<=min(event2[1],event1[1])
        '''

        return event1[0]<=event2[1] and event2[0]<=event1[1]