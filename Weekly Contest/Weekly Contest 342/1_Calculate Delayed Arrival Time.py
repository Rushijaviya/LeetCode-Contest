# 2651. Calculate Delayed Arrival Time
# https://leetcode.com/problems/calculate-delayed-arrival-time/

class Solution:
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        '''
        time = arrivalTime+delayedTime
        if time>=24:
            time-=24
        return time
        '''

        return (arrivalTime+delayedTime)%24