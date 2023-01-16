# 2432. The Employee That Worked on the Longest Task
# https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

class Solution:
    def hardestWorker(self, n, logs):
        '''
        prev=logs[0][1]
        ans=logs[0][0]
        gap=prev
        for i,j in logs[1:]:
            if j-prev>gap:
                gap=j-prev
                ans=i
            elif j-prev==gap:
                ans=min(ans,i)
            prev=j
        return ans
        '''

        prev,ans=0,(0,0)
        for i,j in logs:
            ans=min(ans,(prev-j,i))
            prev=j
        return ans[1]