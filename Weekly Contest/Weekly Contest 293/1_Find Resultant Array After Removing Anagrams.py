# 2273. Find Resultant Array After Removing Anagrams
# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

from itertools import groupby


class Solution:
    def removeAnagrams(self, words):
        i=1
        while i<len(words):
            if sorted(words[i-1])==sorted(words[i]):        # Counter(words[i-1])==Counter(words[i]) - with out sorting
                words.pop(i)
            else:
                i+=1
        return words

        '''
        return [words[i] for i in range(len(words)) if i==0 or sorted(words[i])!=sorted(words[i-1])]
        '''

        '''
        return [next(g) for _, g in groupby(words, sorted)]
        '''