from itertools import combinations
class Combi:
    def __init__(self, word, p, k):
        self.p = p
        self.k = k
        self.word = word

    def split(self, word):
        return [char for char in word]
        

    def firstP(self, str, p, k): 
        perm = list(sorted(''.join(chars) for chars in combinations(str, k)))
        print("Primeras p palabras\n") 
        for x in perm[:p]: 
            print(x)
        print("\n") 

    def lastP(self, str, p, k): 
        perm = sorted(''.join(chars) for chars in combinations(str, k)) 
        print("Ultimas p palabras\n") 
        for x in perm[len(perm)-p:]: 
            print(x) 
        