# 2611. Mice and Cheese
# https://leetcode.com/problems/mice-and-cheese/

class Solution:
    def miceAndCheese(self, reward1, reward2, k):
        l=list(zip(reward2,reward1))
        l.sort(key=lambda x:x[0]-x[1])
        return sum(l[i][1] for i in range(k))+sum(l[i][0] for i in range(k,len(l)))