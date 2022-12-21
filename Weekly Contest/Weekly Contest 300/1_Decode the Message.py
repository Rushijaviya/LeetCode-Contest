# 2325. Decode the Message
# https://leetcode.com/problems/decode-the-message/

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        '''
        d={' ':' '}
        idx=0
        for i in key:
            if i not in d:
                d[i]=chr(idx+97)
                idx+=1
                if idx==26:
                    break
        ans=""
        for i in message:
            ans+=d[i]
        return ans
        '''

        l=[]
        for i in key:
            if i==' ':
                continue
            if i not in l:
                l.append(i)
        ans=""
        for i in message:
            if i==' ':
                ans+=i
            else:
                idx=l.index(i)
                ans+=chr(97+idx)
        return ans