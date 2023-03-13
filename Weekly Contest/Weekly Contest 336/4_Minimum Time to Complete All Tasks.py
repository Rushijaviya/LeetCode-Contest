# 2589. Minimum Time to Complete All Tasks
# https://leetcode.com/problems/minimum-time-to-complete-all-tasks/

class Solution:
    def findMinimumTime(self, tasks):
        '''
        stack=[]
        for idx,(start,end,duration) in enumerate(tasks):
            stack.append((start,0,duration,idx))
            stack.append((end,1,duration,idx))
        stack.sort()
        d={}
        ans=0
        for time,flag,duration,idx in stack:
            if not flag:
                d[idx]=[time,duration]
            else:
                un_used=d[idx][1]
                ans+=un_used
                for num in d:
                    use=min(un_used,d[num][1],time-d[num][0]+1)
                    d[num][1]-=use
                    d[num][0]+=use
                del d[idx]
        return ans
        '''

        tasks.sort(key=lambda x:x[1])
        s=set()
        for start,end,duration in tasks:
            remain=duration
            for time in range(start,end+1):
                if time in s:
                    remain-=1
                    if remain==0:
                        break
            while remain>0:
                if end not in s:
                    s.add(end)
                    remain-=1
                end-=1
        return len(s)