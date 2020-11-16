from itertools import combinations
from collections import Counter
from math import factorial
import numpy as np

#A partir de esta clase se manejan todo el análisis correspondiente a la parte 2
class Combi2:
    def __init__(self, n, k, p):
        self.n = n
        self.k = k
        self.p = p
    
    #Se usa la fórmula asociada al verbo distribuir del método de conteo de palomar
    def distribution(self, n, k):
        return int(factorial(n+k-1)/(factorial(k)*factorial(n-1)))
    
    #Construye una cadena de caracteres correspondiende al conjunto n-ario
    def stringConstruction(self, n):
        str=''
        for i in range(n):
            str = str+f'{i}'
        return str

    #Recibe los caracteres del conjunto de n-ario y devuelve una lista de cadenas de longitud k que contienen tanto al 0 como al 1 al menos 1 vez
    def combAnalisis(self, str, k): 
        perm = list(sorted(''.join(chars) for chars in combinations(str, k)))
        result=[]
        for x in perm:
            if "0" in x and "1" in x:
                result.append(x)
        return result

    #Recibe una lista de cadenas y devuelve las primeras p y las últimas p
    def firstandLastP(self, perm, p): 
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

    #Recibe una lista cadenas, las une en una sola y realiza el conteo de la cantidad de veces que un caracter del conjunto aparece. Luego retorna una lista que contiene internamente una lista con el nombre de las variables y otra lista con su respectivo valor promedio de apariciones
    def getCategories(self, perm):
        permToText = ''.join(perm)
        categories = Counter(permToText)
        result = [[],[]]
        for n in categories:
            result[0].append(n)
            result[1].append(categories[n]/len(perm))
        return result


    

