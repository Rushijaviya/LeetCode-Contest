# 2350. Shortest Impossible Sequence of Rolls
# https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/

class Solution:
    def shortestSequence(self, rolls, k):
        '''
        # TLE
        def rec(temp):
            ans.append(temp)
            for i in range(k):
                if not visited[i]:
                    visited[i]=1
                    rec(temp+[l[i]])
                    visited[i]=0
        
        def rec2(idx,temp):
            if idx==len(rolls):
                ans2.append(temp)
                return 
            rec2(idx+1,temp+[rolls[idx]])
            rec2(idx+1,temp)
            
        l=[i+1 for i in range(k)]
        ans=[]
        visited=[0]*k
        rec([])
        ans.sort(key=lambda x:len(x))
        ans.pop(0)
        ans2=[]
        rec2(0,[])
        for i in ans:
            if i not in ans2:
                return len(i)
        return -1
        '''
        
        '''
        d=defaultdict(int)
        c=0
        ans=0
        for i in rolls:
            d[i]+=1
            if d[i]==1:
                c+=1
                if c==k:
                    ans+=1
                    c=0
                    d=defaultdict(int)
        return ans+1
        '''

        s=set()
        ans=1
        for i in rolls:
            s.add(i)
            if len(s)==k:
                ans+=1
                s=set()
        return ans