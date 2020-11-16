from itertools import combinations
from collections import Counter

class Combi:
    def __init__(self, word, p, k):
        self.p = p
        self.k = k
        self.word = word

    def firstP(self, str, p, k): 
        perm = list(sorted(''.join(chars) for chars in combinations(str, k)))
        if len(perm)>=p:
            fResult = f'Primeras {p} palabras\n'
            for x in perm[:p]: 
                fResult = fResult+"\n"+x
        else:
            fResult=f'La cantidad de palabras que se pueden generar es menor a las requeridas con el parámetro p'
        return fResult 

    def lastP(self, str, p, k): 
        perm = sorted(''.join(chars) for chars in combinations(str, k)) 
        if len(perm)>=p:
            fResult = f'Ultimas {p} palabras\n'
            for x in perm[len(perm)-p:]: 
                fResult = fResult+"\n"+x 
        else:
            fResult='La cantidad de palabras que se pueden generar es menor a las requeridas con el parámetro p'
        return fResult
    
    def getSize(self, str, p, k):
        perm = sorted(''.join(chars) for chars in combinations(str, k))
        return len(perm)

    def getCategories(self, str, p, k):
        perm = list(sorted(''.join(chars) for chars in combinations(str, k)))
        permToText = ''.join(perm)
        categories = Counter(permToText)
        result = [[],[]]
        for n in categories:
            result[0].append(n)
            result[1].append(categories[n])
        return result
