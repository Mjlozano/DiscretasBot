from itertools import combinations
class Combi:
    def __init__(self, word, p, k):
        self.p = p
        self.k = k
        self.word = word

    def firstP(self, str, p, k): 
        perm = list(sorted(''.join(chars) for chars in combinations(str, k)))
        fResult = f'Primeras {p} palabras\n'
        for x in perm[:p]: 
            fResult = fResult+"\n"+x
        return fResult 

    def lastP(self, str, p, k): 
        perm = sorted(''.join(chars) for chars in combinations(str, k)) 
        fResult = f'Ultimas {p} palabras\n'
        for x in perm[len(perm)-p:]: 
            fResult = fResult+"\n"+x 
        return fResult
    
    def getSize(self, str, p, k):
        perm = sorted(''.join(chars) for chars in combinations(str, k))
        return len(perm)
