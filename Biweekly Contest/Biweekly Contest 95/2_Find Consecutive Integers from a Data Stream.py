# 2526. Find Consecutive Integers from a Data Stream
# https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

'''
class DataStream:

    def __init__(self, value: int, k: int):
        self.l=[]
        self.val=value
        self.k=k
        self.count=0

    def consec(self, num: int) -> bool:
        self.l.append(num)
        self.count+=(num==self.val)
        if len(self.l)>self.k:
            self.count-=(self.l.pop(0)==self.val)
        return self.count==self.k
'''

class DataStream:

    def __init__(self, value: int, k: int):
        self.val=value
        self.k=k
        self.count=0

    def consec(self, num: int) -> bool:
        if self.val==num:
            self.count+=1
        else:
            self.count=0
        return self.count>=self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)