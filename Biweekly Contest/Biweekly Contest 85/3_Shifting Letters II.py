# 2381. Shifting Letters II
# https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s, shifts):
        '''
        # TLE
        n=len(s)
        arr=[ord(i)-97 for i in s]
        for start,end,flag in shifts:
            if flag:
                arr[start:end+1]=list(map(lambda x:x+1,arr[start:end+1]))
            else:
                arr[start:end+1]=list(map(lambda x:x-1,arr[start:end+1]))
        ans=""
        for i in arr:
            i%=26
            ans+=chr(i+97)
        return ans
        '''

        n=len(s)
        pref=[0]*n
        for start,end,flag in shifts:
            if flag:
                pref[start]+=1
                if end+1<n:
                    pref[end+1]-=1
            else:
                pref[start]-=1
                if end+1<n:
                    pref[end+1]+=1
        total_sum=0
        ans=""
        for i in range(n):
            total_sum+=pref[i]
            prev=ord(s[i])-97
            new=(prev+total_sum)%26
            ans+=chr(new+97)
        return ans