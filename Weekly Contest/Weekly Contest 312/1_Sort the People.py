# 2418. Sort the People
# https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names, heights):
        '''
        l=[(heights[i],names[i]) for i in range(len(heights))]
        l.sort(key=lambda x:-x[0])
        return [j for i,j in l]
        '''

        return [j for _,j in sorted(zip(heights,names),key=lambda x:-x[0])]