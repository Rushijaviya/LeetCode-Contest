# 2409. Count Days Spent Together
# https://leetcode.com/problems/count-days-spent-together/

from itertools import accumulate

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        '''
        x=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        x=list(accumulate(x))
        starta=(x[int(arriveAlice[:2])-2] if int(arriveAlice[:2])-2>=0 else 0)+int(arriveAlice[3:])
        enda=(x[int(leaveAlice[:2])-2] if int(leaveAlice[:2])-2>=0 else 0)+int(leaveAlice[3:])
        startb=(x[int(arriveBob[:2])-2] if int(arriveBob[:2])-2>=0 else 0)+int(arriveBob[3:])
        endb=(x[int(leaveBob[:2])-2] if int(leaveBob[:2])-2>=0 else 0)+int(leaveBob[3:])
        count=0
        for i in range(starta,enda+1):
            if i in range(startb,endb+1):
                count+=1
        return count
        '''

        x=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        x=list(accumulate(x))
        starta=(x[int(arriveAlice[:2])-2] if int(arriveAlice[:2])-2>=0 else 0)+int(arriveAlice[3:])
        enda=(x[int(leaveAlice[:2])-2] if int(leaveAlice[:2])-2>=0 else 0)+int(leaveAlice[3:])
        startb=(x[int(arriveBob[:2])-2] if int(arriveBob[:2])-2>=0 else 0)+int(arriveBob[3:])
        endb=(x[int(leaveBob[:2])-2] if int(leaveBob[:2])-2>=0 else 0)+int(leaveBob[3:])
        if startb<=starta<=endb:
            return min(endb,enda)-starta+1
        if starta<=startb<=enda:
            return min(endb,enda)-startb+1
        return 0

        '''
        x=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        x=list(accumulate(x))
        starta=(x[int(arriveAlice[:2])-2] if int(arriveAlice[:2])-2>=0 else 0)+int(arriveAlice[3:])
        enda=(x[int(leaveAlice[:2])-2] if int(leaveAlice[:2])-2>=0 else 0)+int(leaveAlice[3:])
        startb=(x[int(arriveBob[:2])-2] if int(arriveBob[:2])-2>=0 else 0)+int(arriveBob[3:])
        endb=(x[int(leaveBob[:2])-2] if int(leaveBob[:2])-2>=0 else 0)+int(leaveBob[3:])        
        start=max(starta,startb)
        end=min(enda,endb)
        return max(0,end-start+1)
        '''