# 2284. Sender With Largest Word Count
# https://leetcode.com/problems/sender-with-largest-word-count/

from collections import defaultdict

class Solution:
    def largestWordCount(self, messages, senders):
        d=defaultdict(int)
        n=len(messages)
        for i in range(n):
            sentence=list(map(str,messages[i].split()))
            d[senders[i]]+=len(sentence)
        d=dict(sorted(d.items(),key=lambda x:(x[1],x[0])))
        return list(d.keys())[-1]
        
        '''
        d={}
        n=len(messages)
        ans=senders[0]
        max_till_now=0
        for i in range(n):
            d[senders[i]]=d.get(senders[i],0)+messages[i].count(' ')+1
            if d[senders[i]]>max_till_now or (d[senders[i]]==max_till_now and senders[i]>ans):
                max_till_now=d[senders[i]]
                ans=senders[i]
        return ans
        '''