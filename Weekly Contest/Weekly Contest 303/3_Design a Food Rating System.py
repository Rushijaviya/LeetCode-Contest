# 2353. Design a Food Rating System
# https://leetcode.com/problems/design-a-food-rating-system/

'''
# TLE
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        n=len(foods)
        self.d=defaultdict(list)
        self.mapp={}
        for i in range(n):
            heappush(self.d[cuisines[i]],(-ratings[i],foods[i]))
            self.mapp[foods[i]]=cuisines[i]
            
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine=self.mapp[food]
        new=[]
        for i,j in self.d[cuisine]:
            if j==food:
                new.append((-newRating,j))
            else:
                new.append((i,j))
        heapify(new)
        self.d[cuisine]=new

    def highestRated(self, cuisine: str) -> str:
        return self.d[cuisine][0][1]
        
# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
'''

'''
# TLE
from collections import defaultdict

class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        n=len(foods)
        self.d=defaultdict(dict)
        self.mapp={}
        self.max={}
        for i in range(n):
            self.d[cuisines[i]][foods[i]]=ratings[i]
            self.mapp[foods[i]]=cuisines[i]
            if cuisines[i] not in self.max or self.max[cuisines[i]][0]<ratings[i] or (self.max[cuisines[i]][0]==ratings[i] and self.max[cuisines[i]][1]>foods[i]):
                self.max[cuisines[i]]=(ratings[i],foods[i])
        
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine=self.mapp[food]
        self.d[cuisine][food]=newRating
        del self.max[cuisine]
        l=self.d[cuisine]
        for i in l:
            if cuisine not in self.max or self.max[cuisine][0]<l[i] or (self.max[cuisine][0]==l[i] and self.max[cuisine][1]>i):
                self.max[cuisine]=(l[i],i)
                    
    def highestRated(self, cuisine: str) -> str:
        return self.max[cuisine][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
'''

'''
from collections import defaultdict
from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        self.fotorat={}
        self.fotocuis={}
        self.d=defaultdict(SortedList)
        for i in range(len(foods)):
            self.fotorat[foods[i]]=ratings[i]
            self.fotocuis[foods[i]]=cuisines[i]
            self.d[cuisines[i]].add((-ratings[i],foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        oldrating=self.fotorat[food]
        cuisine=self.fotocuis[food]
        self.d[cuisine].remove((-oldrating,food))
        self.d[cuisine].add((-newRating,food))
        self.fotorat[food]=newRating

    def highestRated(self, cuisine: str) -> str:
        return self.d[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
'''

from collections import defaultdict
from heapq import heappop, heappush

class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        self.footorat={}
        self.footocui={}
        self.d=defaultdict(list)
        for i in range(len(foods)):
            self.footorat[foods[i]]=ratings[i]
            self.footocui[foods[i]]=cuisines[i]
            heappush(self.d[cuisines[i]],(-ratings[i],foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        cuis=self.footocui[food]
        heappush(self.d[cuis],(-newRating,food))
        self.footorat[food]=newRating

    def highestRated(self, cuisine: str) -> str:
        while -self.d[cuisine][0][0]!=self.footorat[self.d[cuisine][0][1]]:
            heappop(self.d[cuisine])
        return self.d[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)