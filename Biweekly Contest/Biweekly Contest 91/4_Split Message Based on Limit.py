# 2468. Split Message Based on Limit
# https://leetcode.com/problems/split-message-based-on-limit/

class Solution:
    def splitMessage(self, message, limit):
        
        def build(parts):
            n=len(str(parts))+3
            idx=0
            curr=1
            ans=[]
            end='/'+str(parts)+'>'
            while curr<parts:
                length=n+len(str(curr))
                diff=limit-length
                temp=message[idx:idx+diff]
                s=temp+'<'+str(curr)+end
                ans.append(s)
                idx+=diff
                curr+=1
            s=message[idx:]+'<'+str(curr)+end
            ans.append(s)
            return ans
        
        if limit<5:
            return []

        parts=temp=1
        while parts*(3+len(str(parts)))+temp+len(message)>parts*limit:
            if 3+len(str(parts))*2>=limit:
                return []
            parts+=1
            temp+=len(str(parts))

        return build(parts)