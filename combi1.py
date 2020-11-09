class Combi:
    def __init__(self, word, p, k):
        self.p = p
        self.k = k
        self.word = word

    def split(self, word):
        return [char for char in word]

    def firstP(self):
        from itertools import permutations

        perm = permutations(self.split(self.word))
        for i in list(perm):
            print(i)
