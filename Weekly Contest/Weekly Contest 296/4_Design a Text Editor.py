# 2296. Design a Text Editor
# https://leetcode.com/problems/design-a-text-editor/

class TextEditor:

    '''
    def __init__(self):
        self.s=""
        self.idx=0

    def addText(self, text: str) -> None:
        self.s=self.s[:self.idx]+text+self.s[self.idx:]
        self.idx+=len(text)

    def deleteText(self, k: int) -> int:
        temp=len(self.s)
        self.s=self.s[:max(0,self.idx-k)]+self.s[self.idx:]
        self.idx=max(0,self.idx-k)
        return temp-len(self.s)

    def cursorLeft(self, k: int) -> str:
        self.idx=max(0,self.idx-k)
        return self.s[max(0,self.idx-10):self.idx]

    def cursorRight(self, k: int) -> str:
        self.idx=min(len(self.s),self.idx+k)
        return self.s[max(self.idx-10,0):self.idx]

    '''

    def __init__(self):
        self.left=[]
        self.right=[]

    def addText(self, text: str) -> None:
        for i in text:
            self.left.append(i)

    def deleteText(self, k: int) -> int:
        count=0
        while len(self.left) and k:
            self.left.pop()
            k-=1
            count+=1
        return count

    def cursorLeft(self, k: int) -> str:
        while len(self.left) and k:
            self.right.append(self.left.pop())
            k-=1
        return "".join(self.left[max(0,len(self.left)-10):])

    def cursorRight(self, k: int) -> str:
        while len(self.right) and k:
            self.left.append(self.right.pop())
            k-=1
        return "".join(self.left[max(0,len(self.left)-10):])

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)