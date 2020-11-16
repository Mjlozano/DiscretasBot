from itertools import combinations
from collections import Counter

class Combi:
    def __init__(self, word, p, k):
        self.p = p
        self.k = k
        self.word = word

    #Recibe una cadena de caracteres y retorna una lista con las primeras p posibles combinaciones
    def firstP(self, str, p, k): 
        perm = list(sorted(''.join(chars) for chars in combinations(str, k)))
        if len(perm)>=p:
            fResult = f'Primeras {p} palabras\n'
            for x in perm[:p]: 
                fResult = fResult+"\n"+x
        else:
            fResult=f'La cantidad de palabras que se pueden generar es menor a las requeridas con el parámetro p'
        return fResult 

    #Recibe una cadena de caracteres y  retorna una lista con las últimas p posibles combinaciones
    def lastP(self, str, p, k): 
        perm = sorted(''.join(chars) for chars in combinations(str, k)) 
        if len(perm)>=p:
            fResult = f'Ultimas {p} palabras\n'
            for x in perm[len(perm)-p:]: 
                fResult = fResult+"\n"+x 
        else:
            fResult='La cantidad de palabras que se pueden generar es menor a las requeridas con el parámetro p'
        return fResult
    
    #Recibe una cadena de caracteres y  retorna la longitud de una lista con todas las posibles combinaciones
    def getSize(self, str, p, k):
        perm = sorted(''.join(chars) for chars in combinations(str, k))
        return len(perm)

    #Recibe una  cadena, permuta las posibles combinaciones de longitud k,  las une en una sola y realiza el conteo de la cantidad de veces que un caracter del conjunto aparece. Luego retorna una lista que contiene internamente una lista con el nombre de las variables y otra lista con su respectivo valor total de apariciones
    def getCategories(self, str, p, k):
        perm = list(sorted(''.join(chars) for chars in combinations(str, k)))
        permToText = ''.join(perm)
        categories = Counter(permToText)
        result = [[],[]]
        for n in categories:
            result[0].append(n)
            result[1].append(categories[n])
        return result
