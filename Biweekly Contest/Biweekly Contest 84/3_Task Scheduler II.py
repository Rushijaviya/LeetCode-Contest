# 2365. Task Scheduler II
# https://leetcode.com/problems/task-scheduler-ii/

class Solution:
    def taskSchedulerII(self, tasks, space):
        '''
        day=1
        d={}
        idx=0
        n=len(tasks)
        while idx<n:
            if tasks[idx] not in d:
                d[tasks[idx]]=day
                day+=1
                idx+=1
            else:
                if day>d[tasks[idx]]+space:
                    d[tasks[idx]]=day
                    day+=1
                    idx+=1
                else:
                    day=d[tasks[idx]]+space+1
                    d[tasks[idx]]=day
                    day+=1
                    idx+=1
        return day-1
        '''
        
        day=1
        d={}
        idx=0
        n=len(tasks)
        while idx<n:
            if tasks[idx] in d:
                day=max(day,d[tasks[idx]]+space+1)
            d[tasks[idx]]=day
            day+=1
            idx+=1
        return day-1