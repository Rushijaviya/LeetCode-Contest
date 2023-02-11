# 2512. Reward Top K Students
# https://leetcode.com/problems/reward-top-k-students/

class Solution:
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        '''
        d={}
        n=len(report)
        positive_feedback=set(positive_feedback)
        negative_feedback=set(negative_feedback)
        for idx in range(n):
            words=report[idx].split()
            count=0
            for word in words:
                if word in positive_feedback:
                    count+=3
                elif word in negative_feedback:
                    count-=1
            d[student_id[idx]]=count
        l=[(i,j) for i,j in d.items()]
        l.sort(key=lambda x:(-x[1],x[0]))
        return [i for i,_ in l[:k]]
        '''

        n=len(report)
        positive_feedback=set(positive_feedback)
        negative_feedback=set(negative_feedback)
        l=[]
        for idx in range(n):
            words=report[idx].split()
            count=0
            for word in words:
                if word in positive_feedback:
                    count+=3
                elif word in negative_feedback:
                    count-=1
            l.append((student_id[idx],count))
        l.sort(key=lambda x:(-x[1],x[0]))
        return [i for i,_ in l[:k]]