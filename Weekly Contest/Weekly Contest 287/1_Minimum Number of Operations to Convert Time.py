# 2224. Minimum Number of Operations to Convert Time
# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

class Solution:
    def convertTime(self, current, correct):
        '''
        first=int(current[:2])*60+int(current[3:])
        second=int(correct[:2])*60+int(correct[3:])        
        count=0
        while second-first>=60:
            first+=60
            count+=1
        while second-first>=15:
            first+=15
            count+=1
        while second-first>=5:
            first+=5
            count+=1
        while second-first>=1:
            first+=1
            count+=1
        return count
        '''
        diff=(int(correct[:2])-int(current[:2]))*60+(int(correct[3:]))-int(current[3:])
        time=[60,15,5,1]
        count=0
        for i in time:
            count+=(diff//i)
            diff%=i
        return count