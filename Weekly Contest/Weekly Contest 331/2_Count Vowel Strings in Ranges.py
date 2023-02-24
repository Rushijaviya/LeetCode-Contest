# 2559. Count Vowel Strings in Ranges
# https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words, queries):
        n=len(words)
        pref=[0]*n
        vowel='aeiou'
        for idx,word in enumerate(words):
            pref[idx]+=pref[idx-1]
            if word[0] in vowel and word[-1] in vowel:
                pref[idx]+=1
        ans=[]
        for l,r in queries:
            ans.append(pref[r]-(pref[l-1] if l>0 else 0))
        return ans