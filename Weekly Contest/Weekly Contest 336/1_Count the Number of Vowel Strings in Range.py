# 2586. Count the Number of Vowel Strings in Range
# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

class Solution:
    def vowelStrings(self, words, left, right):
        return sum(word[0] in 'aeiou' and word[-1] in 'aeiou' for word in words[left:right+1])