# 2416. Sum of Prefix Scores of Strings
# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

class Node:
    def __init__(self):
        self.links=[None]*26
        self.count=0

    def iscontainkey(self,char):
        return self.links[ord(char)-97]!=None

    def putkey(self,char,node):
        self.links[ord(char)-97]=node
    
    def get(self,char):
        return self.links[ord(char)-97]

    def increasecount(self):
        self.count+=1

    def getcount(self,char):
        return self.count

class Trie:
    def __init__(self):
        self.root=Node()

    def insert(self,word):
        curr=self.root
        for char in word:
            if not curr.iscontainkey(char):
                curr.putkey(char,Node())
            curr=curr.get(char)
            curr.increasecount()
    
    def travel(self,word):
        curr=self.root
        count=0
        for char in word:
            curr=curr.get(char)
            count+=curr.getcount(char)
        return count

class Solution:
    def sumPrefixScores(self, words):
        '''
        d=defaultdict(int)
        for word in words:
            s=""
            for char in word:
                s+=char
                d[s]+=1
        ans=[0]*len(words)
        for idx,word in enumerate(words):
            s=""
            for char in word:
                s+=char
                ans[idx]+=d[s]
        return ans
        '''

        obj=Trie()
        for word in words:
            obj.insert(word)
        
        ans=[]
        for word in words:
            temp=obj.travel(word)
            ans.append(temp)
        return ans