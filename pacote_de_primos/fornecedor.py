# -*- coding: utf-8 -*-
from listas_de_primos import *

# Retorna uma lista de referência a todos os arquivos 
# contidos na biblioteca 'lista_de_primos', permitindo o
# acesso as listas de primos contidos em cada um deles.
def obterListas():
    listas = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14,
              p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27,
              p28, p29, p30]
    return listas

#Total de primos armazendados nos arquivos da biblioteca 'lista_de_primos'.
def contaPrimos():
    primos = obterListas()
    cont = 0
    for p in primos:
        cont += len(p.LISTA)
    return cont
