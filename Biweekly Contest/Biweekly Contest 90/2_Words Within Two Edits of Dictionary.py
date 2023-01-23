# 2452. Words Within Two Edits of Dictionary
# https://leetcode.com/problems/words-within-two-edits-of-dictionary/

class Node:
    def __init__(self) -> None:
        self.links=[None]*26
        self.flag=False

    def contains(self,char):
        return self.links[ord(char)-97]!=None
    
    def put(self,char,node):
        self.links[ord(char)-97]=node

    def get(self,char):
        return self.links[ord(char)-97]

    def markend(self):
        self.flag=True

class Trie:
    def __init__(self) -> None:
        self.root=Node()

    def insert(self,word):
        curr=self.root
        for char in word:
            if not curr.contains(char):
                curr.put(char,Node())
            curr=curr.get(char)
        curr.markend()

    def ispossible(self,word,left,curr=None):
        if not word or left<0:
            return left>=0
        if not curr:
            curr=self.root
        res=False
        for i in range(26):
            char=chr(97+i)
            if curr.contains(char):
                if char==word[0]:
                    res|=self.ispossible(word[1:],left,curr.get(char))
                else:
                    res|=self.ispossible(word[1:],left-1,curr.get(char))
        return res


class Solution:
    def twoEditWords(self, queries, dictionary):
        '''
        def ispossible(s):
            if s in dictionary:
                return True
            for word in dictionary:
                count=0
                for i in range(n):
                    if word[i]!=s[i]:
                        count+=1
                        if count>2:
                            break
                else:
                    return True
            return False

        ans=[]
        n=len(queries[0])
        for word in queries:
            if ispossible(word):
                ans.append(word)
        return ans
        '''

        obj=Trie()
        for word in dictionary:
            obj.insert(word)
        ans=[]
        for word in queries:
            if obj.ispossible(word,2):
                ans.append(word)
        return ans