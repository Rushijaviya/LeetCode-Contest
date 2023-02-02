# 2490. Circular Sentence
# https://leetcode.com/problems/circular-sentence/

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        '''
        sentence=sentence.split()
        return all(sentence[i][-1]==sentence[i+1][0] for i in range(len(sentence)-1)) and sentence[0][0]==sentence[-1][-1]
        '''

        for i in range(len(sentence)):
            if sentence[i]==' ' and sentence[i-1]!=sentence[i+1]:
                return False
        return sentence[0]==sentence[-1]