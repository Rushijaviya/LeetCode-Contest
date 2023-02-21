# 2545. Sort the Students by Their Kth Score
# https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution:
    def sortTheStudents(self, score, k):
        '''
        score.sort(key=lambda x:-x[k])
        return score
        '''
        
        return sorted(score, key=lambda s:s[k], reverse=True)