class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        wone = sentence1.split()
        wtow = sentence2.split()

        if len(wone) < len(wtow):
            wone, wtow = wtow, wone
        
        st, en = 0, 0
        n1, n2 = len(wone), len(wtow)
        
        while st < n2 and wone[st] == wtow[st]:
            st += 1
        
        while en < n2 and wone[n1 - en - 1] == wtow[n2 - en - 1]:
            en += 1
        
        return st + en >= n2
