# 2671. Frequency Tracker
# https://leetcode.com/problems/frequency-tracker/

class FrequencyTracker:

    def __init__(self):
        self.num=[0]*100001
        self.frequency=[0]*100001

    def add(self, number: int) -> None:
        if self.frequency[self.num[number]]>0:
            self.frequency[self.num[number]]-=1
        self.num[number]+=1
        self.frequency[self.num[number]]+=1

    def deleteOne(self, number: int) -> None:
        if self.num[number]>0:
            self.frequency[self.num[number]]-=1
            self.num[number]-=1
            if self.num[number]>0:
                self.frequency[self.num[number]]+=1

    def hasFrequency(self, frequency: int) -> bool:
        return self.frequency[frequency]>0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)

'''
class FrequencyTracker:

    def __init__(self):
        self.num=defaultdict(int)
        self.frequency=defaultdict(int)

    def add(self, number: int) -> None:
        self.frequency[self.num[number]]-=1
        self.num[number]+=1
        self.frequency[self.num[number]]+=1

    def deleteOne(self, number: int) -> None:
        if self.num[number]:
            self.frequency[self.num[number]]-=1
            self.num[number]-=1
            self.frequency[self.num[number]]+=1

    def hasFrequency(self, frequency: int) -> bool:
        return self.frequency[frequency]>0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
'''