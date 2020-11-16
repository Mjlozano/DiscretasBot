from itertools import combinations
from collections import Counter
from math import factorial
import numpy as np

class Combi2:
    def __init__(self, n, k, p):
        self.n = n
        self.k = k
        self.p = p
        
    def distribution(self, n, k):
        return int(factorial(n+k-1)/(factorial(k)*factorial(n-1)))
    
    def stringConstruction(self, n):
        str=''
        for i in range(n):
            str = str+f'{i}'
        return str

    def combAnalisis(self, str, p, k): 
        perm = list(sorted(''.join(chars) for chars in combinations(str, k)))
        result=[]
        for x in perm:
            if "0" in x and "1" in x:
                result.append(x)
        return result

    def firstandLastP(self, perm, p, k): 
        print(f'p{p},lenperm{len(perm)},lenperm*2{len(perm)*2}')
        if (len(perm)) >= p:
            fResult = f'Primeras {p} palabras\n'
            for x in perm[:p]: 
                fResult = fResult+"\n"+x 
            fResult=fResult+ f'\n Últimas {p} palabras'
            for x in perm[len(perm)-p:]: 
                fResult = fResult+"\n"+x 
        else:
            fResult='La cantidad de palabras que se pueden generar es menor a las requeridas por el parámetro p'
        return fResult

    def getCategories(self, perm, p, k):
        permToText = ''.join(perm)
        categories = Counter(permToText)
        result = [[],[]]
        for n in categories:
            result[0].append(n)
            result[1].append(categories[n]/len(perm))
        return result


    

