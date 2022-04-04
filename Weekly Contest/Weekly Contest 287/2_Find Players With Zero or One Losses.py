# 2225. Find Players With Zero or One Losses
# https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches):
        '''
        # TLE
        first=[]
        second=[]
        third=[]
        for i in matches:
            if i[0] not in second and i[0] not in third:
                if i[0] not in first:
                    first.append(i[0])
            if i[1] in third:
                continue
            elif i[1] in first:
                first.remove(i[1])
                second.append(i[1])
            elif i[1] in second:
                second.remove(i[1])
                third.append(i[1])
            else:
                second.append(i[1])
        x1=list(set(first))
        x2=list(set(second))
        x1.sort()
        x2.sort()
        return [x1,x2]
        '''
        v=[[0,0] for _ in range(100001)]
        for i in matches:
            v[i[0]][0]=True
            v[i[1]][0]=True
            v[i[1]][1]+=1
        ans=[[],[]]
        for i in range(100001):
            if v[i][0]:
                if v[i][1]==0:
                    ans[0].append(i)
                elif v[i][1]==1:
                    ans[1].append(i)
        return ans