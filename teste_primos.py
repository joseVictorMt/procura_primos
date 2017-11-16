from pacote_de_primos.fornecedor import obterListas
from math import sqrt
from random import randint

def euclidiano(b, n): #Algoritmo de Euclides para achar M.D.C.
    while (n != 0):
        b, n = n, b % n
    return b

def buscaDivisor(n, raiz, lista): #Busca um divisor primo de 'n'.
    for x in lista:
        if ((n%x) == 0):
            return x
        elif (x > raiz):
            return 0
    return 1

def fatoracaoIngenua(n): #Fatoracao ingenua para achar divisores primos.	
    raiz = long(sqrt(n))
    listasPrimos = obterListas()
    for primos in listasPrimos:
        a = buscaDivisor(n, raiz, primos.LISTA)
        if (a > 1):
            return a
        if (a < 1): #Se a raiz de 'n' for atingida.
            break
    return 1

def composicaoMiller(n): #Teste de Miller e composicao.
    y = n - 1
    exp = []
    while (y % 2 == 0): #Vetor de expoentes menores que 'n-1'.
        y /= 2
        exp.insert(0, y)

    limit = 100 #Definicao do limite de bases.
    if(n <= limit):
        limit = n - 1

    for i in range(100):
        base = randint(2, limit)

        aux = pow(base, exp[0], n) #Teste de Miller.
        if ((aux == -1) or (aux == 1)):
            return False
        for e in exp[1:]:
            if(pow(base, e, n) == -1):
                return False

        if(pow(base, n - 1, n) == 1): #Teste da composicao.
            return False
    return True

def testeLucas(n): #Teste de primalidade.
    i = 1
    achou = False
    limit = 100 #Definicao do limite de bases.
    if(n <= limit):
        limit = n - 1

    while (i < 100):
        base = randint(2, limit)
        if (euclidiano(base, n) == 1):
            if (pow(base, n-1, n) == 1):
                y = n-1
                while (y > 1):
                    d = fatoracaoIngenua(y)
                    if(d == 1):
                        d = y
                    if(pow(base, (n - 1) / d, n) == 1):
                        achou = True
                        break
                    y /= d
                if (not achou):
                    return True
            achou = False
            i += 1
    return False
