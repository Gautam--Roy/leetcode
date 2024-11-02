class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        if ' ' not in sentence:
            return True
        n = len(sentence)
        for i in range(1, n-1):
            if sentence[i] == ' ':
                if sentence[i-1] != sentence[i+1]:
                    return False
        return True
        
